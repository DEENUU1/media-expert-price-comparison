import json

from pydantic import BaseModel, Field
from typing import Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import get_driver
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


class Product(BaseModel):
    shop_id: int
    name: str
    category: str
    currency: str
    price: float
    description: Optional[str] = None
    model: Optional[str] = None


def parse_product_data(product_data: dict) -> Product:
    return Product(
        shop_id=product_data.get("productID"),
        name=product_data.get("name"),
        category=product_data.get("category"),
        currency=product_data.get("offers", {}).get("priceCurrency"),
        price=product_data.get("offers", {}).get("price"),
        description=product_data.get("description"),
        model=product_data.get("model")

    )


def get_product_data(url: str) -> Optional[Product]:
    driver = get_driver()
    logger.info(f"Getting data for {url}")
    driver.get(url)
    logger.info(f"Page title: {driver.title}")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )

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

    if not script_content:
        driver.quit()
        return

    product_data = parse_product_data(script_content)
    logger.info(f"Product data: {product_data}")

    return product_data


get_product_data(
    url="https://www.mediaexpert.pl/smartfony-i-zegarki/smartfony/smartfon-apple-iphone-15-5g-green-128gb"
)
