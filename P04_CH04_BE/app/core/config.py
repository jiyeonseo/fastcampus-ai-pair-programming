import os
class settings:
    
    open_ai_api_key: str = os.getenv("OPEN_AI_API_KEY")
    assistant_id: str = os.getenv("ASSISTANT_ID")

    def get_database_url():
        if os.getenv("ENVIRONMENT","local") == "test":
            return "sqlite:///./test.db"
        else:
            return "{vercel_postgres_url}"
        