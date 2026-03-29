import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

>>>>>>> 182d746 (Versão atual da infra com backend da VM)
settings = Settings()