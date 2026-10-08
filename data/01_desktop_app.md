<!-- FICHIER GÉNÉRÉ par pipeline/build_guide.py — ne pas éditer.
     Corriger dans catalog/, puis régénérer. -->

# Applications desktop

10 outils au catalogue. Généré le 2026-10-08 depuis `catalog/tools.yaml`.

## ChatGPT Desktop

- **Éditeur :** OpenAI
- **Site :** [https://openai.com/chatgpt/desktop](https://openai.com/chatgpt/desktop)
- **Statut :** active
- **Capacités :** MCP

Application unique macOS et Windows regroupant trois espaces : Chat, Work et Codex. La fonction « Work with Apps » lit directement le contexte ouvert dans VS Code, Xcode, Terminal et iTerm2, sans copier-coller.

## Claude Desktop

- **Éditeur :** Anthropic, PBC
- **Site :** [https://claude.ai/download](https://claude.ai/download)
- **Statut :** active
- **Capacités :** MCP
- **Forfait Free :** gratuit — 0,00 € HT · 0,00 € TTC
- **Forfait Pro :** $20 — 17,33 € HT · 20,80 € TTC
- **Forfait Max :** $100 — 86,66 € HT · 103,99 € TTC

Windows et macOS. Serveurs MCP, accès fichiers et outils locaux.

## DeepSeek Harness

- **Éditeur :** DeepSeek
- **Site :** [https://deepseek.com/harness](https://deepseek.com/harness)
- **Documentation :** [https://deepseek-harness.github.io/deepseek-harness/](https://deepseek-harness.github.io/deepseek-harness/)
- **Dépôt :** [https://github.com/deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)
- **Statut :** active
- **Capacités :** BYOK, gratuit

Harnais officiel de DeepSeek, open-source sous MIT, en préversion développeur depuis août 2026 : l'éditeur annonce des ruptures de compatibilité. Distribué d'abord comme application de bureau (macOS Apple Silicon, Windows 64 bits), et comme interface web locale lancée par `npx @deepseek-ai/dsh web`. La commande `dsh` sert de lanceur (mode headless pour l'intégration continue, ACP, SDK) ; aucune interface terminal n'est livrée par défaut. Architecture où tout est greffon (framework Cordis).

## Google Antigravity

- **Éditeur :** Google
- **Site :** [https://antigravity.google/](https://antigravity.google/)
- **Tarifs :** [https://antigravity.google/pricing](https://antigravity.google/pricing)
- **Statut :** active
- **Capacités :** gratuit
- **Forfait Individuel :** gratuit — 0,00 € HT · 0,00 € TTC

Plateforme de développement agentique de Google, poste de commande pour plusieurs agents locaux : conversations organisées en projets, sous-agents personnalisés, tâches planifiées en arrière-plan. Version 2.0 annoncée à Google I/O le 19/05/2026. Gratuite pour un développeur individuel ; offre organisation via Google Cloud. Partage son harnais d'agent avec Antigravity CLI.

## Hermes Desktop

- **Éditeur :** Nous Research
- **Site :** [https://hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com)
- **Dépôt :** [https://github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- **Statut :** active
- **Capacités :** BYOK, gratuit

Application de bureau native de Hermes Agent, en préversion publique depuis juin 2026 (macOS, Windows, Linux), sous licence MIT. Même agent, mêmes compétences, même mémoire et mêmes sessions que la version terminal : on passe de l'une à l'autre sans perdre le contexte. Lancement depuis le terminal par `hermes desktop`, ou par installeur.

## Jan

- **Éditeur :** Menlo Research
- **Site :** [https://jan.ai](https://jan.ai)
- **Documentation :** [https://jan.ai/docs/desktop/api-server](https://jan.ai/docs/desktop/api-server)
- **Dépôt :** [https://github.com/janhq/jan](https://github.com/janhq/jan)
- **Statut :** active
- **Capacités :** modèles locaux, gratuit
- **Endpoint local :** `http://127.0.0.1:1337/v1`

Application de bureau qui fait tourner les modèles hors ligne sur le poste (moteur llama.cpp). Un serveur local compatible OpenAI s'active depuis les réglages, pour y brancher un harnais. Windows, macOS (Apple Silicon), Linux. Open-source sous Apache-2.0.

## Kimi Work

- **Éditeur :** Moonshot AI
- **Site :** [https://kimi.com](https://kimi.com)
- **Statut :** active
- **Capacités :** —

Agent desktop macOS et Windows conçu en local-first : lit les fichiers de la machine, pilote le navigateur et exécute des tâches planifiées. Annoncé avec un essaim pouvant atteindre 300 agents, réservé aux paliers élevés.

## LM Studio Bionic

- **Éditeur :** Element Labs, Inc.
- **Site :** [https://lmstudio.ai](https://lmstudio.ai)
- **Documentation :** [https://lmstudio.ai/docs](https://lmstudio.ai/docs)
- **Statut :** active
- **Capacités :** modèles locaux, gratuit

Agent pour le travail et le code, annonce par l'editeur comme couvrant les taches de developpement, l'automatisation et le controle de la machine.

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

