from abc import ABC

class usuario(ABC):
    def __init__(self, name, lastName, age, numTel, CUIL):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.numTel = numTel
        self.CUIL = CUIL
    def __str__(self):
        return self.name + " " + self.lastName
        
