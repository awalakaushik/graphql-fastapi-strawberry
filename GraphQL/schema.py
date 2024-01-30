import asyncio
import typing

import strawberry
from strawberry.asgi import GraphQL

from GraphQL.queries.task_queries import TaskQueries
from GraphQL.queries.user_queries import UserQueries
from Service.UserService import UserService
from Shared.models import User


@strawberry.type
class Query(UserQueries, TaskQueries):
    pass

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, email: str, username: str) -> User:
        return UserService.create(username=username, email=email)

@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, target: int = 100) -> typing.AsyncGenerator[int, None]:
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)
graphql_app = GraphQL(schema=schema)