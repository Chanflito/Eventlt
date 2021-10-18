from citizen import ciudadano as creadordeciudadano
import pandas

class CitizenList():

    def __init__ (self):
        self.citizenlist=[]
        self.BannedCitizenList=[]
        df = pandas.read_csv(r"D:\Codigos\TP1Prog\Database.csv")
        i = 0
        while i != len(df['CUIL']):
            self.citizenlist.append(creadordeciudadano.init_citizen_creation(df['name'][i], df['surname'][i], df['age'][i], df['CUIL'][i], df['Phonenumber'][i]))
            i += 1
            
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
