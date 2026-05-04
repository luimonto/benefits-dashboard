class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/Login")

    def login(self, username, password):
        self.page.fill("#username", username)
        self.page.fill("#passwrof", password)
        self.page.click("button[type='submit']")
        