from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from features.locators.locators import HomePageLocators
from features.pages.BasePage import BasePage


class HomePage(BasePage):

    def hover_on_product(self):
        ActionChains(self.driver).move_to_element(*HomePageLocators.PRODUCT).perform()

    def add_product_to_cart(self):
        self.hover_on_product()
        self.driver.find_element(*HomePageLocators.PRODUCT_LIST_ADD_TO_CART).click()

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

    def add_product_to_cart_quick_view(self):
        self.driver.find_element(*HomePageLocators.PRODUCT_VIEW_ADD_TO_CART).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*HomePageLocators.PROCEED_TO_CHECKOUT).click()