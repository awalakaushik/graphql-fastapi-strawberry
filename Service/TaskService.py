from typing import List
import uuid
from Repository.UserRepository import UserRepository
from Repository.TaskRepository import TaskRepository
from Shared.models import Task, User

class TaskService:

    @staticmethod
    def get_all() -> List[Task]:
        task_list = TaskRepository.get_all()

        tasks = []

        for task in task_list.data:
            user = UserRepository.get_by_id(task['created_by'])

            user_dto = User.toDto(user.data)
            task_dto = Task.toDto(task, user_dto)

            tasks.append(task_dto)

        return tasks
    
    @staticmethod
    def get_by_id(taskId: uuid.UUID) -> Task:
        task = TaskRepository.get_by_id(taskId)
        return Task.toDto(task)
    
    @staticmethod
    def create(task: Task) -> Task:
        TaskRepository.create(task)
        return task
    
    @staticmethod
    def update(taskId: uuid.UUID, task: Task) -> Task:
        TaskRepository.update(taskId, task)
        return task
    
    @staticmethod
    def delete(taskId: uuid.UUID) -> uuid.UUID:
        TaskRepository.delete(taskId)
        return taskId