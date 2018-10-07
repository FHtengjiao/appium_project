from utils.INIParser import ReadIni


class ElementLocator(object):

    def __init__(self, driver):
        self.driver = driver
        self.reader = ReadIni()

    def locator(self, key):
        method = self.reader.read_config(key).split('>')[0]
        info = self.reader.read_config(key).spolit('>')[1]
        methods = ("id", 'xpath', "className", "Uiautomator")
        if method in methods:
            if method == 'id':
                value = self.driver.find_element_by_id(info)
            elif method == 'xpath':
                value = self.driver.find_element_by_xpath(info)
            elif method == 'className':
                value = self.driver.find_element_by_class_name(info)
            else:
                value = self.driver.find_element_by_android_uiautomator(info)
            return value
        else:
            raise Exception("定位方法出错")

