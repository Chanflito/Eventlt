class EventType:
    def __init__(self, description, location):
        self.description=description
        self.location = location
        self.peopleQuantity = 0
        self.listOfPeople = []

    def getDescrition(self):
        return self.description

    def getLocation(self):
        return self.location