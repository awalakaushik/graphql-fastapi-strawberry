import typing
import strawberry

@strawberry.type
class User:
    id: str
    username: str
    email: str

    @staticmethod
    def toDto(user_data):
        return User(id=user_data['id'], username=user_data['username'], email=user_data['email'])

@strawberry.type
class Task:
    id: str
    title: str
    description: str
    status: str
    created_by: typing.Optional[User]

    @staticmethod
    def toDto(task_data, created_by=None):
        return Task(id=task_data['id'], title=task_data['title'], description=task_data['description'], status=task_data['status'], created_by=created_by)