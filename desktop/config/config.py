from dotenv import load_dotenv
import os 

load_dotenv()

class Settings:
    API_URL = os.getenv("APIURL")
    WS_URL = os.getenv("WSURL")
    CURRENT_VERSION = os.getenv("CURRENT_VERSION")
    UPDATE_URL = os.getenv("UPDATE_URL")

    if not API_URL:
        raise   Exception("API_URL is not set")
    if not WS_URL:
        raise   Exception("WS_URL is not set")
    if not UPDATE_URL:
        raise   Exception("UPDATE_URL is not set")
    
settings = Settings()