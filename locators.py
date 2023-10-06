from selenium.webdriver.common.by import By


class MainPageLocators:
    # главная страница
    BUTTON_PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет")  # кнопка "Личный Кабинет"
    BUTTON_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")  # кнопка "Конструктор"
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # логотип "Stellar Burgers"


class AuthPageLocators:
    # форма авторизации
    EMAIL = (By.XPATH, "//input[@name='name']")  # поле ввода "email" для авторизации
    PASSWORD = (By.XPATH, "//input[@name='Пароль']")  # поле ввода "пароль" для авторизации
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")  # кнопка "Войти"
    TEXT_BUTTON_REG_ACCOUNT = (By.LINK_TEXT, "Зарегистрироваться")  # текст-кнопка "Войти"
    TEXT_BUTTON_RECOVERY_PASSWORD = (By.LINK_TEXT, "Зарегистрироваться")  # текст-кнопка "Восстановить пароль"


class AccountPageLocators:
    # форма "Личный Кабинет"
    TEXT_BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")  # текст-кнопка "Выход"


class RegPageLocators:
    # форма регистрации
    TEXT_BUTTON_LOGIN = (By.LINK_TEXT, "Войти")  # текст-кнопка "Войти"
    CREATED_NAME = (By.XPATH, "(//input[@name='name'])[1]")  # поле ввода "Имя" для регистрации
    CREATED_EMAIL = (By.XPATH, "(//input[@name='name'])[2]")  # поле ввода "Email" для регистрации
    CREATED_PASSWORD = (By.XPATH, "//input[@name='Пароль']")  # поле ввода "Пароль" для регистрации
    BUTTON_REG_ACCOUNT = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться"
    ERROR_INCORRECT_PASSWORD = (By.CSS_SELECTOR, "p.input__error.text_type_main-default") # ошибка "Некорректный пароль"


class ConstrPageLocators:
    # конструктор
    BUTTON_CONSTRUCTOR_BUNS = (By.XPATH, "//span[text()='Булки']")  # раздел "Булки" в конструкторе
    BUTTON_CONSTRUCTOR_SAUCES = (By.XPATH, "//span[text()='Соусы']")  # раздел "Соусы" в конструкторе
    BUTTON_CONSTRUCTOR_FILLING = (By.XPATH, "//span[text()='Начинки']")  # раздел "Начинки" в конструкторе
    BUTTON_CONSTRUCTOR_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")  # активная кнопка в конструкторе
    TITLE_ASSEMBLE_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']") # заголовок "Собери бургер"
