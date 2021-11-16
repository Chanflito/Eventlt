from listadeCuidadanos import etlist
from listaDeEventos import eventos

class administrator():
  
    def __init__(self, user):
        self.user = user

    def addEvent(self, location, description):
        eventos.eventCreator(location, description)

    def banCitizen(self,citizen):
        citizen.citizenBan=True
        etlist.addBannedCitizen(citizen)
        
    def unbanCitizen(self,citizen):
        citizen.citizenBan=False
        etlist.removeBannedCitizen(citizen)

admin_bot = administrator("bobot")