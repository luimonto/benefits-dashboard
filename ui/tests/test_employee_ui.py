import pytest

from config.settings import UI_USERNAME, UI_PASSWORD

from ui.pages.login_page import LoginPage
from ui.pages.dashboard_page import DashboardPage


@pytest.mark.ui
def test_add_employee_ui(page):

    login = LoginPage(page=page)
    dashboard = DashboardPage(page=page)

    login.navigate()
    login.login(username=UI_USERNAME, password=UI_PASSWORD)

    dashboard.add_employee(firstname="Luis", lastname="Montoya")

    assert dashboard.employee_exists("Luis Montoya")
