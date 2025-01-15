import logging

import pytest
import webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from driver.uidriver import ChromeDriver

from .utils import open_page, take_screenshot

log = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def driver():
    """
    create / close web driver
    """
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--no-sandbox")
        driver = ChromeDriver(
            service=Service(webdriver_manager.chrome.ChromeDriverManager().install())
        )

        driver.implicitly_wait(10)
        yield driver

    finally:
        driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def teardown(request, driver):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        log.critical(f"setting up a test failed! {request.node.nodeid}")
        take_screenshot(
            driver,
            (
                str(request.node.nodeid)
                .replace("tests/", "")
                .replace(".py", "-")
                .replace("::", "_")
            ),
        )

    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            log.critical(f"executing test failed {request.node.nodeid}")
            take_screenshot(
                driver,
                (
                    str(request.node.nodeid)
                    .replace("tests/", "")
                    .replace(".py", "")
                    .replace("::", "_")
                ),
            )


@pytest.fixture
def open_home_page(driver):
    open_page(
        driver
    )  # TODO bad design, scope should be changed, but first need to create page objects for main page and for each choice of the project type
    return driver
