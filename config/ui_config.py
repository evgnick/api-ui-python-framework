import os
from dotenv import load_dotenv

load_dotenv()


class UiConfig:
    UI_HOST = os.getenv("UI_HOST")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    CHROME_OPTIONS = os.getenv("CHROME_OPTIONS", "").split(";")
