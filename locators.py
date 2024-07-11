from selenium.webdriver.common.by import By

# локаторы для регистрации
class registrationlocators:
    name_field = (By.XPATH, "//input[@name='name']")
    email_field = (By.XPATH, "//fieldset[2]/div/div/input[@name='name']")
    password_field = (By.XPATH, "//input[@name='Пароль']")
    registration_button = (By.XPATH, "//button[text()='Зарегистрироваться']")
    error_message = (By.XPATH, "//p[text()='Некорректный пароль']")
    login_button = (By.XPATH, "//button[text()='Войти']")

# локаторы для активации
class loginlocators:
    login_to_account_button = (By.XPATH, "//button[text()='Войти в аккаунт']")
    login_field = (By.XPATH, "//input[@name='name']")
    password_field = (By.XPATH, "//input[@name='Пароль']")
    login_button = (By.XPATH, "//button[text()='Войти']")
    personal_account = (By.XPATH, "//p[text()='Личный Кабинет']")
    order_button = (By.XPATH, "//button[text()='Оформить заказ']")
    login_link = (By.XPATH, "//a[text()='Войти']")

# локаторы для переходов
class gopagelocators:
    login_to_account_button = (By.XPATH, "//button[text()='Войти в аккаунт']")
    login_field = (By.XPATH, "//input[@name='name']")
    password_field = (By.XPATH, "//input[@name='Пароль']")
    login_button = (By.XPATH, "//button[text()='Войти']")
    order_button = (By.XPATH, "//button[text()='Оформить заказ']")
    personal_account = (By.XPATH, "//p[text()='Личный Кабинет']")
    profile = (By.XPATH, "//a[text()='Профиль']")
    constructor = (By.XPATH, "//p[text()='Конструктор']")
    logo = (By.XPATH, "//*[@id='root']/div/header/nav/div")
    exit_button = (By.XPATH, "//button[text()='Выход']")

# локаторы для контструктора
class constructorlocators:
    login_to_account_button = (By.XPATH, "//button[text()='Войти в аккаунт']")
    login_field = (By.XPATH, "//input[@name='name']")
    password_field = (By.XPATH, "//input[@name='Пароль']")
    login_button = (By.XPATH, "//button[text()='Войти']")
    personal_account = (By.XPATH, "//p[text()='Личный Кабинет']")
    order_button = (By.XPATH, "//button[text()='Оформить заказ']")
    sauces = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span')
    buns = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span')
    fillings = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span')
