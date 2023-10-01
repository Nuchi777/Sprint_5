from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from random import randint

class TestStellarBurgers:
    def test_registration_new_account(self, driver):
        fake = Faker()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет"))).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))).click()
        driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys(fake.name())
        driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys(fake.email())
        driver.find_element(By.XPATH, "//fieldset[3]/div/div/input").send_keys(randint(000000, 999999))
        driver.find_element(By.XPATH, "//form/button").click()
        assert WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "//form/button[text()='Войти']"))).text == "Войти"
