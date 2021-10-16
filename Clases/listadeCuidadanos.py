class CitizenList():
    def __init__ (self):
        self.citizenlist=[]
    def addCitizen(self, citizen):
        self.citizenlist.append(citizen)
    def getcl(self):
        return(self.citizenlist)

etlist = CitizenList()