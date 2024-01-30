import uuid
from Shared.supabase_client import supabase
from Shared.models import Task, TaskInput

class TaskRepository:
    
    @staticmethod
    def get_all():
        tasks = supabase.table("Tasks").select("*").execute()
        return tasks
    
    @staticmethod
    def get_by_id(taskId: uuid.UUID):
        task = supabase.table("Tasks").select("*").eq("id", taskId).single().execute()
        return task
    
    @staticmethod
    def create(__self__, task: TaskInput):
        new_task = supabase.table(__self__.TASKS).insert(task).execute()
        return new_task
    
    @staticmethod
    def update(taskId: uuid.UUID, task: Task):
        updated_task = supabase.table("Tasks").update(task).eq("id", taskId).execute()
        return updated_task
    
    @staticmethod
    def delete(taskId: uuid.UUID):
        deleted_task = supabase.table("Tasks").delete().eq("id", taskId).execute()
        return deleted_task