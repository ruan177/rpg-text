from src.Models.Character import Character, Base, URL
from src.Views.defineCharacterName import defineName
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
        nome = defineName()
        character = Character(nome=nome, level= "1" , exp="10", damage="20", life="100", classe='')
        session.add(character)


if __name__ == "__main__":
    main()