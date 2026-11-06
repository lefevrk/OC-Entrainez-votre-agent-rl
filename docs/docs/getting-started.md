# Démarrage

## Installation

Le projet utilise [uv](https://docs.astral.sh/uv/) :

```bash
uv sync
```

!!! note
    Le dossier `data/` est ignoré par git : les données doivent être copiées manuellement. `data/raw/` est **immuable**, aucune étape ne le modifie.

## Commandes utiles

```bash
make data    # Préparer le jeu de données
make lint    # Vérifier le formatage et le linting
make format  # Appliquer le formatage et les corrections Ruff
make test    # Exécuter les tests
```

## Construire cette documentation

```bash
uv run mkdocs serve -f docs/mkdocs.yml   # aperçu local
uv run mkdocs build -f docs/mkdocs.yml   # génération du site, dans docs/site
```
