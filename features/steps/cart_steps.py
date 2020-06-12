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


# Scenario: Change product qty in a cart by icons
@step("I click '+' icon in qty field")
def step_impl(context):
    page = SummaryPage(context.driver)
    context.products_price = page.get_total_product_price()
    page.increase_product_qty_by_1()


@then("Products qty should be 2")
def step_impl(context):
    page = SummaryPage(context.driver)
    assert page.get_product_qty() == 2


@step("Total products price should be 2 times bigger")
def step_impl(context):
    page = SummaryPage(context.driver)
    assert context.products_price * 2 == page.get_total_product_price()


# Scenario: Change product qty in a cart by input
@step("I click in Qty input field and set 2")
def step_impl(context):
    page = SummaryPage(context.driver)
    context.products_price = page.get_total_product_price()
    page.set_product_qty(2)
