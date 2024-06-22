from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    SELENIUM_GRID: str = os.getenv("SELENIUM_GRID")
    MONGO_CONNECTION_STRING: str = os.getenv("MONGO_CONNECTION_STRING")
    MONGO_DATABASE_NAME: str = os.getenv("MONGO_DATABASE_NAME")


settings = Settings()
