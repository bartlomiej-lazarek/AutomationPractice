from behave import when, then, step

from features.pages.base_page import BasePage
from features.pages.checkout_process import SummaryPage
from features.pages.home_page import HomePage


# Scenario Outline: Check total products price
@when("I add {products_qty} random products to cart")
def step_impl(context, products_qty):
    page = HomePage(context.driver)
    page.add_products_to_cart(products_qty)


@step("I go to cart")
def step_impl(context):
    page = BasePage(context.driver)
    page.go_to_cart()


@then("Total products price should be equal to sum all unit products price in cart")
def step_impl(context):
    page = SummaryPage(context.driver)
    page.check_total_products_price()