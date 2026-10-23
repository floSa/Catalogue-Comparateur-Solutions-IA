# Changelog — édition 2026-09

Comparaison avec l'instantané `2026-10-08.json`.

## Modèles entrants

- `Muse-Spark-Open-816B-A42B` (meta)
- `claude-haiku-5-5` (anthropic)
- `deepseek-v4.1-flash-1017` (deepseek)
- `kimi-k2.7-code-highspeed` (moonshot)
- `mistral-large-4-0` (mistral)
- `muse-wonder-1.0` (meta)

## Modèles sortants

- `claude-haiku-4-5-20251001`
- `claude-haiku-4-5-20251001_16K`
- `claude-haiku-4-5-20251001_1K`
- `claude-haiku-4-5-20251001_32K`
- `claude-haiku-4-5-20251001_8K`

## Mouvements tarifaires et de statut

- `gemini-3.5-flash` entrée : $1.5 → — •
- `gemini-3.5-flash` sortie : $9 → — •
- `gemini-3.7-flash` entrée : $0.75 → — •
- `gemini-3.7-flash` sortie : $3.75 → — •
- `mistral-large-4` entrée : $0.68 → $1.36 ↑
- `mistral-large-4` sortie : $2.09 → $4.18 ↑
- `muse-spark-1.1` entrée : — → $1.25 •
- `muse-spark-1.1` sortie : — → $4.25 •
- `muse-spark-1.2` entrée : — → $1.25 •
- `muse-spark-1.2` sortie : — → $4.25 •

## Relevés et corrections du 23/10/2026

- `claude-sonnet-5-5` entrée en cache : $0.20 → **$0.10** (la grille Anthropic facture la lecture en cache à 5 % de l'entrée pour Sonnet 5.5 ; la saisie du 02/10 était fausse).
- `claude-haiku-5-5` : 0,10 / 0,01 / 0,50 jusqu'à 100k jetons, 0,50 / 0,05 / 2,50 au-delà ; fenêtre 1M.
- `gemini-4-argon` : disponible pour tous depuis le 13/10 et inscrit sur la grille. Tarif promotionnel inchangé (2,00 / 0,10 / 10,00) mais limité au 30/11/2026, puis 4,00 / 0,20 / 20,00. Fenêtre relue : 1 048 576 jetons.
- `gemini-3.7-flash` et `gemini-3.5-flash` : dépréciés le 08/10, requêtes redirigées vers 3.8 Flash et 3.6 Flash, retirés de la grille.
- `mistral-large-4` : fin du tarif promotionnel (1,36 / 0,14 / 4,18) ; l'identifiant mesuré `mistral-large-4-0` désigne le même modèle.
- `kimi-k2.7-code-highspeed` : 1,90 / 0,38 / 8,00, fenêtre 262 144.
- `kimi-k3` : écriture en cache 3,00 $ (5 min) ou 6,00 $ (1 h).
- Z.ai : entrée en cache désormais affichée pour GLM-5.3-FlashX (0,075), GLM-5.2 et 5.1 (0,26), GLM-5 (0,20), GLM-4.7 (0,11).
- `muse-wonder-1.0` (Meta, sorti le 12/10) : 4,00 / 0,20 / 20,00, fenêtre 1 048 576. Muse Spark 1.2 et 1.1 réapparaissent sur la grille Meta à 1,25 / 0,15 / 4,25.
- `Muse-Spark-Open-816B-A42B` (15/10) : poids ouverts, non servi par l'API de Meta — pas de tarif éditeur.
- `deepseek-flash` sert DeepSeek-V4.1-Flash-1017 depuis le 17/10, au même tarif.

## Harnais

- `deepseek-harness` : six préversions du 09/10 au 23/10 (0.2.1-rc.3 sur npm), compatibilité expérimentale avec les mods de Claude Code, recherche web via les API Search et Fetch de DeepSeek.
- `muse-code` : forfait Maximum Usage à 200 $/mois, modèle Muse Wonder, SDK en préversion.
- Écartés avec motif : Elephant-Goldfish Model (plugin de compétences Google, pas un harnais) et Amplio (harnais de recherche Google DeepMind, non lancé comme produit).

## Ingestion

- HLE et DeepSWE : le fichier source a disparu des métadonnées Epoch ; rattaché à la main (`FALLBACK_FILE`).
- Terminal-Bench 4.0 : `Qwen3.8-Max-0902` rattaché à son identifiant Epoch (`ALIASES`).

## Sources consultées

| Laboratoire | Tarifs | Fenêtre de contexte, annonces |
| :-- | :-- | :-- |
| Anthropic | claude.com/pricing | platform.claude.com/docs/en/about-claude/models/overview |
| Google | ai.google.dev/gemini-api/docs/pricing | ai.google.dev/gemini-api/docs/models/gemini-4-argon, …/changelog |
| Moonshot | platform.kimi.ai/docs/pricing/chat (tableaux lus dans le code source de la page) | platform.kimi.ai/docs/models, …/platform-changelog |
| Z.ai | docs.z.ai/guides/overview/pricing | docs.z.ai/release-notes/new-released |
| Meta | dev.meta.ai/docs/pricing-rate-limits | dev.meta.ai/models/muse-wonder, research.meta.ai/blog |
| DeepSeek | api-docs.deepseek.com/quick_start/pricing/index.html | api-docs.deepseek.com/news/news261017 |
| Mistral | docs.mistral.ai/models/mistral-large-4-0 | idem |

## État de l'art par benchmark

- `GDP.pdf` : 34.2% `gpt-6-astra_max` → **35.0%** `gpt-6.1-sol_max`
- `GPQA diamond` : 95.8% `gpt-6-astra_max` → **96.4%** `gemini-4-argon_high`
- `Remote Labor Index` : 20.8% `gpt-6-astra_unknown` → **21.2%** `claude-opus-5-5_unknown`

## Volumétrie

| | précédent | courant |
| :-- | --: | --: |
| Modèles | 160 | 161 |
| Harnais | 65 | 65 |
| Mesures | 918 | 972 |

---

Données de benchmark : Epoch AI — *Capabilities & Benchmarking* (CC-BY 4.0).
