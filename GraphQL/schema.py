import asyncio
import typing
import uuid

import strawberry
from strawberry.asgi import GraphQL

from Service.TaskService import TaskService
from Service.UserService import UserService

@strawberry.type
class User:
    id: uuid.UUID
    username: str
    email: str

@strawberry.type
class Task:
    id: uuid.UUID
    title: str
    description: str
    status: str
    created_by: typing.Optional[User]

@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> typing.List[User]:
        return UserService.get_all()
    
    @strawberry.field
    def tasks(self) -> typing.List[Task]:
        return TaskService.get_all()

# @strawberry.type
# class Mutation:
#     @strawberry.mutation
#     def add_task(self, title: str, description: str, c) -> Book:
#         print(f"Adding {title} by {author}")

#         return Book(title=title, author=author)

@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, target: int = 100) -> typing.AsyncGenerator[int, None]:
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)

schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema=schema)