from behave import when, step


@when("I click on first product on page")
def step_impl(context):
    page = HomePage(context.driver)
    page.click_on_product()


@step("I click Add to cart button")
def step_impl(context):
    page = HomePage(context.driver)
    page.add_product_to_cart("hover")


@step("I click Add to cart button on product page")
def step_impl(context):
    page = HomePage(context.driver)
    page.add_product_to_cart("page_view")


@step("I click Proceed to checkout and go to Cart")
def step_impl(context):
    page = HomePage(context.driver)
    page.proceed_to_checkout()


@when("I open authentication page")
def step_impl(context):
    page = BasePage(context.driver)
    page.sign_in()