def employee_payload(firstname="", lastname="", username="", dependants=0):
    return {
        "firstName": firstname,
        "lastName": lastname,
        "username": username,
        "dependants": dependants or 0
    }
