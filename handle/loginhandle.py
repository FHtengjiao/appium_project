from page.loginpage import LoginPage


class LoginHandle(object):

    def __init__(self, index):
        self.loginpage = LoginPage(index)

    def username_input(self, username):
        self.loginpage.get_username_element().send_keys(username)

    def password_input(self, password):
        self.loginpage.get_password_element().send_keys(password)

    def click_login_button(self):
        self.loginpage.get_login_button_element().click()

