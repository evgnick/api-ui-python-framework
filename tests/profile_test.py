import allure
import pytest

from helpers.login_helper import LoginHelper


@allure.feature("Profile functionality")
class TestProfile:

    @allure.title("Change profile name")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_change_profile_name(self, driver):
        new_name = "Maggie"

        self.first_name = (LoginHelper(driver)
                           .login_to_application()
                           .click_my_info_link()
                           .change_name(new_name)
                           .save_changes()
                           .get_first_name())

        assert self.first_name == new_name
