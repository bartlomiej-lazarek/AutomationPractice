from behave import when, then, step
from features.pages.authentication_page import AuthenticationPage
from features.pages.base_page import BasePage


# Scenario: Log in using valid data
@step("login with username 'tester@tester.pl' and password 'tester'")
def step_impl(context):
    context.authentication_page.login("authentication_page", "tester@tester.pl", "tester")


@then("I verify that I successfully logged in by checking account name")
def step_impl(context):
    account_name = BasePage(context.driver).get_account_name()
    assert account_name == "Tester Tester"


# Scenario: Log in using invalid data
@step("login with username 'tester@tester.pl' and password 'tester123'")
def step_impl(context):
    context.authentication_page.login("authentication_page", "tester@tester.pl", "tester123")


@then("I verify that I unsuccessfully logged in by checking error message")
def step_impl(context):
    assert AuthenticationPage(context.driver).check_error_login_is_displayed()


# Scenario: Log in with empty email field
@when("login with empty username and password 'tester123'")
def step_impl(context):
    context.authentication_page.login("authentication_page", "", "tester123")


@then("Verify error message contains 'An email address required'")
def step_impl(context):
    AuthenticationPage(context.driver).check_given_error_in_errors_list_exist("An email address required", "login")


# Scenario: Log in with empty password field
@when("login with empty username 'tester@tester.pl' and empty password")
def step_impl(context):
    context.authentication_page.login("authentication_page", "tester@tester.pl", "")


@then("Verify error message contains 'Password is required.'")
def step_impl(context):
    AuthenticationPage(context.driver).check_given_error_in_errors_list_exist("Password is required", "login")