import shutil
from pathlib import Path
from utils.logger import setup_logger

logger = setup_logger()


def copy_data(metadata):
    """
    Copies a file from source to destination
    metadata = {
        "source_file": "data/sample.txt",
        "destination_file": "output/sample.txt"
    }
    """
    source = Path(metadata.get("source_file", ""))
    destination = Path(metadata.get("destination_file", ""))

    if not source.exists():
        raise FileNotFoundError(f"Source file not found: {source}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(source, destination)
    logger.info(f"File copied from {source} to {destination}")
