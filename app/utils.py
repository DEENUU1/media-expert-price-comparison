from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from config.database import engine
from models import Source, Product, Price


def get_driver() -> WebDriver:
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument("--start-maximized")
    options.add_argument("user-agent={}".format(user_agent))

    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    return driver


def init_db() -> None:
    Source.metadata.create_all(engine)
    Product.metadata.create_all(engine)
    Price.metadata.create_all(engine)
