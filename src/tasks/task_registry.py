import json
from pathlib import Path
from typing import List
from tasks.task_model import Task

TASK_FILE = Path(__file__).parent / "tasks.json"


class TaskRegistry:
    def __init__(self):
        self.tasks: List[Task] = []
        self.load_tasks()

    def load_tasks(self):
        if TASK_FILE.exists():
            with open(TASK_FILE, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(item) for item in data]
        else:
            self.tasks = []

    def save_tasks(self):
        with open(TASK_FILE, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, task: Task):
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        return self.tasks

    def enable_task(self, task_id: str):
        for task in self.tasks:
            if task.id == task_id:
                task.enabled = True
                self.save_tasks()
                return True
        return False

    def disable_task(self, task_id: str):
        for task in self.tasks:
            if task.id == task_id:
                task.enabled = False
                self.save_tasks()
                return True
        return False
