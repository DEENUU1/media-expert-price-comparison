import logging
from scraper import scraper

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


def main():
    logger.info('Starting scraper')
    scraper()
    logger.info('Finished scraper')


if __name__ == '__main__':
    main()
