from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestStellarBurgersConstructor:
    def test_constructor_go_to_buns(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Соусы']"))).click()
        driver.find_element(By.XPATH, "//span[text()='Булки']").click()
        text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Булки']"))).text
        assert text == "Булки"

    def test_constructor_go_to_sauces(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Соусы']"))).click()
        text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Соусы']"))).text
        assert text == "Соусы"

    def test_constructor_go_to_filling(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Начинки']"))).click()
        text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Начинки']"))).text
        assert text == "Начинки"