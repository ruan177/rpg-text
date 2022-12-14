from src.Models.Character import Character, Base, URL
from src.Views.defineCharacterName import defineName
from src.Views.defineClasse import escolheClasse
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import create_engine, select

Character()
def main():
    engine = create_engine(url=URL)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # mysql> DESC Pessoa;

    Session = sessionmaker(engine, expire_on_commit=False)

    with Session.begin() as session:
        nome = defineName()
        classe = escolheClasse()
        character = Character(nome=nome, hp= 100 , level=1, forca=20, destreza=15, classe=classe)
        session.add(character)

    with Session.begin() as session:
        character = session.query(Character).get(1)
        print(character)

if __name__ == "__main__":
    main()