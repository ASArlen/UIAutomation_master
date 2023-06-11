import time
from allure_behave.hooks import allure_report
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        context.browser.cur.close()
    except BaseException:
        pass

    try:
        context.browser.quit()
    except BaseException:
        pass
    # ScreenRecorder.stoprecord(ScreenRecorder())


def before_step(context, step):
    try:
        attach(context.browser.driver.get_screenshot_as_png(), name="ScreenShot", attachment_type=AttachmentType.PNG)
    except BaseException:
        pass

def after_step(context, step):
    try:
        attach(context.browser.driver.get_screenshot_as_png(), name="ScreenShot", attachment_type=AttachmentType.PNG)
    except BaseException:
        pass

# def after_feature(context,feature):
#     context.browser.driver.switch_to.default_content()
#     try:
#         context.browser.quit()
#     except BaseException:
#         pass