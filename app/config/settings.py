from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
from starlette.templating import Jinja2Templates

load_dotenv()


class Settings(BaseSettings):
    SQLITE_DATABASE_URL: str | None = "sqlite:///database.db"
    POSTGRES_DB: str | None = os.getenv("POSTGRES_DB")
    POSTGRES_USER: str | None = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str | None = os.getenv("POSTGRES_PASSWORD")
    POSTGRE_PORT: str | None = os.getenv('POSTGRES_PORT')
    POSTGRE_HOST: str | None = os.getenv("POSTGRES_HOST")
    POSTGRE_DATABASE_URL: str | None = os.getenv("POSTGRE_DATABASE_URL")
    TITLE: str | None = "Media expert price comparison"
    DEBUG: bool | None = os.getenv("DEBUG") == "True"
    TEMPLATES: Jinja2Templates = Jinja2Templates(directory="templates")
    CELERY_BROKER: str | None = os.getenv("CELERY_BROKER")
    CELERY_BACKEND: str | None = os.getenv("CELERY_BACKEND")


settings = Settings()
