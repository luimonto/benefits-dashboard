import pytest
from api.clients.employee import Employee


@pytest.fixture
def employee():
    return Employee()
