import pytest
from pages.login_page import LoginPage
from config.ui_config import UiConfig


class BaseTest:

    config: UiConfig
    login_page: LoginPage

    @classmethod
    @pytest.fixture(autouse=True)
    def setup(cls, request, driver):
        request.cls.driver = driver
        request.cls.config = UiConfig()
        request.cls.login_page = LoginPage(driver)
