import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Application settings
APP_NAME = os.getenv("APP_NAME", "TaskFlow")
APP_ENV = os.getenv("APP_ENV", "development")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Paths
LOG_DIR = BASE_DIR / os.getenv("LOG_DIR", "logs")
REPORT_DIR = BASE_DIR / os.getenv("REPORT_DIR", "reports_output")

# Scheduler settings
SCHEDULER_INTERVAL_MINUTES = int(
    os.getenv("SCHEDULER_INTERVAL_MINUTES", 60)
)

# Email settings
EMAIL_CONFIG = {
    "host": "smtp.gmail.com",
    "port": 587,  # STARTTLS
    "user": os.getenv("EMAIL_USER"),
    "password": os.getenv("EMAIL_PASSWORD")
}


# Ensure required directories exist
LOG_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)
