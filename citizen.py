from usuario import usuario as user
from listadeCuidadanos import etlist
class citizen(user):
    def __init__(self, name, lastName, age, CUIL):
        super().__init__(name, lastName, age, CUIL)
        self.coordenates = []
        self.involvedEvents = []
        self.citizenBan = False

    @classmethod
    def create_citizen(cls, name, lastName, age, CUIL):
         cls.CUIL = cls(name, lastName, age, CUIL)
         etlist.addCitizen(citizen)
         return cls.CUIL
        
        #append to citicen class (not created yet)
        

    def asistEvent(self):
        pass

    def unAsistEvent(self):
        pass