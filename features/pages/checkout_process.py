from features.locators.locators import AddressPageLocators, CheckoutProcessLocators, ShippingPageLocators, \
    PaymentPageLocators
from features.pages.base_page import BasePage
from features.pages.registration_page import RegistrationPage


class CheckoutPage(BasePage):

    def get_current_step(self):
        return self.driver.find_element(*CheckoutProcessLocators.CURRENT_STEP).text

    def continue_shopping(self):
        self.driver.find_element(*CheckoutProcessLocators.CONTINUE_SHOPPING).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*CheckoutProcessLocators.PROCEED_TO_CHECKOUT).click()


class SummaryPage(CheckoutPage):
    pass


class AddressPage(CheckoutPage):

    def add_comment(self, comment):
        self.driver.find_element(*AddressPageLocators.COMMENT).send_keys(comment)

    def change_address(self, address_type, **kwargs):
        if address_type == "delivery":
            self.driver.find_element(*AddressPageLocators.UPDATE_DELIVERY_ADDRESS).click()
        elif address_type == "invoice":
            self.driver.find_element(*AddressPageLocators.UPDATE_INVOICE_ADDRESS).click()

        page = RegistrationPage(self.driver)
        page.change_address(**kwargs)


class ShippingPage(CheckoutPage):

    def agree_terms(self):
        self.driver.find_element(*ShippingPageLocators.AGREE_TERMS).click()


class PaymentPage(CheckoutPage):

    def pay_by_bank_wire(self):
        self.driver.find_element(*PaymentPageLocators.PAY_BY_BANK_WIRE).click()

    def pay_by_check(self):
        self.driver.find_element(*PaymentPageLocators.PAY_BY_CHECK).click()

    def confirm_order(self):
        self.driver.find_element(*PaymentPageLocators.CONFIRM_ORDER).click()