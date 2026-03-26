import requests
from utils.config import Config

session = requests.Session()
session.headers.update(Config.HEADERS)

def test_get_users_list():
    response = session.get(f"{Config.BASE_URL}/users")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_user():
    payload = {
        "name": "Ivan Vega",
        "username": "ivega.qa",
        "email": "ivan@example.com"
    }
    response = session.post(f"{Config.BASE_URL}/users", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Ivan Vega"

def test_user_not_found():
    response = session.get(f"{Config.BASE_URL}/users/999")
    assert response.status_code == 404