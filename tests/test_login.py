from pages.login_page import LoginPage
# This file is the test
def _setup_login_page(driver): # this is the helper "private" class to simplify steps
   login_page = LoginPage(driver)
   login_page.open()
   return login_page

def test_valid_login(driver):# setup will be injected from the conftestfiles
   login_page = _setup_login_page(driver)
   login_page.login("tomsmith", "SuperSecretPassword!")# does this overwrites the username and password in login_page?
   message = login_page.get_message()
   assert "You logged into a secure area!" in message

def test_invalid_login(driver):
   login_page = _setup_login_page(driver)
   login_page.login("wrong", "NotPassword")
   message = login_page.get_message()
   assert  "Your username is invalid!" in message

def test_invalid_login_wrong_username(driver):
   login_page = _setup_login_page(driver)
   login_page.login("tomsmiths", "SuperSecretPassword!")
   message = login_page.get_message()
   assert "Your username is invalid!" in message

def test_login_empty_fields(driver):
   login_page = _setup_login_page(driver)
   login_page.login("", "")
   message = login_page.get_message()
   assert "Your username is invalid!" in message


