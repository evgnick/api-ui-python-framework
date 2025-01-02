from config.ui_config import UiConfig


class TestLoad:

    def test_load(self):
        self.driver.get(UiConfig.UI_HOST)
        print(self.driver.current_url)
