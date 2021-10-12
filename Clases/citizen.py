from usuario import usuario as user

class citizen(user):
    def __init__(self, name, lastName, age, CUIL):
        super().__init__(name, lastName, age, CUIL)
        self.coordenates = []
        self.involvedEvents = []
        self.citizenBan = False

    def asistEvent(self):
        pass

    def unAsistEvent(self):
        pass
