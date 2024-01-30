import os
from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()

url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key) # Create a new client instance
