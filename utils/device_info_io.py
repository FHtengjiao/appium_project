import yaml


class DeviceInfoIO(object):

    def read_yaml(self):
        with open('/Users/tengjiaoxie/PycharmProjects/appium_project/config/deviceinfo.yaml') as fp:
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
        with open('/Users/tengjiaoxie/PycharmProjects/appium_project/config/deviceinfo.yaml', 'a') as fp:
            yaml.dump(info, fp)

    def clear_file(self):
        with open('/Users/tengjiaoxie/PycharmProjects/appium_project/config/deviceinfo.yaml', 'w') as fp:
            fp.truncate()


if __name__ == '__main__':
    io = DeviceInfoIO()
    info = io.read_yaml()
    print(info['device_info_0']['p'])