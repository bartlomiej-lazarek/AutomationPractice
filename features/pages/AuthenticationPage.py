from features.locators.locators import AuthenticationPageLocators
from features.pages.BasePage import BasePage


class AuthenticationPage(BasePage):

    def login(self, email, password):
        self.driver.find_element(*AuthenticationPageLocators.LOGIN_EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*AuthenticationPageLocators.LOGIN_PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*AuthenticationPageLocators.LOGIN_BUTTON).click()
