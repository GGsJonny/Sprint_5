import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helper_test import random_mail
from locators import RegistrationLocators

class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*RegistrationLocators.NAME_FIELD).send_keys("stellar")
        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys(random_mail.generate_mail())
        driver.find_element(*RegistrationLocators.PASSWORD_FIELD).send_keys("stellarburgers")
        driver.find_element(*RegistrationLocators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationLocators.LOGIN_BUTTON))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_registration_password_error(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*RegistrationLocators.NAME_FIELD).send_keys("stellar")
        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys(random_mail.generate_mail())
        driver.find_element(*RegistrationLocators.PASSWORD_FIELD).send_keys("123")
        driver.find_element(*RegistrationLocators.REGISTRATION_BUTTON).click()

        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationLocators.ERROR_MESSAGE))

        assert error_message.text == 'некорректный пароль'
