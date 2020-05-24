from selenium.webdriver.common.by import By


class BasePageLocators:
    CONTACT_US = (By.CSS_SELECTOR, "[title='Contact Us']")
    SIGN_IN = (By.CSS_SELECTOR, ".login")
    MY_ACCOUNT = (By.CSS_SELECTOR, ".account")
    PRODUCT_SEARCH_INPUT = (By.CSS_SELECTOR, "#search_query_top")
    PRODUCT_SEARCH_BUTTON = (By.CSS_SELECTOR, "[name='submit_search']")
    SHOP_LOGO = (By.CSS_SELECTOR, ".logo ")
    SHOPPING_CART = (By.CSS_SELECTOR, ".shopping_cart [href='http://automationpractice.com/index.php?controller=order']")
    WOMAN_CATEGORY = (By.CSS_SELECTOR, "a[title='Women']")
    DRESSES_CATEGORY = (By.CSS_SELECTOR, "a[title='Dresses']")
    T_SHIRTS_CATEGORY = (By.CSS_SELECTOR, "a[title='T-shirts']")
    POPULAR_FILTER = (By.CSS_SELECTOR, "a.homefeatured")
    BEST_SELLERS_FILTER = (By.CSS_SELECTOR, "a.blockbestsellers")
    PRODUCTS_LIST = (By.CSS_SELECTOR, ".product_list")


class AuthenticationPageLocators:
    CREATE_ACCOUNT_EMAIL_INPUT = (By.CSS_SELECTOR, "label[for='email_create'] + input")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "#SubmitCreate")
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "label[for='email'] + input")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#passwd")


class RegistrationPageLocators:
    TITLE_MR = (By.CSS_SELECTOR, "#id_gender1")
    TITLE_MRS = (By.CSS_SELECTOR, "#id_gender2")
    FIRST_NAME = (By.CSS_SELECTOR, "#customer_firstname")
    LAST_NAME = (By.CSS_SELECTOR, "customer_lastname")
    EMAIL = (By.CSS_SELECTOR, "#email")
    PASSWORD = (By.CSS_SELECTOR, "passwd")
    BIRTH_DATE_DAY = (By.CSS_SELECTOR, "days")
    BIRTH_DATE_MONTH = (By.CSS_SELECTOR, "months")
    BIRTH_DATE_YEAR = (By.CSS_SELECTOR, "years")
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
