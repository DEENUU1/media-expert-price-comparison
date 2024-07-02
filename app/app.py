from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from config.settings import settings
from views.router import router
from utils import init_db
from tasks.celery_worker import task_scraper


app = FastAPI(
    debug=settings.DEBUG,
    title=settings.TITLE,
)


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/scraper")
def scraper():
    task_scraper.delay()
    return {"message": "Scraper started"}


app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)
