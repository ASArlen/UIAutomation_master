from selenium import webdriver

from features.browser import Browser
from features.function.Log import logger


class test1(Browser):

    def reset_driver(self,driver):
        global py_web_driver
        py_web_driver = driver


    def __init__(self):
        global py_web_driver
        py_web_driver = self.driver
        global test_url
        test_url = self.url


    def Login111(self,text):
        logger.info(f'the text is {text}')
        py_web_driver.get(test_url)