from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    SELENIUM_GRID: str = os.getenv("SELENIUM_GRID")


settings = Settings()
