import uuid
from fastapi import APIRouter, status

from Service.UserService import UserService
from Shared.models import UserInput

router = APIRouter()

# Get all users
@router.get("/", tags=["Users"])
def get_users():
    users = UserService.get_all()
    return users

# Get a user by id
@router.get("/{userId}", tags=["Users"])
def get_user_by_id(userId: uuid.UUID):
    user = UserService.get_by_id(userId)
    return user

# Create a new user
@router.post("/", status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(user: UserInput):
    new_user = UserService.create(user)
    return new_user

# Update a user
@router.put("/{userId}", tags=["Users"])
def update_user(userId: uuid.UUID, user: UserInput):
    updated_user = UserService.update(userId, user.email, user.username)
    return updated_user

# Delete a user
@router.delete("/{userId}", tags=["Users"])
def delete_user(userId: uuid.UUID):
    deleted_user = UserService.delete(userId)
    return deleted_user