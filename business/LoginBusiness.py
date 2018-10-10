from handle.loginhandle import LoginHandle


class LoginBusiness(object):

    def __init__(self, index):
        self.loginhandle = LoginHandle(index)

    def send_username(self):
        self.loginhandle.username_input("bz070109")

    def send_password(self):
        self.loginhandle.password_input('s09')

    def login_in(self):
        self.loginhandle.click_login_button()