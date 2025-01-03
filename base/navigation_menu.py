import allure
from selenium.webdriver.support import expected_conditions as ec
from base.base_page import BasePage


class NavigationMenu:

    _BURGER_BUTTON = ("xpath", "//button[@id='react-burger-menu-btn']")
    _ALL_ITEMS_BUTTON = ("xpath", "//a[@id='inventory_sidebar_link']']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = BasePage(driver).wait

    @allure.step("Click burger menu")
    def click_burger_menu(self):
        self.wait.until(ec.element_to_be_clickable(self._BURGER_BUTTON)).click()
        return self

    @allure.step("Select all items")
    def click_all_items(self):
        from pages.products_page import ProductsPage
        self.wait.until(ec.element_to_be_clickable(self._ALL_ITEMS_BUTTON)).click()
        return ProductsPage(self.driver)
