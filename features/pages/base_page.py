from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from features.locators.locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def sign_in(self):
        self.driver.find_element(*BasePageLocators.SIGN_IN).click()

    def sign_out(self):
        self.driver.find_element(*BasePageLocators.SIGN_OUT).click()

    def search_product(self, product):
        self.driver.find_element(*BasePageLocators.PRODUCT_SEARCH_INPUT).send_keys(product)
        self.driver.find_element(*BasePageLocators.PRODUCT_SEARCH_BUTTON).click()

    def go_to_cart(self):
        self.driver.find_element(*BasePageLocators.SHOPPING_CART).click()

    def go_to_my_account(self):
        self.driver.find_element(*BasePageLocators.MY_ACCOUNT).click()

    def hover_on_cart(self):
        ActionChains(self.driver).move_to_element(*BasePageLocators.SHOPPING_CART).perform()

    def get_account_name(self):
        try:
            return self.driver.find_element(*BasePageLocators.MY_ACCOUNT).text
        except NoSuchElementException:
            raise Exception("You are not log in")

