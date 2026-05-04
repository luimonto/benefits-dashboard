def employee_payload(firstname="", lastname="", dependents=None):
    return {
        "firstName": firstname,
        "lastName": lastname,
        "dependents": dependents or []
    }
