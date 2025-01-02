import time

from config.ui_config import UiConfig
from pages.login_page import LoginPage
from utils.login_helper import LoginHelper


class TestLoad:

    def test_load(self):
        self.login_page = (LoginPage(self.driver)
                           .open()
                           .login(UiConfig.USERNAME, UiConfig.PASSWORD)
                           .get_url())

    def test_load_2(self):
        self.dashboard_page = (LoginHelper(self.driver)
                               .login_to_application()
                               .get_url())
