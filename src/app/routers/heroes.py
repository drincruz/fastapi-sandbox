from app.database import SessionDep
from fastapi import APIRouter
from app.services.hero_service import get_all_heroes

router = APIRouter(prefix='/heroes', tags=['heroes'])

@router.get('/all')
def get_heroes(session: SessionDep):
    return get_all_heroes(session)