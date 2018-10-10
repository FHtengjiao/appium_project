from basedriver.BaseDriver import BaseDriver
from utils.Locator import ElementLocator
from utils.device_info_io import DeviceInfoIO


class LoginPage(object):

    def __init__(self, index):
        infoio = DeviceInfoIO()
        info = infoio.read_yaml()
        p = info['device_info_%d' % index]['p']
        device = info['device_info_%d' % index]['device']
        driver = BaseDriver.get_driver(p, device)
        self.locator = ElementLocator(driver)

    def get_username_element(self):
        return self.locator.locator("username")

    def get_password_element(self):
        return self.locator.locator("password")

    def get_login_button_element(self):
        return self.locator.locator("login_button")
