from Shared.supabase_client import supabase
from Shared.models import User

class UserRepository:
    
    @staticmethod
    def get_all():
        users = supabase.table("Users").select("*").execute()
        return users
    
    @staticmethod
    def get_by_id(userId: int):
        user = supabase.table("Users").select("*").eq("id", userId).single().execute()
        return user
    
    @staticmethod
    def create(__self__, user: User):
        new_user = supabase.table("Users").insert(user).execute()
        return new_user
    
    @staticmethod
    def update(userId: int, user: User):
        updated_user = supabase.table("Users").update(user).eq("id", userId).execute()
        return updated_user
    
    @staticmethod
    def delete(userId: int):
        deleted_user = supabase.table("Users").delete().eq("id", userId).execute()
        return deleted_user