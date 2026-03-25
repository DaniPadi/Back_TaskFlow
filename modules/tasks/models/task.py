from abc import ABC, abstractmethod
import copy

from modules.tasks.models.enum import TaskType, TaskStatus, PriorityTask

class Task(ABC):

    def __init__(self, title, description,
                 status=TaskStatus.To_Do,
                 priority=PriorityTask.Medium):

        self.title = title
        self.description = description
        self.status = status
        self.priority = priority

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass

    def clone(self):
        return copy.deepcopy(self)