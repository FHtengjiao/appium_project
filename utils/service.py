from utils.CLT_util import CLTUtil
from utils.Port import Port


class Service(object):

    def __init__(self):
        self.clt_util = CLTUtil()
        self.port = Port(self.clt_util)

    def get_devices(self):
        devices = []
        result = self.clt_util.execute_command_result("adb devices")
        for i in range(1, len(result)):
            if 'device' in result[i]:
                devices.append(result[i].split('\t')[0])
        return devices

    def get_port(self, start, port_num):
        port_list = self.port.create_port(start, port_num)
        return port_list

    def create_command(self):
        command_list = []
        devices = self.get_devices()
        num = len(devices)
        p = self.get_port(4723, num)
        bp = self.get_port(4900, num)
        for i in range(0, num):
            command = "appium -p %d -bp %d -U %s -no Reset --session-override" % (p[i], bp[i], devices[i])
            command_list.append(command)
        return command_list


if __name__ == '__main__':
    service = Service()
    print(service.create_command())