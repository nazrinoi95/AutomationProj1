from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# This file main fn is for actions
class Actions:
    def __init__(self,driver): # can explain why init? and also self parameter for python
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def click(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    def type(self,locator,text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
    def get_text(self,locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    def get_url(self):
        return self.driver.current_url
