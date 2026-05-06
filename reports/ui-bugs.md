# UI Bugs

## BUG-001: Dependants field accepts non-numbers input

## Description

The `dependants` input field allows non-numeric values (e.g., letters), because the input field is defined as 
`<input type="text">` instead of  `<input type="number">`

## Steps to reproduce

1. Navigate to Benefits Dashboard
2. Click "Add Employee"
3. Fill
    - firstName: Luis
    - lastName: Montoya
    - dependants: a
4. Click "Add"

## Actual result

The new employee is not added but no validation message is displayed and the modal keeps in the front

## Expected result

. Display an error message when click on "Add" button 

## Impact

. User does not know what happened with the new registry

## Recommendation

. Change input type to `number`
. Add frontend validation

---

## BUG-002: UI does not handle 401 unauthorized responses

## Description 

The backend correctly returns a 401 Unauthorized response when the user session expires but the frontend does not
handle this response properly. The user remains on the dashboard page with no redirection or error message.

## Steps to reproduce 
1. Login with your credentials
2. Navigate to the dashboard
3. Invalidate session (clear cookies or wait until session expires)
4. Trigger an API request (refresh the page or try to do some action)

## Actual result

. Backend returns 401 unauthorized
. UI remains on dashboard
. No error message is displayed
. No redirection to login page occurs

## Expected result

The user should be redirected to Login or a clear message should be shown ("Session expired")

## Impact
. The user operates on invalid session state
. No feedback for the user from the UI
. Security risk (UI still accessible visually)
. Inconsistent frontend/backend behavior

## Recommendation 

Implement global HTTP interceptor to catch 401 responses and redirect user to login page

