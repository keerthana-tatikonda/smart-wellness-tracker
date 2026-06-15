import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Smart Wellness Tracker API"
    }


def test_get_entries():
    response = client.get("/entries")

    assert response.status_code == 200

    assert isinstance(response.json(), list)