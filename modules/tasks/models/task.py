from abc import ABC, abstractmethod
import copy
from datetime import datetime

from modules.tasks.models.enum import TaskType, TaskStatus, PriorityTask

class Task(ABC):

    def __init__(self, title, description, status: TaskStatus, priority: PriorityTask, due_date=None, column_id=None, **kwargs):
        self.id = None
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.due_date = due_date
        self.column_id = column_id
        self.history = []
        self.comments = []
        self.time_logs = []
        self.attachments = []

    @abstractmethod
    def get_type(self):
        pass

    def to_dict(self):
        return {
            "task_id": self.id,
            "column_id": self.column_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority if self.priority else None,
            "type": self.get_type().value,
            "due_date": self.due_date.isoformat() if self.due_date else None,
        }

    def clone(self):
        return copy.deepcopy(self)

    # Métodos comunes que replican ITaskService
    def update_task(self, data: dict):
        # Atributos estándar
        if "title" in data:
            self.title = data["title"]
        if "description" in data:
            self.description = data["description"]
        if "status" in data:
            if isinstance(data["status"], TaskStatus):
                self.status = data["status"]
            else:
                self.status = TaskStatus(data["status"])  # <-- convertir a enum
        if "priority" in data:
            if isinstance(data["priority"], PriorityTask):
                self.priority = data["priority"]
            else:
                self.priority = PriorityTask(data["priority"])  # <-- convertir a enum
        if "due_date" in data:
            self.due_date = data["due_date"]
        if "column_id" in data:
            self.column_id = data["column_id"]

        # Atributos específicos de la subclase
        for key, value in data.items():
            if key not in ["title", "description", "status", "priority", "due_date", "column_id"]:
                setattr(self, key, value)

        self.history.append("Task updated")
        return self.to_dict()

    def delete_task(self):
        self.history.append("Task deleted")
        return {"message": "Deleted"}

    def move_task(self, column_id):
        old_column = self.column_id
        self.column_id = column_id
        self.history.append(f"Moved from {old_column} to {column_id}")
        return self.to_dict()

    def add_comment(self, comment):
        self.comments.append({
            "text": comment,
            "created_at": datetime.now().isoformat()
        })
        self.history.append("Comment added")
        return self.to_dict()

    def add_time_log(self, hours):
        self.time_logs.append({
            "hours": hours,
            "date": datetime.now().isoformat()
        })
        return self.to_dict()

    def add_attachment(self, file):
        self.attachments.append({
            "file": file,
            "uploaded_at": datetime.now().isoformat()
        })
        return self.to_dict()
    
    def get_deadline_hours(self):
        if not self.due_date:
            return None
        delta = self.due_date - datetime.now()
        return max(delta.total_seconds() / 3600, 0)