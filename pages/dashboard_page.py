from base.base_page import BasePage
from base.navigation_menu import NavigationMenu


class DashboardPage(BasePage, NavigationMenu):

    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self):
        return self.driver.current_url
