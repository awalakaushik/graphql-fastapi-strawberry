import asyncio
import random
import typing

import strawberry
from strawberry.asgi import GraphQL

from GraphQL.queries.task_queries import TaskQueries
from GraphQL.queries.user_queries import UserQueries

from GraphQL.mutations.user_mutations import UserMutations


@strawberry.type
class Query(UserQueries, TaskQueries):
    pass

@strawberry.type
class Mutation(UserMutations):
    pass

@strawberry.type
class Subscription:
    @strawberry.subscription
    async def random_task(self, target: int = 100) -> typing.AsyncGenerator[str, None]:
        task_names = ["Design new logo", "Implement authentication", "Fix broken links", "Write blog post", "Optimize database"]
        for _ in range(target):
            yield random.choice(task_names)
            await asyncio.sleep(5)

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)
graphql_app = GraphQL(schema=schema)