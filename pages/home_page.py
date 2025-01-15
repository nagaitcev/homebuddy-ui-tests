from selenium.webdriver.common.by import By

from .base_page import BasePage
from .wizard_page import WizardPageProjectType


class HomePage(BasePage):

    header = (By.CSS_SELECTOR, "h2.header__zipTitle")
    header_text = "What Is Your ZIP Code?"
    zip_code_field = (By.CSS_SELECTOR, "input#zipCode")
    get_estimate_button = (By.CSS_SELECTOR, "div.header__content button[type='submit']")

    def verify_page(self):
        super().verify_page()
        self.action(self.driver).verify_header(self.header, self.header_text)

    def set_zip_code(self, zip_code):
        self.action(self.driver).clear_and_send_text(self.zip_code_field, zip_code)

    def click_set_estimate(self):
        self.action(self.driver).click(self.get_estimate_button)
        return WizardPageProjectType(self.driver, previous_page=self)
