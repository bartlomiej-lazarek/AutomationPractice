import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from features.locators.locators import HomePageLocators
from features.pages.base_page import BasePage


class HomePage(BasePage):

    def hover_on_product(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*HomePageLocators.PRODUCT)).perform()

    def click_on_product(self):
        self.driver.find_element(*HomePageLocators.PRODUCT).click()

    def add_product_to_cart(self, view):
        if view == "hover":
            self.driver.find_element(*HomePageLocators.PRODUCT_LIST_ADD_TO_CART).click()
        elif view == "quick_view":
            self.driver.switch_to.frame(self.driver.find_element(*HomePageLocators.QUICK_VIEW_IFRAME))
            self.driver.find_element(*HomePageLocators.PRODUCT_VIEW_ADD_TO_CART).click()
            self.driver.switch_to.default_content()

        elif view == "page_view":
            self.driver.find_element(*HomePageLocators.PRODUCT_VIEW_ADD_TO_CART).click()

    def add_products_to_cart(self, products_qty):

        for i in range(int(products_qty)):
            products = self.driver.find_elements(*HomePageLocators.ACTIVE_PRODUCTS_LIST)
            products[random.randint(0, len(products)-1)].click()
            # todo better wait
            time.sleep(3)
            self.driver.find_element(*HomePageLocators.PRODUCT_VIEW_ADD_TO_CART).click()
            self.driver.find_element(*HomePageLocators.CONTINUE_SHOPPING).click()
            self.driver.find_element(*HomePageLocators.SHOP_LOGO).click()

    def switch_to_popular_products(self):
        self.driver.find_element(*HomePageLocators.POPULAR_TAB).click()

    def switch_to_bestsellers(self):
        self.driver.find_element(*HomePageLocators.BEST_SELLERS_TAB).click()

    def open_product_quick_view(self):
        self.hover_on_product()
        self.driver.find_element(*HomePageLocators.QUICK_VIEW).click()

    def set_product_qty(self, product_qty):
        self.driver.find_element(*HomePageLocators.PRODUCT_VIEW_PRODUCT_QTY).clear()
        self.driver.find_element(*HomePageLocators.PRODUCT_VIEW_PRODUCT_QTY).send_keys(product_qty)

    def set_product_size(self, product_size):
        Select(self.driver.find_element(*HomePageLocators.PRODUCT_VIEW_SIZE_SELECT)).select_by_visible_text(product_size)

    def proceed_to_checkout(self):
        self.driver.find_element(*HomePageLocators.PROCEED_TO_CHECKOUT).click()

    def check_search_warning_displayed(self):
        return len(self.driver.find_elements(*HomePageLocators.SEARCH_WARNING)) > 0

    def check_search_results(self, search_keyword):
        products = self.driver.find_elements(*HomePageLocators.PRODUCTS_LIST)

        for product in products:
            if search_keyword not in product.find_element(*HomePageLocators.PRODUCT_NAME).text:
                return False
            else:
                continue
        return True

    def check_product_added_successfully(self):
        return len(self.driver.find_elements(*HomePageLocators.LABEL_SUCCESSFULLY_ADDED_PRODUCT)) > 0

