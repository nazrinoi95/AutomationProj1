import pytest
from utils.screenshot import take_screenshot
from core.driver import get_driver

def pytest_addoption(parser):
    # Registers CLI options so tests can be run with --browser and --headless flags
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store_true")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = get_driver(browser=browser, headless=headless)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            take_screenshot(driver,item.name)