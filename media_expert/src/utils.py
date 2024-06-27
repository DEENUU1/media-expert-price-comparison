import subprocess
from contextlib import asynccontextmanager

from fastapi import FastAPI
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from config.settings import settings

APP_DIR = Path(__file__).resolve().parent
STATIC_DIR = APP_DIR / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Context manager for FastAPI app. It will run all code before `yield`
    on app startup, and will run code after `yield` on app shutdown.
    """

    try:
        subprocess.run([
            "tailwindcss",
            "-i",
            f"{STATIC_DIR}/src/tailwind.css",
            "-o",
            f"{STATIC_DIR}/css/main.css",
            "--minify"
        ])
    except Exception as e:
        print(f"Error running tailwindcss: {e}")

    yield


def get_driver() -> WebDriver:
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"

    options = webdriver.ChromeOptions()
    # options.add_argument('--headless=new')
    options.add_argument("--start-maximized")
    options.add_argument("user-agent={}".format(user_agent))

    driver = webdriver.Remote(
        command_executor=settings.SELENIUM_GRID,
        options=options
    )

    return driver
