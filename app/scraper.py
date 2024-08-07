import json
from datetime import date

from typing import Optional, Dict

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import get_driver
from repository.product_repository import create_product, product_exists_by_shop_id, get_product_by_shop_id
from repository.price_repository import create_price
from schemas.product_schemas import ProductInputSchema
from schemas.price_schemas import PriceInputSchema
import logging
from concurrent.futures import ThreadPoolExecutor

from sqlalchemy.orm import Session

from config.database import get_db
from repository.source_repository import get_sources

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


def parse_product_data(product_data: dict) -> ProductInputSchema:
    price = PriceInputSchema(
        price=product_data.get("offers", {}).get("price"),
        date=str(date.today())
    )

    return ProductInputSchema(
        shop_id=product_data.get("productID"),
        name=product_data.get("name"),
        category=product_data.get("category"),
        description=product_data.get("description"),
        model=product_data.get("model"),
        prices=[price],
        url=product_data.get("url")
    )


def get_schema_script(driver, _type: str) -> Optional[Dict]:
    scripts = driver.find_elements(By.XPATH, '//script[@type="application/ld+json"]')
    script_content = None

    for script in scripts:
        html_script = script.get_attribute("innerHTML")
        try:
            script_json = json.loads(html_script)

            if script_json.get("@type") == "Product":
                script_content = script_json
                logger.info(f"Found product data")
                driver.quit()

        except json.JSONDecodeError:
            continue

    return script_content


def get_product_data(url: str) -> Optional[ProductInputSchema]:
    driver = get_driver()
    logger.info(f"Getting data for {url}")
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    logger.info(f"Page title: {driver.title}")

    script_content = get_schema_script(driver, _type="Product")

    if not script_content:
        driver.quit()
        return

    product_data = parse_product_data(script_content)
    driver.quit()
    return product_data


def scraper(db: Session, url: str) -> None:
    product = get_product_data(url=url)
    logger.info(f"Product data: {product}")

    if not product:
        return

    if not product_exists_by_shop_id(db, product.shop_id):
        product_object = create_product(db, product)

        product.prices[0].product_id = product_object.id

        create_price(db, product.prices[0])
        return

    existing_product_object = get_product_by_shop_id(db, product.shop_id)

    product.prices[0].product_id = existing_product_object.id
    create_price(db, product.prices[0])


def main():
    logger.info('Starting scraper')

    db: Session = next(get_db())

    urls = get_sources(db)

    for url in urls:
        scraper(db, url.url)

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(scraper, urls)

    logger.info('Finished scraper')


if __name__ == '__main__':
    main()
