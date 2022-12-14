import random
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def selection(self) -> None:
        pass

## Concrete strategies
class Warrior(Strategy):
    ## actual application will have the algorithm instead this method
    def selection(self) -> str:
        return "Warrior"

class Mage(Strategy):
    def selection(self) -> str:
        return "Mage"

class Healer(Strategy):
    def selection(self) -> str:
        return "Healer"

class Random(Strategy):
    def selection(self) -> str:
        options = ["Rock", "Paper", "Scissors"]
        return random.choice(options)

def escolheClasse():

    while True:
        escolha = input('Escolha sua classe: 1 for Warrior , 2 for Mage, 3 for Healer and 4 ,for aleatory: ')

        if escolha == "1":
            warrior = Warrior()
            return warrior.selection()
            break

        elif escolha == "2":
            mage = Mage()
            return mage.selection()
            break

        elif escolha == "3":
            healer = Healer()
            return healer.selection()
            break

        elif escolha == "4":
            random = Random()
            return random.selection()
            break

        else:
            print('Escolha uma opção válida')
            continue

