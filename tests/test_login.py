from pages.login_page import LoginPage
# This file is the test
def test_valid_login(driver):# setup will be injected from the conftestfiles
   login_page = LoginPage(driver)
   login_page.open()
   login_page.login("tomsmith", "SuperSecretPassword!")# does this overwrites the username and password in login_page?

   message = login_page.get_message()
   assert "You logged into a secure area!" in message

