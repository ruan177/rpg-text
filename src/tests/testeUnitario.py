import unittest
from src.Views.defineClasse import Warrior

# python -m unittest src/tests/testeUnitario.py


class testeStrategy(unittest.TestCase):
    def test_Name(self):
        warrior = Warrior()
        self.assertEqual(warrior.selection(), 'Warrior')

if __name__== '__name__':
    unittest.main()