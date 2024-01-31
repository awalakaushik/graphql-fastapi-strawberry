import uuid
from Shared.supabase_client import supabase
from Shared.models import UserInput

class UserRepository:
    
    @staticmethod
    def get_all():
        users = supabase.table("Users").select("*").execute()
        return users
    
    @staticmethod
    def get_by_id(userId: uuid.UUID):
        user = supabase.table("Users").select("*").eq("id", userId).single().execute()
        return user
    
    @staticmethod
    def get_by_email(email: str):
        user = supabase.table("Users").select("*").eq("email", email).single().execute()
        return user
    
    @staticmethod
    def get_by_username(username: str):
        user = supabase.table("Users").select("*").eq("username", username).single().execute()
        return user
    
    @staticmethod
    def create(new_user: UserInput):
        new_user_dict = new_user.__dict__
        api_response = supabase.table("Users").insert(new_user_dict).execute()
        return api_response
    
    @staticmethod
    def update(userId: uuid.UUID, user: UserInput):
        update_user_dict = user.__dict__
        updated_user = supabase.table("Users").update(update_user_dict).eq("id", userId).execute()
        return updated_user
    
    @staticmethod
    def delete(userId: uuid.UUID):
        deleted_user = supabase.table("Users").delete().eq("id", userId).execute()
        return deleted_user