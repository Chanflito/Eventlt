from listadeCuidadanos import etlist

class administrator():
  
    def __init__(self, user):
        self.user = user

    def addEvent(self):
        pass

    def banCitizen(self,citizen):
        citizen.citizenBan=True
        etlist.addBannedCitizen(citizen)
        
    def unbanCitizen(self,citizen):
        citizen.citizenBan=False
        etlist.removeBannedCitizen(citizen)
