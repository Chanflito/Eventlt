from usuario import usuario as user

class administrator(user):
    def __init__(self, name, lastName, age, numTel, CUIL):
        super().__init__(name, lastName, age, numTel, CUIL)

    def addEvent(self):
        pass

    def banCitizen(self):
        pass

    def unbanCitizen(self):
        pass