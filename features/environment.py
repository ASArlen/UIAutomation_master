from selenium import webdriver

from features.browser import Browser
from features.pages.test1_page import test1

def before_all(context):
    context.browser = Browser()



def before_feature(context,feature):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(r'F:\chromedriver.exe',options = options)
    options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    driver.maximize_window()
    context.browser.reset_driver(driver)
    context.driver = driver

    context.test1_page = test1()
    context.test1_page.reset_driver(driver)


def after_all(context):
    try:
        context.browser.close()
    except BaseException:
        pass