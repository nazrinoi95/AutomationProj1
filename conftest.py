import pytest
from core.driver import get_driver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store_true")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    driver = get_driver(browser=browser, headless=headless)
    yield driver # Give driver to test here
    driver.quit()