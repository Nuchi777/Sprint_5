# StellarBurgers
## Это космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов.

### Bспользованные библиотеки и зависимости:
pytest~=7.4.2
selenium~=4.13.0
webdriver-manager~=4.0.1
Faker~=19.6.2

### Регистрация:
* test_registration_new_account_valid_password
#Тест регистрации нового пользователя с валидными данными

* test_registration_new_account_not_valid_password
#Тест регистрации нового пользователя с не валидным паролем

### Вход:

* test_login_button_login_to_account_main_page
#Тест входа в аккаунт по кнопке «Войти в аккаунт» на главной странице

* test_login_button_personal_account_main_page
#Тест входа в аккаунт по кнопке «Личный кабинет» на главной странице

* test_login_button_registration_form
#Тест входа в аккаунт через кнопку "Войти" в форме регистрации

* test_login_button_password_recovery_form
#Тест входа в аккаунт через кнопку "Войти" в форме восстановления пароля

### Переход в личный кабинет 

* test_go_to_personal_account_login_user
#Тест перехода по клику на «Личный кабинет» в личный кабинет авторизованного пользователя

### Переход из личного кабинета в конструктор 

* test_go_to_constructor_by_click_constructor
#Тест перехода из личного кабинета в конструктор по клику на «Конструктор»

* test_go_to_constructor_by_click_logo
#Тест перехода из личного кабинета в конструктор по клику на «логотип Stellar Burgers»

### Выход из аккаунта

* test_logout
#Тест выхода из аккаунта по кнопке «Выйти» в личном кабинете

### Раздел «Конструктор»

* test_constructor_go_to_buns
#Тест перехода к разделу «Булки» в конструкторе

* test_constructor_go_to_sauces
#Тест перехода к разделу «Соусы» в конструкторе

* test_constructor_go_to_filling
#Тест перехода к разделу «Начинки» в конструкторе
