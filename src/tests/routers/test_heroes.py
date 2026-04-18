from app.main import app
from fastapi.testclient import TestClient


def test_create_hero(client: TestClient):
    response = client.post(
        '/heroes/', 
        json={'name': 'Deadpond', 'secret_name': 'Dive Wilson'}
    )

    assert response.status_code == 200