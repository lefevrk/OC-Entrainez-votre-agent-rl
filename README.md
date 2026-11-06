<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Entraînez votre agent RL</h3>

  <p align="center">
    Entraînement d'un agent d'apprentissage par renforcement.
    <br />
    <a href="https://lefevrk.github.io/OC-Entrainez-votre-agent-rl/"><strong>Explorer la doc »</strong></a>
    <br />
    <br />
    <a href="https://github.com/lefevrk/OC-Entrainez-votre-agent-rl/issues/new?labels=bug&template=bug_report.md">Signaler un bug</a>
    &middot;
    <a href="https://github.com/lefevrk/OC-Entrainez-votre-agent-rl/issues/new?labels=enhancement&template=feature_request.md">Proposer une fonctionnalité</a>
  </p>

  [![Docs](https://github.com/lefevrk/OC-Entrainez-votre-agent-rl/actions/workflows/docs.yml/badge.svg)](https://github.com/lefevrk/OC-Entrainez-votre-agent-rl/actions/workflows/docs.yml)
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Sommaire</summary>
  <ol>
    <li><a href="#à-propos-du-projet">À propos du projet</a></li>
    <li>
      <a href="#démarrage">Démarrage</a>
      <ul>
        <li><a href="#prérequis">Prérequis</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#utilisation">Utilisation</a></li>
    <li><a href="#organisation-du-projet">Organisation du projet</a></li>
    <li><a href="#remerciements">Remerciements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## À propos du projet

Ce dépôt contient le projet *Entraînez votre agent RL* du parcours OpenClassrooms AI Engineer.

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

<!-- GETTING STARTED -->
## Démarrage

### Prérequis

- [Python 3.12+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) pour gérer les dépendances

### Installation

1. Cloner le dépôt
   ```bash
   git clone https://github.com/lefevrk/OC-Entrainez-votre-agent-rl.git
   cd OC-Entrainez-votre-agent-rl
   ```

2. Installer les dépendances
   ```bash
   uv sync
   ```

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

<!-- USAGE EXAMPLES -->
## Utilisation

Détail complet dans la [documentation](docs/docs/getting-started.md).

### Consulter la documentation

```bash
uv run mkdocs serve -f docs/mkdocs.yml
```

### Commandes utiles

```bash
make data          # Préparer le jeu de données
make lint          # Vérifier le formatage et le linting
make format        # Appliquer le formatage et les corrections Ruff
make test          # Exécuter les tests
make docs          # Construire le site de documentation
```

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

## Organisation du projet

```
├── Makefile           <- Commandes de développement courantes
├── README.md          <- Documentation principale du projet
├── data
│   ├── external       <- Données provenant de sources tierces
│   ├── interim        <- Données intermédiaires transformées
│   ├── processed      <- Données prêtes pour la modélisation
│   └── raw            <- Données brutes immuables
│
├── docs               <- Documentation MkDocs (voir docs/mkdocs.yml)
│
├── models             <- Modèles entraînés et prédictions sérialisées
│
├── notebooks          <- Notebooks d'exploration et de modélisation
│
├── pyproject.toml     <- Métadonnées du package `rl-pilot` et outils de développement
│
├── references         <- Énoncé de la mission et livrables attendus
│
├── reports
│   └── figures        <- Graphiques destinés aux rapports et présentations
│
├── src
│   └── rl_pilot                 <- Package Python du projet
│       ├── __init__.py          <- Initialise le package
│       ├── config.py            <- Chemins, paramètres communs et masquage des chemins
│       ├── dataset.py           <- Chargement et préparation des données
│       ├── features.py          <- Construction des variables d'entrée
│       ├── modeling
│       │   ├── __init__.py
│       │   ├── predict.py       <- Inférence avec un modèle entraîné
│       │   └── train.py         <- Entraînement
│       └── plots.py             <- Visualisations
│
└── tests              <- Tests unitaires
```

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Remerciements

Projet réalisé par **Kilian LEFEVRE** dans le cadre du parcours OpenClassrooms AI Engineer - Projet : *Entraînez votre agent RL*.

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>
