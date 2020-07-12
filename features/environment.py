from selenium import webdriver

from features.pages.authentication_page import AuthenticationPage
from features.pages.base_page import BasePage
from features.pages.checkout_process import CheckoutPage, SummaryPage, AddressPage, ShippingPage, PaymentPage
from features.pages.home_page import HomePage
from features.pages.registration_page import RegistrationPage


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(2)
    context.driver.get("http://automationpractice.com")

    if "skip" in scenario.tags:
        scenario.skip("Marked with @skip")
        return
    if "base_page" in scenario.tags:
        context.base_page = BasePage(context.driver)
    if "home_page" in scenario.tags:
        context.home_page = HomePage(context.driver)
    if "authentication_page" in scenario.tags:
        context.authentication_page = AuthenticationPage(context.driver)
    if "registration_page" in scenario.tags:
        context.registration_page = RegistrationPage(context.driver)
    if "checkout_page" in scenario.tags:
        context.checkout_page = CheckoutPage(context.driver)
    if "summary_page" in scenario.tags:
        context.summary_page = SummaryPage(context.driver)
    if "address_page" in scenario.tags:
        context.address_page = AddressPage(context.driver)
    if "shipping_page" in scenario.tags:
        context.shipping_page = ShippingPage(context.driver)
    if "payment_page" in scenario.tags:
        context.payment_page = PaymentPage(context.driver)


def after_scenario(context, feature):
    context.driver.quit()