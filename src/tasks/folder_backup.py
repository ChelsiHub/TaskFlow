import shutil
from datetime import datetime
from utils.logger import setup_logger

logger = setup_logger()


def backup_folder(metadata):
    """
    Copies folder to backup location
    metadata = {
        "source": "data",
        "destination": "backup"
    }
    """
    source = metadata.get("source")
    destination = metadata.get("destination")

    if not source or not destination:
        raise ValueError("Missing source or destination for folder backup task")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{destination}_backup_{timestamp}"

    shutil.copytree(source, backup_path)

    logger.info(f"Backup created at {backup_path}")
