import pytest
from config.settings import UI_USERNAME, UI_PASSWORD

from ui.pages.login_page import LoginPage
from ui.pages.dashboard_page import DashboardPage


@pytest.mark.ui
def test_add_employee_ui(page):

    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.navigate()
    login.login(UI_USERNAME, UI_PASSWORD)

    first_name = "Luis"
    last_name = "Montoya"
    dependants = 1

    dashboard.add_employee(first_name, last_name, dependants)
    row = dashboard.get_employee_row(first_name)

    assert row is not None
    assert first_name in row.inner_text()
    assert last_name in row.inner_text()


@pytest.mark.ui
def test_table_headers(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.navigate()
    login.login(UI_USERNAME, UI_PASSWORD)

    headers = dashboard.employees_table.get_headers()

    assert headers == [
        "Id",
        "Last Name",
        "First Name",
        "Dependents",
        "Salary",
        "Gross Pay",
        "Benefits Cost",
        "Net Pay",
        "Actions"
    ]