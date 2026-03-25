from modules.tasks.models.enum import TaskType
from modules.tasks.models.task_types import (
    BugTask,
    FeatureTask,
    SimpleTask,
    ImprovementTask
)


class TaskFactory:

    @staticmethod
    def create_task(task_type, title, description, **kwargs):

        if task_type == TaskType.Bug:
            return BugTask(title, description, **kwargs)

        elif task_type == TaskType.Feature:
            return FeatureTask(title, description, **kwargs)

        elif task_type == TaskType.Task:
            return SimpleTask(title, description, **kwargs)

        elif task_type == TaskType.Improvement:
            return ImprovementTask(title, description, **kwargs)

        else:
            raise ValueError("Invalid Task Type")