import pytest
import allure
from config.ui_config import UiConfig
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helpers.screenshot import attach_screenshot


def configure_chrome_options(chrome_options_list):
    options = Options()
    for opt in chrome_options_list:
        if opt:
            options.add_argument(opt)

    return options


@pytest.fixture(scope="function")
@allure.title("Prepare for the test")
def driver(request):
    chrome_options = UiConfig.CHROME_OPTIONS
    options = configure_chrome_options(chrome_options)
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
@allure.title("Attach screenshot")
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            attach_screenshot(driver)
