from selenium.webdriver.support import expected_conditions as ec

from base.base_page import BasePage
from pages.my_info_page import MyInfoPage


class NavigationMenu:

    _MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = BasePage(driver).wait

    def click_my_info_link(self):
        self.wait.until(ec.element_to_be_clickable(self._MY_INFO_BUTTON)).click()
        return MyInfoPage(self.driver)
