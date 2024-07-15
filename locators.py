from selenium.webdriver.common.by import By

# Локаторы для регистрации
class RegistrationLocators:
    NAME_FIELD = (By.XPATH, "//input[@name='name']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    REGISTRATION_BUTTON = (By.XPATH, "//button[@id='register-button']")
    ERROR_MESSAGE = (By.XPATH, "//p[@id='error-message']")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='login-button']")

# Локаторы для активации
class LoginLocators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[@id='login-to-account-button']")
    LOGIN_FIELD = (By.XPATH, "//input[@id='login-field']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password-field']")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='login-button']")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[@id='personal-account']")
    ORDER_BUTTON = (By.XPATH, "//button[@id='order-button']")
    LOGIN_LINK = (By.XPATH, "//a[@id='login-link']")

# Локаторы для переходов
class GoPageLocators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[@id='login-to-account-button']")
    LOGIN_FIELD = (By.XPATH, "//input[@id='login-field']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password-field']")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='login-button']")
    ORDER_BUTTON = (By.XPATH, "//button[@id='order-button']")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[@id='personal-account']")
    PROFILE = (By.XPATH, "//a[@id='profile']")
    CONSTRUCTOR = (By.XPATH, "//p[@id='constructor']")
    LOGO = (By.XPATH, "//div[@id='logo']")
    EXIT_BUTTON = (By.XPATH, "//button[@id='exit-button']")

# Локаторы для конструктора
class ConstructorLocators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[@id='login-to-account-button']")
    LOGIN_FIELD = (By.XPATH, "//input[@id='login-field']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password-field']")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='login-button']")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[@id='personal-account']")
    ORDER_BUTTON = (By.XPATH, "//button[@id='order-button']")
    SAUCES = (By.XPATH, "//span[@id='sauces']")

