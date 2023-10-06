from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators
from locators import AccountPageLocators
from locators import AuthPageLocators
import time


class TestStellarBurgersLogout:
    def test_logout(self, driver, login):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(AccountPageLocators.TEXT_BUTTON_LOGOUT)).click()
        text = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(AuthPageLocators.BUTTON_LOGIN)).text
        assert text == "Войти"
