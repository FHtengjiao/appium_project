import threading

from utils.CLT_util import CLTUtil
from utils.Port import Port


class Service(object):

    def __init__(self):
        self.clt_util = CLTUtil()
        self.port = Port(self.clt_util)
        self.devices = self.get_devices()
        self.commands = self.create_command()

    def get_devices(self):
        devices = []
        result = self.clt_util.execute_command_result("adb devices")
        for i in range(1, len(result)):
            if 'device' in result[i]:
                devices.append(result[i].split('\t')[0])
        return devices

    def create_command(self):
        command_list = []
        num = len(self.devices)
        p = self.port.create_port(4700, num)
        bp = self.port.create_port(4900, num)
        for i in range(0, num):
            command = "appium -p %d -bp %d -U %s --no-reset --session-override" % (p[i], bp[i], self.devices[i])
            command_list.append(command)
        return command_list

    def start_server(self, i):
        self.clt_util.execute_command(self.commands[i])

    def main(self):
        i = 0
        while i != len(self.devices):
            exe_thread = threading.Thread(target=self.start_server, args=(i,))
            exe_thread.start()
            i = i + 1


if __name__ == '__main__':
    service = Service()
    service.main()