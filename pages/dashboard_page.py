from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec


class DashboardPage(BasePage):

    MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_my_info_link(self):
        self.wait.until(ec.element_to_be_clickable(self.MY_INFO_BUTTON)).click()

    def get_url(self):
        return self.driver.current_url
