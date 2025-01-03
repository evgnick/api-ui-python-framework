import allure
from base.base_page import BasePage
from base.navigation_menu import NavigationMenu


class ProductsPage(BasePage, NavigationMenu):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get current title")
    def get_title(self):
        return self.driver.title
