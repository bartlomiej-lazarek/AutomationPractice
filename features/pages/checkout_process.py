import time

from selenium.webdriver.common.keys import Keys
from features.locators.locators import AddressPageLocators, CheckoutProcessLocators, ShippingPageLocators, \
    PaymentPageLocators, CartSummaryPageLocators
from features.pages.base_page import BasePage
from features.pages.registration_page import RegistrationPage


class CheckoutPage(BasePage):

    def get_current_step(self):
        return self.driver.find_element(*CheckoutProcessLocators.CURRENT_STEP).text

    def continue_shopping(self):
        self.driver.find_element(*CheckoutProcessLocators.CONTINUE_SHOPPING).click()

    def proceed_to_checkout(self):
        self.driver.find_elements(*CheckoutProcessLocators.PROCEED_TO_CHECKOUT)[1].click()

    def check_current_step_equals_to_given(self, step):
        if step in self.get_current_step():
            return True
        else:
            return False


class SummaryPage(CheckoutPage):

    def check_total_products_price(self):
        total_products_price = float(self.driver.find_element(*CartSummaryPageLocators.TOTAL_PRODUCTS_PRICE).text[1:])
        all_products_total_price = 0
        products_prices = self.driver.find_elements(*CartSummaryPageLocators.PRODUCT_TOTAL_PRICE)

        for product in products_prices:
            all_products_total_price += float(product.text[1:])
        assert round(total_products_price, 2) == round(all_products_total_price, 2)

    def increase_product_qty_by_1(self):
        self.driver.find_element(*CartSummaryPageLocators.QTY_PLUS_ICON).click()
        time.sleep(2)

    def decrease_product_qty_by_1(self):
        self.driver.find_element(*CartSummaryPageLocators.QTY_MINUS_ICON).click()

    def get_product_qty(self):
        return int(self.driver.find_element(*CartSummaryPageLocators.PRODUCT_QTY_INPUT).get_attribute('value'))

    def get_total_product_price(self):
        return float(self.driver.find_element(*CartSummaryPageLocators.TOTAL_PRODUCTS_PRICE).text[1:])

    def set_product_qty(self, product_qty):
        self.driver.find_element(*CartSummaryPageLocators.PRODUCT_QTY_INPUT).clear()
        self.driver.find_element(*CartSummaryPageLocators.PRODUCT_QTY_INPUT).send_keys(product_qty)
        self.driver.find_element(*CartSummaryPageLocators.PRODUCT_QTY_INPUT).send_keys(Keys.ENTER)
        time.sleep(2)


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

    def check_order_was_created(self):
        if self.driver.find_element(*PaymentPageLocators.COMPLETE_ORDER_INFORMATION).text == "Your order on My Store is complete.":
            return True
        else:
            return False