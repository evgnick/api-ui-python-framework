import allure
from allure_commons.types import AttachmentType


def attach_screenshot(driver):
    allure.attach(
        body=driver.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=AttachmentType.PNG
    )
