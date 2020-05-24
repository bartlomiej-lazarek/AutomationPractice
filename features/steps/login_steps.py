from behave import when, then, step
from features.pages.AuthenticationPage import AuthenticationPage
from features.pages.BasePage import BasePage


# Scenario: Log in using valid data
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


# Scenario: Log in using invalid data
@step("login with username 'tester@tester.pl' and password 'tester123'")
def step_impl(context):
    page = AuthenticationPage(context.driver)
    page.login("tester@tester.pl", "tester123")


@then("I verify that I unsuccessfully logged in by checking error message")
def step_impl(context):
    assert AuthenticationPage(context.driver).check_error_login_is_displayed()


# Scenario: Log in with empty email field
@when("login with empty username and password 'tester123'")
def step_impl(context):
    page = AuthenticationPage(context.driver)
    page.login("", "tester123")


@then("Verify error message contains 'An email address required'")
def step_impl(context):
    errors_list = AuthenticationPage(context.driver).get_login_errors_list()

    for error in errors_list:
        if error == 'An email address required':
            return True