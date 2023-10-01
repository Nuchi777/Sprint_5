import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=options, service=service)
    browser.get("https://stellarburgers.nomoreparties.site/")
    yield browser
    browser.quit()
