from dotenv import load_dotenv
import os 

load_dotenv()

class Settings:
    API_URL = os.getenv("APIURL")
    WS_URL = os.getenv("WSURL")

    if not API_URL:
        raise   Exception("API_URL is not set")
    if not WS_URL:
        raise   Exception("WS_URL is not set")
    
settings = Settings()