from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
from config.settings import settings
from views.router import router
from utils import lifespan


app = FastAPI(
    debug=settings.DEBUG,
    title=settings.TITLE,
    lifespan=lifespan,
)

files_in_current_dir = os.listdir('.')
print(files_in_current_dir)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)
