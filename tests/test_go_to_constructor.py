from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestStellarBurgersAccount:
    def test_go_to_constructor_login_user(self, driver, login):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет"))).click()
        driver.find_element(By.XPATH, "//p[text()='Конструктор']").click()
        text = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//h1[text()='Соберите бургер']"))).text
        assert text == "Соберите бургер"
