from selenium.webdriver.common.by import By


class Locators:
    # главная страница
    BUTTON_PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет") #кнопка "Личный Кабинет"
    BUTTON_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']") #кнопка "Войти в аккаунт"

    #форма авторизации
    EMAIL = (By.XPATH, "//input[@name='name']") #поле ввода "email" для авторизации
    PASSWORD = (By.XPATH, "//input[@name='Пароль']") #поле ввода "пароль" для авторизации
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']") #кнопка "Войти"
    TEXT_BUTTON_REG_ACCOUNT = (By.LINK_TEXT, "Зарегистрироваться") #текст-кнопка "Войти"
    TEXT_BUTTON_RECOVERY_PASSWORD = (By.LINK_TEXT, "Зарегистрироваться") #текст-кнопка "Восстановить пароль"

    # форма "Личный Кабинет"
    TEXT_BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']") #текст-кнопка "Выход"


    # форма регистрации
    TEXT_BUTTON_LOGIN = (By.LINK_TEXT, "Войти")  #текст-кнопка "Войти"
    CREATED_NAME = (By.XPATH, "//fieldset[1]/div/div/input") #поле ввода "Имя" для регистрации
    CREATED_EMAIL = (By.XPATH, "//fieldset[2]/div/div/input") #поле ввода "Email" для регистрации
    CREATED_PASSWORD = (By.XPATH, "//fieldset[3]/div/div/input") #поле ввода "Пароль" для регистрации
    BUTTON_REG_ACCOUNT = (By.XPATH, "//form/button") #кнопка "Зарегистрироваться"