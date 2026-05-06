from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_ERROR = "text=The Username field is required"
    PASSWORD_ERROR = "text=The Password field is required"

    def navigate(self):
        self.page.goto("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/Login")

    def login(self, username, password):
        self.fill("#Username", username)
        self.fill("#Password", password)
        self.click("button[type='submit']")\

    def get_username_error(self):
        return self.page.locator(self.USERNAME_ERROR)

    def get_password_error(self):
        return self.page.locator(self.PASSWORD_ERROR)