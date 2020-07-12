from behave import when, step


@when("I click on first product on page")
def step_impl(context):
    context.home_page.click_on_product()


@step("I click Add to cart button")
def step_impl(context):
    context.home_page.add_product_to_cart("hover")


@step("I click Add to cart button on product page")
def step_impl(context):
    context.home_page.add_product_to_cart("page_view")


@step("I click Proceed to checkout and go to Cart")
def step_impl(context):
    context.home_page.proceed_to_checkout()


@when("I open authentication page")
def step_impl(context):
    context.base_page.sign_in()
