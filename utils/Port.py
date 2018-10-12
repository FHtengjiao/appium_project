# -*- coding: utf-8 -*-
from utils.getplatform import Platform


class Port(object):

    def __init__(self, tool):
        self.clt_tool = tool
        self.sys = Platform.get_platform_name()

    def check_port(self, port):

        flag = True
        # 创建check port命令：
        # netstat -anp tcp | grep port_number
        # lsof -i port_number
        if self.sys == 'macOS':
            command = "netstat -anp tcp | grep %d" % port
        else:
            command = "netstat -ano | findstr %d" % port
        result = self.clt_tool.execute_command_result(command)

        if len(result[0]) == 0:
            flag = False

        return flag

    def create_port(self, start_port, num):
        port_list = []
        while len(port_list) != num:
            if not self.check_port(start_port):
                port_list.append(start_port)
            start_port = start_port + 1
        return port_list


