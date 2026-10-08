<!-- FICHIER GÉNÉRÉ par pipeline/build_guide.py — ne pas éditer.
     Corriger dans catalog/, puis régénérer. -->

# Agrégateurs cloud

7 outils au catalogue. Généré le 2026-10-08 depuis `catalog/tools.yaml`.

## Cloudflare AI Gateway

- **Éditeur :** Cloudflare
- **Site :** [https://developers.cloudflare.com/ai-gateway/](https://developers.cloudflare.com/ai-gateway/)
- **Tarifs :** [https://developers.cloudflare.com/ai-gateway/reference/pricing/](https://developers.cloudflare.com/ai-gateway/reference/pricing/)
- **Statut :** active
- **Capacités :** gratuit

Passerelle hébergée : journalisation, cache, limitation de débit. Fonctions de base gratuites. En facturation unifiée, 5 % de frais sur l'achat de crédits, inférence sans marge.

## Hugging Face Inference Providers

- **Éditeur :** Hugging Face
- **Site :** [https://huggingface.co/docs/inference-providers](https://huggingface.co/docs/inference-providers)
- **Tarifs :** [https://huggingface.co/docs/inference-providers/pricing](https://huggingface.co/docs/inference-providers/pricing)
- **Statut :** active
- **Capacités :** BYOK

Accès unifié à plusieurs fournisseurs d'inférence via un compte Hugging Face : tarif du fournisseur répercuté sans marge ; avec sa propre clé fournisseur, Hugging Face ne facture pas l'appel. Crédits inclus : aucun en Free, 2 $/mois en PRO.

## LiteLLM (proxy)

- **Éditeur :** BerriAI
- **Site :** [https://docs.litellm.ai/docs/](https://docs.litellm.ai/docs/)
- **Documentation :** [https://docs.litellm.ai/docs/](https://docs.litellm.ai/docs/)
- **Dépôt :** [https://github.com/BerriAI/litellm](https://github.com/BerriAI/litellm)
- **Statut :** active
- **Capacités :** BYOK, gratuit

Passerelle à héberger soi-même : une API au format OpenAI devant plus de 100 fournisseurs, avec ses propres clés. Open-source sous MIT (hors module entreprise, sous licence propre). Offre Enterprise sur devis.

## OpenRouter

- **Éditeur :** OpenRouter, Inc.
- **Site :** [https://openrouter.ai](https://openrouter.ai)
- **Documentation :** [https://openrouter.ai/docs](https://openrouter.ai/docs)
- **Tarifs :** [https://openrouter.ai/docs/faq](https://openrouter.ai/docs/faq)
- **Statut :** active
- **Capacités :** —

Passerelle universelle au format OpenAI : une clé pour tous les laboratoires. Aucune marge sur l'inférence — le tarif du fournisseur est répercuté tel quel. La facturation porte sur l'achat de crédits : 5,5 % par carte (0,80 $ minimum), 5 % en USDC. En BYOK, 5 % sur l'usage au-delà de 25 000 $/mois (200 000 $ en entreprise). Pas d'abonnement.

## Portkey

- **Éditeur :** Portkey AI
- **Site :** [https://portkey.ai](https://portkey.ai)
- **Dépôt :** [https://github.com/Portkey-AI/gateway](https://github.com/Portkey-AI/gateway)
- **Tarifs :** [https://portkey.ai/pricing](https://portkey.ai/pricing)
- **Statut :** active
- **Capacités :** gratuit

Passerelle open-source (MIT) à héberger soi-même, ou plateforme hébergée facturée au volume de journaux : Developer gratuit (10 000 journaux/mois), Production 49 $/mois pour 100 000 journaux puis 9 $ par tranche de 100 000.

## Requesty

- **Éditeur :** Requesty
- **Site :** [https://www.requesty.ai](https://www.requesty.ai)
- **Tarifs :** [https://www.requesty.ai/pricing](https://www.requesty.ai/pricing)
- **Statut :** active
- **Capacités :** BYOK, gratuit

Passerelle hébergée : 5 % de marge sur le coût des modèles. Offre gratuite limitée aux modèles gratuits, 200 requêtes par jour.

## Vercel AI Gateway

- **Éditeur :** Vercel
- **Site :** [https://vercel.com/docs/ai-gateway](https://vercel.com/docs/ai-gateway)
- **Tarifs :** [https://vercel.com/docs/ai-gateway/pricing](https://vercel.com/docs/ai-gateway/pricing)
- **Statut :** active
- **Capacités :** BYOK

Passerelle hébergée : aucune marge ni frais de plateforme sur les jetons, frais de paiement à la charge du client. Clés personnelles acceptées sans marge, mais l'achat de crédits reste obligatoire. Offre gratuite limitée à une partie des modèles. Options payantes (dont la rétention nulle à l'échelle de l'équipe, 0,10 $ pour 1 000 requêtes).

