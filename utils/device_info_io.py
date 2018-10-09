import yaml


class DeviceInfoIO(object):

    def read_yaml(self):
        with open('../config/deviceinfo.yaml') as fp:
            load = yaml.load(fp)
        return load

    # def write_yaml(self):
    #     with open('../config/deviceinfo.yaml', 'a') as fp:

    def write_to_yaml(self, i, p, bp, device):
        info = {
            "device_info_%s" % i: {
                "p": p,
                "bp": bp,
                "device": device
            }
        }
        with open('../config/deviceinfo.yaml', 'a') as fp:
            yaml.dump(info, fp)

    def clear_file(self):
        with open('../config/deviceinfo.yaml', 'w') as fp:
            fp.truncate()


if __name__ == '__main__':
    io = DeviceInfoIO()
    io.write_to_yaml(0, 4723, 4724, "HuaweiC5")