from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestStellarBurgersLogout:
    def test_logout(self, driver, login):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет"))).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Выход']"))).click()
        text = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))).text
        assert text == "Войти"
