from behave import then, when
from features.pages.home_page import HomePage


# Scenario: Search with empty value
@when("I search for empty value")
def step_impl(context):
    context.home_page.search_product("")


@then("I see message Please enter a search keyword")
def step_impl(context):
    assert context.home_page.check_search_warning_displayed()


# Scenario: Search with 'Printed' phrase
@when("I search for 'Printed'")
def step_impl(context):
    context.home_page.search_product("Printed")


@then("I see only products witch name contains 'Printed'")
def step_impl(context):
    assert context.home_page.check_search_results("Printed")