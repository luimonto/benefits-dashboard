class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.click(locator)

    def fill(self, locator, value):
        self.page.fill(locator, value)

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()