from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestStellarBurgersAccount:
    def test_go_to_constructor_by_click_constructor(self, driver, login):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT)).click()
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        text = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//h1[text()='Соберите бургер']"))).text
        assert text == "Соберите бургер"

    def test_go_to_constructor_by_click_logo(self, driver, login):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT)).click()
        driver.find_element(*Locators.LOGO).click()
        text = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//h1[text()='Соберите бургер']"))).text
        assert text == "Соберите бургер"