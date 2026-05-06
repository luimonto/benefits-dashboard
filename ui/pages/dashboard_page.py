from ui.pages.base_page import BasePage
from ui.locators.locators import DashboardLocators


class DashboardPage(BasePage):

    def add_employee(self, firstname, lastname):
        self.click(DashboardLocators.ADD_EMPLOYEE_BTN)
        self.fill(DashboardLocators.FIRST_NAME_INPUT, firstname)
        self.fill(DashboardLocators.LAST_NAME_INPUT, lastname)
        self.click(DashboardLocators.SAVE_BUTTON)

    def employee_exists(self, fullname):
        return self.page.locator(f"text={fullname}").is_visible()