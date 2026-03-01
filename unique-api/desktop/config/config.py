from dotenv import load_dotenv
import os 

load_dotenv()

class Settings:
    API_URL = os.getenv("APIURLDESENV")

    if not API_URL:
        raise   Exception("API_URL is not set")
    
settings = Settings()