from datetime import datetime

from modules.tasks.factory.task_factory import TaskFactory
from modules.tasks.models.Itask_service import ITaskService



class TaskService(ITaskService):

    def __init__(self, repository):
        self.repository = repository

    def get_all_tasks(self):
        return self.repository.get_all()

    def create_task(self, data):

        data["task_id"] = self.repository.get_last_id() + 1
        task = TaskFactory.from_dict(data)

        return self.repository.create(task.to_dict())

    def get_task(self, task_id):
        data = self.repository.get_by_id(task_id)
        task = TaskFactory.from_dict(data)
        return task

    def update_task(self, task_id, data):
        task = self.get_task(task_id)
        if not task:
            return None

        task = self.repository.update(task_id, data)

        return task

    def delete_task(self, task_id):
        return self.repository.delete(task_id)

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
        
        task.add_attachment(file)

        return task

    def clone_task(self, task_id):
        task = self.get_task(task_id)
        if not task:
            return None

        new_task = task.clone()

        new_task.task_id = self.repository.get_last_id() + 1
        
        self.repository.create(new_task.to_dict())

        return new_task.to_dict()

    def get_deadline_hours(self, task_id):
        task = self.get_task(task_id)
        if not task:
            return None

        return task.get_deadline_hours()