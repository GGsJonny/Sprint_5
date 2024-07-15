from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data import password, login, base_url
from locators import GoPageLocators
import pytest

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    driver.get(base_url)
    yield driver
    driver.quit()

class TestGoToPage:
    @staticmethod
    def login(driver):
        driver.find_element(*GoPageLocators.LOGIN_FIELD).send_keys(login)
        driver.find_element(*GoPageLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*GoPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(GoPageLocators.ORDER_BUTTON))

    def test_go_to_personal_account_from_main(self, driver):
        driver.find_element(*GoPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        self.login(driver)

        driver.find_element(*GoPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(GoPageLocators.PROFILE))

        assert driver.current_url == f'{base_url}/account/profile'

    def test_go_to_designer_from_personal_account_click_button(self, driver):
        driver.find_element(*GoPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        self.login(driver)

        driver.find_element(*GoPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(GoPageLocators.PROFILE))

        driver.find_element(*GoPageLocators.CONSTRUCTOR).click()
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(GoPageLocators.ORDER_BUTTON))

        assert driver.current_url == f'{base_url}/'

    def test_go_to_designer_from_personal_account_click_logo(self, driver):
        driver.find_element(*GoPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        self.login(driver)

        driver.find_element(*GoPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(GoPageLocators.PROFILE))

        driver.find_element(*GoPageLocators.LOGO).click()
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(GoPageLocators.ORDER_BUTTON))

        assert driver.current_url == f'{base_url}/'

    def test_logout_in_personal_account_page(self, driver):
        driver.find_element(*GoPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        self.login(driver)

        driver.find_element(*GoPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(GoPageLocators.PROFILE))

        driver.find_element(*GoPageLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(GoPageLocators.LOGIN_BUTTON))

        assert driver.current_url == f'{base_url}/login'


