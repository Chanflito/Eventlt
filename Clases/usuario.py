from abc import ABC, abstractmethod

class usuario(ABC):
    @abstractmethod
    def __init__(self, name, lastName, age, numTel, CUIL):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.numTel = numTel
        self.CUIL = CUIL