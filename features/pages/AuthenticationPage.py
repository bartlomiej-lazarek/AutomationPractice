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

    def get_login_errors_list(self):
        errors_list = []
        li_elements_list = self.driver.find_elements(*AuthenticationPageLocators.LOGIN_ALERT_ERRORS_LIST)

        for element in li_elements_list:
            errors_list.append(element.text)

        return errors_list
