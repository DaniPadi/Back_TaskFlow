from modules.tasks.models.task import Task
from modules.tasks.models.enum import TaskType


# Bug Task
class BugTask(Task):

    def __init__(self, title, description, severity="medium", **kwargs):
        super().__init__(title, description, **kwargs)
        self.severity = severity

    def get_type(self):
        return TaskType.Bug

    def to_dict(self):
        return {
            "type": self.get_type().value,
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "priority": self.priority.value,
            "severity": self.severity
        }


# Feature Task
class FeatureTask(Task):

    def __init__(self, title, description, module="general", **kwargs):
        super().__init__(title, description, **kwargs)
        self.module = module

    def get_type(self):
        return TaskType.Feature

    def to_dict(self):
        return {
            "type": self.get_type().value,
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "priority": self.priority.value,
            "module": self.module
        }

    def clone(self):
        return FeatureTask(
            self.title,
            self.description,
            module=self.module,
            status=self.status,
            priority=self.priority
        )


# Normal Task
class SimpleTask(Task):

    def get_type(self):
        return TaskType.Task

    def to_dict(self):
        return {
            "type": self.get_type().value,
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "priority": self.priority.value
        }


# Improvement Task
class ImprovementTask(Task):

    def __init__(self, title, description, impact="medium", **kwargs):
        super().__init__(title, description, **kwargs)
        self.impact = impact

    def get_type(self):
        return TaskType.Improvement

    def to_dict(self):
        return {
            "type": self.get_type().value,
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "priority": self.priority.value,
            "impact": self.impact
        }