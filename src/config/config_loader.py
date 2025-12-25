# src/config/config_loader.py
import os
from dotenv import load_dotenv
from config.settings import EMAIL_CONFIG, APP_NAME, APP_ENV, DEBUG, LOG_DIR, REPORT_DIR

load_dotenv()  # ensure .env is loaded

def load_config():
    config = {
        "APP_NAME": APP_NAME,
        "APP_ENV": APP_ENV,
        "DEBUG": DEBUG,
        "LOG_DIR": str(LOG_DIR),
        "REPORT_DIR": str(REPORT_DIR),
        "EMAIL_HOST": EMAIL_CONFIG.get("host"),
        "EMAIL_PORT": EMAIL_CONFIG.get("port"),
        "EMAIL_USER": EMAIL_CONFIG.get("user"),
        "EMAIL_PASSWORD": EMAIL_CONFIG.get("password"),
        "EMAIL_RECIPIENTS": os.getenv("EMAIL_RECIPIENTS", "")
    }

    if not config["EMAIL_USER"] or not config["EMAIL_PASSWORD"]:
        raise ValueError("EMAIL_USER or EMAIL_PASSWORD not set in environment variables")

    return config
