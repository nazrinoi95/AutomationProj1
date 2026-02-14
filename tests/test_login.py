from pages.login_page import LoginPage

def test_valid_login(driver):# setup will be injected from the conftestfiles
   login = LoginPage(driver)
   login.open()
   login.login("tomsmith", "SuperSecretPassword!")

   assert "You logged into a secure area!" in login.get_message()

