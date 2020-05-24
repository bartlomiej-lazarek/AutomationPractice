from behave import when, then, step

from features.pages.AuthenticationPage import AuthenticationPage
from features.pages.BasePage import BasePage


@when("I open authentication page")
def step_impl(context):
    page = BasePage(context.driver)
    page.sign_in()


@step("login with username 'tester@tester.pl' and password 'tester'")
def step_impl(context):
    page = AuthenticationPage(context.driver)
    page.login("tester@tester.pl", "tester")


@then("I verify that I successfully logged in by checking account name")
def step_impl(context):
    account_name = BasePage(context.driver).get_account_name()
    assert account_name == "Tester Tester"
