from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestStellarBurgersConstructor:
    def test_constructor_go_to_buns(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.BUTTON_CONSTRUCTOR_SAUCES)).click()
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR_BUNS).click()
        text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUTTON_CONSTRUCTOR_BUNS)).text
        assert text == "Булки"

    def test_constructor_go_to_sauces(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.BUTTON_CONSTRUCTOR_SAUCES)).click()
        text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUTTON_CONSTRUCTOR_SAUCES)).text
        assert text == "Соусы"

    def test_constructor_go_to_filling(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.BUTTON_CONSTRUCTOR_FILLING)).click()
        text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.BUTTON_CONSTRUCTOR_FILLING)).text
        assert text == "Начинки"
