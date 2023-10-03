from selenium.webdriver.common.by import By


class Locators:
    #главная страница
    BUTTON_PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет") #кнопка "Личный Кабинет"
    BUTTON_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']") #кнопка "Войти в аккаунт"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']") #кнопка "Конструктор"
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']") #логотип "Stellar Burgers"

    #форма авторизации
    EMAIL = (By.XPATH, "//input[@name='name']") #поле ввода "email" для авторизации
    PASSWORD = (By.XPATH, "//input[@name='Пароль']") #поле ввода "пароль" для авторизации
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']") #кнопка "Войти"
    TEXT_BUTTON_REG_ACCOUNT = (By.LINK_TEXT, "Зарегистрироваться") #текст-кнопка "Войти"
    TEXT_BUTTON_RECOVERY_PASSWORD = (By.LINK_TEXT, "Зарегистрироваться") #текст-кнопка "Восстановить пароль"

    #форма "Личный Кабинет"
    TEXT_BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']") #текст-кнопка "Выход"

    #форма регистрации
    TEXT_BUTTON_LOGIN = (By.LINK_TEXT, "Войти")  #текст-кнопка "Войти"
    CREATED_NAME = (By.XPATH, "//fieldset[1]/div/div/input") #поле ввода "Имя" для регистрации
    CREATED_EMAIL = (By.XPATH, "//fieldset[2]/div/div/input") #поле ввода "Email" для регистрации
    CREATED_PASSWORD = (By.XPATH, "//fieldset[3]/div/div/input") #поле ввода "Пароль" для регистрации
    BUTTON_REG_ACCOUNT = (By.XPATH, "//form/button") #кнопка "Зарегистрироваться"

    #конструктор
    BUTTON_CONSTRUCTOR_BUNS = (By.XPATH, "//span[text()='Булки']") #раздел "Булки" в конструкторе
    BUTTON_CONSTRUCTOR_SAUCES = (By.XPATH, "//span[text()='Соусы']")  #раздел "Соусы" в конструкторе
    BUTTON_CONSTRUCTOR_FILLING = (By.XPATH, "//span[text()='Начинки']")  #раздел "Начинки" в конструкторе