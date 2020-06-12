from selenium.webdriver.common.by import By


class BasePageLocators:
    CONTACT_US = (By.CSS_SELECTOR, "[title='Contact Us']")
    SIGN_IN = (By.CSS_SELECTOR, ".login")
    SIGN_OUT = (By.CSS_SELECTOR, ".logout")
    MY_ACCOUNT = (By.CSS_SELECTOR, ".account")
    PRODUCT_SEARCH_INPUT = (By.CSS_SELECTOR, "#search_query_top")
    PRODUCT_SEARCH_BUTTON = (By.CSS_SELECTOR, "[name='submit_search']")
    SHOP_LOGO = (By.CSS_SELECTOR, ".logo ")
    SHOPPING_CART = (By.CSS_SELECTOR, ".shopping_cart [href='http://automationpractice.com/index.php?controller=order']")
    WOMAN_CATEGORY = (By.CSS_SELECTOR, "a[title='Women']")
    WOMAN_TOPS = (By.CSS_SELECTOR, "[title='Tops']")
    WOMAN_TSHIRTS = (By.CSS_SELECTOR, "[title='T-shirts']")
    WOMAN_BLOUSES = (By.CSS_SELECTOR, "[title='Blouses']")
    WOMAN_DRESSES = (By.CSS_SELECTOR, "[title='Dresses']")
    WOMAN_CASUAL_DRESSES = (By.CSS_SELECTOR, "[title='Casual Dresses']")
    WOMAN_EVENING_DRESSES = (By.CSS_SELECTOR, "[title='Evening Dresses']")
    WOMAN_SUMMER_DRESSES = (By.CSS_SELECTOR, "[title='Summer Dresses']")
    DRESSES_CATEGORY = (By.CSS_SELECTOR, "a[title='Dresses']")
    T_SHIRTS_CATEGORY = (By.CSS_SELECTOR, "a[title='T-shirts']")


class AuthenticationPageLocators(BasePageLocators):
    CREATE_ACCOUNT_EMAIL_INPUT = (By.CSS_SELECTOR, "label[for='email_create'] + input")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "#SubmitCreate")
    CREATE_ACCOUNT_ERROR = (By.CSS_SELECTOR, "#create_account_error")
    CREATE_ACCOUNT_ERROR_LIST = (By.CSS_SELECTOR, "div#create_account_error > ol > li")
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "label[for='email'] + input")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#passwd")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#SubmitLogin")
    LOGIN_ALERT_ERROR = (By.CSS_SELECTOR, "h1 + .alert-danger")
    LOGIN_ALERT_ERRORS_LIST = (By.CSS_SELECTOR, "h1 + .alert-danger ol li")
    RETRIEVE_PASSWORD = (By.CSS_SELECTOR, "[title='Recover your forgotten password']")
    RETRIEVE_PASSWORD_EMAIL = (By.CSS_SELECTOR, "#email")
    RETRIEVE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "p.submit [type='submit']")


class RegistrationPageLocators(BasePageLocators):
    TITLE_MR = (By.CSS_SELECTOR, "#id_gender1")
    TITLE_MRS = (By.CSS_SELECTOR, "#id_gender2")
    FIRST_NAME = (By.CSS_SELECTOR, "#customer_firstname")
    LAST_NAME = (By.CSS_SELECTOR, "#customer_lastname")
    EMAIL = (By.CSS_SELECTOR, "#email")
    PASSWORD = (By.CSS_SELECTOR, "#passwd")
    BIRTH_DATE_DAY = (By.CSS_SELECTOR, "#days")
    BIRTH_DATE_MONTH = (By.CSS_SELECTOR, "#months")
    BIRTH_DATE_YEAR = (By.CSS_SELECTOR, "#years")
    NEWSLETTER_CHECKBOX = (By.CSS_SELECTOR, "[name='newsletter']")
    SPECIAL_OFFERS_CHECKBOX = (By.CSS_SELECTOR, "#optin")
    COMPANY = (By.CSS_SELECTOR, "#company")
    ADDRESS_LINE1 = (By.CSS_SELECTOR, "#address1")
    ADDRESS_LINE2 = (By.CSS_SELECTOR, "#address2")
    CITY = (By.CSS_SELECTOR, "#city")
    STATE = (By.CSS_SELECTOR, "#id_state")
    POST_CODE = (By.CSS_SELECTOR, "#postcode")
    COUNTRY = (By.CSS_SELECTOR, "#id_country")
    ADDITIONAL_INFORMATION = (By.CSS_SELECTOR, "[name='other']")
    HOME_PHONE = (By.CSS_SELECTOR, "#phone")
    MOBILE_PHONE = (By.CSS_SELECTOR, "#phone_mobile")
    ADDRESS_ALIAS = (By.CSS_SELECTOR, "#alias")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#submitAccount")
    REGISTRATION_ERROR = (By.CSS_SELECTOR, ".alert-danger")


class HomePageLocators(BasePageLocators):
    POPULAR_TAB = (By.CSS_SELECTOR, "[href='#homefeatured']")
    BEST_SELLERS_TAB = (By.CSS_SELECTOR, "[href='#blockbestsellers']")
    PRODUCTS_LIST = (By.CSS_SELECTOR, ".product_list > li")
    ACTIVE_PRODUCTS_LIST = (By.CSS_SELECTOR, ".product_list.active li .product-container")
    PRODUCT = (By.CSS_SELECTOR, "div.product-container")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.right-block span.product-price.price")
    PRODUCT_DISCOUNT_PERCENT = (By.CSS_SELECTOR, "div.right-block span.price-percent-reduction")
    PRODUCT_PRICE_BEFORE_DISCOUNT = (By.CSS_SELECTOR, "div.right-block span.old-price")
    PRODUCT_LIST_ADD_TO_CART = (By.CSS_SELECTOR, "a.ajax_add_to_cart_button")
    QUICK_VIEW = (By.CSS_SELECTOR, "a.quick-view")
    PRODUCT_VIEW_PRODUCT_QTY = (By.CSS_SELECTOR, "#quantity_wanted")
    PRODUCT_VIEW_SIZE_SELECT = (By.CSS_SELECTOR, "#group_1")
    PRODUCT_VIEW_COLOR_LIST = (By.CSS_SELECTOR, "#color_to_pick_list")
    PRODUCT_VIEW_ADD_TO_CART = (By.CSS_SELECTOR, "button.exclusive")
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, "[title='Continue shopping']")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, "[title='Proceed to checkout']")
    SEARCH_RESULT = (By.CSS_SELECTOR, ".heading-counter")
    SEARCH_WARNING = (By.CSS_SELECTOR, ".alert-warning")
    LABEL_SUCCESSFULLY_ADDED_PRODUCT = (By.CSS_SELECTOR, ".layer_cart_product > h2")
    QUICK_VIEW_LOADING = (By.CSS_SELECTOR, "#fancybox-loading")
    QUICK_VIEW_IFRAME = (By.CSS_SELECTOR, ".fancybox-iframe")


class CheckoutProcessLocators(BasePageLocators):
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, ".button-medium")
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, "[title='Continue shopping']")
    CURRENT_STEP = (By.CSS_SELECTOR, ".step_current span")


class CartSummaryPageLocators(CheckoutProcessLocators):
    PRODUCT_LIST = (By.CSS_SELECTOR, "tbody tr")
    PRODUCT_QTY_INPUT = (By.CSS_SELECTOR, ".cart_quantity_input")
    QTY_PLUS_ICON = (By.CSS_SELECTOR, ".icon-plus")
    QTY_MINUS_ICON = (By.CSS_SELECTOR, ".icon-minus")
    PRODUCT_UNIT_PRICE = (By.CSS_SELECTOR, ".cart_unit span span.price")
    PRODUCT_TOTAL_PRICE = (By.CSS_SELECTOR, ".cart_total span.price")
    TOTAL_PRODUCTS_PRICE = (By.CSS_SELECTOR, "#total_product")
    TOTAL_SHIPPING_PRICE = (By.CSS_SELECTOR, "#total_shipping")
    TOTAL_PRICE_NET = (By.CSS_SELECTOR, "#total_price_without_tax")
    TOTAL_TAX = (By.CSS_SELECTOR, "#total_tax")
    TOTAL_PRICE_GROSS = (By.CSS_SELECTOR, "#total_price")


class AddressPageLocators(RegistrationPageLocators, CheckoutProcessLocators):
    COMMENT = (By.CSS_SELECTOR, "[name='message']")
    UPDATE_INVOICE_ADDRESS = (By.CSS_SELECTOR, "#address_invoice .address_update a.button")
    UPDATE_DELIVERY_ADDRESS = (By.CSS_SELECTOR, "#address_delivery .address_update a.button")


class ShippingPageLocators(CheckoutProcessLocators):
    AGREE_TERMS = (By.CSS_SELECTOR, "#cgv")
    DELIVERY_OPTION = (By.CSS_SELECTOR, "input.delivery_option_radio")
    BOX_ERROR = (By.CSS_SELECTOR, ".fancybox-error")


class PaymentPageLocators(CheckoutProcessLocators):
    PAY_BY_BANK_WIRE = (By.CSS_SELECTOR, ".bankwire")
    PAY_BY_CHECK = (By.CSS_SELECTOR, ".cheque")
    OTHER_PAYMENT_METHODS = (By.CSS_SELECTOR, "#cart_navigation a")
    CONFIRM_ORDER = (By.CSS_SELECTOR, "#cart_navigation button")
    COMPLETE_ORDER_INFORMATION = (By.CSS_SELECTOR, ".box p strong.dark")