import json
from pathlib import Path
from typing import List
from src.execution.execution_model import ExecutionRecord

EXECUTION_FILE = Path(__file__).parent / "executions.json"

class ExecutionRegistry:
    def __init__(self):
        self.executions: List[dict] = []
        self.load()

    def load(self):
        if EXECUTION_FILE.exists():
            with open(EXECUTION_FILE, "r") as f:
                try:
                    self.executions = json.load(f)
                except json.JSONDecodeError:
                    self.executions = []
        else:
            self.executions = []

    def save(self):
        with open(EXECUTION_FILE, "w") as f:
            json.dump(self.executions, f, indent=4)

    def add_execution(self, record: ExecutionRecord):
        self.executions.append(record.__dict__)
        self.save()
