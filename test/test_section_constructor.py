from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data import password, login
from locators import ConstructorLocators

class TestSectionConstructor:
    @staticmethod
    def login(driver):
        driver.find_element(*ConstructorLocators.LOGIN_FIELD).send_keys(login)
        driver.find_element(*ConstructorLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*ConstructorLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(ConstructorLocators.ORDER_BUTTON))

    def test_go_to_sections_buns(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*ConstructorLocators.PERSONAL_ACCOUNT).click()
        self.login(driver)

        driver.find_element(*ConstructorLocators.SAUCES).click()
        buns_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.BUNS))
        buns_element.click()

        driver.quit()

    def test_go_to_sections_sauces(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*ConstructorLocators.PERSONAL_ACCOUNT).click()
        self.login(driver)

        sauces_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.SAUCES))
        sauces_element.click()

        driver.quit()

    def test_go_to_sections_fillings(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*ConstructorLocators.PERSONAL_ACCOUNT).click()
        self.login(driver)

        fillings_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.FILLINGS))
        fillings_element.click()

        driver.quit()

