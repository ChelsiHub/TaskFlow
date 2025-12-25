from datetime import datetime
from tasks.task_registry import TaskRegistry
from execution.execution_model import ExecutionRecord
from execution.execution_registry import ExecutionRegistry
from utils.logger import setup_logger

logger = setup_logger()


class AutomationEngine:
    def __init__(self):
        self.registry = TaskRegistry()
        self.execution_registry = ExecutionRegistry()

    def run(self):
        logger.info("Automation Engine started")

        for task in self.registry.list_tasks():
            if not task.enabled:
                logger.info(f"Skipping disabled task: {task.name}")
                continue

            start_time = datetime.now()
            execution = ExecutionRecord(
                task_id=task.id,
                task_name=task.name,
                status="RUNNING",
                start_time=start_time.isoformat()
            )

            try:
                logger.info(f"Running task: {task.name}")
                task.status = "RUNNING"

                self.execute_task(task)

                end_time = datetime.now()
                execution.status = "SUCCESS"
                execution.end_time = end_time.isoformat()
                execution.duration_seconds = (
                    end_time - start_time
                ).total_seconds()

                task.status = "SUCCESS"
                logger.info(f"Task succeeded: {task.name}")

            except Exception as e:
                end_time = datetime.now()
                execution.status = "FAILED"
                execution.end_time = end_time.isoformat()
                execution.duration_seconds = (
                    end_time - start_time
                ).total_seconds()
                execution.error_message = str(e)

                task.status = "FAILED"
                logger.error(f"Task failed: {task.name} | {str(e)}")

            finally:
                self.execution_registry.add(execution)
                self.registry.save_tasks()

        logger.info("Automation Engine finished")

    def execute_task(self, task):
        task_type = task.task_type.upper()

        if task_type == "FILE_CLEANUP":
            from tasks.file_cleanup import cleanup_files
            cleanup_files(task.metadata)

        elif task_type == "FOLDER_BACKUP":
            from tasks.folder_backup import backup_folder
            backup_folder(task.metadata)

        elif task_type == "DATA_COPY":
            from tasks.data_copy import copy_data
            copy_data(task.metadata)

        else:
            raise ValueError(f"Unknown task type: {task.task_type}")
