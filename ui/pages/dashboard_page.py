from ui.locators.locators import DashboardLocators

class DashboardPage:

    def __init__(self, page):
        self.page = page

    def add_employee(self, firstname, lastname):
        self.page.click(DashboardLocators.ADD_EMPLOYEE_BTN)
        self.page.fill(DashboardLocators.FIRST_NAME_INPUT, firstname)
        self.page.fill(DashboardLocators.LAST_NAME_INPUT, lastname)
        self.page.click(DashboardLocators.SAVE_BUTTON)

    def employee_exists(self, firstname):
        return self.page.locator(f"text={firstname}").is_visible()
