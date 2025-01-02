from base.base_page import BasePage
from pages.dashboard_page import DashboardPage
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(BasePage):

    _USERNAME_FIELD = ("xpath", "//input[@name='username']")
    _PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    _SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_login(self, login):
        self.wait.until(ec.element_to_be_clickable(self._USERNAME_FIELD)).send_keys(login)
        return self

    def enter_password(self, password):
        self.wait.until(ec.element_to_be_clickable(self._PASSWORD_FIELD)).send_keys(password)
        return self

    def click_submit_button(self):
        self.wait.until(ec.element_to_be_clickable(self._SUBMIT_BUTTON)).click()
        return DashboardPage(self.driver)
