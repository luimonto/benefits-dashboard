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

---

# MAJOR BUGS

---

## BUG-002: `salary` field incorrectly modeled in schema

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

## BUG-003: Missing error response definitions in Swagger

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

## BUG-004: API silently ignores unknown fields instead of rejecting request

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


## MINOR BUGS


