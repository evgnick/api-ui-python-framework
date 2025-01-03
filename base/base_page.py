import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

from config.ui_config import UiConfig


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def open(self):
        with allure.step(f"Open page: {UiConfig.UI_HOST}"):
            self.driver.get(UiConfig.UI_HOST)
            return self
