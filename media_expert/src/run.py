import logging

from sqlalchemy.orm import Session

from scraper import scraper
from concurrent.futures import ThreadPoolExecutor
from config.database import get_db
from repository.source_repository import get_sources


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


def main():
    logger.info('Starting scraper')

    db: Session = next(get_db())

    urls = get_sources(db)

    for url in urls:
        scraper(db, url.url)

    # with ThreadPoolExecutor(max_workers=4) as executor:
    #     executor.map(scraper, urls)

    logger.info('Finished scraper')


if __name__ == '__main__':
    main()
