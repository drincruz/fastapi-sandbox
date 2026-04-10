from app.database import SessionDep
from app.models.team import Team


def create_team(team: Team, session: SessionDep) -> Team:
    session.add(team)
    session.commit()
    session.refresh(team)

    return team