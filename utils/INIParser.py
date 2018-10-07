import os

from configparser import ConfigParser


class ReadIni:

    def __init__(self, file_path=None):

        if file_path is None:
            file_path = "../config/conf.ini"

        reader = ConfigParser()
        reader.read(file_path)
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
    value = reader.read_config("name")
    print(value)