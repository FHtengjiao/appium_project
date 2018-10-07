import os


class CLTUtil(object):

    def execute_command(self, command):
        os.system(command)

    def execute_command_result(self, command):
        file = os.popen(command)
        # result = file.readlines()
        result = file.read().strip('\n').split('\n')
        return result


if __name__ == '__main__':
    tool = CLTUtil()
    tool.execute_command_result("netstat -anp tcp | grep 4723")
    # tool.execute_command_result("adb devices")