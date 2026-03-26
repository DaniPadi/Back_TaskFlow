from modules.tasks.models.enum import TaskType
from modules.tasks.models.task_types import (
    BugTask,
    FeatureTask,
    SimpleTask,
    ImprovementTask
)

from datetime import datetime


class TaskFactory:

    @staticmethod
    def create_task(task_type, title, description, due_date, **kwargs):

        if task_type == TaskType.Bug:
            return BugTask(title, description, due_date, **kwargs)

        elif task_type == TaskType.Feature:
            return FeatureTask(title, description, due_date, **kwargs)

        elif task_type == TaskType.Task:
            return SimpleTask(title, description, due_date, **kwargs)

        elif task_type == TaskType.Improvement:
            return ImprovementTask(title, description, due_date, **kwargs)

        else:
            raise ValueError("Invalid Task Type")
    
    # TaskFactory
    @staticmethod
    def from_dict(data):
        task_type = TaskType(data["type"])
        title = data["title"]
        description = data.get("description")
        due_date = datetime.fromisoformat(data["due_date"])
        status = data.get("status", "pending")
        priority = data.get("priority", None)
        extra = data.get("extra", {})

        task = TaskFactory.create_task(
            task_type,
            title,
            description,
            due_date,
            status=status,
            priority=priority,
            extra=extra
        )
        return task