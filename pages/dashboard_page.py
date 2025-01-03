import allure
from base.base_page import BasePage
from base.navigation_menu import NavigationMenu


class DashboardPage(BasePage, NavigationMenu):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get current url")
    def get_url(self):
        return self.driver.current_url
