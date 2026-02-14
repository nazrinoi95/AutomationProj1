from selenium.webdriver.common.by import By

class LoginPage:

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']") # assigning the locators to a var
    SUCCESS_MSG = (By.ID, "flash")

    def __init__(self, driver): #this is for getting the driver
        self.driver = driver

    def open (self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login (self, user, pwd):
        self.driver.find_element(*self.USERNAME).send_keys(user)
        self.driver.find_element(*self.PASSWORD).send_keys(pwd)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def get_message(self):
        return self.driver.find_element(*self.SUCCESS_MSG).text