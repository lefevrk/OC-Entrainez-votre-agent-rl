import os
from pathlib import Path
import random

from dotenv import load_dotenv
from loguru import logger
import numpy as np

# Load environment variables from .env file if it exists
load_dotenv()

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

MODELS_DIR = PROJ_ROOT / "models"

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# Constantes partagées par plusieurs étapes du projet.
SEED = 42

# Étiquette qui remplace la racine du projet dans les sorties affichées.
SAFE_ROOT_LABEL = "<PROJECT_ROOT>"
SAFE_HOME_LABEL = "~"

# If tqdm is installed, configure loguru with tqdm.write
# https://github.com/Delgan/loguru/issues/135
try:
    from tqdm import tqdm

    logger.remove(0)
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
except ModuleNotFoundError:
    pass


def mask_path(value: str | Path) -> str:
    """Remplace les chemins personnels par des étiquettes neutres.

    La racine du projet devient `<PROJECT_ROOT>` et le dossier personnel `~`,
    pour qu'aucun chemin local n'apparaisse dans les sorties de notebook.

    Args:
        value: Chemin (ou texte contenant des chemins) à masquer.

    Returns:
        Le texte avec la racine du projet et le dossier personnel masqués.
    """
    masked = str(value).replace(str(PROJ_ROOT), SAFE_ROOT_LABEL)
    return masked.replace(str(Path.home()), SAFE_HOME_LABEL)


def set_seed(seed: int = SEED) -> None:
    """Fixe les graines de `random` et NumPy, et de PyTorch s'il est installé.

    PyTorch n'est importé que s'il est installé : le module reste léger pour
    les étapes qui n'en ont pas besoin.

    Args:
        seed: Graine commune.
    """
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    try:
        import torch
    except ModuleNotFoundError:
        return
    torch.manual_seed(seed)
