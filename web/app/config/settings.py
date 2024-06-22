from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
from starlette.templating import Jinja2Templates

load_dotenv()


class Settings(BaseSettings):
    MONGO_CONNECTION_STRING: str = os.getenv("MONGO_CONNECTION_STRING")
    MONGO_DATABASE_NAME: str = os.getenv("MONGO_DATABASE_NAME")
    TITLE: str = "Media expert price comparison"
    DEBUG: bool = True
    TEMPLATES: Jinja2Templates = Jinja2Templates(directory="templates")


settings = Settings()
