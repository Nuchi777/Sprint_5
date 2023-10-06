from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import ConstrPageLocators


class TestStellarBurgersConstructor:
    def test_constructor_go_to_buns(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(ConstrPageLocators.BUTTON_CONSTRUCTOR_SAUCES)).click()
        driver.find_element(*ConstrPageLocators.BUTTON_CONSTRUCTOR_BUNS).click()
        assert driver.find_element(*ConstrPageLocators.BUTTON_CONSTRUCTOR_ACTIVE).text == 'Булки'

    def test_constructor_go_to_sauces(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(ConstrPageLocators.BUTTON_CONSTRUCTOR_SAUCES)).click()
        assert driver.find_element(*ConstrPageLocators.BUTTON_CONSTRUCTOR_ACTIVE).text == 'Соусы'

    def test_constructor_go_to_filling(self, driver):
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(ConstrPageLocators.BUTTON_CONSTRUCTOR_FILLING)).click()
        assert driver.find_element(*ConstrPageLocators.BUTTON_CONSTRUCTOR_ACTIVE).text == 'Начинки'
