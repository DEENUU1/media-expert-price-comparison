from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
from starlette.templating import Jinja2Templates

load_dotenv()


class Settings(BaseSettings):
    SQLITE_DATABASE_URL: str = "sqlite:///database.db"
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRE_PORT: str = os.getenv('POSTGRES_PORT')
    POSTGRE_HOST: str = os.getenv("POSTGRES_HOST")
    POSTGRE_DATABASE_URL: str = os.getenv("POSTGRE_DATABASE_URL")
    TITLE: str = "Media expert price comparison"
    DEBUG: bool = os.getenv("DEBUG") == "True"
    TEMPLATES: Jinja2Templates = Jinja2Templates(directory="templates")


settings = Settings()
