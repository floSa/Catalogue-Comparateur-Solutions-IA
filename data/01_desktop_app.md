<!-- FICHIER GÉNÉRÉ par pipeline/build_guide.py — ne pas éditer.
     Corriger dans catalog/, puis régénérer. -->

# Applications desktop

19 outils au catalogue. Généré le 2026-10-08 depuis `catalog/tools.yaml`.

## ChatGPT Desktop

- **Éditeur :** OpenAI
- **Site :** [https://learn.chatgpt.com/docs/app](https://learn.chatgpt.com/docs/app)
- **Statut :** active
- **Capacités :** MCP

Application unique regroupant trois espaces : Chat, Work et Codex. macOS et Windows ; Linux en préversion. Serveurs MCP pris en charge.

## Claude Desktop

- **Éditeur :** Anthropic, PBC
- **Site :** [https://claude.com/download](https://claude.com/download)
- **Statut :** active
- **Capacités :** MCP
- **Forfait Free :** gratuit — 0,00 € HT · 0,00 € TTC
- **Forfait Pro :** $20 — 17,33 € HT · 20,80 € TTC
- **Forfait Max :** $100 — 86,66 € HT · 103,99 € TTC

macOS et Windows ; Linux en bêta (Ubuntu, Debian). Serveurs MCP, accès aux fichiers et outils locaux.

## Cline

- **Éditeur :** Cline Bot Inc.
- **Site :** [https://cline.bot](https://cline.bot)
- **Dépôt :** [https://github.com/cline/cline](https://github.com/cline/cline)
- **Statut :** active
- **Capacités :** BYOK, modèles locaux, MCP, gratuit

Agent de code open-source (Apache-2.0), désormais proposé d'abord en application de bureau (macOS, Windows, Linux, sans éditeur), et toujours en extension VS Code, en extension JetBrains (accès anticipé) et en CLI. Clés personnelles, modèles locaux (Ollama, LM Studio), MCP. Approbation humaine de chaque action.

## DeepSeek Harness

- **Éditeur :** DeepSeek
- **Site :** [https://deepseek.com/harness](https://deepseek.com/harness)
- **Documentation :** [https://deepseek-harness.github.io/deepseek-harness/](https://deepseek-harness.github.io/deepseek-harness/)
- **Dépôt :** [https://github.com/deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)
- **Statut :** active
- **Capacités :** BYOK, gratuit

Harnais officiel de DeepSeek, open-source sous MIT, en préversion développeur depuis août 2026 : l'éditeur annonce des ruptures de compatibilité. Distribué d'abord comme application de bureau (macOS Apple Silicon, Windows 64 bits), et comme interface web locale lancée par `npx @deepseek-ai/dsh web`. La commande `dsh` sert de lanceur (mode headless pour l'intégration continue, ACP, SDK) ; aucune interface terminal n'est livrée par défaut. Architecture où tout est greffon (framework Cordis).

## Droid (Factory)

- **Éditeur :** Factory
- **Site :** [https://factory.com](https://factory.com)
- **Documentation :** [https://docs.factory.com/cli/getting-started/overview](https://docs.factory.com/cli/getting-started/overview)
- **Tarifs :** [https://factory.com/pricing](https://factory.com/pricing)
- **Statut :** active
- **Capacités :** BYOK, modèles locaux, MCP

Agent de développement de Factory, proposé d'abord en application de bureau (Factory App, macOS et Windows), et aussi en CLI (commande `droid`, mode non interactif `droid exec`) et en SDK. Code fermé. Clés personnelles (OpenAI, Anthropic, fournisseurs open-source) et modèles locaux acceptés en BYOK. Forfaits Pro 20 $/mois, Plus 100 $/mois, Max 200 $/mois ; Teams 60 $/mois + 40 $ par siège.

## Freebuff

- **Éditeur :** CodebuffAI
- **Site :** [https://freebuff.com](https://freebuff.com)
- **Dépôt :** [https://github.com/CodebuffAI/freebuff](https://github.com/CodebuffAI/freebuff)
- **Statut :** active
- **Capacités :** gratuit

Agent de code gratuit sans clé d'API : l'accès aux modèles inclus est financé par des publicités textuelles ; des forfaits payants donnent accès à d'autres modèles. Proposé d'abord en application de bureau (macOS, Windows, Linux), aussi en CLI, sur le web et dans le cloud. Open-source sous Apache-2.0, construit sur Codebuff.

## GitHub Copilot (application)

- **Éditeur :** GitHub / Microsoft
- **Site :** [https://github.com/features/copilot](https://github.com/features/copilot)
- **Tarifs :** [https://github.com/features/copilot/plans](https://github.com/features/copilot/plans)
- **Statut :** active
- **Capacités :** —

Application de bureau de GitHub Copilot, mise en avant en premier sur la page produit (macOS, Windows, Linux). Mêmes forfaits que les extensions et la CLI.

## Google Antigravity

- **Éditeur :** Google
- **Site :** [https://antigravity.google/](https://antigravity.google/)
- **Tarifs :** [https://antigravity.google/pricing](https://antigravity.google/pricing)
- **Statut :** active
- **Capacités :** gratuit
- **Forfait Individuel :** gratuit — 0,00 € HT · 0,00 € TTC

Plateforme de développement agentique de Google, poste de commande pour plusieurs agents locaux : conversations organisées en projets, sous-agents personnalisés, tâches planifiées en arrière-plan. Version 2.0 annoncée à Google I/O le 19/05/2026. Gratuite pour un développeur individuel ; offre organisation via Google Cloud. Partage son harnais d'agent avec Antigravity CLI.

## Goose

- **Éditeur :** Agentic AI Foundation (Linux Foundation)
- **Site :** [https://goose-docs.ai/](https://goose-docs.ai/)
- **Documentation :** [https://goose-docs.ai/docs/getting-started/installation](https://goose-docs.ai/docs/getting-started/installation)
- **Dépôt :** [https://github.com/aaif-goose/goose](https://github.com/aaif-goose/goose)
- **Statut :** active
- **Capacités :** BYOK, modèles locaux, MCP, gratuit

Agent open-source (Apache-2.0) lancé par Block, désormais hébergé par l'Agentic AI Foundation, aux côtés de MCP et d'AGENTS.md. Application de bureau en tête, puis CLI et API. Plus de 15 fournisseurs, modèles locaux via Ollama, plus de 70 extensions MCP. Se présente comme un agent généraliste, pas seulement de code.

## Hermes Desktop

- **Éditeur :** Nous Research
- **Site :** [https://hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com)
- **Dépôt :** [https://github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- **Statut :** active
- **Capacités :** BYOK, gratuit

Application de bureau de Hermes Agent, mise en avant en premier sur le site de l'éditeur ; sortie en juin 2026, considérée comme stable depuis la v0.17.0. macOS et Windows, sous licence MIT. Même agent, mêmes compétences, même mémoire et mêmes sessions que la version terminal. Lancement depuis le terminal par `hermes desktop`, ou par installeur.

## Jan

- **Éditeur :** Menlo Research
- **Site :** [https://jan.ai](https://jan.ai)
- **Documentation :** [https://jan.ai/docs/desktop/api-server](https://jan.ai/docs/desktop/api-server)
- **Dépôt :** [https://github.com/janhq/jan](https://github.com/janhq/jan)
- **Statut :** active
- **Capacités :** modèles locaux, gratuit
- **Endpoint local :** `http://127.0.0.1:1337/v1`

Application de bureau qui fait tourner les modèles hors ligne sur le poste (moteur llama.cpp). Un serveur local compatible OpenAI s'active depuis les réglages, pour y brancher un harnais. Windows, macOS (Apple Silicon), Linux. Open-source sous Apache-2.0.

## Kimi Code

- **Éditeur :** Moonshot AI
- **Site :** [https://www.kimi.com/code](https://www.kimi.com/code)
- **Documentation :** [https://moonshotai.github.io/kimi-code/en/](https://moonshotai.github.io/kimi-code/en/)
- **Dépôt :** [https://github.com/MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code)
- **Statut :** active
- **Capacités :** —

Agent de code de Moonshot, décliné en application de bureau (mise en avant en premier), en CLI (binaire autonome, sans Node.js) et en extensions IDE via le protocole ACP (Zed, JetBrains). Le dépôt historique MoonshotAI/kimi-cli est archivé ; au premier lancement, l'outil propose de migrer configuration et sessions.

## Kimi Work

- **Éditeur :** Moonshot AI
- **Site :** [https://www.kimi.com/products/kimi-work](https://www.kimi.com/products/kimi-work)
- **Statut :** active
- **Capacités :** —

Agent de bureau pour Windows et Mac Apple Silicon : lit les fichiers de la machine, pilote le navigateur et exécute des tâches planifiées. Annoncé avec un essaim pouvant atteindre 300 agents.

## Kiro Crew

- **Éditeur :** Amazon Web Services
- **Site :** [https://kiro.dev/crew/](https://kiro.dev/crew/)
- **Dépôt :** [https://github.com/kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew)
- **Statut :** active
- **Capacités :** gratuit

Espace de travail de développement persistant, open-source (Apache-2.0), qui tourne sur la machine de l'utilisateur ou sur un serveur : application de bureau (macOS, Windows, Linux), tableau de bord web, CLI, Slack et Discord. Tâches longues sans surveillance, travaux planifiés. Mis en avant en premier sur kiro.dev.

## LM Studio Bionic

- **Éditeur :** Element Labs, Inc.
- **Site :** [https://lmstudio.ai](https://lmstudio.ai)
- **Documentation :** [https://lmstudio.ai/docs/bionic](https://lmstudio.ai/docs/bionic)
- **Statut :** active
- **Capacités :** modèles locaux, gratuit

Agent pour le travail et le code, annonce par l'editeur comme couvrant les taches de developpement, l'automatisation et le controle de la machine.

## OpenHands

- **Éditeur :** OpenHands
- **Site :** [https://www.openhands.dev](https://www.openhands.dev)
- **Dépôt :** [https://github.com/OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- **Tarifs :** [https://www.openhands.dev/pricing](https://www.openhands.dev/pricing)
- **Statut :** active
- **Capacités :** BYOK, gratuit

Agent d'ingénierie open-source (MIT), proposé d'abord sous forme d'Agent Canvas : une interface graphique servie en local, sur la machine du développeur ; aussi en interface terminal, en CLI, en SDK et en cloud. Sandbox Docker facultative. Offre cloud individuelle gratuite (clé personnelle ou fournisseurs à prix coûtant) ; seule l'offre Enterprise est payante.

## Qwen Studio

- **Éditeur :** Alibaba
- **Site :** [https://chat.qwen.ai](https://chat.qwen.ai)
- **Statut :** active
- **Capacités :** gratuit

Application desktop Windows et macOS donnant accès aux modèles Qwen : recherche approfondie, analyse de documents, génération d'images et de vidéo. Orientée usage général plutôt que développement.

## Warp

- **Éditeur :** Warp
- **Site :** [https://www.warp.dev](https://www.warp.dev)
- **Documentation :** [https://docs.warp.dev](https://docs.warp.dev)
- **Dépôt :** [https://github.com/warpdotdev/warp](https://github.com/warpdotdev/warp)
- **Tarifs :** [https://www.warp.dev/pricing](https://www.warp.dev/pricing)
- **Statut :** active
- **Capacités :** BYOK, gratuit

Terminal doté d'agents de code intégrés, dont le code est devenu public sous AGPL-3.0. Son agent existe aussi en CLI utilisable dans n'importe quel terminal. Forfaits : Free 0 $ (inférence personnelle possible), Build 20 $/mois, Max 200 $/mois, Business 50 $/utilisateur/mois.

## ZCode

- **Éditeur :** Z.ai (Zhipu AI)
- **Site :** [https://zcode.z.ai/en](https://zcode.z.ai/en)
- **Documentation :** [https://zcode.z.ai/en/docs/welcome](https://zcode.z.ai/en/docs/welcome)
- **Statut :** active
- **Capacités :** —
- **Forfait Lite :** $12.6 — 10,92 € HT · 13,10 € TTC
- **Forfait Pro :** $56 — 48,53 € HT · 58,24 € TTC
- **Forfait Max :** $117.6 — 101,91 € HT · 122,29 € TTC

Environnement de développement agentique (ADE) livré en application de bureau, présenté par l'éditeur comme le harnais officiel de GLM-5.3 — pas un éditeur dérivé de VS Code. macOS (Apple Silicon et Intel), Windows (x64 et ARM64), Linux x64 et ARM64 en bêta. Gestion de tâches longues par « Goals », pilotage à distance depuis WeChat, Feishu ou Telegram, collaboration multi-agents.

