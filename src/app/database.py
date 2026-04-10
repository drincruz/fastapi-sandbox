import os
from app.models.hero import Hero
from app.models.team import Team
from fastapi import Depends
from typing import Annotated
from sqlmodel import Session, SQLModel, create_engine


POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_TEST_DB = os.getenv('POSTGRES_TEST_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}'

engine = create_engine(DB_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]