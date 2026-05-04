# API Bugs

## Bug 1: Empty first name allowed

Severity: Medium

Steps:
1. POST /employees
2. Send empty firstName

Expected:
Validation error

Actual:
Employee created