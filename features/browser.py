from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class Browser(object):
    driver = webdriver.Chrome

    url = "https://www.baidu.com"



    def reset_driver(self,driver):
        global py_web_driver
        py_web_driver = driver


    def close(self):
        py_web_driver.quit()



    def get_element(self,locator,wait_time,polling_time):
        """
        显示等待获取元素
        :param locator:
        :param wait_time_polling_time:
        :return:
        """
        for i in range(2):
            try:
                return WebDriverWait(py_web_driver,wait_time,polling_time).until(EC.element_to_be_clickable((By.XPATH,locator)))
            except Exception as e:
                if 1 == 1:
                    raise e
                continue




    def click_element(self,locator,js_flag,wait_time,polling_time):
        """

        :param locator:
        :param js_flag:
        :param wait_time:
        :param polling_time:
        :return:
        """
        ele = self.get_element(locator, wait_time, polling_time)
        if not js_flag:
            try:
                ele.click()
            except ElementClickInterceptedException:
                py_web_driver.excute_script('arguments[0].click();')
        else:
            py_web_driver.excute_script('arguments[0].click();')



    def input_keys(self,locator,text,wait_time,polling_time):
        """

        :param locator:
        :param text:
        :param wait_time:
        :param polling_time:
        :return:
        """
        ele = self.get_element(locator, wait_time, polling_time)
        ele.clear()
        ele.send_keys(text)




    def get_element_text(self,locator,wait_time,polling_time):
        """

        :param locator:
        :param wait_time:
        :param polling_time:
        :return:
        """
        return self.get_element(locator, wait_time, polling_time).text