from ui.components.modal_component import ModalComponent
from ui.pages.base_page import BasePage
from ui.locators.locators import DashboardLocators
from ui.components.table_component import TableComponent
from ui.components.modal_component import ModalComponent
from ui.components.form_component import FormComponent


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.employee_table = TableComponent(page, "#employeesTable")
        self.add_employee_modal = ModalComponent(page, ".modal_dialog")
        self.form = FormComponent(page, ".modal.show")

    def add_employee(self, firstname, lastname, dependants):
        self.page.wait_for_timeout(1000)
        self.employee_table.wait_until_visible()
        # click on add employee
        self.click(DashboardLocators.ADD_EMPLOYEE_BTN)
        self.page.wait_for_timeout(1000)
        # fill inputs
        self.form.fill_form(
            {
                DashboardLocators.FIRST_NAME_INPUT: firstname,
                DashboardLocators.LAST_NAME_INPUT: lastname,
                DashboardLocators.DEPENDANTS: dependants
            }
        )

        # click on add button to save new employee
        self.click(DashboardLocators.SAVE_BUTTON)

    def get_employee_row(self, firstname):
        rows = self.employee_table.get_rows()

        for i in range(rows.count()):
            row = rows.nth(i)
            if firstname in row.inner_text():
                return row

        return None