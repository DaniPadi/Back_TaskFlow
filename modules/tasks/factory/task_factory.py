from modules.tasks.models.enum import TaskType
from modules.tasks.models.task_types import (
    BugTask,
    FeatureTask,
    SimpleTask,
    ImprovementTask
)

from datetime import datetime


class TaskFactory:
    _creators = {
        TaskType.Bug: BugTask,
        TaskType.Feature: FeatureTask,
        TaskType.Task: SimpleTask,
        TaskType.Improvement: ImprovementTask,
    }

    @staticmethod
    def create_task(task_id, task_type, title, description, due_date,**kwargs):
        task_type = TaskType(task_type)
        factory = TaskFactory._creators.get(task_type)
        if not factory:
            raise ValueError(f"No creator defined for task type {task_type}")
        
        task = factory(task_id, title, description, due_date, **kwargs)

        return task
        
    
    # TaskFactory
    @staticmethod
    def from_dict(data):
        task_id = data["task_id"]
        task_type = TaskType(data["type"])
        title = data["title"]
        description = data.get("description")
        due_date = datetime.fromisoformat(data["due_date"])
        status = data.get("status", "pending")
        priority = data.get("priority", None)
        extra = data.get("extra", {})

        task = TaskFactory.create_task(
            task_id,
            task_type,
            title,
            description,
            due_date,
            status=status,
            priority=priority,
            extra=extra
        )
        return task