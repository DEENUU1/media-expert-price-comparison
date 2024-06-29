from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
from starlette.templating import Jinja2Templates

load_dotenv()


class Settings(BaseSettings):
    SQLITE_DATABASE_URL: str = "sqlite:///database.db"
    TITLE: str = "Media expert price comparison"
    DEBUG: bool = True
    TEMPLATES: Jinja2Templates = Jinja2Templates(directory="templates")
    SELENIUM_GRID: str = os.getenv("SELENIUM_GRID")


settings = Settings()
