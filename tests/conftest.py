import os
import pytest
from sqlmodel import SQLModel, create_engine, text 

POSTGRES_TEST_DB = os.getenv('POSTGRES_TEST_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
ADMIN_DB_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/postgres'
TEST_DB_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_TEST_DB}'

admin_engine = create_engine(ADMIN_DB_URL, isolation_level="AUTOCOMMIT")
test_engine = create_engine(TEST_DB_URL)

def create_test_db():
    with admin_engine.connect() as connection:
        try:
            connection.execute(
                text(f'CREATE DATABASE {POSTGRES_TEST_DB}')
            )
        except Exception as err:
            print(f'[WARN] Test database error {err}')

@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    create_test_db()
    SQLModel.metadata.create_all(bind=test_engine)
    yield
    SQLModel.metadata.drop_all(bind=test_engine)
