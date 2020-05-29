import time
from datetime import datetime
import random

from selenium.webdriver.support.select import Select

from features.locators.locators import RegistrationPageLocators
from features.pages.BasePage import BasePage


class RegistrationPage(BasePage):

    def set_title(self, title):
        if title.upper() == "MR":
            self.driver.find_element(*RegistrationPageLocators.TITLE_MR).click()
        else:
            self.driver.find_element(*RegistrationPageLocators.TITLE_MRS).click()

    def set_first_name(self, name):
        self.driver.find_element(*RegistrationPageLocators.FIRST_NAME).send_keys(name)

    def set_last_name(self, last_name):
        self.driver.find_element(*RegistrationPageLocators.LAST_NAME).send_keys(last_name)

    def set_email(self, email):
        self.driver.find_element(*RegistrationPageLocators.EMAIL).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*RegistrationPageLocators.PASSWORD).send_keys(password)

    def set_birth_date(self, date):
        date_time = datetime.fromisoformat(date)
        self.driver.find_element(*RegistrationPageLocators.BIRTH_DATE_DAY).send_keys(date_time.day)
        self.driver.find_element(*RegistrationPageLocators.BIRTH_DATE_MONTH).send_keys(date_time.month)
        self.driver.find_element(*RegistrationPageLocators.BIRTH_DATE_YEAR).send_keys(date_time.year)

    def set_company(self, company):
        self.driver.find_element(*RegistrationPageLocators.COMPANY).send_keys(company)

    def set_address(self, address):
        self.driver.find_element(*RegistrationPageLocators.ADDRESS_LINE1).send_keys(address)

    def set_address_line2(self, address):
        self.driver.find_element(*RegistrationPageLocators.ADDRESS_LINE2).send_keys(address)

    def set_city(self, city):
        self.driver.find_element(*RegistrationPageLocators.CITY).send_keys(city)

    def set_random_state(self):
        time.sleep(1)
        Select(self.driver.find_element(*RegistrationPageLocators.STATE)).select_by_index(random.randint(1, 50))

    def set_postal_code(self, postal_code):
        self.driver.find_element(*RegistrationPageLocators.POST_CODE).send_keys(postal_code)

    def set_country(self):
        Select(self.driver.find_element(*RegistrationPageLocators.COUNTRY)).select_by_visible_text("United States")

    def set_additional_information(self, text):
        self.driver.find_element(*RegistrationPageLocators.ADDITIONAL_INFORMATION).send_keys(text)

    def set_home_phone(self, phone):
        self.driver.find_element(*RegistrationPageLocators.HOME_PHONE).send_keys(phone)

    def set_mobile_phone(self, phone):
        self.driver.find_element(*RegistrationPageLocators.MOBILE_PHONE).send_keys(phone)

    def set_address_alias(self, address_alias):
        self.driver.find_element(*RegistrationPageLocators.ADDRESS_ALIAS).send_keys(address_alias)

    def register(self, title, name, last_name, password, address, city, postal_code, phone):
        self.set_title(title)
        self.set_first_name(name)
        self.set_last_name(last_name)
        self.set_password(password)
        self.set_address(address)
        self.set_city(city)
        self.set_random_state()
        self.set_postal_code(postal_code)
        self.set_country()
        self.set_mobile_phone(phone)
        self.driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
