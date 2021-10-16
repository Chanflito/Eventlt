class CitizenList():
    def __init__ (self):
        self.citizenlist=[]
        self.BannedCitizenList=[]
    def addCitizen(self, citizen):
        self.citizenlist.append(citizen)
    def addBannedCitizen(self, citizen):
        self.BannedCitizenList.append(citizen)
    def removeBannedCitizen(self, citizen):
        i=0
        while i<len(self.BannedCitizenList):
            if citizen==self.BannedCitizenList[i]:
                del self.BannedCitizenList[i]
                return self.BannedCitizenList
            else:
                i=i+1
    def getcl(self):
        return(self.citizenlist)

etlist = CitizenList()
