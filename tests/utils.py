from pages.home_page import HomePage


def open_page(driver):
    page = HomePage(driver)
    page.open()
    page.verify_page()
    driver.set_page(page)


def take_screenshot(driver, prefix="screenshot"):
    page = driver.get_page()
    page.take_screenshot(prefix=f"{prefix}_{page.__class__.__name__}")


def create_project(
    driver,
    zip_code: str,
    project_type: str,
    equipment: str,
    hvac: str,
    age: str,
    property_type: str,
    house_area: int,
    authorized: str,
    name: str,
    email: str,
    phone_number: str,
):
    page = driver.get_page()
    page.verify_page()
    page.set_zip_code(zip_code)
    page = page.click_set_estimate()  # go to wizard step 1
    page.verify_page()
    page.click_project_type(project_type)
    page = page.click_next()  # go to wizard step 2
    page.verify_page()
    page.click_equipment(equipment)
    page = page.click_next()  # go to wizard step 3
    page.verify_page()
    page.click_hvac(hvac)
    page = page.click_next()  # go to wizard step 4
    page.verify_page()
    page.click_age(age)
    page = page.click_next()  # go to wizard step 5
    page.verify_page()
    page.click_property_type(property_type)
    page = page.click_next()  # go to wizard step 6
    page.verify_page()
    page.fill_house_area(house_area)
    page = page.click_next()  # go to wizard step 7
    page.verify_page()
    page.click_authorized(authorized)
    page = page.click_next()  # go to wizard step 8
    page.verify_page()
    page.fill_name(name)
    page.fill_email(email)
    page = page.click_next()  # go to wizard step 9
    page.verify_page()
    page.fill_phone_number(phone_number)
    page = page.click_next()  # go to wizard step 10
    page.verify_page()
    return page.get_message()
