import typing
from Service.TaskService import TaskService
import strawberry

from Shared.models import Task

@strawberry.type
class TaskQueries:
    @strawberry.field
    def tasks(self) -> typing.List[Task]:
        return TaskService.get_all()