from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict


@dataclass
class Task:
    id: str
    name: str
    task_type: str
    enabled: bool = True
    status: str = "PENDING"
    metadata: Dict = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self):
        """Convert Task object to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "task_type": self.task_type,
            "enabled": self.enabled,
            "status": self.status,
            "metadata": self.metadata,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data: Dict):
        """Create Task object from dictionary"""
        return Task(
            id=data["id"],
            name=data["name"],
            task_type=data["task_type"],
            enabled=data.get("enabled", True),
            status=data.get("status", "PENDING"),
            metadata=data.get("metadata", {}),
            created_at=data.get("created_at")
        )
