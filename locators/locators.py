from selenium.webdriver.common.by import By


class BasePageLocators:
    CONTACT_US = (By.CSS_SELECTOR, "[title='Contact Us']")
    SIGN_IN = (By.CSS_SELECTOR, ".login")
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
