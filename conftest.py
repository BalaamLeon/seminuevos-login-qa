import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils import data

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")

    service = Service(ChromeDriverManager().install())
    d = webdriver.Chrome(service=service, options=options)
    d.set_page_load_timeout(30)

    yield d
    d.quit()

@pytest.fixture(scope="function")
def login_page(driver):
    driver.get(data.login_url)
    return LoginPage(driver)

@pytest.fixture(scope="function")
def home_page(driver):
    return HomePage(driver)
