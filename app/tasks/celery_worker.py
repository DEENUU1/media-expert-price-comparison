import asyncio
import logging

from celery import Celery
from celery.schedules import crontab

from config.settings import settings
from config.database import get_db
from repository.source_repository import get_sources

from concurrent.futures import ThreadPoolExecutor

from scraper import scraper

logger = logging.getLogger(__name__)

celery_app: Celery = Celery(
    "tasks",
    broker=settings.CELERY_BROKER,
    backend=settings.CELERY_BACKEND,
)
celery_app.conf.beat_schedule = {
    "task-scraper": {
        "task": "task_scraper",
        "schedule": crontab(minute="10", hour="12"),
    },
}
celery_app.conf.timezone = "UTC"  # Set your timezone if needed
celery_app.conf.worker_redirect_stdouts = False
celery_app.conf.task_routes = {"tasks.*": {"queue": "celery"}}
celery_app.conf.update(
    result_expires=3600,
)


@celery_app.task(name="scraper")
def task_scraper() -> None:
    logger.info("Starting scraper")

    db = next(get_db())
    urls = get_sources(db)

    for url in urls:
        scraper(db, url.url)

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(scraper, urls)

    logger.info("Scraper finished")
