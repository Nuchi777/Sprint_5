import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_page():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.maximize_window()
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет"))).click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys(
        "evgenykoloskov1777@yandex.ru")
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(
        "230315")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa").click()
    time.sleep(3)
    assert driver.find_element(By.CSS_SELECTOR, "h1.text.text_type_main-large.mb-5.mt-10").text == "Соберите бургер"
