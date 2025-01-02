import os
from dotenv import load_dotenv

load_dotenv()


class UiConfig:

    UI_HOST = os.getenv("UI_HOST")
    USERNAME = os.getenv("ADMIN_USERNAME")
    PASSWORD = os.getenv("ADMIN_PASSWORD")
    CHROME_OPTIONS = os.getenv("CHROME_OPTIONS", "").split(";")
