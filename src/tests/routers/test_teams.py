from fastapi.testclient import TestClient


def test_create_team(client: TestClient):
    response = client.post(
        '/teams', 
        json={'name': 'A Team', 'headquarters': 'NYC'}
    )

    assert response.status_code == 200