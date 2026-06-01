from selenium.webdriver.common.by import By
from core.actions import Actions


# This file is for login page
class LoginPage:
    # This section is assigning locators to a variables
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MSG = (By.ID, "flash")
    LOGOUT_BTN = (By.PARTIAL_LINK_TEXT, "Logout")

    def __init__(self, driver):  # this is for getting the driver
        """Initialize the LoginPage class with a WebDriver instance and Actions helper."""
        self.driver = driver
        self.actions = Actions(driver)

    def open(self):
        """Navigate to the login page URL."""
        self.driver.get(self.URL)

    def login(self, username, password):
        """Perform login by filling the username and password fields and clicking the login button."""
        fields = {
            self.USERNAME: username,
            self.PASSWORD: password
        }
        self.actions.fill_form(fields)
        self.actions.click(self.LOGIN_BTN)
        return self

    def get_message(self):
        """Get the flash message text displayed after login attempt."""
        return self.actions.get_text(self.FLASH_MSG)

    def get_current_url(self):
        """Get the current URL of the browser."""
        return self.actions.get_url()

    def get_pagetitle(self):
        """Get the title of the current page."""
        return self.driver.title

    def is_logout_button_visible(self):
        """Check the logout button is visible in the secure area."""
        return self.actions.is_element_visible(self.LOGOUT_BTN)

    def is_login_button_visible(self):
        """Check the login button is visible in the login page."""
        return self.actions.is_element_visible(self.LOGIN_BTN)