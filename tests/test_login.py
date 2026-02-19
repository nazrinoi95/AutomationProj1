from pages.login_page import LoginPage

def test_valid_login(driver):# setup will be injected from the conftestfiles
   login_page = LoginPage(driver)
   login_page.open()
   login_page.login("tomsmith", "SuperSecretPassword!")

   message = login_page.get_message()
   assert "You logged into a secure area!" in login_page.get_message()

