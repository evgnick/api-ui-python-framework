from config.ui_config import UiConfig


class TestLoad:

    def test_load(self):
        url = self.driver.get(UiConfig.UI_HOST)
        print(url)
