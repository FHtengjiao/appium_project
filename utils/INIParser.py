# -*- coding: utf-8 -*-

from configparser import ConfigParser

from utils.getplatform import Platform


class ReadIni:

    def __init__(self, file_path=None):
        sys = Platform.get_platform_name()
        if file_path is None:
            if sys == 'macOS':
                file_path = r"/Users/tengjiaoxie/PycharmProjects/appium_project/config/conf.ini"
            else:
                file_path = r"F:\PythonProject\appium_project\config\conf.ini"
        reader = ConfigParser()
        reader.read(file_path, encoding='utf-8')
        self.reader = reader

    def read_config(self, key, selection=None):

        if selection is None:
            selection = "element"

        try:
            value = self.reader.get(selection, key)
        except:
            value = None

        return value


if __name__ == '__main__':
    reader = ReadIni()
    print(reader.read_config('username'))
