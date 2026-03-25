from modules.tasks.models.task import Task
from modules.tasks.models.enum import TaskType


# Bug Task
class BugTask(Task):

    def __init__(self, title, description, due_date=None, severity="medium", **kwargs):
        super().__init__(title, description, due_date=due_date, **kwargs)
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
            "severity": self.severity,
            "due_date": self.due_date.isoformat() if self.due_date else None
        }


# Feature Task
class FeatureTask(Task):

    def __init__(self, title, description, due_date=None, module="general", **kwargs):
        super().__init__(title, description, due_date=due_date, **kwargs)
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
            "module": self.module,
            "due_date": self.due_date.isoformat() if self.due_date else None
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
            "priority": self.priority.value,
            "due_date": self.due_date.isoformat() if self.due_date else None
        }


# Improvement Task
class ImprovementTask(Task):

    def __init__(self, title, description, due_date=None, impact="medium", **kwargs):
        super().__init__(title, description, due_date=due_date, **kwargs)
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
            "impact": self.impact,
            "due_date": self.due_date.isoformat() if self.due_date else None
        }