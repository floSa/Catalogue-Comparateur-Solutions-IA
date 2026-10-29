#!/usr/bin/env python3
"""Règles de la section SLM : fiches complètes, seuil de taille, rapprochements univoques."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml

CATALOG = Path(__file__).resolve().parent.parent / "catalog"
load = lambda n: yaml.safe_load((CATALOG / n).read_text(encoding="utf-8")) or {}


class TestSLM(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.slm, cls.sc = load("slm.yaml"), load("slm_scores.yaml")
        cls.classes = set(load("ocr.yaml")["licence_classes"])

    def test_fiches_completes(self):
        ids = [e["id"] for e in self.slm["entries"]]
        self.assertEqual(len(ids), len(set(ids)), "identifiant de fiche en double")
        for e in self.slm["entries"]:
            self.assertIn(e["licence_classe"], self.classes, e["id"])
            self.assertIn(e["architecture"], ("dense", "moe", "hybride", None), e["id"])
            self.assertTrue(e.get("url") and e.get("verified_on") and e.get("motif"), e["id"])
            # Seuil : 35 Md annoncés ; le compte exact des poids peut dépasser de moins de 1 Md.
            self.assertLess(e["params_total_b"], 36, e["id"])
            if e["architecture"] == "moe":
                self.assertLess(e.get("params_actifs_b") or 0, e["params_total_b"], e["id"])

    def test_une_ligne_une_fiche_au_plus(self):
        norm = lambda x: re.sub(r"[^a-z0-9.]+", "-", x.lower()).strip("-")
        for r in self.sc["scores"]:
            hits = [e["id"] for e in self.slm["entries"] if re.search(e["motif"], norm(r["name"]))]
            self.assertEqual(hits, [r["entry"]], r["name"])

    def test_scores(self):
        b = {x["id"]: x for x in self.slm["benchmarks"]}
        for r in self.sc["scores"]:
            self.assertIn(r["benchmark"], b)
            if b[r["benchmark"]]["max"]:
                self.assertTrue(0 <= r["score"] <= b[r["benchmark"]]["max"], r)
            if r.get("ci"):
                self.assertLessEqual(r["ci"][0], r["ci"][1], r)


if __name__ == "__main__":
    unittest.main()
