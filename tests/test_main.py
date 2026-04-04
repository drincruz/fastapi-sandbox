from src.app.database import TEST_DB_URL, get_session
from fastapi.testclient import TestClient
from src.app.main import app
from sqlmodel import Session, SQLModel, create_engine


def test_get_root():
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == { 'message': 'Hello World'}

def test_create_hero():
    engine = create_engine(TEST_DB_URL)
    print(f'[INFO] {TEST_DB_URL}')
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:

        client = TestClient(app)
        def get_session_override():
            return session
        
        app.dependency_overrides[get_session] = get_session_override
        response = client.post(
            '/heroes/', 
            json={'name': 'Deadpond', 'secret_name': 'Dive Wilson'}
        )
        app.dependency_overrides.clear()
        data = response.json()
        assert response.status_code == 200