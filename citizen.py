from usuario import usuario as user
from pandas import pandas
import os

class ciudadano(user):
    def __init__(self, name, lastName, age, CUIL, phoneNumber):
        super().__init__(name, lastName, age, CUIL)
        self.phoneNumber = phoneNumber
        self.coordenates = []
        self.involvedEvents = []
        self.citizenBan = False
    friends=[]

    @staticmethod
    def create_citizen(name, lastName, age, CUIL, phoneNumber):
        from listadeCuidadanos import etlist
        x = ciudadano(name, lastName, age, CUIL, phoneNumber)
        etlist.addCitizen(x)

    @staticmethod
    def init_citizen_creation(name, lastName, age, CUIL, phoneNumber):
        x = ciudadano(name, lastName, age, CUIL, phoneNumber)
        return x

    def asistEvent(self):
        pass

    def unAsistEvent(self):
        pass #apens
    
    def añadir_amigo(self):
        df = pandas.read_csv(os.path.abspath("Database.csv"))
        friend_cuil=int(input("Ingrese el Cuil de la persona que quieres añadir a tu lista de amigos: "))
        Check_cuil=False
        i=0
        for a in df['CUIL']:
            if str(a)==str(friend_cuil):
                Check_cuil=True
                break
            i+=1

        if [friend_cuil] in ciudadano.friends:
            print ("La persona ya se encuentra en tu lista de amigos")
        else:
            if Check_cuil==True:
                ciudadano.friends.append([friend_cuil])
                print (f"La persona con cuil {friend_cuil} fue agregada a tu lista de amigos.")
            else:
                print ("La persona no se encuentra el database del Anses.")
