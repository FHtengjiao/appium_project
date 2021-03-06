# -*- coding: utf-8 -*-
import multiprocessing
import time
import threading
import unittest

from business.LoginBusiness import LoginBusiness
from utils.service import Service


class ParamTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', param=None):
        super(ParamTestCase, self).__init__(methodName)
        global params
        params = param


class TestCase(ParamTestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.loginbusiness = LoginBusiness(params)

    def test_login_in_correct(self):
        self.loginbusiness.send_username()
        self.loginbusiness.send_password()
        self.loginbusiness.login_in()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


def get_suite(i):
  suite = unittest.TestSuite()
  suite.addTest(TestCase("test_login_in_correct", param=i))
  unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    server = Service()
    server.main()
    time.sleep(10)
    num = server.get_device_num()
    for i in range(num):
        process = multiprocessing.Process(target=get_suite, args=(i,))
        process.start()
