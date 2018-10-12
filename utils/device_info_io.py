# -*- coding: utf-8 -*-
import yaml

from utils.getplatform import Platform


class DeviceInfoIO(object):

    def __init__(self):
        sys = Platform.get_platform_name()
        if sys == 'Windows':
            self.file_path = r'F:\PythonProject\appium_project\config\deviceinfo.yaml'
        elif sys == 'Linux':
            self.file_path = ''
        elif sys == 'macOS':
            self.file_path = r'/Users/tengjiaoxie/PycharmProjects/appium_project/config/deviceinfo.yaml'

    def read_yaml(self):
        with open(self.file_path) as fp:
            loader = yaml.load(fp)
            return loader

    def write_to_yaml(self, i, p, bp, device):
        info = {
            "device_info_%s" % i: {
                "p": p,
                "bp": bp,
                "device": device
            }
        }
        with open(self.file_path, 'a') as fp:
            yaml.dump(info, fp)

    def clear_file(self):
        with open(self.file_path, 'w') as fp:
            fp.truncate()


if __name__ == '__main__':
    io = DeviceInfoIO()
    info = io.read_yaml()
    print(info['device_info_0']['p'])
