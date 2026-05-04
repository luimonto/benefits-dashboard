import pytest
from api.tests.test_data import employee_payload


@pytest.mark.api
def test_create_employee(employee):
    payload = employee_payload(firstname="Luis", lastname="Montoya")

    response = employee.create_employee(payload=payload)

    assert response.status_code == 200
    data = response.json()

    assert data["firstName"] == "Luis"


@pytest.mark.api
def test_create_employee_invalid(employee):
    payload = employee_payload(firstname="", lastname="Montoya")

    response = employee.create_employee(payload=payload)

    assert response.status_code in [400, 402]