FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN playwright install --with-deps

ENTRYPOINT ["pytest"]

# docker build -t benefits-dashboard .
# docker run --env-file .env benefits-dashboard
# docker run --env-file .env benefits-dashboard -m api # all api tests
# docker run --env-file .env benefits-dashboard -m api -k test_create_employee # individual test
# docker-compose run tests -k test_create_employee -s
# docker run --env-file .env benefits-dashboard -m ui @ all ui tests