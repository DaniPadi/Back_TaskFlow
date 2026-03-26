from modules.tasks.models.task import Task
from modules.tasks.models.enum import TaskType


# Bug Task
class BugTask(Task):

    def __init__(self, title, description, due_date=None, severity="medium", **kwargs):
        super().__init__(title, description, due_date=due_date, **kwargs)
        self.severity = severity

    def get_type(self):
        return TaskType.Bug


# Feature Task
class FeatureTask(Task):

    def __init__(self, title, description, due_date=None, module="general", **kwargs):
        super().__init__(title, description, due_date=due_date, **kwargs)
        self.module = module

    def get_type(self):
        return TaskType.Feature


# Normal Task
class SimpleTask(Task):

    def get_type(self):
        return TaskType.Task


# Improvement Task
class ImprovementTask(Task):

    def __init__(self, title, description, due_date=None, impact="medium", **kwargs):
        super().__init__(title, description, due_date=due_date, **kwargs)
        self.impact = impact

    def get_type(self):
        return TaskType.Improvement