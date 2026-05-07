class DashboardLocators:
    ADD_EMPLOYEE_BTN = "text=Add Employee"
    FIRST_NAME_INPUT = "#firstName"
    LAST_NAME_INPUT = "#lastName"
    DEPENDANTS = "#dependants"
    SAVE_BUTTON = "#addEmployee"
    UPDATE_BUTTON = "#updateEmployee"
    DELETE_BUTTON = "#deleteEmployee"

class LoginLocators:
    USERNAME = "#Username"
    PASSWORD = "#Password"
    LOGIN_BUTTON = "button[type='submit']"

class TableLocators:
    ICON_BUTTONS = {
        "edit": "i.fa-edit",
        "delete": "i.fa-times",
    }
    TABLE_ID = "#employeesTable"

class ModalLocators:
    DIALOG_CLASS = ".modal_dialog"

class FormLocators:
    DIALOG_CLASS = ".modal.show"