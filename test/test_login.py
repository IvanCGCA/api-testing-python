import requests
from utils.config import Config

session = requests.Session()
session.headers.update(Config.HEADERS)

def test_create_post():
    """Validar creación de un post (Equivalente a funcionalidad crítica)"""
    payload = {
        "title": "QA Portfolio",
        "body": "Testing Python automation",
        "userId": 1
    }
    response = session.post(f"{Config.BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    assert "id" in response.json()

def test_get_invalid_endpoint():
    """Prueba negativa: Endpoint que no existe"""
    response = session.get(f"{Config.BASE_URL}/invalid-route")
    assert response.status_code == 404