import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Keys

from conftest import driver


class MyInfoPage(BasePage):

    _FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    _SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")
    _SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    def __init__(self, driver):
        super().__init__(driver)
        self.name = None

    def change_name(self, new_name):
        with allure.step(f"Change name to: {new_name}"):
            first_name_field = self.wait.until(ec.element_to_be_clickable(self._FIRST_NAME_FIELD))
            first_name_field.click()
            first_name_field.send_keys(Keys.CONTROL + "A")
            first_name_field.send_keys(Keys.BACKSPACE)
            first_name_field.send_keys(new_name)
            self.name = new_name
            return self

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(ec.element_to_be_clickable(self._SAVE_BUTTON)).click()
        return self

    @allure.step("Get first name")
    def get_first_name(self):
        return self.wait.until(ec.visibility_of_element_located(self._FIRST_NAME_FIELD)).get_attribute("value")
