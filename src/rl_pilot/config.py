from pathlib import Path

from dotenv import load_dotenv
from loguru import logger

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

# Constants shared by several steps of the project.
SEED = 42

# Labels that replace the project root and home directory in displayed output.
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
    """Replace personal paths with neutral labels.

    The project root becomes `<PROJECT_ROOT>` and the home directory becomes
    `~`, so that no local path appears in notebook outputs.

    Args:
        value: Path (or text containing paths) to mask.

    Returns:
        The text with the project root and home directory masked.
    """
    masked = str(value).replace(str(PROJ_ROOT), SAFE_ROOT_LABEL)
    return masked.replace(str(Path.home()), SAFE_HOME_LABEL)
