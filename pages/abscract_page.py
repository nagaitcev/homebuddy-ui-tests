import datetime
import logging
import os

from resources.actions import Actions

log = logging.getLogger(__name__)


class AbstractPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://hb-autotests.stage.sirenltd.dev/hvac"

    def open(self):
        self.driver.get(self.url)

    def take_screenshot(self, prefix):
        screenshot_dir = "screenshots"

        file_name = f"{prefix}_{datetime.datetime.now()}.png"
        log.info(
            f"Taking screenshot.\n"
            f"It will be saved in {screenshot_dir}\n"
            f"Name of the file: {file_name}"
        )
        self.driver.save_screenshot(os.path.join(screenshot_dir, file_name))

    def action(self, driver):
        return Actions(driver)

    def verify_page(self):
        """Page verification, should be defined for each page."""
        raise NotImplementedError
