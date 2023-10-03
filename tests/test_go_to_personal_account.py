from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestStellarBurgersAccount:
    def test_go_to_personal_account_login_user(self, driver, login):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT)).click()
        text = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.TEXT_BUTTON_LOGOUT)).text
        assert text == "Выход"
