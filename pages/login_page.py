import allure
from base.base_page import BasePage
from pages.products_page import ProductsPage
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(BasePage):

    _USERNAME_FIELD = ("xpath", "//input[@name='user-name']")
    _PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    _SUBMIT_BUTTON = ("xpath", "//input[@id='login-button']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_login(self, login):
        with allure.step("Enter login"):
            self.wait.until(ec.element_to_be_clickable(self._USERNAME_FIELD)).send_keys(login)
            return self

    def enter_password(self, password):
        with allure.step("Enter password"):
            self.wait.until(ec.element_to_be_clickable(self._PASSWORD_FIELD)).send_keys(password)
            return self

    @allure.step("Click login button")
    def click_submit_button(self):
        self.wait.until(ec.element_to_be_clickable(self._SUBMIT_BUTTON)).click()
        return ProductsPage(self.driver)
