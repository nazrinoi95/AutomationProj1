from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_driver(browser = "chrome", headless=False):
    # Using Lower to make it not case-sensitive.
    if browser.lower() == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--start-maximized")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service, options=options)
    elif browser.lower() == "firefox":
        options = FirefoxOptions()
        if headless:
            # Firefox is using old headless flag.
            options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        # Firefox doesn't have start-maximized flag, this should be default after creating the driver.
        driver.maximize_window()
    else:
        raise ValueError(f"Browser not supported: {browser}")

    return driver
