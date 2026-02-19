from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def get_driver(browser = "chrome", headless=False):
    if browser.lower() == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    elif browser.lower() == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--start-maximised")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Browser not supported: {browser}")

    return driver
