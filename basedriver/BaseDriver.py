import time

from appium import webdriver


class BaseDriver(object):
    @staticmethod
    def get_driver(port, device):
        print(port, device)
        desired_caps = {
            'platform': 'Android',
            'deviceName': '%s' % device,
            'platformVersion': '8.0',
            'appPackage': 'com.newhjapp',
            'appActivity': 'com.newhjapp.MainActivity',
            'unicodeKeyboard': True,
            'restKeyboard': True,
            'automationName': 'uiautomator2'
        }

        driver = webdriver.Remote('http://127.0.0.1:'+str(port)+'/wd/hub', desired_caps)
        time.sleep(10)
        return driver
