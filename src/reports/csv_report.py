import csv
from datetime import date
from pathlib import Path
from config.settings import REPORT_DIR
from execution.execution_registry import ExecutionRegistry


def generate_csv_report():
    registry = ExecutionRegistry()
    executions = registry.executions

    if not executions:
        return None

    today = date.today().isoformat()
    report_file = REPORT_DIR / f"execution_report_{today}.csv"

    with open(report_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "task_id",
                "task_name",
                "status",
                "start_time",
                "end_time",
                "duration_seconds",
                "error_message"
            ]
        )
        writer.writeheader()
        writer.writerows(executions)

    return report_file
