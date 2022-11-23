from src.Models.Character import Character, Base, URL
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import create_engine

Character()
def main():
    engine = create_engine(url=URL)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # mysql> DESC Pessoa;

    Session = sessionmaker(engine, expire_on_commit=False)

    with Session.begin() as session:
        character = Character(nome="Parry", level= "1" , exp="10", damage="20", life="100", classe="Archiever")

        session.add(character)


if __name__ == "__main__":
    main()