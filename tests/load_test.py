from config.ui_config import UiConfig
from base.base_test import BaseTest


class TestLoad(BaseTest):

    def test_load(self):
        self.login_page.open()
        self.login_page.enter_login(UiConfig.USERNAME)
        print(UiConfig.USERNAME)
        print(UiConfig.PASSWORD)
        self.login_page.enter_password(UiConfig.PASSWORD)
        self.login_page.click_submit_button()
