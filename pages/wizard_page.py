from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage


class WizardPage(BasePage):

    logo = (By.CSS_SELECTOR, "div.logo")
    mascot = (By.CSS_SELECTOR, "img[alt='HomeBuddy Mascot']")
    header = (By.CSS_SELECTOR, "div#StepBodyId h4")
    header_text = ""

    def __init__(self, driver, previous_page=None):
        super().__init__(driver)
        self.previous_page = previous_page

    def verify_page(self):
        super().verify_page()
        self.action(self.driver).verify_element(self.mascot)
        if not self.header_text:
            raise ValueError("Header text is not set")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_any_elements_located(self.header)
            )
            self.action(self.driver).verify_header(self.header, self.header_text)
        except AssertionError:
            self.action(self.driver).sleep(3)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_any_elements_located(self.header)
            )
            self.action(self.driver).verify_header(self.header, self.header_text)


class WizardPageProjectType(WizardPage):

    header_text = "What type of project is this?"
    project_types = {
        "Replacement/installation": "replacementorinstallation",
        "Repair": "repair",
    }
    next_button = (By.CSS_SELECTOR, "div.typesOfProject button[type='submit']")

    def click_project_type(self, project_type):
        self.action(self.driver).click(
            (
                By.CSS_SELECTOR,
                f"li:has(input[data-autotest-projecttype-{self.project_types[project_type]}])",
            )
        )

    def click_next(self):
        self.action(self.driver).click(self.next_button)

        from .wizard_page import WizardPageProjectEquipment

        return WizardPageProjectEquipment(self.driver)


class WizardPageProjectEquipment(WizardPage):

    header_text = "What equipment is involved in your project?"
    equipment_types = {
        "Air conditioner": "airconditioner",
        "Central heating/furnace": "heatingorfurnace",
        "Boiler/radiator": "boilerorradiator",
        "Heat pump": "heatpump",
        "Water heater": "waterheater",
    }
    next_button = (By.CSS_SELECTOR, "div.involvedEquipment button[type='submit']")

    def click_equipment(self, equipment):
        self.action(self.driver).click(
            (
                By.CSS_SELECTOR,
                f"li:has(input[data-autotest-equipment-{self.equipment_types[equipment]}])",
            )
        )

    def click_next(self):
        self.action(self.driver).click(self.next_button)

        from .wizard_page import WizardPageProjectHVAC

        return WizardPageProjectHVAC(self.driver)


class WizardPageProjectHVAC(WizardPage):

    header_text = "What runs your HVAC system?"
    hvac_types = {
        "Gas": "gas",
        "Electricity": "electricity",
        "Propane": "propane",
        "Oil": "oil",
        "Not sure": "notsure",
    }
    next_button = (By.CSS_SELECTOR, "div.energySource button[type='submit']")

    def click_hvac(self, hvac):
        self.action(self.driver).click(
            (
                By.CSS_SELECTOR,
                f"li:has(input[data-autotest-energysource-{self.hvac_types[hvac]}])",
            )
        )

    def click_next(self):
        self.action(self.driver).click(self.next_button)

        from .wizard_page import WizardPageProjectAge

        return WizardPageProjectAge(self.driver)


class WizardPageProjectAge(WizardPage):

    header_text = "How old is your equipment?"
    ages = {
        "Less than 5 years": "5",
        "5 to 10 years": "10",
        "Older than 10 years": "10plus",
        "Not sure": "notsure",
    }
    next_button = (By.CSS_SELECTOR, "div.equipmentAge button[type='submit']")

    def click_age(self, age):
        self.action(self.driver).click(
            (
                By.CSS_SELECTOR,
                f"li:has(input[data-autotest-equipmentage-{self.ages[age]}])",
            )
        )

    def click_next(self):
        self.action(self.driver).click(self.next_button)

        from .wizard_page import WizardPagePropertyType

        return WizardPagePropertyType(self.driver)


class WizardPagePropertyType(WizardPage):

    header_text = "What type of property is this?"
    property_types = {
        "Detached, semi-detached, row house": "detached",
        "Mobile, modular, manufactured home": "mobile",
        "Commercial": "commercial",
        "Apartment building or condominium": "apartment",
    }
    next_button = (By.CSS_SELECTOR, "div.typeOfProperty button[type='submit']")

    def click_property_type(self, property_type):
        self.action(self.driver).click(
            (
                By.CSS_SELECTOR,
                f"li:has(input[data-autotest-propertytype-{self.property_types[property_type]}])",
            )
        )

    def click_next(self):
        self.action(self.driver).click(self.next_button)

        from .wizard_page import WizardPagePropertySize

        return WizardPagePropertySize(self.driver)


class WizardPagePropertySize(WizardPage):

    header_text = "Approximately how large is your house in square feet?"
    house_area_field = (By.CSS_SELECTOR, "input#squareFeet")
    next_button = (By.CSS_SELECTOR, "div#StepBodyId button[type='button']")

    def fill_house_area(self, house_area):
        self.action(self.driver).clear_and_send_text(self.house_area_field, house_area)

    def click_next(self):
        self.action(self.driver).click(self.next_button)

        from .wizard_page import WizardPageAuthorizedChanges

        return WizardPageAuthorizedChanges(self.driver)


class WizardPageAuthorizedChanges(WizardPage):

    header_text = "Are you the homeowner or authorized to make property changes?"
    is_authorized = {
        "Yes": "yes",
        "No": "no",
    }
    next_button = (By.CSS_SELECTOR, "div#StepBodyId button[type='submit']")

    def click_authorized(self, authorized):
        self.action(self.driver).click(
            (
                By.CSS_SELECTOR,
                f"input[data-autotest-owner-{self.is_authorized[authorized]}] + label",
            )
        )

    def click_next(self):
        self.action(self.driver).click(self.next_button)

        from .wizard_page import WizardPagePersonalData

        return WizardPagePersonalData(self.driver)


class WizardPagePersonalData(WizardPage):

    header_text = "Who should I prepare this estimate for?"
    name_field = (By.CSS_SELECTOR, "input#fullName")
    email_field = (By.CSS_SELECTOR, "input#email")
    next_button = (By.CSS_SELECTOR, "div#StepBodyId button[type='submit']")

    def fill_name(self, name):
        self.action(self.driver).clear_and_send_text(self.name_field, name)

    def fill_email(self, email):
        self.action(self.driver).clear_and_send_text(self.email_field, email)

    def click_next(self):
        self.action(self.driver).click(self.next_button)

        from .wizard_page import WizardPagePhoneNumber

        return WizardPagePhoneNumber(self.driver)


class WizardPagePhoneNumber(WizardPage):

    header_text = "What is your phone number?"
    phone_field = (By.CSS_SELECTOR, "input#phoneNumber")
    next_button = (By.CSS_SELECTOR, "div#StepBodyId button[type='button']")
    processing_button = (By.CSS_SELECTOR, "button[data-state='processing']")

    def fill_phone_number(self, name):
        self.action(self.driver).clear_and_send_text(self.phone_field, name)

    def click_next(self):
        self.action(self.driver).click(self.next_button)
        self.action(self.driver).wait_for_element_to_disappear(
            self.processing_button, delay=120
        )

        from .wizard_page import WizardPageFinal

        return WizardPageFinal(self.driver)


class WizardPageFinal(WizardPage):

    message_field = (By.CSS_SELECTOR, "h2")
    home_page_button = (By.CSS_SELECTOR, "a.customButton")

    def verify_page(self):
        self.action(self.driver).verify_element(self.home_page_button)

    def get_message(self):
        return self.action(self.driver).get_text_from_element(self.message_field)

    def click_home_page(self):
        self.action(self.driver).click(self.home_page_button)

        from .home_page import HomePage

        return HomePage(self.driver)
