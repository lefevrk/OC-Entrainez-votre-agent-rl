# Module `rl_pilot.config`

Chemins et paramètres communs, centralisés pour que les notebooks et les modules les partagent.

## Chemins

| Nom | Valeur |
|---|---|
| `PROJ_ROOT` | Racine du projet |
| `RAW_DATA_DIR` | `data/raw/` (immuable) |
| `INTERIM_DATA_DIR` | `data/interim/` |
| `PROCESSED_DATA_DIR` | `data/processed/` |
| `EXTERNAL_DATA_DIR` | `data/external/` |
| `MODELS_DIR` | `models/` |
| `REPORTS_DIR` | `reports/` |
| `FIGURES_DIR` | `reports/figures/` (figures des notebooks, publiées dans cette documentation) |

## Paramètres communs

| Nom | Valeur | Rôle |
|---|---|---|
| `SEED` | `42` | Valeur de graine de référence (son application aux générateurs aléatoires reste à la charge du développeur) |

## Sorties sans chemin personnel

Les sorties de notebook ne doivent révéler aucun chemin de la machine de l'auteur. `mask_path` remplace la racine du projet par `<PROJECT_ROOT>` et le dossier personnel par `~` (constantes `SAFE_ROOT_LABEL` et `SAFE_HOME_LABEL`).

::: rl_pilot.config.mask_path
