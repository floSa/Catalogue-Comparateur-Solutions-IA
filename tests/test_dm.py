#!/usr/bin/env python3
"""Règles de la section Modèles de décision : fiches complètes, rapprochements univoques."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml

CATALOG = Path(__file__).resolve().parent.parent / "catalog"
load = lambda n: yaml.safe_load((CATALOG / n).read_text(encoding="utf-8")) or {}


class TestDM(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dm, cls.sc = load("dm.yaml"), load("dm_scores.yaml")
        cls.classes = set(load("ocr.yaml")["licence_classes"])

    def test_fiches_completes(self):
        ids = [e["id"] for e in self.dm["entries"]]
        self.assertEqual(len(ids), len(set(ids)), "identifiant de fiche en double")
        for e in self.dm["entries"]:
            self.assertIn(e["licence_classe"], self.classes, e["id"])
            self.assertTrue(e.get("url") and e.get("verified_on") and e.get("motif"), e["id"])

    def test_une_ligne_une_fiche_au_plus(self):
        # Deux motifs qui attrapent la même ligne attribueraient un score à la mauvaise fiche.
        noms = [r["name"] for r in self.sc["scores"]] + [r["model"] for r in self.dm["aa_scores"]]
        for n in noms:
            hits = [e["id"] for e in self.dm["entries"] if re.search(e["motif"], n)]
            self.assertLessEqual(len(hits), 1, f"{n} rattaché à {hits}")

    def test_scores_sources(self):
        bids = {b["id"] for b in self.dm["benchmarks"]}
        for r in self.sc["scores"] + self.dm["aa_scores"]:
            self.assertIn(r["benchmark"], bids)
            self.assertTrue(0 <= r["score"] <= 100, r)
        for r in self.dm["aa_scores"]:
            self.assertTrue(r.get("source_url") and r.get("verified_on"))


if __name__ == "__main__":
    unittest.main()
