FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN playwright install --with-deps

ENTRYPOINT ["pytest"]

# docker build -t benefits-dashboard-automation .
# docker run --env-file .env benefits-dashboard-automation
# docker run --env-file .env benefits-dashboard-automation -m api
# docker run --env-file .env benefits-dashboard-automation -m ui