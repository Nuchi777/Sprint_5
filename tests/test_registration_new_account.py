from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from faker import Faker
from locators import MainPageLocators
from locators import AuthPageLocators
from locators import RegPageLocators
from locators import AccountPageLocators

fake = Faker()


class TestStellarBurgersRegistration:
    def test_registration_new_account_valid_password(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)).click()
        driver.find_element(*AuthPageLocators.TEXT_BUTTON_REG_ACCOUNT).click()
        name = fake.name()
        driver.find_element(*RegPageLocators.CREATED_NAME).send_keys(name)
        email = fake.email()
        driver.find_element(*RegPageLocators.CREATED_EMAIL).send_keys(email)
        password = randint(100000, 999999)
        driver.find_element(*RegPageLocators.CREATED_PASSWORD).send_keys(password)
        driver.find_element(*RegPageLocators.BUTTON_REG_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(AuthPageLocators.BUTTON_LOGIN))
        driver.find_element(*AuthPageLocators.EMAIL).send_keys(email)
        driver.find_element(*AuthPageLocators.PASSWORD).send_keys(password)
        driver.find_element(*AuthPageLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)).click()
        button_lo = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(AccountPageLocators.TEXT_BUTTON_LOGOUT))
        assert button_lo.is_displayed()


    def test_registration_new_account_not_valid_password(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)).click()
        driver.find_element(*AuthPageLocators.TEXT_BUTTON_REG_ACCOUNT).click()
        driver.find_element(*RegPageLocators.CREATED_NAME).send_keys(fake.name())
        driver.find_element(*RegPageLocators.CREATED_EMAIL).send_keys(fake.email())
        driver.find_element(*RegPageLocators.CREATED_PASSWORD).send_keys(randint(10000, 99999))
        driver.find_element(*RegPageLocators.BUTTON_REG_ACCOUNT).click()
        text = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(RegPageLocators.ERROR_INCORRECT_PASSWORD)).text
        assert text == "Некорректный пароль"
