# -*- coding: utf-8 -*-
import threading

from basedriver.BaseDriver import BaseDriver
from utils.CLT_util import CLTUtil
from utils.Port import Port
from utils.device_info_io import DeviceInfoIO
from utils.getplatform import Platform


class Service(object):

    def __init__(self):
        self.clt_util = CLTUtil()
        self.port = Port(self.clt_util)
        self.info_io = DeviceInfoIO()
        self.devices = self.get_devices()
        self.commands = self.create_command()

    def get_device_num(self):
        return len(self.devices)

    def get_devices(self):
        devices = []
        result = self.clt_util.execute_command_result("adb devices")
        for i in range(1, len(result)):
            if 'device' in result[i]:
                devices.append(result[i].split('\t')[0])
        print(devices)
        return devices

    def create_command(self):
        self.info_io.clear_file()
        command_list = []
        num = len(self.devices)
        p = self.port.create_port(4700, num)
        bp = self.port.create_port(4900, num)
        for i in range(0, num):
            command = "appium -p %d -bp %d -U %s --session-override" % (p[i], bp[i], self.devices[i])
            command_list.append(command)
            self.info_io.write_to_yaml(i, p[i], bp[i], self.devices[i])
        print(command_list)
        return command_list

    def start_server(self, i):
        self.clt_util.execute_command(self.commands[i])

    def kill_server(self):
        sys = Platform.get_platform_name()
        if sys == 'macOS':
            pid_list = []
            command = 'ps | grep "node"'
            results = self.clt_util.execute_command_result(command)
            for i in results:
                if "appium" in i:
                    pid = i.strip(' ').split(' ')[0]
                    pid_list.append(pid)
            while len(pid_list) != 0:
                self.clt_util.execute_command("kill %s" % pid_list[0])
                pid_list.pop(0)
        else:
            command = 'tasklist | find "node.exe"'
            results = self.clt_util.execute_command_result(command)
            if len(results) > 0:
                self.clt_util.execute_command("taskkill -F -PID node.exe")

    def main(self):
        threads = []
        self.kill_server()
        i = 0
        while i != len(self.devices):
            exe_thread = threading.Thread(target=self.start_server, args=(i,))
            threads.append(exe_thread)
            i = i + 1
        for j in threads:
            j.start()


if __name__ == '__main__':
    service = Service()
    service.main()
    infoio = DeviceInfoIO()
    info = infoio.read_yaml()
    driver_list = []
    # driver = BaseDriver.get_driver(p, device)
    # self.locator = ElementLocator(driver)
    for i in range(service.get_device_num()):
        p = info['device_info_%d' % i]['p']
        device = info['device_info_%d' % i]['device']
        driver = BaseDriver.get_driver(p, device)
        driver_list.append(driver_list)
    print(len(driver_list))