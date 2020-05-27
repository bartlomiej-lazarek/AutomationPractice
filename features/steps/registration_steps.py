from unittest import TestCase

from behave import when, then, step

from features.pages.AuthenticationPage import AuthenticationPage
from features.pages.BasePage import BasePage
from features.pages.RegistrationPage import RegistrationPage


@step("I set {email} address, next I click Create an account button")
def step_impl(context, email):
    page = AuthenticationPage(context.driver)
    page.start_creating_account(email)


@step("I set {title}, {name}, {last_name}, {password}, {address}, {city}, {postal_code}, {phone}, next I click Register button")
def step_impl(context, title, name, last_name, password, address, city, postal_code, phone):
    page = RegistrationPage(context.driver)
    page.register(title, name, last_name, password, address, city, postal_code, phone)



@then("I should {result} register new account")
def step_impl(context, result):
    page = BasePage(context.driver)

