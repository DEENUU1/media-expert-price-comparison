from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from config.settings import settings


def get_driver() -> WebDriver:
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"

    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument("--start-maximized")
    options.add_argument("user-agent={}".format(user_agent))

    driver = webdriver.Remote(
        command_executor=settings.SELENIUM_GRID,
        options=options
    )

    return driver
