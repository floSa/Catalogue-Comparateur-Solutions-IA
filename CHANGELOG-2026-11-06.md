# Changelog — édition 2026-10

Comparaison avec l'instantané `2026-11-05.json`.

## Volumétrie

| | précédent | courant |
| :-- | --: | --: |
| Modèles | 162 | 162 |
| Harnais | 98 | 98 |
| Mesures | 972 | 972 |

## Nouveautés

- **Décision** : curseur de taille (seul le Jev Decision Index publie la taille), LLM généralistes
  masquables dans l'Artificial Analysis Decision Index, phrase expliquant que la catégorie et ses trois
  classements sont bâtis sur le format de Jev.
- **Décision — licences** : licence lue sur chaque dépôt Hugging Face (`pipeline/dm_ingest.py`, cache
  `sources/raw/hf_licences.json`) ; « licence non relevée » ou « licence maison » affichées au lieu d'un vide.
- **Contrôles communs** : filtre de licence dans LLM (accessibilité des poids selon Epoch), curseur de
  taille et top dans OCR, affichage 10 / 20 / tout dans tous les onglets.
- **Couverture** : filtrée dans SLM (au moins 2 scores par défaut, taille maximale), ajoutée dans OCR et
  Décision avec le même composant.
- **Légende de provenance commune** : mesuré par l'auteur du benchmark (plein), par un tiers (contour),
  publié par l'éditeur du modèle (hachuré).

---

Données de benchmark : Epoch AI — *Capabilities & Benchmarking* (CC-BY 4.0).
