# Changelog — édition 2026-09

Comparaison avec l'instantané `2026-10-23.json`.

## Modèles entrants

- `gpt-6.1-terra` (openai)

## État de l'art par benchmark

- `WeirdML v3` : nouveau suivi — 42.2% par `gpt-6-astra_xhigh`

## Benchmarks

- Section « Que mesure chaque benchmark ? » sous le graphique : pour chacun, ce qu'il évalue,
  comment il est noté et ce qu'il dit pour choisir un modèle (`catalog/benchmark_guide.yaml`).
- `WeirdML v3` entre au suivi : agents de code (Claude Code, Codex CLI, Gemini CLI, OpenCode,
  Kimi Code) sur 11 tâches d'apprentissage automatique, avec IC95 et coût par essai.
- `PostTrainBench` retiré : Epoch ne relaie plus ses mesures depuis juillet 2026.
- `OSWorld 2.0` retiré : en sommeil, classement officiel arrêté à Claude Opus 4.8.
- Descriptions corrigées sur sources primaires : GDP.pdf (questions sur des PDF
  professionnels, pas des livrables jugés par des experts), FrontierCode (acceptabilité par un
  mainteneur), CursorBench (version 4.0, harnais non publié), APEX-Agents, MirrorCode.
- Tous les benchmarks de l'export Epoch sont désormais classés : 14 suivis, 78 écartés avec leur motif.

## Tarifs

- `gpt-6.1-terra` : 1,00 / 0,05 / 5,00 $ par million de tokens (developers.openai.com).

## Volumétrie

| | précédent | courant |
| :-- | --: | --: |
| Modèles | 161 | 162 |
| Harnais | 98 | 98 |
| Mesures | 972 | 972 |

---

Données de benchmark : Epoch AI — *Capabilities & Benchmarking* (CC-BY 4.0).
