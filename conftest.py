import pytest
from api.clients.employee import Employee
from ui.browser.browser import Browser


@pytest.fixture
def page():
    browser = Browser(headless=True)
    page = browser.start()
    yield page
    browser.close()


@pytest.fixture
def employee():
    return Employee()
