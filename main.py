import uvicorn
from fastapi import FastAPI
from GraphQL.schema import graphql_app

from Controllers.tasks import router as tasks_router
from Controllers.users import router as users_router

app = FastAPI()

app.include_router(tasks_router, prefix="/tasks")
app.include_router(users_router, prefix="/users")

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8888, reload=True)