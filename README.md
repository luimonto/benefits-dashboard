# Benefits Dashboard – Test Automation

Automated API and UI test framework for the Benefits Dashboard application

The project validates both frontend and backend functionality, including CRUD operations, authentication handling, business calculations, API contract validation, and UI workflows.

---

# Tech Stack

| Tool | Purpose |
|---|---|
| Python | Main programming language |
| Pytest | Test runner and assertions |
| Playwright | UI automation |
| Docker | Reproducible execution environment |

---

# Project Structure

```bash
.
├── api/
│   ├── clients/          # API clients/employees
│   └── tests/            # API test cases
│
├── ui/
│   ├── browser/          # Launch browser instance
│   ├── pages/            # Pages in the UI
│   ├── components/       # Reusable UI components
│   ├── locators/         # UI locators
│   └── tests/            # UI test cases
│
├── config/               # Settings, constants and utilities
├── reports/              # API/UI bug reports
├── conftest.py           # Shared pytest fixtures
├── Dockerfile
├── docker-compose.yml
└── pytest.ini
```

---


# Design Decisions

## Why API vs UI separation?

Business logic and validations were prioritized at the API level because:
- Faster execution
- Better debugging
- Easier validation of edge cases

UI automation focuses on:
- User workflows
- Rendering
- Interaction behavior

---

## Framework Design

The UI framework follows a Page Object / component-based approach:
- BasePage
- TableComponent
- FormComponent
- ModalComponent

This improves:
- Reusability
- Readability
- Maintainability

---

# Environment Configuration

Create a `.env` file in the project root.

You can rename the provided:

```bash
.env.example
```

Required variables:

```env
API_BASE_URL=
UI_USERNAME=
UI_PASSWORD=
AUTH_TOKEN=
```

---

# Build Docker Image

```bash
docker-compose build
```

---

# Running Tests

## Run all tests

```bash
docker-compose run tests
```

## Run API tests

```bash
docker-compose run tests -m api
```

## Run UI tests

```bash
docker-compose run tests -m ui
```

## Run specific test

```bash
docker-compose run tests -k test_create_employee -s
```

---

# Pytest Markers

| Marker | Description |
|---|---|
| api | API test suite |
| ui | UI test suite |

---

# Known Issues / Bugs Found

The project includes documented findings in:

- `reports/api-bugs.md`
- `reports/ui-bugs.md`

---

# Future Improvements

Potential future enhancements:
- CI/CD integration
- Parallel execution
- HTML reporting
- Test data factories
- Retry strategies
- Playwright tracing/screenshots on failure


