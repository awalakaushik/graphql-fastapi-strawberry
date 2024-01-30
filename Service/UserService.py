from typing import List
import uuid
from Repository.UserRepository import UserRepository
from Shared.models import User

class UserService:
    
    @staticmethod
    def get_all() -> List[User]:
        user_list = UserRepository.get_all()
        users = [User.toDto(user) for user in user_list.data]
        return users
    
    @staticmethod
    def get_by_id(userId) -> User:
        user = UserRepository.get_by_id(userId)
        return User.toDto(user)
    
    @staticmethod
    def create(user: User) -> User:
        UserRepository.create(user)
        return user

    @staticmethod
    def update(userId: uuid.UUID, user: User) -> User:
        UserRepository.update(userId, user)
        return user
    
    @staticmethod
    def delete(userId) -> int:
        UserRepository.delete(userId)
        return userId