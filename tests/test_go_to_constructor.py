from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators
from locators import ConstrPageLocators


class TestStellarBurgersAccount:
    def test_go_to_constructor_by_click_constructor(self, driver, login):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)).click()
        driver.find_element(*MainPageLocators.BUTTON_CONSTRUCTOR).click()
        text = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(ConstrPageLocators.TITLE_ASSEMBLE_BURGER)).text
        assert text == "Соберите бургер"

    def test_go_to_constructor_by_click_logo(self, driver, login):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)).click()
        driver.find_element(*MainPageLocators.LOGO).click()
        text = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(ConstrPageLocators.TITLE_ASSEMBLE_BURGER)).text
        assert text == "Соберите бургер"