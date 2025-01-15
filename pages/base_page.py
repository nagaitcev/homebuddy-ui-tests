from selenium.webdriver.common.by import By

from .abscract_page import AbstractPage


class BasePage(AbstractPage):
    logo = (
        By.CSS_SELECTOR,
        "a.logo__container",
    )

    def __init__(self, driver):
        super().__init__(driver)

    def verify_page(self):
        self.action(self.driver).verify_element(self.logo)
