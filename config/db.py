from supabase import create_client
import os

class SupabaseClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SupabaseClient, cls).__new__(cls)

            url = os.getenv("SUPABASE_URL")
            key = os.getenv("SUPABASE_KEY")

            if not url or not key:
                raise ValueError("SUPABASE_URL o SUPABASE_KEY no están definidos")

            cls._instance.client = create_client(url, key)

        
        return cls._instance
    
    def get_client(self):
        return self.client
