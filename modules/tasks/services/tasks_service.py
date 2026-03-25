from datetime import datetime

from modules.tasks.builder.task_builder import TaskBuilder
from modules.tasks.models.Itask_service import ITaskService
from modules.tasks.models.enum import TaskType, TaskStatus, PriorityTask



class TaskService(ITaskService):

    def __init__(self):
        self.tasks = {}
        self.current_id = 1

    def create_task(self, data):

        builder = TaskBuilder()

        task = (
            builder
            .set_type(TaskType(data["task_type"]))
            .set_title(data["title"])
            .set_description(data["description"])
            .set_due_date(datetime.fromisoformat(data["due_date"]))
        )

        if "status" in data:
            task.set_status(TaskStatus(data["status"]))

        if "priority" in data:
            task.set_priority(PriorityTask(data["priority"]))

        if "extra" in data:
            for key, value in data["extra"].items():
                task.add_extra(key, value)

        task = task.build()

        # asignar ID
        task.id = self.current_id

        self.tasks[self.current_id] = task
        self.current_id += 1

        return task.to_dict()

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def update_task(self, task_id, data):
        task = self.get_task(task_id)
        if not task:
            return None

        task.update_task(
            data
        )

        task.history.append("Task updated")
        return task.to_dict()

    def delete_task(self, task_id):
        return self.tasks.pop(task_id, None)

    def move_task(self, task_id, column_id):
        task = self.get_task(task_id)
        if not task:
            return None

        old_column = getattr(task, "column_id", None)
        task.column_id = column_id

        task.history.append(f"Moved from {old_column} to {column_id}")
        return task.history

    def add_comment(self, task_id, comment):
        task = self.get_task(task_id)
        if not task:
            return None

        task.comments.append({
            "text": comment,
            "created_at": datetime.now().isoformat()
        })

        task.history.append("Comment added")
        return task.comments

    def add_time_log(self, task_id, hours):
        task = self.get_task(task_id)
        if not task:
            return None

        task.time_logs.append({
            "hours": hours,
            "date": datetime.now().isoformat()
        })

        return task.time_logs

    def add_attachment(self, task_id, file):
        task = self.get_task(task_id)
        if not task:
            return None

        task.attachments.append({
            "file": file,
            "uploaded_at": datetime.now().isoformat()
        })

        return task.to_dict()

    def clone_task(self, task_id):
        task = self.get_task(task_id)
        if not task:
            return None

        new_task = task.clone()

        self.tasks[self.current_id] = new_task
        self.current_id += 1

        return new_task.to_dict()

    def get_deadline_hours(self, task_id):
        task = self.get_task(task_id)
        if not task:
            return None

        return task.get_deadline_hours()