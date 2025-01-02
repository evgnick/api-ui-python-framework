from helpers.login_helper import LoginHelper


class TestProfile:

    def test_change_profile_name(self, driver):
        self.result = (LoginHelper(self.driver)
                       .login_to_application()
                       .click_my_info_link()
                       .change_name("Maggie")
                       .save_changes()
                       .is_changes_saved())
