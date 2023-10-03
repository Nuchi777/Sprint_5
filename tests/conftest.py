import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=options, service=service)
    browser.get("https://stellarburgers.nomoreparties.site/")
    yield browser
    browser.quit()


@pytest.fixture()
def login(driver):
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))).click()
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys('evgenykoloskov1777@yandex.ru')
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys('230315')
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

