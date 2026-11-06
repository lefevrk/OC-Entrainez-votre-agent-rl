# Décisions

Les choix faits pendant le projet, avec leur justification.

## Les données brutes restent immuables

**Décision.** `data/raw/` n'est jamais modifié. Toute transformation produit un fichier dans `data/interim/` ou `data/processed/`.

**Raison.** Le traitement reste rejouable et on peut toujours revenir aux données d'origine.

## La logique vit dans `src/`, pas dans les notebooks

**Décision.** Le code réutilisable est dans `rl_pilot`, testé par `pytest`. Les notebooks importent ces fonctions.

**Raison.** Une même logique n'est écrite qu'une fois, elle est testable, et les notebooks restent des supports d'analyse.
