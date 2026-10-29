#!/usr/bin/env python3
"""
Ingestion des scores des petits modèles (SLM, ≤ 35 Md de paramètres).

Trois sources, toutes mesurées par un tiers et publiées sous licence ouverte :
- Epoch AI (CC-BY 4.0) : l'indice ECI, GPQA Diamond et OTIS Mock AIME, lus dans
  l'archive déjà téléchargée par epoch_ingest.py ;
- LMArena (CC-BY 4.0) : classement texte « overall », jeu de données Hugging Face ;
- Vectara (Apache-2.0) : taux d'hallucination en résumé, tableau du README.
Seules les lignes rattachées à une fiche de catalog/slm.yaml (champ `motif`) sont
gardées. On en tire catalog/slm_scores.yaml — fichier GÉNÉRÉ, à ne pas éditer.

  python3 pipeline/slm_ingest.py                    # utilise le cache
  python3 pipeline/slm_ingest.py --force-download   # relit les sources
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import urllib.request
import zipfile
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "sources" / "raw"
OUT = ROOT / "catalog" / "slm_scores.yaml"
EPOCH_ZIP = RAW / "epoch_benchmark_data.zip"
EPOCH_URL = "https://epoch.ai/data/benchmark_data.zip"
LMA_RAW = RAW / "lmarena_text_overall.json"
LMA_API = ("https://datasets-server.huggingface.co/rows?dataset=lmarena-ai/leaderboard-dataset"
           "&config=text&split=latest&offset={o}&length=100")
LMA_PAGE = "https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset"
VEC_RAW = RAW / "vectara_hallucination.md"
VEC_URL = "https://raw.githubusercontent.com/vectara/hallucination-leaderboard/main/README.md"
VEC_PAGE = "https://github.com/vectara/hallucination-leaderboard"
EPOCH_FILES = {"gpqa-diamond": "gpqa_diamond.csv", "otis-aime": "otis_mock_aime_2024_2025.csv"}
EFFORTS = ("none", "minimal", "low", "medium", "high", "xhigh", "max", "unknown")


def norm(x: str) -> str:
    """Noms des trois sources ramenés à une forme commune : « Gemma 4 31B » et
    « google/gemma-4-31b-it » donnent « gemma-4-31b » et « google-gemma-4-31b-it »."""
    return re.sub(r"[^a-z0-9.]+", "-", x.lower()).strip("-")


def get(url: str, raw: Path, force: bool) -> Path:
    if force or not raw.exists():
        raw.parent.mkdir(parents=True, exist_ok=True)
        print(f"  téléchargement {url}")
        urllib.request.urlretrieve(url, raw)
    return raw


def lmarena(force: bool) -> list[dict]:
    """Le jeu « latest » est trié par catégorie, « overall » en tête : on pagine
    jusqu'à la première ligne d'une autre catégorie."""
    if force or not LMA_RAW.exists():
        rows, o = [], 0
        while True:
            with urllib.request.urlopen(LMA_API.format(o=o), timeout=90) as r:
                page = [x["row"] for x in json.load(r)["rows"]]
            rows += [x for x in page if x["category"] == "overall"]
            if not page or page[-1]["category"] != "overall":
                break
            o += 100
        LMA_RAW.parent.mkdir(parents=True, exist_ok=True)
        LMA_RAW.write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")
    return json.loads(LMA_RAW.read_text(encoding="utf-8"))


def vectara(force: bool) -> list[dict]:
    out = []
    for l in get(VEC_URL, VEC_RAW, force).read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) >= 3 and c[1].endswith("%") and c[0] != "Model":
            out.append({"name": c[0], "rate": float(c[1].rstrip(" %"))})
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force-download", action="store_true")
    a = ap.parse_args()
    cat = yaml.safe_load((ROOT / "catalog" / "slm.yaml").read_text(encoding="utf-8"))
    motifs = [(e["id"], re.compile(e["motif"])) for e in cat["entries"]]

    def fiche(nom: str) -> str | None:
        n = norm(nom)
        hits = [i for i, m in motifs if m.search(n)]
        assert len(hits) <= 1, f"{nom} rattaché à plusieurs fiches : {hits}"
        return hits[0] if hits else None

    rows = []
    z = zipfile.ZipFile(get(EPOCH_URL, EPOCH_ZIP, False))
    eci = csv.DictReader(io.StringIO(z.read("epoch_capabilities_index/eci_scores.csv").decode("utf-8")))
    for x in eci:
        if (e := fiche(x["Model"])) and x["eci"]:
            rows.append({"benchmark": "epoch-eci", "entry": e, "name": x["Display name"],
                         "score": round(float(x["eci"]), 1),
                         "ci": [round(float(x["eci_ci_low"]), 1), round(float(x["eci_ci_high"]), 1)]})
    for b, f in EPOCH_FILES.items():
        best: dict[str, dict] = {}
        for x in csv.DictReader(io.StringIO(z.read(f).decode("utf-8"))):
            v, _, eff = x["Model version"].rpartition("_")
            if eff not in EFFORTS:
                v, eff = x["Model version"], None
            if not (e := fiche(v)) or not x["mean_score"]:
                continue
            s, se = float(x["mean_score"]) * 100, float(x["stderr"] or 0) * 100
            r = {"benchmark": b, "entry": e, "name": v, "effort": eff, "score": round(s, 1),
                 "ci": [round(s - 1.96 * se, 1), round(s + 1.96 * se, 1)] if se else None}
            # Un modèle mesuré à plusieurs niveaux d'effort : on garde le meilleur, effort nommé.
            if e not in best or r["score"] > best[e]["score"]:
                best[e] = r
        rows += best.values()
    lma = lmarena(a.force_download)
    for x in lma:
        if e := fiche(x["model_name"]):
            rows.append({"benchmark": "lmarena-text", "entry": e, "name": x["model_name"],
                         "score": round(x["rating"]), "ci": [round(x["rating_lower"]), round(x["rating_upper"])],
                         "rank": int(x["rank"]), "votes": int(x["vote_count"])})
    for x in vectara(a.force_download):
        if e := fiche(x["name"].split("/")[-1]):
            rows.append({"benchmark": "vectara-hhem", "entry": e, "name": x["name"], "score": x["rate"]})
    out = {
        "_generated": {
            "by": "pipeline/slm_ingest.py", "on": date.today().isoformat(),
            "epoch": EPOCH_URL, "lmarena": LMA_PAGE,
            "lmarena_published": lma[0].get("leaderboard_publish_date") if lma else None,
            "vectara": VEC_PAGE,
            "warning": "Fichier généré. Relancer pipeline/slm_ingest.py, ne pas éditer.",
        },
        "scores": rows,
    }
    OUT.write_text(yaml.safe_dump(out, allow_unicode=True, sort_keys=False, width=100), encoding="utf-8")
    n = {b: sum(r["benchmark"] == b for r in rows) for b in dict.fromkeys(r["benchmark"] for r in rows)}
    print(f"  écrit {OUT.relative_to(ROOT)} — {len(rows)} lignes {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
