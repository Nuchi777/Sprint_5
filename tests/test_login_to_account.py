from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators
from locators import AuthPageLocators
from locators import ConstrPageLocators
from locators import RegPageLocators
from data import PersonStellarBurgers


class TestStellarBurgersLogin:
    def test_login_button_login_to_account_main_page(self, driver, login):
        text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(ConstrPageLocators.TITLE_ASSEMBLE_BURGER)).text
        assert text == "Соберите бургер"

    def test_login_button_personal_account_main_page(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)).click()
        driver.find_element(*AuthPageLocators.EMAIL).send_keys(PersonStellarBurgers.EMAIL)
        driver.find_element(*AuthPageLocators.PASSWORD).send_keys(PersonStellarBurgers.PASSWORD)
        driver.find_element(*AuthPageLocators.BUTTON_LOGIN).click()
        text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(ConstrPageLocators.TITLE_ASSEMBLE_BURGER)).text
        assert text == "Соберите бургер"

    def test_login_button_registration_form(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)).click()
        driver.find_element(*AuthPageLocators.TEXT_BUTTON_REG_ACCOUNT).click()
        driver.find_element(*RegPageLocators.TEXT_BUTTON_LOGIN).click()
        driver.find_element(*AuthPageLocators.EMAIL).send_keys(PersonStellarBurgers.EMAIL)
        driver.find_element(*AuthPageLocators.PASSWORD).send_keys(PersonStellarBurgers.PASSWORD)
        driver.find_element(*AuthPageLocators.BUTTON_LOGIN).click()
        text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(ConstrPageLocators.TITLE_ASSEMBLE_BURGER)).text
        assert text == "Соберите бургер"

    def test_login_button_password_recovery_form(self, driver):
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_ACCOUNT)).click()
        driver.find_element(*AuthPageLocators.TEXT_BUTTON_RECOVERY_PASSWORD).click()
        driver.find_element(*RegPageLocators.TEXT_BUTTON_LOGIN).click()
        driver.find_element(*AuthPageLocators.EMAIL).send_keys(PersonStellarBurgers.EMAIL)
        driver.find_element(*AuthPageLocators.PASSWORD).send_keys(PersonStellarBurgers.PASSWORD)
        driver.find_element(*AuthPageLocators.BUTTON_LOGIN).click()
        text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(ConstrPageLocators.TITLE_ASSEMBLE_BURGER)).text
        assert text == "Соберите бургер"
