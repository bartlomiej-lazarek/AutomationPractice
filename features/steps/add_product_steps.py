from behave import when, then, step
from features.pages.home_page import HomePage


# Scenario: Add product to cart using button on hover on product
@when("I hover on first product on page")
def step_impl(context):
    page = HomePage(context.driver)
    page.hover_on_product()




@then("Should be displayed message Product successfully added to your shopping cart")
def step_impl(context):
    page = HomePage(context.driver)
    assert page.check_product_added_successfully()


# Scenario: Add product to cart using quick view
@step("I click Quick view button")
def step_impl(context):
    page = HomePage(context.driver)
    page.open_product_quick_view()


@step("I click Add to cart button on quick view")
def step_impl(context):
    page = HomePage(context.driver)
    page.add_product_to_cart("quick_view")

