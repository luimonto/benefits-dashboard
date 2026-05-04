import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "")
AUTH_TOKEN = os.getenv("AUTH_TOKEN", "")

UI_USERNAME = os.getenv("UI_USERNAME")
UI_PASSWORD = os.getenv("UI_PASSWORD")

HEADERS = {
    "Authorization": f"Basic {AUTH_TOKEN}",
    "Content-Type": "application/json"
}
