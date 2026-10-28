#!/usr/bin/env python3
"""Règles de la section OCR : chaque score est sourcé, daté et porte sa provenance."""
from __future__ import annotations

import unittest
from pathlib import Path

import yaml

CATALOG = Path(__file__).resolve().parent.parent / "catalog"
load = lambda n: yaml.safe_load((CATALOG / n).read_text(encoding="utf-8")) or {}


class TestOCR(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ocr, cls.ob = load("ocr.yaml"), load("ocr_benchmarks.yaml")
        cls.ids = {e["id"] for e in cls.ocr["entries"]}

    def test_fiches_completes(self):
        classes = set(self.ocr["licence_classes"])
        self.assertEqual(len(self.ids), len(self.ocr["entries"]), "identifiant de fiche en double")
        for e in self.ocr["entries"]:
            self.assertIn(e["famille"], {"modele", "moteur", "chaine"}, e["id"])
            self.assertIn(e["licence_classe"], classes, e["id"])
            self.assertTrue(e.get("url") and e.get("verified_on"), e["id"])

    def test_scores_sources_et_provenance(self):
        bids = {b["id"] for b in self.ob["benchmarks"]}
        for r in self.ob["scores"]:
            self.assertIn(r["benchmark"], bids)
            self.assertIn(r["provenance"], {"officiel", "editeur", "tiers"})
            self.assertTrue(r.get("source_url") and r.get("verified_on"), r["model"])
            self.assertTrue(0 <= r["score"] <= 100, r)
            if r.get("entry"):
                self.assertIn(r["entry"], self.ids, r["model"])

    def test_un_seul_score_par_outil_et_benchmark(self):
        # Un chiffre éditeur ou tiers ne double jamais une ligne du classement officiel.
        vus = {}
        for r in self.ob["scores"]:
            if r.get("entry"):
                k = (r["benchmark"], r["entry"])
                if k in vus:
                    self.assertEqual({vus[k], r["provenance"]}, {"officiel"},
                                     f"{k} : score officiel doublé par un chiffre {r['provenance']}")
                vus[k] = r["provenance"]


if __name__ == "__main__":
    unittest.main()
