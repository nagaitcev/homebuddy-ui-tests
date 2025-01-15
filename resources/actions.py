import logging
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

log = logging.getLogger(__name__)


class Actions(object):
    def __init__(self, driver):
        self.driver = driver

    def sleep(self, seconds: float, message: str = None):
        if message:
            log.info(f"Sleeping {seconds} seconds. Message: {message}")
        time.sleep(seconds)

    def verify_element(self, locator, verification_type="visibility", delay=30):
        verifications = {
            "clickable": ec.element_to_be_clickable,
            "visibility": ec.visibility_of_element_located,
        }
        try:
            WebDriverWait(self.driver, delay).until(
                verifications[verification_type](locator)
            )
        except TimeoutException:
            raise Exception(
                f"Failed to verify element '{locator[1]}' " f"{verification_type}"
            )

    def verify_header(self, locator, header_text):
        self.verify_element(locator)
        assert self.get_text_from_element(locator) == header_text, (
            f"Header is {self.get_text_from_element(locator)}, "
            f"doesn't match with expected: {header_text}"
        )

    def click(self, locator: tuple):
        self.verify_element(locator, verification_type="clickable")
        self.driver.find_element(*locator).click()
        self.sleep(1)

    def send_text(self, locator: tuple, text: str):
        self.verify_element(locator)
        self.driver.find_element(*locator).send_keys(text)
        self.sleep(0.3)

    def clear_field(self, locator: tuple):
        """Clear field by sending COMMAND + A + DELETE."""
        self.verify_element(locator)
        self.driver.find_element(*locator).send_keys(Keys.COMMAND, "a", Keys.DELETE)

    def clear_and_send_text(self, locator: tuple, text: str):
        self.verify_element(locator)
        self.clear_field(locator)
        self.send_text(locator, text)

    def get_text_from_element(self, locator):
        self.verify_element(locator)
        return self.driver.find_element(*locator).text

    def wait_for_element_to_disappear(self, locator, delay=30):
        try:
            WebDriverWait(self.driver, delay).until(
                ec.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            raise Exception(f"Element '{locator[1]}' is still visible")
