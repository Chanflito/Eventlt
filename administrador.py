from listadeCuidadanos import etlist
from listaDeEventos import eventos

class administrator():
    listaderevision=[]

    def __init__(self, user):
        self.user = user

    @classmethod
    def mandar_a_revision(cls,citizen):
        cls.listaderevision.append(citizen)

    def addEvent(self, location, description):
        eventos.eventCreator(location, description)

    @staticmethod
    def banCitizen(citizen):
        citizen.citizenBan=True
        etlist.addBannedCitizen(citizen)
        
    @staticmethod
    def unbanCitizen(citizen):
        citizen.citizenBan=False
        etlist.removeBannedCitizen(citizen)
