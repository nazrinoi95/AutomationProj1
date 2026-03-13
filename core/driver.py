from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions #Import and rename
from selenium.webdriver.firefox.options import Options as FirefoxOptions #Import and rename


def get_driver(browser = "chrome", headless=False): #This one set the default value as chrome and headless false
    if browser.lower() == "chrome": #Lower used so that it's not case-sensitive
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new") # Chrome have this flag
        options.add_argument("--start-maximized") #Starts with max screen
        driver = webdriver.Chrome(options=options)#This pass options we created in to webdriver.Chrome(options..
    elif browser.lower() == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless") #Firefox only have old flag
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Browser not supported: {browser}")

    return driver
