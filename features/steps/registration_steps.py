from behave import then, step

import random


# Scenario Outline: Register new account
@step("I set {email} address, next I click Create an account button")
def step_impl(context, email):
    email = str(random.randint(1, 99999)) + email
    context.authentication_page.start_creating_account(email)


@step("I set {title}, {name}, {last_name}, {password}, {address}, "
      "{city}, {postal_code}, {phone}, next I click Register button")
def step_impl(context, title, name, last_name, password, address, city, postal_code, phone):
    if password and city == "empty":
        password = ""
        city = ""
    context.registration_page.register(title, name, last_name, password, address, city, postal_code, phone)


@then("I should {result} register new account")
def step_impl(context, result):
    try:
        context.base_page.get_account_name()
    except Exception:
        if result == "successfully":
            raise AssertionError("You should successfully register account. Something went wrong.")


#  Scenario: Register using invalid email
@step("I set email 'invalid@', next I click Create an account button")
def step_impl(context):
    context.authentication_page.start_creating_account("invalid@")


@then("I verify that error message contains: Invalid email address")
def step_impl(context):
    context.authentication_page.check_given_error_in_errors_list_exist("Invalid email address", "register")


