import pytest
from http import HTTPStatus

from api.tests.test_data import employee_payload
from config.utils import calculate_expected_benefits


@pytest.mark.api
def test_get_employee(employee):
    response = employee.get_employee("cb5c559f-9bd6-4b9b-9213-2d3851e5e550")

    assert response.status_code == HTTPStatus.OK


@pytest.mark.api
@pytest.mark.xfail(
    reason="API overrides username with authenticated user"
)
def test_create_employee(employee):
    payload = employee_payload(
        firstname="Luis",
        lastname="Montoya",
        username="luimonto",
        dependants=2
    )

    response = employee.create_employee(payload=payload)
    print(response.status_code)
    print(response.text)

    assert response.status_code == HTTPStatus.OK
    data = response.json()

    assert data["firstName"] == "Luis"
    assert data["lastName"] == "Montoya"
    assert data["username"] == "luimonto"
    assert data["dependants"] == 2


@pytest.mark.api
def test_create_employee_blank_field(employee):
    payload = employee_payload(lastname="Montoya")

    response = employee.create_employee(payload=payload)

    assert response.status_code in (
        HTTPStatus.BAD_REQUEST,
        HTTPStatus.UNPROCESSABLE_ENTITY
    )

    data = response.json()
    assert data is not None


@pytest.mark.api
def test_update_without_id(employee):
    payload = employee_payload(
        firstname="noid",
        lastname="update",
        username="noid_update"
    )

    res = employee.update_employee(payload)

    assert res.status_code != HTTPStatus.OK


@pytest.mark.api
def test_duplicated_username(employee):
    payload = employee_payload(
        firstname="duplicated",
        lastname="user",
        username="duplicated_user"
    )

    res1 = employee.create_employee(payload)
    res2 = employee.create_employee(payload)

    assert res2.status_code != HTTPStatus.INTERNAL_SERVER_ERROR


@pytest.mark.api
def test_invalid_expiration_format(employee):
    payload = employee_payload(
        firstname="date",
        lastname="test",
        username="date_test"
    )

    payload["expiration"] = "invalid_format"

    res = employee.create_employee(payload)

    assert res.status_code != HTTPStatus.OK


@pytest.mark.api
def test_float_precision(employee):
    payload = employee_payload(
        firstname="float",
        lastname="test",
        username="float_test",
        dependants=1
    )

    res = employee.create_employee(payload)
    data = res.json()

    assert isinstance(data["gross"], (int, float))
    assert round(data["net"], 2) == data["net"]


@pytest.mark.api
def test_benefits_calculation(employee):
    payload = employee_payload(
        firstname="Some",
        lastname="One",
        username="some_one",
        dependants=2
    )

    response = employee.create_employee(payload=payload)
    data = response.json()

    gross, benefits, net, yearly_salary = calculate_expected_benefits(payload.get("dependants"))

    assert data["gross"] == gross
    assert round(data["benefitsCost"], 2) == round(benefits, 2)
    assert round(data["benefitsCost"], 2) == round(benefits, 2)


@pytest.mark.api
def test_benefits_calculation_with_zero_dependants(employee):
    payload = employee_payload(
        firstname="zero",
        lastname="deps",
        username="zero_dep",
        dependants=0
    )

    res = employee.create_employee(payload)
    data = res.json()

    gross, benefits, net, yearly_salary = calculate_expected_benefits(0)

    assert round(data["benefitsCost"], 2) == round(benefits, 2)


@pytest.mark.api
def test_negative_dependants(employee):
    payload = employee_payload(
        firstname="negative",
        lastname="dependants",
        username="neg_test",
        dependants=-1
    )

    res = employee.create_employee(payload)

    assert res.status_code != HTTPStatus.OK


@pytest.mark.api
def test_dependants_boundary(employee):
    payload = employee_payload(
        firstname="test",
        lastname="test",
        username="test_test",
        dependants=33
    )

    res = employee.create_employee(payload)

    assert res.status_code in (
        HTTPStatus.BAD_REQUEST,
        HTTPStatus.UNPROCESSABLE_ENTITY
    )


@pytest.mark.api
@pytest.mark.xfail(reason="API returns 405 instead of validation error for invalid data type")
def test_dependants_invalid_type(employee):
    payload = employee_payload(
        firstname="type",
        lastname="invalid",
        username="type_invalid"
    )

    payload["dependants"] = "two"

    res = employee.create_employee(payload)

    assert res.status_code in (
        HTTPStatus.BAD_REQUEST,
        HTTPStatus.UNPROCESSABLE_ENTITY
    )


@pytest.mark.api
def test_delete_employee(employee):
    payload = employee_payload(
        firstname="Luis",
        lastname="Montoya",
        username="luimonto",
        dependants=2
    )

    response = employee.create_employee(payload=payload)
    assert response.status_code == HTTPStatus.OK

    employee_id = response.json()["id"]

    delete_response = employee.delete_employee(employee_id)
    assert delete_response.status_code == HTTPStatus.OK

    get_response = employee.get_employee(employee_id)
    assert get_response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.api
def test_readonly_fields_are_ignored_or_rejected(employee):
    payload = employee_payload(
        firstname="read",
        lastname="only",
        username="read_only",
        dependants=1
    )

    # Inject readOnly fields
    payload["gross"] = 999999
    payload["benefitsCost"] = 0
    payload["net"] = 999999

    res = employee.create_employee(payload)
    assert res.status_code == HTTPStatus.OK

    data = res.json()

    # Backend should ignore client values
    assert data["gross"] != 999999
    assert data["benefitsCost"] != 0
    assert data["net"] != 999999


@pytest.mark.api
@pytest.mark.xfail(reason="API does not enforce additionalProperties=false")
def test_unknown_fields_are_ignored(employee):
    payload = employee_payload(
        firstname="extra",
        lastname="field",
        username="extra_field"
    )

    payload["unexpectedField"] = "boom"

    res = employee.create_employee(payload)

    assert res.status_code == HTTPStatus.OK
    assert "unexpectedField" not in res.json()


@pytest.mark.api
@pytest.mark.xfail(reason="API returns 500 instead of 400/404 for invalid UUID")
def test_get_employee_invalid_uuid(employee):
    invalid_id = "123-not-a-uuid"

    res = employee.get_employee(invalid_id)

    assert res.status_code in (
        HTTPStatus.BAD_REQUEST,
        HTTPStatus.NOT_FOUND
    )