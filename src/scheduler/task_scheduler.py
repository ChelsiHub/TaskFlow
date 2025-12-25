import time
import schedule
from tasks.automation_engine import AutomationEngine
from utils.logger import setup_logger
from config.settings import SCHEDULER_INTERVAL_MINUTES

logger = setup_logger()


class TaskScheduler:
    def __init__(self):
        self.engine = AutomationEngine()

    def run_tasks(self):
        """Trigger automation engine manually or by scheduler"""
        logger.info("Scheduler triggered task execution")
        self.engine.run()

    def start(self):
        """Start interval-based scheduler"""
        logger.info(
            f"Starting scheduler (every {SCHEDULER_INTERVAL_MINUTES} minutes)"
        )

        schedule.every(SCHEDULER_INTERVAL_MINUTES).minutes.do(self.run_tasks)

        while True:
            schedule.run_pending()
            time.sleep(1)
