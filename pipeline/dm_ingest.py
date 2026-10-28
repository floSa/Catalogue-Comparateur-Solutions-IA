#!/usr/bin/env python3
"""
Ingestion du Jev Decision Index (modèles de décision).

Sources, toutes deux publiées en JSON par leurs auteurs :
- Jev Decision Index, classement communautaire tenu par multimodalart sur Hugging Face ;
- JevBench, banc indépendant de Benchmark Heaven (API publique, licence MIT).
On en tire catalog/dm_scores.yaml — fichier GÉNÉRÉ, à ne pas éditer à la main.
Les scores de l'Artificial Analysis Decision Index, sans export, sont relevés à la
main dans catalog/dm.yaml.

  python3 pipeline/dm_ingest.py                    # utilise le cache
  python3 pipeline/dm_ingest.py --force-download   # relit la source
"""
from __future__ import annotations

import argparse
import json
import urllib.request
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "sources" / "raw" / "jev_decision_index.json"
OUT = ROOT / "catalog" / "dm_scores.yaml"
SPACE = "https://huggingface.co/spaces/multimodalart/jev-decision-index"
DATA_URL = SPACE + "/resolve/main/data/index.json"
JB_RAW = ROOT / "sources" / "raw" / "jevbench.json"
JB_PAGE = "https://benchmarkheaven.com/jev-models"
JB_URL = "https://benchmarkheaven.com/api/jevbench/latest"


def fetch(force: bool, url: str = DATA_URL, raw: Path = RAW) -> dict:
    if force or not raw.exists():
        raw.parent.mkdir(parents=True, exist_ok=True)
        print(f"  téléchargement {url}")
        urllib.request.urlretrieve(url, raw)
    return json.loads(raw.read_text(encoding="utf-8"))


def jevbench(d: dict) -> list[dict]:
    """Score de tête de JevBench : la « capacité » (moyenne exactitude + calibration),
    classée seulement pour les systèmes sous les plafonds de coût et de latence."""
    out = []
    for x in d.get("systems", []):
        cap = x.get("capability") or {}
        if not (cap.get("eligible") and x.get("listing") == "ranked" and cap.get("score") is not None):
            continue
        ax = x.get("axes") or {}
        out.append({"benchmark": "jevbench", "name": x["name"], "engine": x.get("key"),
                    "board": x.get("board"), "weights_url": x.get("source_url"),
                    "score": round(cap["score"], 2), "composite": round(x["composite_score"], 2)
                    if x.get("composite_score") is not None else None,
                    "axes": {k: round(v, 1) for k, v in ax.items() if v is not None},
                    "usd_per_1000": round((x.get("price") or {}).get("usd_per_1000_decisions") or 0, 4) or None,
                    "price_estimated": (x.get("price") or {}).get("kind") == "estimate",
                    "p50_s": round((x.get("latency") or {}).get("p50_s_adjusted") or 0, 3) or None,
                    "measured_on": (x.get("draw") or {}).get("measured_on")})
    return sorted(out, key=lambda r: -r["score"])


def lien(x: str | None) -> str | None:
    """Les dépôts sont donnés tantôt en URL, tantôt en `org/nom` Hugging Face."""
    if not x:
        return None
    return x if x.startswith("http") else f"https://huggingface.co/{x}"


def ligne(m: dict, jev: bool = False) -> dict:
    meta, sc, v = m.get("meta") or {}, m.get("scores") or {}, m.get("v03") or {}
    p = meta.get("served_params")
    return {
        "benchmark": "jev-decision-index",
        "name": m["name"],
        "engine": m.get("engine"),
        "kind": "hosted API" if jev else meta.get("kind"),
        "base_model": meta.get("base_model"),
        "params_b": round(p / 1e9, 1) if p else None,
        "weights_url": lien(meta.get("weights_repo") or meta.get("model_url")),
        "code_url": meta.get("code_url"),
        "score": sc.get("balanced_skill"),          # « Full score » de l'index
        "public": sc.get("public_skill"),
        "tie_band": v.get("rank_tie"),
        "coverage": m.get("coverage"),
        "domains": {c["id"]: round(c["skill"] * 100, 1)
                    for c in m.get("categories") or [] if c.get("skill") is not None},
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force-download", action="store_true")
    a = ap.parse_args()
    d = fetch(a.force_download)
    rows = [ligne(m) for m in d["models"] if (m.get("scores") or {}).get("balanced_skill") is not None]
    if (d.get("jev") or {}).get("scores"):
        rows.append(ligne(d["jev"], jev=True))
    rows.sort(key=lambda r: -r["score"])
    jb = fetch(a.force_download, JB_URL, JB_RAW)
    rows += jevbench(jb)
    suite = d.get("suite") or {}
    out = {
        "_generated": {
            "by": "pipeline/dm_ingest.py",
            "on": date.today().isoformat(),
            "upstream": f"Jev Decision Index — {suite.get('label', '')}",
            "upstream_url": SPACE,
            "data_url": DATA_URL,
            "upstream_generated_utc": d.get("generated_utc"),
            "hardware": suite.get("hardware"),
            "domains": {c["id"]: c["label"] for c in d.get("categories", [])},
            "jevbench": {"url": JB_PAGE, "api": JB_URL, "revision": jb.get("revision"),
                         "headline": "capability = moyenne exactitude + calibration, systèmes sous les "
                                     "plafonds de coût et de latence"},
            "warning": "Fichier généré. Relancer pipeline/dm_ingest.py, ne pas éditer.",
        },
        "scores": rows,
    }
    OUT.write_text(yaml.safe_dump(out, allow_unicode=True, sort_keys=False, width=100), encoding="utf-8")
    print(f"  écrit {OUT.relative_to(ROOT)} — {len(rows)} lignes (index {suite.get('label')}, "
          f"JevBench {jb.get('revision')})")
    assert all(0 <= r["score"] <= 100 for r in rows), "score hors échelle"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
