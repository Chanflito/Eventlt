from usuario import usuario as user

class ciudadano(user):
    def __init__(self, name, lastName, age, CUIL, phoneNumber):
        super().__init__(name, lastName, age, CUIL)
        self.phoneNumber = phoneNumber
        self.zone = -1
        self.involvedEvents = []
        self.citizenBan = False
        self.friends=[]
        self.solicitudes=[]
        self.quien_me_rechazo = []

    def __repr__(self):
        return self.name + " " + self.lastName
    
    @classmethod
    def create_citizen(cls, name, lastName, age, CUIL, phoneNumber):
        from listadeCuidadanos import etlist
        x = ciudadano(name, lastName, age, CUIL, phoneNumber)
        etlist.addCitizen(x)

    @classmethod
    def init_citizen_creation(cls, name, lastName, age, CUIL, phoneNumber):
        x = ciudadano(name, lastName, age, CUIL, phoneNumber)
        return x

    def asistEvent(self):
        pass

    def unAsistEvent(self):
        pass 
    
    def enviar_solicitud(self, friend_cuil):
        from listadeCuidadanos import etlist
        Check_cuil=False
        i=0
        for a in etlist.citizenlist:
            if int(a.CUIL) == int(friend_cuil):
                Check_cuil=True
                break
            i+=1

        if [friend_cuil] in self.friends:
            return ("La persona ya se encuentra en tu lista de amigos")
        
        if [self] in etlist.citizenlist[i].solicitudes:
            return 'ya enviaste una solicitud de amistad a esta persona'

        if Check_cuil==True:
            etlist.citizenlist[i].solicitudes.append(self)
            return f"Enviaste una solicitud a la persona con cuil {friend_cuil}."
        else:
            return "La persona no se encuentra el database del Anses."

    def ver_solicitudes(self):
        if len(self.solicitudes) == 0:
            return 'no hay solicitudes de amistad'
        print('tus solicitudes son:')
        i = 0
        for solicitudes in self.solicitudes:
            print(f'{i}| nombre: {solicitudes.name} | cuil: {solicitudes.CUIL}\n')
            i += 1
        return 'para seleccionar un amigo, por favor ponga el numero correspondiente en la pestaña "aceptar_solicitud" o "rechazar solicitud'
        

    def aceptar_solicitud(self, idem):
        idem = int(idem)
        if len(self.solicitudes) == 0:
            return 'no hay solicitudes de amistad'
        elif idem - 1 > len(self.solicitudes):
            return 'Ok, regresando al menu de amigos'
        elif idem < 0:
            return "ese es un numero negativo"
        self.friends.append(self.solicitudes[idem])
        del self.solicitudes[idem]
        return f'se agrego a {self.friends[-1].name} {self.friends[-1].lastName} (cuil: {self.friends[-1].CUIL}) correctamente'
        
    def rechazar_solicitud(self, idem):
        if len(self.solicitudes) == 0:
            return 'no hay solicitudes de amistad'
        elif idem - 1 > len(self.solicitudes):
            return 'ese numero no es valido'
        elif idem < 0:
            return "ese es un numero negativo"
        self.solicitudes[idem].quien_me_rechazo.append(self.CUIL)
        del self.solicitudes[idem]
        return 'La solicitud se elimino correctamente'
        
    def change_zone(self, num):
        self.zone = num
        return num
