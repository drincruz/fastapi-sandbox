from app.models.team import Team
from sqlmodel import Session

def test_create_team(session: Session):
    team = Team(name='A Team', headquarters='NYC')
    session.add(team)
    session.commit()
    session.refresh(team)

    assert team.id is not None
    assert team.name == 'A Team'
    assert team.headquarters == 'NYC'