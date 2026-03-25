from abc import ABC, abstractmethod


class ITaskService(ABC):

    @abstractmethod
    def create_task(self, data):
        pass

    @abstractmethod
    def get_task(self, task_id):
        pass

    @abstractmethod
    def update_task(self, task_id, data):
        pass

    @abstractmethod
    def delete_task(self, task_id):
        pass

    @abstractmethod
    def move_task(self, task_id, column_id):
        pass

    @abstractmethod
    def add_comment(self, task_id, comment):
        pass

    @abstractmethod
    def add_time_log(self, task_id, hours):
        pass

    @abstractmethod
    def add_attachment(self, task_id, file):
        pass

    @abstractmethod
    def clone_task(self, task_id):
        pass

    @abstractmethod
    def get_deadline_hours(self, task_id):
        pass