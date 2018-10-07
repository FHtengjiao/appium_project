from utils.CLT_util import CLTUtil


class Port(object):

    def __init__(self, tool):
        self.clt_tool = tool

    def check_port(self, port):

        flag = True

        # 创建check port命令：
        # netstat -anp tcp | grep port_number
        # lsof -i port_number
        command = "netstat -anp tcp | grep " + str(port)
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


if __name__ == '__main__':
    port_tool = Port()
    port_list = port_tool.create_port(4700, 7)
    print(port_list)
