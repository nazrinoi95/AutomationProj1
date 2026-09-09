import pytest
import csv
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

def _load_login_data(file='tests/data/login_data.csv'):
    """Load login data from CSV file"""
    with open(file) as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            params = (row['username'], row['password'], row['expected_message'], row['expected_path'])
            if (row['username'] == 'tomsmith' and row['password'] == 'SuperSecretPassword!' or
                    (row['username'] == 'invalid_user' and row['password'] == 'invalid_password')):
                data.append(pytest.param(*params, marks=pytest.mark.smoke))
            else:
                data.append(params)
        return data

@pytest.mark.regression
@pytest.mark.parametrize("username,password,expected_message,expected_path", _load_login_data())
def test_login_parametrized(driver, username,password,expected_message,expected_path):
    """Test login with multiple credential combinations from CSV."""
    login_page =_setup_login_page(driver)
    login_page.login(username, password)
    actual_message = login_page.get_message()
    logger.info(f"Login message: {actual_message}")

    assert expected_message in actual_message
    assert login_page.get_current_url() == get_config("BASE_URL") + expected_path