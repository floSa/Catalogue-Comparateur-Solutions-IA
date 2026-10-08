# Changelog — édition 2026-09

Comparaison avec l'instantané `2026-10-02.json`.

## Modèles entrants

- `codestral-2508` (mistral)
- `deepseek-v4.1-flash_none` (deepseek)
- `ministral-3-14b-2512` (mistral)
- `ministral-3-3b-2512` (mistral)
- `ministral-3-8b-2512` (mistral)
- `mistral-large-4` (mistral)
- `mistral-small-2603` (mistral)
- `muse-glimmer` (meta)

## Modèles sortants

- `gpt-5-pro-2025-10-06`

## État de l'art par benchmark

- `APEX-Agents` : 75.5% `claude-sonnet-5-5_max` → **82.2%** `gemini-4-argon_unknown`
- `GDP.pdf` : 30.7% `gpt-5.6-sol_unknown` → **34.2%** `gpt-6-astra_max`
- `Terminal-Bench 4.0` : 58.2% `gpt-6-astra_max` → **64.8%** `claude-opus-5-5_max` (harnais : Claude Code)

## Harnais

- entrant : `deepseek-harness`
- entrant : `factory-droid`
- entrant : `hermes-desktop`
- entrant : `oh-my-pi`
- entrant : `pi`
- entrant : `amp`
- entrant : `cloudflare-ai-gateway`
- entrant : `copilot-cli`
- entrant : `crush`
- entrant : `cursor-cli`
- entrant : `freebuff`
- entrant : `gemini-cli`
- entrant : `goose`
- entrant : `hf-inference-providers`
- entrant : `jan`
- entrant : `jetbrains-ai`
- entrant : `kilo-code`
- entrant : `kiro`
- entrant : `kiro-cli`
- entrant : `litellm`
- entrant : `llama-cpp`
- entrant : `llamafile`
- entrant : `localai`
- entrant : `mlx-lm`
- entrant : `sglang`
- entrant : `tabnine`
- entrant : `vercel-ai-gateway`
- entrant : `vllm`
- entrant : `warp`
- entrant : `github-copilot-app`
- entrant : `junie-cli`
- entrant : `kiro-crew`
- `continue` : active → retired (a rejoint Cursor, dépôt en lecture seule)
- `windsurf` : unknown → active (renommé Devin Desktop)

## Catégories corrigées

Relevé sur la forme principale proposée par chaque éditeur (site officiel, page de téléchargement, dépôt) :

- `deepseek-harness` : agents CLI → applications desktop
- `factory-droid` : agents CLI → applications desktop
- `freebuff` : agents CLI → applications desktop
- `goose` : agents CLI → applications desktop
- `openhands` : agents CLI → applications desktop (Agent Canvas, interface servie en local)
- `kimi-cli` (Kimi Code) : agents CLI → applications desktop
- `cline` : extensions VS Code → applications desktop
- `zcode` : IDE dérivés → applications desktop

## Volumétrie

| | précédent | courant |
| :-- | --: | --: |
| Modèles | 153 | 160 |
| Harnais | 33 | 65 |
| Mesures | 848 | 918 |

---

Données de benchmark : Epoch AI — *Capabilities & Benchmarking* (CC-BY 4.0).
