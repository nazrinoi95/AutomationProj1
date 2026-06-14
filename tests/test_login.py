import pytest
from pages.login_page import LoginPage
from utils.logger import get_logger
from utils.config import get_config

# Logger tracks test execution flow and helps debug failures.
logger = get_logger(__name__)

def _setup_login_page(driver):
    """Helper function to initialize and open the login page."""
    login_page = LoginPage(driver)
    login_page.open()
    return login_page

@pytest.mark.regression
@pytest.mark.smoke
def test_valid_login(driver):
    """Tests successful login with valid credentials."""
    login_page = _setup_login_page(driver)
    login_page.login(get_config("VALID_USERNAME"), get_config("VALID_PASSWORD"))
    success_message = login_page.get_message()
    logger.info(f"Login success message: {success_message}")

    assert "You logged into a secure area!" in success_message
    assert login_page.get_current_url() == get_config("BASE_URL") + "/secure"
    assert login_page.is_logout_button_visible() == True

    logger.info("Test 'test_valid_login' passed successfully.")

@pytest.mark.regression
@pytest.mark.smoke
def test_invalid_login(driver):
    """Tests login failure with invalid username and password."""
    login_page = _setup_login_page(driver)
    login_page.login(get_config("INVALID_USERNAME"), get_config("INVALID_PASSWORD"))
    error_message = login_page.get_message()
    logger.info(f"Login error message: {error_message}")

    assert "Your username is invalid!" in error_message
    assert login_page.get_current_url() == get_config("BASE_URL") + "/login"
    assert login_page.is_login_button_visible()== True

    logger.info("Test 'test_invalid_login' passed successfully.")

@pytest.mark.regression
def test_invalid_login_wrong_username(driver):
    """Tests login failure with incorrect username but correct password."""
    login_page = _setup_login_page(driver)
    login_page.login(get_config("INVALID_USERNAME"), get_config("VALID_PASSWORD"))
    error_message = login_page.get_message()
    logger.info(f"Login error message: {error_message}")

    assert "Your username is invalid!" in error_message
    assert login_page.get_current_url() == get_config("BASE_URL") + "/login"
    assert login_page.is_login_button_visible() == True

    logger.info("Test 'test_invalid_login_wrong_username' passed successfully.")

@pytest.mark.regression
def test_invalid_login_wrong_password(driver):
    """Tests login failure with correct username but incorrect password."""
    login_page = _setup_login_page(driver)
    login_page.login(get_config("VALID_USERNAME"), get_config("INVALID_PASSWORD"))
    error_message = login_page.get_message()
    logger.info(f"Login error message: {error_message}")

    assert "Your password is invalid!" in error_message
    assert login_page.get_current_url() == get_config("BASE_URL") + "/login"
    assert login_page.is_login_button_visible() == True

    logger.info("Test 'test_invalid_login_wrong_password' passed successfully.")

@pytest.mark.regression
def test_login_empty_fields(driver):
    """Tests login failure when both username and password fields are empty."""
    login_page = _setup_login_page(driver)
    login_page.login("", "")
    error_message = login_page.get_message()
    logger.info(f"Login error message: {error_message}")

    assert "Your username is invalid!" in error_message
    assert login_page.get_current_url() == get_config("BASE_URL") + "/login"
    assert login_page.is_login_button_visible() == True

    logger.info("Test 'test_login_empty_fields' passed successfully.")
