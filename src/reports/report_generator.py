from execution.execution_registry import ExecutionRegistry
from reports.csv_report import generate_csv_report
from utils.logger import setup_logger

logger = setup_logger()


class ReportGenerator:
    def __init__(self):
        self.registry = ExecutionRegistry()

    def generate_daily_report(self):
        executions = self.registry.executions

        total = len(executions)
        success = sum(1 for e in executions if e["status"] == "SUCCESS")
        failed = sum(1 for e in executions if e["status"] == "FAILED")

        logger.info("Daily Execution Summary")
        logger.info(f"Total Runs   : {total}")
        logger.info(f"Successful  : {success}")
        logger.info(f"Failed      : {failed}")

        csv_file = generate_csv_report()
        if csv_file:
            logger.info(f"CSV report generated: {csv_file}")
        else:
            logger.info("No execution data found")

        return {
            "total": total,
            "success": success,
            "failed": failed
        }
