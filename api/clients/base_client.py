import requests
from config.settings import BASE_URL, HEADERS


class BaseClient:

    def get(self, endpoint):
        return requests.get(url=f"{BASE_URL}{endpoint}", headers=HEADERS)

    def post(self, endpoint, payload):
        return requests.post(f"{BASE_URL}{endpoint}", json=payload, headers=HEADERS)

    def put(self, endpoint, payload):
        return requests.put(f"{BASE_URL}{endpoint}", json=payload, headers=HEADERS)

    def delete(self, endpoint):
        return requests.delete(f"{BASE_URL}{endpoint}", headers=HEADERS)
