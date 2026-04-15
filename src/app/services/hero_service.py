from app.database import SessionDep
from app.models.hero import Hero
from app.models.team import Team
from sqlmodel import select
from typing import List


def get_all_heroes(session: SessionDep) -> List[dict]:
    statement = select(Hero, Team).join(Team)
    results = session.exec(statement).all()

    response = list()
    for hero, team in results:
        response.append(
            {
                'hero_id': hero.id,
                'name': hero.name,
                'age': hero.age,
                'age': hero.age,
                'secret_name': hero.secret_name,
                'team': team
             }
        )

    return response