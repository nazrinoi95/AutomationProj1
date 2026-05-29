from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions #Import and rename
from selenium.webdriver.firefox.options import Options as FirefoxOptions #Import and rename
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_driver(browser = "chrome", headless=False): #This one set the default value as chrome and headless false
    if browser.lower() == "chrome": #Lower used so that it's not case-sensitive
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new") # Chrome have this flag
        options.add_argument("--start-maximized") #Starts with max screen
        service = ChromeService(ChromeDriverManager().install()) #This is for using webdriver manager to automatically download the driver
        driver = webdriver.Chrome(service = service, options=options)#This pass options we created in to webdriver.Chrome(options..
    elif browser.lower() == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless") #Firefox only have old flag
        service = FirefoxService(GeckoDriverManager().install()) #This is for using webdriver manager to automatically download the driver
        driver = webdriver.Firefox(service=service, options=options) #This pass options we created in to webdriver.Firefox(options..)
        driver.maximize_window() #Firefox doesn't have start-maximized flag, so we need to maximize the window after creating the driver
    else:
        raise ValueError(f"Browser not supported: {browser}")

    return driver
