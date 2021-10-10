import unittest
import menu
import citizen
import administrador
import usuario
import evento
class TestCitizen(unittest.TestCase):
    def test_str(self):
        Armando=citizen("Armando","Paredes",18,8,11111111111)
        result=Armando.str()
        self.assertEqual(result,"Armando Paredes")
