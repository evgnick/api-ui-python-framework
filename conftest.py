import pytest
from config.ui_config import UiConfig
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def configure_chrome_options(chrome_options_list):
    options = Options()
    for opt in chrome_options_list:
        if opt:
            options.add_argument(opt)

    return options


@pytest.fixture(autouse=True)
def driver(request):
    chrome_options = UiConfig.CHROME_OPTIONS
    options = configure_chrome_options(chrome_options)
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver

    yield

    driver.quit()
