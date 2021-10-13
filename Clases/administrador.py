from usuario import usuario as user

class administrator(user):
    def __init__(self, name, lastName, age, CUIL):
        super().__init__(name, lastName, age, CUIL)

    def addEvent(self):
        pass

    def banCitizen(self):
        pass

    def unbanCitizen(self):
        pass
