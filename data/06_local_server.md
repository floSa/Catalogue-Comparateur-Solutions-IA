<!-- FICHIER GÉNÉRÉ par pipeline/build_guide.py — ne pas éditer.
     Corriger dans catalog/, puis régénérer. -->

# Serveurs locaux

8 outils au catalogue. Généré le 2026-10-08 depuis `catalog/tools.yaml`.

## LM Studio (serveur local)

- **Éditeur :** Element Labs, Inc.
- **Site :** [https://lmstudio.ai](https://lmstudio.ai)
- **Statut :** active
- **Capacités :** modèles locaux, gratuit
- **Endpoint local :** `http://localhost:1234/v1`

Charge des modeles GGUF et expose un serveur HTTP compatible API OpenAI, auquel se branchent les harnais de la couche 1.

## LocalAI

- **Éditeur :** LocalAI (open-source)
- **Site :** [https://localai.io](https://localai.io)
- **Documentation :** [https://localai.io/docs/installation/](https://localai.io/docs/installation/)
- **Dépôt :** [https://github.com/mudler/LocalAI](https://github.com/mudler/LocalAI)
- **Statut :** active
- **Capacités :** modèles locaux, gratuit
- **Endpoint local :** `http://localhost:8080/v1`

Serveur local multimodal (texte, vision, voix, image, vidéo) qui fédère plus de 60 moteurs, dont llama.cpp, vLLM, SGLang et MLX, derrière une même API compatible OpenAI et Anthropic. Fonctionne sans GPU. Interface web intégrée. Open-source sous MIT.

## MLX-LM (serveur)

- **Éditeur :** ml-explore (Apple)
- **Documentation :** [https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md)
- **Dépôt :** [https://github.com/ml-explore/mlx-lm](https://github.com/ml-explore/mlx-lm)
- **Statut :** active
- **Capacités :** modèles locaux, gratuit
- **Endpoint local :** `http://localhost:8080/v1`

Exécution des modèles sur Apple Silicon via le framework MLX ; `mlx_lm.server` expose une API proche de celle d'OpenAI. L'éditeur le déconseille en production (contrôles de sécurité minimaux). Open-source sous MIT.

## Ollama

- **Éditeur :** Ollama
- **Site :** [https://ollama.com](https://ollama.com)
- **Statut :** active
- **Capacités :** modèles locaux, gratuit
- **Endpoint local :** `http://localhost:11434/v1`

Serveur local compatible OpenAI.

## SGLang

- **Éditeur :** SGLang Project
- **Site :** [https://sglang.io](https://sglang.io)
- **Documentation :** [https://docs.sglang.io](https://docs.sglang.io)
- **Dépôt :** [https://github.com/sgl-project/sglang](https://github.com/sgl-project/sglang)
- **Statut :** active
- **Capacités :** modèles locaux, gratuit
- **Endpoint local :** `http://localhost:30000/v1`

Moteur de service haute performance, concurrent direct de vLLM : même usage (plusieurs utilisateurs, GPU NVIDIA ou AMD, TPU), service distribué possible. API compatible OpenAI. Open-source sous Apache-2.0.

## llama.cpp (llama-server)

- **Éditeur :** ggml-org
- **Site :** [https://llama.app](https://llama.app)
- **Documentation :** [https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- **Dépôt :** [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
- **Statut :** active
- **Capacités :** modèles locaux, gratuit
- **Endpoint local :** `http://127.0.0.1:8080/v1`

Moteur d'inférence en C/C++ pour les modèles GGUF, sur lequel s'appuient LM Studio, Jan ou KoboldCpp. Son serveur (`llama-server`, ou `llama serve`) expose une API compatible OpenAI et une interface web. Tourne sur CPU seul, Apple Silicon, NVIDIA, AMD, Intel ou Vulkan, et en mode hybride CPU + GPU. Open-source sous MIT.

## llamafile

- **Éditeur :** Mozilla.ai
- **Site :** [https://docs.mozilla.ai/llamafile](https://docs.mozilla.ai/llamafile)
- **Documentation :** [https://docs.mozilla.ai/llamafile](https://docs.mozilla.ai/llamafile)
- **Dépôt :** [https://github.com/mozilla-ai/llamafile](https://github.com/mozilla-ai/llamafile)
- **Statut :** active
- **Capacités :** modèles locaux, gratuit
- **Endpoint local :** `http://127.0.0.1:8080/v1`

Un modèle et son moteur réunis en un seul exécutable, sans installation : on le télécharge, on le lance. Construit sur llama.cpp ; API compatible OpenAI et interface web intégrées. CPU, Apple Silicon, NVIDIA, AMD, Vulkan. Open-source sous Apache-2.0.

## vLLM

- **Éditeur :** vLLM Project
- **Site :** [https://vllm.ai](https://vllm.ai)
- **Documentation :** [https://docs.vllm.ai/en/latest/](https://docs.vllm.ai/en/latest/)
- **Dépôt :** [https://github.com/vllm-project/vllm](https://github.com/vllm-project/vllm)
- **Statut :** active
- **Capacités :** modèles locaux, gratuit
- **Endpoint local :** `http://localhost:8000/v1`

Moteur de service à haut débit, conçu pour servir plusieurs utilisateurs à la fois sur GPU (NVIDIA, AMD, Intel) ou CPU, depuis un poste ou un serveur interne. API compatible OpenAI et Anthropic. Open-source sous Apache-2.0. C'est le remplaçant recommandé par Hugging Face pour TGI.

