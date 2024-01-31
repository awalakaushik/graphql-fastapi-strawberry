import typing
from Service.UserService import UserService
import strawberry

from Shared.models import User

@strawberry.type
class UserQueries:
    @strawberry.field
    def users(self) -> typing.List[User]:
        return UserService.get_all()
    
    @strawberry.field
    def user(self, userId: str) -> User:
        return UserService.get_by_id(userId)
    
    @strawberry.field
    def user_by_email(self, email: str) -> User:
        return UserService.get_by_email(email)
    
    @strawberry.field
    def user_by_username(self, username: str) -> User:
        return UserService.get_by_username(username)