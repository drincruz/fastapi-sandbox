from app.database import SessionDep
from app.models.hero import Hero
from app.services.hero_service import get_all_heroes
from fastapi import APIRouter

router = APIRouter(prefix='/heroes', tags=['heroes'])

@router.get('/')
def get_heroes(session: SessionDep):
    return get_all_heroes(session)

@router.post('/')
def create_hero(hero: Hero, session: SessionDep) -> Hero:
    session.add(hero)
    session.commit()
    session.refresh(hero)

    return hero