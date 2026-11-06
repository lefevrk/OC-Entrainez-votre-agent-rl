# Conventions

Les règles de travail du projet : nommage des notebooks, organisation du code et workflow git.

## Notebooks

Les notebooks se nomment `PHASE.NUMÉRO-initiales-description` (standard cookiecutter-data-science), par exemple `01.01-kl-data-exploration`.

Règles communes :

- Un notebook **raconte une analyse** : il pose des questions, mesure, conclut. Son texte se lit seul.
- La **logique réutilisable vit dans `src/`** et est testée par `pytest` ; les notebooks l'importent.
- Les sorties ne contiennent **aucun chemin personnel** : voir [`rl_pilot.config`](reference/config.md).
- Les notebooks sont **modifiés sur place**, jamais régénérés par un script.

## Code

- Le code du projet est dans `src/rl_pilot/`.
- Docstrings au format Google, en français ; la documentation de référence est générée à partir d'elles.
- Dans `src/`, une condition invalide **lève une exception explicite** : `assert` est réservé aux notebooks et aux tests.
- Avant chaque commit, `pre-commit` vérifie le formatage (`ruff`), le linting et lance les tests.

```bash
make lint    # Vérifier le formatage et le linting
make format  # Appliquer le formatage et les corrections
make test    # Exécuter les tests
```

## Workflow git

Le dépôt suit un **git-flow** :

| Branche | Rôle |
|---|---|
| `main` | Version publiée. La documentation est construite depuis cette branche |
| `develop` | Intégration des travaux terminés |
| `feature/...` | Un chantier, créé depuis `develop` |
| `release/x.y.z` | Préparation d'une version, fusionnée dans `main` et `develop` |

Les messages de commit suivent le format `type(portée): message`, en anglais, à l'impératif : `feat(notebooks)`, `fix`, `refactor`, `test`, `docs`, `build`, `chore`.

Dans une branche, l'ordre habituel est : le notebook d'abord, puis le code extrait dans `src/`, puis les tests, puis la documentation.
