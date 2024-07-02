from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from config.settings import settings
from views.router import router
from utils import init_db


app = FastAPI(
    debug=settings.DEBUG,
    title=settings.TITLE,
)


@app.on_event("startup")
def on_startup():
    init_db()


app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)