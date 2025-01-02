from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Keys


class MyInfoPage(BasePage):

    _FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    _SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")
    _SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    def __init__(self, driver):
        super().__init__(driver)
        self.name = None

    def change_name(self, new_name):
        first_name_field = self.wait.until(ec.element_to_be_clickable(self._FIRST_NAME_FIELD))
        first_name_field.click()
        first_name_field.send_keys(Keys.CONTROL + "A")
        first_name_field.send_keys(Keys.BACKSPACE)
        first_name_field.send_keys(new_name)
        self.name = new_name
        return self

    def save_changes(self):
        self.wait.until(ec.element_to_be_clickable(self._SAVE_BUTTON)).click()
        return self

    def is_changes_saved(self):
        self.wait.until(ec.invisibility_of_element_located(self._SPINNER))
        self.wait.until(ec.visibility_of_element_located(self._FIRST_NAME_FIELD))
        self.wait.until(ec.text_to_be_present_in_element_value(self._FIRST_NAME_FIELD, self.name))
