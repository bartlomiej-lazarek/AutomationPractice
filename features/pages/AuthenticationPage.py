from features.locators.locators import AuthenticationPageLocators
from features.pages.BasePage import BasePage


class AuthenticationPage(BasePage):

    def login(self, email, password):
        self.driver.find_element(*AuthenticationPageLocators.LOGIN_EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*AuthenticationPageLocators.LOGIN_PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*AuthenticationPageLocators.LOGIN_BUTTON).click()

    def start_creating_account(self, email):
        self.driver.find_element(*AuthenticationPageLocators.CREATE_ACCOUNT_EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*AuthenticationPageLocators.CREATE_ACCOUNT_BUTTON).click()

    def retrieve_password(self, email):
        self.driver.find_element(*AuthenticationPageLocators.RETRIEVE_PASSWORD).click()
        self.driver.find_element(*AuthenticationPageLocators.RETRIEVE_PASSWORD_EMAIL).send_keys(email)
        self.driver.find_element(*AuthenticationPageLocators.RETRIEVE_PASSWORD_BUTTON).click()


    def check_error_login_is_displayed(self):
        return self.driver.find_element(*AuthenticationPageLocators.LOGIN_ALERT_ERROR).is_displayed()
