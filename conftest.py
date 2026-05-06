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

@pytest.fixture(scope="session")
def created_employees():
    return []


@pytest.fixture(scope="session", autouse=True)
def cleanup_employees(created_employees, employee):
    yield

    for emp_id in created_employees:
        try:
            employee.delete_employee(emp_id)
        except Exception as e:
            print(f"Cleanup failed for {emp_id}: {e}")
