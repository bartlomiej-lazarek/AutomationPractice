from features.locators.locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def sign_in(self):
        self.driver.find_element(*BasePageLocators.SIGN_IN).click()

    def sign_out(self):
        self.driver.find_element(*BasePageLocators.SIGN_OUT).click()
