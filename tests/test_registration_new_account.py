from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from faker import Faker
fake = Faker()

class TestStellarBurgersRegistration:
    def test_registration_new_account_valid_password(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет"))).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))).click()
        driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys(fake.name())
        driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys(fake.email())
        driver.find_element(By.XPATH, "//fieldset[3]/div/div/input").send_keys(randint(000000, 999999))
        driver.find_element(By.XPATH, "//form/button").click()
        text = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//form/button[text()='Войти']"))).text
        assert text == "Войти"

    def test_registration_new_account_not_valid_password(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет"))).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))).click()
        driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys(fake.name())
        driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys(fake.email())
        driver.find_element(By.XPATH, "//fieldset[3]/div/div/input").send_keys(randint(00000, 99999))
        driver.find_element(By.XPATH, "//form/button").click()
        text = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p.input__error.text_type_main-default"))).text
        assert text == "Некорректный пароль"
