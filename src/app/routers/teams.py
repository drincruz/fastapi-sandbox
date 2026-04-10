from app.database import SessionDep
from app.models.team import Team
from fastapi import APIRouter, Depends
from app.services.team_service import create_team

router = APIRouter(prefix='/teams', tags=['teams'])

@router.post('/')
def create_new_team(team: Team, session: SessionDep):
    return create_team(team, session)