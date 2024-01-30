from typing import List
import uuid
from Repository.UserRepository import UserRepository
from Shared.models import User, UserInput

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
    def create(username: str, email: str) -> User:
        user_input = UserInput(username=username, email=email)
        create_response = UserRepository.create(user_input)
        new_user = User.toDto(create_response.data[0])
        return new_user

    @staticmethod
    def update(userId: uuid.UUID, user: User) -> User:
        UserRepository.update(userId, user)
        return user
    
    @staticmethod
    def delete(userId) -> int:
        UserRepository.delete(userId)
        return userId