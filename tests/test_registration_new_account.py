from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from random import randint
from faker import Faker

fake = Faker()


class TestStellarBurgersRegistration():
    def test_registration_new_account_valid_password(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT)).click()
        driver.find_element(*Locators.TEXT_BUTTON_REG_ACCOUNT).click()
        driver.find_element(*Locators.CREATED_NAME).send_keys(fake.name())
        driver.find_element(*Locators.CREATED_EMAIL).send_keys(fake.email())
        driver.find_element(*Locators.CREATED_PASSWORD).send_keys(randint(000000, 999999))
        driver.find_element(*Locators.BUTTON_REG_ACCOUNT).click()
        text = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.BUTTON_LOGIN)).text
        assert text == "Войти"

    def test_registration_new_account_not_valid_password(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет"))).click()
        driver.find_element(*Locators.TEXT_BUTTON_REG_ACCOUNT).click()
        driver.find_element(*Locators.CREATED_NAME).send_keys(fake.name())
        driver.find_element(*Locators.CREATED_EMAIL).send_keys(fake.email())
        driver.find_element(*Locators.CREATED_PASSWORD).send_keys(randint(00000, 99999))
        driver.find_element(*Locators.BUTTON_REG_ACCOUNT).click()
        text = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p.input__error.text_type_main-default"))).text
        assert text == "Некорректный пароль"
