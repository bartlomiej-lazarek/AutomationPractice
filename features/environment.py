from selenium import webdriver


def before_feature(context, feature):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(2)
    context.driver.get("http://automationpractice.com")


def after_feature(context, feature):
    context.driver.quit()