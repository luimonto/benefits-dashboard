# API Bug Report - Benefits Dashboard

## Summary

| Severity | Count |
|----------|-------|
| Critial  |       |
| Major    |       |
| Minor    |       |

---

# CRITICAL BUGS

---

## BUG-001: Inconsistent financial units (yearly vs per paycheck)

## Description

The API mixes financial units

. `Salary` is yearly

. `gross`, `benefitsCost`, and `net` are paycheck

This behavior is not documented

## Steps to reproduce:
1. Create employee
```
{
  "firstName": "Steve",
  "lastName": "Rogers",
  "username": "test_user_1",
  "dependants": 1
}
```
2 . Retrieve employee

## Actual result

```
{
  "salary": 52000,
  "gross": 2000,
  "benefitsCost": 57.69231,
  "net": 1942.3077
}
```

## Expected result:
. All fields use same unit (yearly or paycheck), or units are clearly documented

## Impact:
. Misleading financial data 
. High risk of incorrect calculations
. Breaks business logic clarity

## Recommendation
Standardize units or document them clearly in the API contract


## BUG-002 GET employee with invalid UUID return 500 internal server error

## Description

The API returns `500 inetranl server error` when an invalid UUID is providen in the path parameter this indicates the 
request is not properly validated before processing

## Steps to reproduce

1. Send GET `/api/Employee/{id}` with an invalid UUID
```
/api/Employee/123-not-a-uuid
```

## Actual result

`500 internal server error`

## Expected result

. Should return `400 bad reuqest` if want to return invalid format or `404 not found` if want to be treated as not 
existing resource

## Impact

. Indicates unhandled exception in the backend 
. Causes not proper way to handle client side error 

## Recommendation

Validate UUID format before processing and then return appropiate client error.


---

# MAJOR BUGS

---

## BUG-003: `salary` field incorrectly modeled in schema

## Description

The `salary` field is defined as a writable field in the schema but behaves as a server calculated value

## Steps to reproduce

1. Send POST `/api/Employees` without `salary` field
2. Inspect response

## Actual result

```
"salary": 52000
```

## Expected result

. `salary` is requiered as an input or marked as `"readOnly": true`

## Impact

. Confusing API contract
. Inconsistent with other computed fields

## Recommendation

Mark `salary` as `readOnly` or make it as required input

---

## BUG-004: Missing error response definitions in Swagger

## Description

Swagger documentation only defines `200 success` responses and does not include error responses

## Steps to reproduce

1. Open swagger json
2. Inspect any endpoint response 

## Actual result

```
"responses": {
  "200": {
    "description": "Success"
  }
}
```

## Expected result

The swagger documentation should include:
 . `400 Bad Request`
 . `401 Unauthorized`
 . `404 Not Found`
 . `422 Unprocessable Entity`

## Impact

 . Prevents accurate API contract validation 
 . Confuses API consumers 
 . Limits test coverage

## Recommendation

Define complete reponse schemas for all endpoints

---

## BUG-005: API silently ignores unknown fields instead of rejecting request

## Description

The API accepts requests containing unknown fields and silently ignores them, it returns `200 OK` response. This 
behavior contradicts the API schema which specifies `"additionalProppeerties: false"` this indicates that not known 
fields should not be allowed

## Steps to reproduce

1. Send POST `/api/Employee` with payload like 
```
{
  "firstName": "extra",
  "lastName": "field",
  "username": "extra_field",
  "unexpectedField": "boom"
}
```

## Actual result

 . Response `200 OK`
 . Employee is created successfully 
 . `unexpectedField` is not present in the response
```
{
  "firstName": "extra",
  "lastName": "field",
  "username": "extra_field"
}
```

## Expected result

. Request should be rejected with:
  - `400 Bad Request` or `422 Unprocessable Entity`
. Error message indicating unknown field is not allowed

## Impact

. Violated API contract (`additionalProperties: false`)
. Causes silent data loss (client assumes field was accepted)

## Recommendation
 
Reject request containing unknown fields and return error message indicating invalid properties


## BUG-006: Invalid data type returns 405 method not allowed

## Description

When sending and invalid data type for field (string instead integer for dependants), the API returns 
`405 method not allowed` which is unrelated to the request content

## Steps to reproduce

1. Send incorrect data type (string in `dependants` field)
```
{
  "firstName": "Type",
  "lastName": "Test",
  "username": "type_test",
  "dependants": "two"
}
```

## Actual result

. Response with `405 method not allowed`

## Expected result

. Response with `400 bad request` or `422 unprocessable entity`

## Impact 
. Incorrect HTTP status code
. Makes debugging harder

## Recommendation 

Implement proper request validation and return correct status code



## MINOR BUGS


