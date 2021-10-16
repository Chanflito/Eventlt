from usuario import usuario as user
from listadeCuidadanos import etlist
class administrator(user):
    def __init__(self, name, lastName, age, CUIL):
        super().__init__(name, lastName, age, CUIL)

    def addEvent(self):
        pass

    def banCitizen(self,citizen):
        citizen.citizenBan=True
        etlist.addBannedCitizen(citizen)
        

    def unbanCitizen(self,citizen):
        citizen.citizenBan=False
        etlist.removeBannedCitizen(citizen)
