import logging
from scraper import scraper
from repository.source_repository import SourceRepository
from concurrent.futures import ThreadPoolExecutor


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


def main():
    logger.info('Starting scraper')

    source_repo = SourceRepository()

    urls = source_repo.get_sources()

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(scraper, urls)

    logger.info('Finished scraper')


if __name__ == '__main__':
    main()
