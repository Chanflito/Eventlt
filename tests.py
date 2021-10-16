import unittest
import login
from Clases import citizen
from Clases import listadeCuidadanos
from Clases import administrador
class TestCitizen(unittest.TestCase):
    def test_str(self):
        Armando=citizen("Armando","Paredes",18,11111111111)
        result=Armando.str()
        self.assertEqual(result,"Armando Paredes")
class TesttCitizenList(unittest.TestCase):
    def test_addCitizen(self):
        Armando=citizen("Armando","Paredes",18,11111111111)
        Trylist=listadeCuidadanos()
        Trylist.addCitizen(Armando)
        self.assertIn(Armando, Trylist)
class TestAdmin(unittest.TestCase):
    def test_banCitizen(self):
        Armando=citizen("Armando","Paredes",18,11111111111)
        Susana=administrador("Susuana", "Oria",18,22222222222)
        Susana.banCitizen(Armando)
        result=Armando.citizenBan
        self.assertTrue(result)
