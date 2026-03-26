from config.db import SupabaseClient

class TaskRepository:
    def __init__(self):
        self.client = SupabaseClient().get_client()
        self.table = "tasks"

    def get_all(self):
        response = self.client.table(self.table).select("*").execute()

        return response.data
    
    def get_by_id(self, task_id):
        response = self.client.table(self.table)\
        .select("*")\
        .eq("task_id", task_id)\
        .single()\
        .execute()

        return response.data
    
    def create(self, data):
        response = self.client.table(self.table)\
            .insert(data)\
            .execute()
        
        return response.data[0]
    
    def update(self, task_id, data):
        response = self.client.table(self.table)\
            .update(data)\
            .eq("task_id", task_id)\
            .execute()
        
        if not response.data:
            return None
        
        return response.data[0]
    
    def delete(self, task_id):
        response = self.client.table(self.table)\
            .delete()\
            .eq("task_id", task_id)\
            .execute()
        
        if not response.data:
            return None
        
        return response.data[0]
