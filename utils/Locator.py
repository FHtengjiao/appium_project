# -*- coding: utf-8 -*-
from utils.INIParser import ReadIni


class ElementLocator(object):

    def __init__(self, driver):
        self.driver = driver
        self.reader = ReadIni()

    def locator(self, key):
        element = None
        method = self.reader.read_config(key).split('>')[0]
        info = self.reader.read_config(key).split('>')[1]
        methods = ("id", 'xpath', "className", "Uiautomator")
        if method in methods:
            if method == 'id':
                element = self.driver.find_element_by_id(info)
            elif method == 'xpath':
                element = self.driver.find_element_by_xpath(info)
            elif method == 'className':
                element = self.driver.find_element_by_class_name(info)
            else:
                element = self.driver.find_element_by_android_uiautomator('new UiSelector().%s' % info)
            return element
        else:
            raise Exception("定位方法出错")

