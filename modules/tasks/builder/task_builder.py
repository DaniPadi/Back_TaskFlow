from modules.tasks.models.enum import TaskType, TaskStatus, PriorityTask
from modules.tasks.factory.task_factory import TaskFactory


class TaskBuilder:

    def __init__(self):
        self.reset()

    def reset(self):
        self._task_type = None
        self._title = None
        self._description = None
        self._status = TaskStatus.To_Do
        self._priority = PriorityTask.Medium
        self._extra_fields = {}

    def set_type(self, task_type: TaskType):
        self._task_type = task_type
        return self

    def set_title(self, title: str):
        self._title = title
        return self

    def set_description(self, description: str):
        self._description = description
        return self

    def set_status(self, status: TaskStatus):
        self._status = status
        return self

    def set_priority(self, priority: PriorityTask):
        self._priority = priority
        return self

    def add_extra(self, key, value):
        self._extra_fields[key] = value
        return self

    def build(self):

        if not self._task_type:
            raise ValueError("Task type is required")

        if not self._title or not self._description:
            raise ValueError("Title and description are required")

        task = TaskFactory.create_task(
            self._task_type,
            self._title,
            self._description,
            status=self._status,
            priority=self._priority,
            **self._extra_fields
        )

        self.reset()
        return task