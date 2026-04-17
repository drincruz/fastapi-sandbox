from app.models.team import Team
from app.services.team_service import create_team
from sqlmodel import Session

def test_create_team(session: Session):
    team = Team(name='A Team', headquarters='NYC')
    result = create_team(team, session)

    assert result.id is not None
    assert result.name == team.name
    assert result.headquarters == team.headquarters