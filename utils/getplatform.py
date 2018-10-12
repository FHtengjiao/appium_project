# -*- coding: utf-8 -*-
import platform


class Platform(object):
    @staticmethod
    def get_platform_name():
        return platform.uname().system
