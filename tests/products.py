import allure
import pytest

from helpers.login_helper import LoginHelper


@allure.feature("Products item")
class TestProductsItem:

    @allure.title("Go to products")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_go_to_products(self, driver):

        self.actual_title = (LoginHelper(driver)
                             .login_to_application()
                             .get_title())

        assert self.actual_title == "Swag Labs1"
