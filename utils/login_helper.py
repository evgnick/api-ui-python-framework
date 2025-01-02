from config.ui_config import UiConfig
from pages.login_page import LoginPage


class LoginHelper:

    def __init__(self, driver):
        self.driver = driver

    def login_to_application(self):
        dashboard_page = (LoginPage(self.driver)
                          .open()
                          .enter_login(UiConfig.USERNAME)
                          .enter_password(UiConfig.PASSWORD)
                          .click_submit_button())
        return dashboard_page
