from selenium.webdriver.common.by import By
from core.actions import Actions
#This file is for login page
class LoginPage:
    #This section is assigning locators to a variables
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MSG = (By.ID, "flash")

    def __init__(self, driver): #this is for getting the driver
        self.driver = driver
        self.actions = Actions(driver)

    def open(self):
        self.driver.get(self.URL)

    def login (self, username, password):
        self.actions.type(self.USERNAME, username)
        self.actions.type(self.PASSWORD, password)
        self.actions.click(self.LOGIN_BTN)

    def get_message(self):
        return  self.actions.get_text(self.SUCCESS_MSG)