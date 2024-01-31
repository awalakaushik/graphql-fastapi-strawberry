from Service.UserService import UserService
import strawberry
import uuid

from Shared.models import User

@strawberry.type
class UserMutations:
    @strawberry.mutation
    def create_user(self, email: str, username: str) -> User:
        return UserService.create(username=username, email=email)

    @strawberry.mutation
    def update_user(self, userId: str, email: str, username: str) -> User:
        return UserService.update(userId, email, username)

    @strawberry.mutation
    def delete_user(self, userId: str) -> uuid.UUID:
        return UserService.delete(userId)