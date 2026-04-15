from app.models.hero import Hero
from app.models.team import Team
from app.services.hero_service import get_all_heroes
from sqlmodel import Session


def test_get_all_heroes(session: Session):
    a_team = Team(name="A Team", headquarters="NYC")
    session.add(a_team)
    session.commit()
    session.refresh(a_team)

    hero1 = Hero(name="Ka Ying So", age=27, secret_name="Secret Asian Woman", team_id=a_team.id)
    hero2 = Hero(name="Yik Fung Poon", age=30, secret_name="Secret Asian Man", team_id=a_team.id)

    session.add(hero1)
    session.add(hero2)
    session.commit()
    session.refresh(hero1)
    session.refresh(hero2)

    response = get_all_heroes(session)

    assert len(response) == 2