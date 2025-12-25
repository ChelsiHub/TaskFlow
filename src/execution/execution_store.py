from datetime import datetime
from src.execution.execution_model import ExecutionRecord
from src.execution.execution_registry import ExecutionRegistry

registry = ExecutionRegistry()

def save_execution(task_id, task_name, status, start_time, end_time, error=None):
    duration = (end_time - start_time).total_seconds()
    record = ExecutionRecord(
        task_id=task_id,
        task_name=task_name,
        status=status,
        start_time=start_time.isoformat(),
        end_time=end_time.isoformat(),
        duration_seconds=duration,
        error_message=error
    )
    registry.add_execution(record)
