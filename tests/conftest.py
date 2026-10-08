import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from helpers import Credential, generate_random_string, generate_unique_email
from pages import SinginPage, SingupPage


@pytest.fixture(scope="function")
def driver():
    """Фикстура драйвера с параметризацией по браузерам."""
    host = "selenoid"
    port = "4444"
    url = f"http://{host}:{port}/wd/hub"
    options = ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless")
    driver = webdriver.Remote(command_executor=url, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def credentials():
    return Credential(
        FIRST_NAME=generate_random_string(),
        LAST_NAME=generate_random_string(),
        USERNAME=generate_random_string(),
        EMAIL=generate_unique_email(),
        PASSWORD=generate_random_string(),
    )


@pytest.fixture
def registration_user(driver, credentials):
    singin = SinginPage(driver)
    singin.open_page()
    singin.click_singup_button()
    singup = SingupPage(driver)
    singup.first_name_input(credentials.FIRST_NAME)
    singup.last_name_input(credentials.LAST_NAME)
    singup.username_input(credentials.USERNAME)
    singup.email_input(credentials.EMAIL)
    singup.password_input(credentials.PASSWORD)
    singup.click_registaion_button()
    return credentials
