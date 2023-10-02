from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestStellarBurgersLogin:
    def test_login_button_login_to_account_main_page(self, driver):
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))).click()
        driver.find_element(By.XPATH, "//input[@name='name']").send_keys('evgenykoloskov1777@yandex.ru')
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys('230315')
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        text = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//h1[text()='Соберите бургер']"))).text
        assert text == "Соберите бургер"

    def test_login_button_personal_account_main_page(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет"))).click()
        driver.find_element(By.XPATH, "//input[@name='name']").send_keys('evgenykoloskov1777@yandex.ru')
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys('230315')
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        text = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//h1[text()='Соберите бургер']"))).text
        assert text == "Соберите бургер"

    def test_login_button_registration_form(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет"))).click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        driver.find_element(By.LINK_TEXT, "Войти").click()
        driver.find_element(By.XPATH, "//input[@name='name']").send_keys('evgenykoloskov1777@yandex.ru')
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys('230315')
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        text = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//h1[text()='Соберите бургер']"))).text
        assert text == "Соберите бургер"

    def test_login_button_password_recovery_form(self, driver):
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))).click()
        driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()
        driver.find_element(By.LINK_TEXT, "Войти").click()
        driver.find_element(By.XPATH, "//input[@name='name']").send_keys('evgenykoloskov1777@yandex.ru')
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys('230315')
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        text = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//h1[text()='Соберите бургер']"))).text
        assert text == "Соберите бургер"
