from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class ExecutionRecord:
    task_id: str
    task_name: str
    status: str
    start_time: str
    end_time: Optional[str] = None
    duration_seconds: Optional[float] = None
    error_message: Optional[str] = None

    @staticmethod
    def now_iso():
        return datetime.now().isoformat()
