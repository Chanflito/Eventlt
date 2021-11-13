from usuario import usuario as user


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
        name_persona=input("Ingrese el nombre de la persona: ")
        surname_persona=input("Ingrese el apellido de la persona: ")
        check_name=False
        check_surname=False
        for i in df["Name"]:
            if str(i)==str(name_persona):
                check_name=True
                break
        for z in df["Surname"]:
            if str(z)==str(surname_persona):
                check_surname=True
                break

        if [name_persona,surname_persona] in ciudadano.friends:
            print ("La persona ya se encuentra en tu lista de amigos")
        else:
            if check_name==True and check_surname==True:
                ciudadano.friends.append([name_persona,surname_persona])
                print (f"La persona llamada {name_persona} {surname_persona} fue agregada exitosamente.")
            else:
                print ("La persona no se encuentra el database del Anses.")
