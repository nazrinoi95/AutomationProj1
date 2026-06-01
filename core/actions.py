from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# This file main fn is for actions
class Actions:
    def __init__(self, driver):  # can explain why init? and also self parameter for python
        """Initialize the Actions class with a WebDriver instance and set up WebDriverWait."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        """Click on an element identified by the given locator after waiting for it to be clickable."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        """Type the specified text into an element identified by the given locator after waiting for visibility."""
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def fill_form(self, fields_dict):
        """Fill multiple form fields using a dictionary of {locator: value} pairs."""
        for locator, value in fields_dict.items():
            self.type(locator, value)

    def get_text(self, locator):
        """Get the text content of an element identified by the given locator after waiting for visibility."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def get_url(self):
        """Get the current URL of the browser."""
        return self.driver.current_url

    def is_element_visible(self, locator):
        """Check if an element identified by the given locator is visible on the page."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False