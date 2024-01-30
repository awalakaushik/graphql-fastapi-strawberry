import uuid
from fastapi import APIRouter, status

from Service.TaskService import TaskService

router = APIRouter()

# Get all tasks
@router.get("/", tags=["Tasks"])
def get_tasks():
    tasks = TaskService.get_all()
    return tasks

# Get a task by id
@router.get("/{taskId}", tags=["Tasks"])
def get_task_by_id(taskId: uuid.UUID):
    task = TaskService.get_by_id(taskId)
    return task

# Create a new task
@router.post("/", status_code=status.HTTP_201_CREATED, tags=["Tasks"])
def create_task(task: dict):
    new_task = TaskService.create(task)
    return new_task

# Update a task
@router.put("/{taskId}", tags=["Tasks"])
def update_task(taskId: uuid.UUID, task: dict):
    updated_task = TaskService.update(taskId, task)
    return updated_task

# Delete a task
@router.delete("/{taskId}", tags=["Tasks"])
def delete_task(taskId: uuid.UUID):
    deleted_task = TaskService.delete(taskId)
    return deleted_task