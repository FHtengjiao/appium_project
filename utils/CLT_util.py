import os


class CLTUtil(object):

    def execute_command(self, command):
        os.system(command)

    def execute_command_result(self, command):
        file = os.popen(command)
        result = file.read().strip('\n').split('\n')
        return result

