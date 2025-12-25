# src/notification/notifier.py
import os
import yagmail
from utils.logger import setup_logger
from execution.execution_registry import ExecutionRegistry
from reports.report_generator import ReportGenerator

logger = setup_logger()

class Notifier:
    def __init__(self, config):
        self.config = config
        self.registry = ExecutionRegistry()
        self.report_generator = ReportGenerator()

        # Email recipients as list
        self.recipients = [
            email.strip() for email in config.get("EMAIL_RECIPIENTS", "").split(",") if email
        ]

        # Email credentials
        self.sender = config.get("EMAIL_USER")
        self.password = config.get("EMAIL_PASSWORD")
        self.smtp_host = config.get("EMAIL_HOST", "smtp.gmail.com")
        self.smtp_port = int(config.get("EMAIL_PORT", 587))

        # Initialize yagmail client properly (STARTTLS for port 587)
        self.client = yagmail.SMTP(
            user=self.sender,
            password=self.password,
            host=self.smtp_host,
            port=self.smtp_port,
            smtp_starttls=True,
            smtp_ssl=False
        )

    def send_failure_alerts(self):
        failures = [e for e in self.registry.executions if e["status"] == "FAILED"]
        if not failures:
            logger.info("No task failures to notify")
            return

        subject = "TaskFlow Alert: Task Failures Detected"
        body = "The following tasks failed:\n\n"
        for e in failures:
            body += f"- {e['task_name']} | Error: {e['error_message']}\n"

        for recipient in self.recipients:
            try:
                self.client.send(to=recipient, subject=subject, contents=body)
                logger.info(f"Failure alert sent to {recipient}")
            except Exception as ex:
                logger.error(f"Failed to send email to {recipient} | {ex}")

    def send_daily_summary(self):
        summary = self.report_generator.generate_daily_report()
        if not summary:
            logger.warning("No executions to summarize")
            return

        subject = "TaskFlow Daily Summary"
        body = (
            f"Total tasks run: {summary['total']}\n"
            f"Successful: {summary['success']}\n"
            f"Failed: {summary['failed']}\n"
        )
        attachments = []
        # Add CSV or PDF attachments if generated
        if summary.get("csv"):
            attachments.append(summary["csv"])
        if summary.get("pdf"):
            attachments.append(summary["pdf"])

        for recipient in self.recipients:
            try:
                self.client.send(to=recipient, subject=subject, contents=body, attachments=attachments)
                logger.info(f"Daily summary sent to {recipient}")
            except Exception as ex:
                logger.error(f"Failed to send daily summary to {recipient} | {ex}")
