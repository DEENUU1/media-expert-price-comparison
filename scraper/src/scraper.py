import json
from datetime import date

from typing import Optional, Dict
from models.product import Product
from models.price import Price

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import get_driver
import logging
from repository.product_repository import ProductRepository


logger = logging.getLogger(__name__)


def parse_product_data(product_data: dict) -> Product:
    price = Price(
        price=product_data.get("offers", {}).get("price"),
        date=date.today()
    )

    return Product(
        shop_id=product_data.get("productID"),
        name=product_data.get("name"),
        category=product_data.get("category"),
        description=product_data.get("description"),
        model=product_data.get("model"),
        prices=[price]
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


def get_product_data(url: str) -> Optional[Product]:
    driver = get_driver()
    logger.info(f"Getting data for {url}")
    driver.get(url)
    logger.info(f"Page title: {driver.title}")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )

    script_content = get_schema_script(driver, _type="Product")

    if not script_content:
        driver.quit()
        return

    product_data = parse_product_data(script_content)
    logger.info(f"Product data: {product_data}")

    return product_data


def scraper(url: str) -> None:
    product = get_product_data(url=url)

    product_repo = ProductRepository()
    product_repo.create_product(product)
