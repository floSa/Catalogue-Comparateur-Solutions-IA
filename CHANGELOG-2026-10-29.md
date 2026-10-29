# Changelog — édition 2026-10

Comparaison avec l'instantané `2026-10-28.json`.

## Volumétrie

| | précédent | courant |
| :-- | --: | --: |
| Modèles | 162 | 162 |
| Harnais | 98 | 98 |
| Mesures | 972 | 972 |

## Nouveautés

- **Onglet SLM (petits modèles ouverts).** 102 modèles à poids ouverts de 35 Md de
  paramètres ou moins (51 familles : Gemma 4, Qwen 3.5/3.6/3.8, Ministral 3, Granite 4.2,
  gpt-oss-20b, Nemotron 3.5, OLMo 3, Phi-4, GLM-4.7-Flash, MiniCPM…), avec taille totale
  et active, architecture (dense, MoE, hybride), contexte, licence. Sources : fiches
  Hugging Face des éditeurs. 137 modèles écartés, chacun avec son motif.
- **Scores tiers des petits modèles** : Epoch Capabilities Index, GPQA Diamond et OTIS
  Mock AIME (Epoch AI), LMArena texte, Vectara (hallucinations) — 35 scores, 18 modèles.
  Nouveau script `pipeline/slm_ingest.py`. 12 sources examinées et écartées, avec motif.
- **Méthodologie** passe de l'onglet à un bouton dans l'en-tête.

---

Données de benchmark : Epoch AI — *Capabilities & Benchmarking* (CC-BY 4.0).
