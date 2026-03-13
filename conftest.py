import pytest #This imports the pytest library
from core.driver import get_driver #This imports from core file with driver fn and import the get_driver method

def pytest_addoption(parser): #method
    parser.addoption("--browser", action="store", default="chrome") #This stores browser = chrome, that is what action does
    parser.addoption("--headless", action="store_true") #This ones stores if true, eg: --headless = Y , --headless = true
    #Why do we use the parser.adoption method or class idk?

@pytest.fixture #This provide resources for test : setup → give resource → cleanup. Resource now is SWD?
def driver(request):#method
    browser = request.config.getoption("--browser") #This read the value from command line and store it
    headless = request.config.getoption("--headless") #This read the value from command line and store it

    driver = get_driver(browser=browser, headless=headless) #Calls the driver.py
    yield driver # This one for cleanup
    driver.quit()

    #Flow would be
    # driver created
    # ↓
    # yield driver
    # ↓
    # test uses driver
    # ↓
    # driver.quit()