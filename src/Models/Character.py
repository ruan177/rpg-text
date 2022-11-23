from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

URL = "mysql+mysqlconnector://root:residentevil6@localhost:3306/RpgText"

# $ cd C:\Program Files\MySQL\MySQL Server 8.0\bin
# $ .\mysql.exe -u aluno -p
# mysql> CREATE DATABASE ORM_1N_N1;
# mysql> USE ORM_1N_N1;
# mysql> SHOW TABLES;
Base = declarative_base()


class Character(Base):
    __tablename__ = "Character"
    id_character = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)
    level = Column(String(150), nullable=False)
    exp = Column(String(150), nullable=False)
    damage = Column(String(150), nullable=False)
    life = Column(String(150), nullable=False)
    classe = Column(String(150), nullable=False)


    def __str__(self):
        return "Character(id_character={}, nome=\"{}\", level=\"{}\", exp=\"{}\", damage=\"{}\", life=\"{}\", classe=\"{}\")".format(
            self.id_character, self.nome, self.level, self.exp, self.damage, self.life, self.classe)
