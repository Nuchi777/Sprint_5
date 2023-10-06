import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import UrlsStellarBurgers
from data import PersonStellarBurgers
from locators import MainPageLocators
from locators import AuthPageLocators

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=options, service=service)
    browser.get(UrlsStellarBurgers.URL)
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(MainPageLocators.BUTTON_ACCOUNT)).click()
    driver.find_element(*AuthPageLocators.EMAIL).send_keys(PersonStellarBurgers.EMAIL)
    driver.find_element(*AuthPageLocators.PASSWORD).send_keys(PersonStellarBurgers.PASSWORD)
    driver.find_element(*AuthPageLocators.BUTTON_LOGIN).click()
    return driver
