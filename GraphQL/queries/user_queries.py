import typing
from Service.UserService import UserService
import strawberry

from Shared.models import User

@strawberry.type
class UserQueries:
    @strawberry.field
    def users(self) -> typing.List[User]:
        return UserService.get_all()