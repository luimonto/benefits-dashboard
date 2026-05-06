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

    dashboard.add_employee("Luis", "Montoya")

    assert dashboard.employee_exists("Luis Montoya")