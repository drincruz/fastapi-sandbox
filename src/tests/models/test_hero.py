from app.models.hero import Hero
from sqlmodel import Session


def test_create_hero(session: Session) -> None:
    hero = Hero(name="Deadpond", secret_name="Dive Wilson")
    session.add(hero)
    session.commit()
    session.refresh(hero)

    assert hero.id is not None
    assert hero.name == "Deadpond"
    assert hero.secret_name == "Dive Wilson"
    assert hero.age is None