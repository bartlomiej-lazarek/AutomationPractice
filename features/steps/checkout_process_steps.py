import time

from behave import when, step, given


@given("Login with username 'tester@tester.pl' and password 'tester'")
def step_impl(context):
    context.authentication_page.login("home_page", "tester@tester.pl", "tester")


@when("I go to Home Page")
def step_impl(context):
    context.base_page.go_to_home_page()


@step("I click Proceed to checkout and go to Address step")
def step_impl(context):
    context.checkout_page.proceed_to_checkout()
    assert context.checkout_page.check_current_step_equals_to_given("Address")


@step("I click I click Proceed to checkout and go to Shipping step")
def step_impl(context):
    context.checkout_page.proceed_to_checkout()
    assert context.checkout_page.check_current_step_equals_to_given("Shipping")


@step("I click checkbox Terms of service")
def step_impl(context):
    context.shipping_page.agree_terms()


@step("I click Proceed to checkout and go to Payment step")
def step_impl(context):
    context.checkout_page.proceed_to_checkout()
    assert context.checkout_page.check_current_step_equals_to_given("Payment")


@step("I click Pay by bank wire")
def step_impl(context):
    context.payment_page.pay_by_bank_wire()


@step("I click confirm my order")
def step_impl(context):
    context.payment_page.confirm_order()


@step("Should be displayed information that order is complete")
def step_impl(context):
    time.sleep(10)
    assert context.payment_page.check_order_was_created()
