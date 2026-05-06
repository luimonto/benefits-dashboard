Benefits Dashboard – Test Automation

This project contains automated API and UI tests for the Benefits Dashboard application, it is built using pytest (API) and Playwright (UI), and fully containerized with Docker.

Requirements

Make sure you have installed:

Docker
Docker Compose

Environment Configuration

Create a .env file in the root of the project, you can rename .env.example that is already in the project.

Build the Docker Image with docker-compose

docker-compose build

Running Tests

Run all tests
docker-compose run tests

Run all API tests
docker-compose run tests -m api

Run all UI tests
docker-compose run tests -m ui

Run a specific test
docker-compose run tests -k test_create_employee -s

Test Structure
tests/
│
├── api/        # API test cases
├── ui/         # UI test cases (Playwright)

