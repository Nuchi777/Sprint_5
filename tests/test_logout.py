from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestStellarBurgersLogout:
    def test_logout(self, driver, login):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.TEXT_BUTTON_LOGOUT)).click()
        text = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.BUTTON_LOGIN)).text
        assert text == "Войти"
