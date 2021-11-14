import os, csv, pandas
from creadorDeEventos import EventType

class eventList:
    
    def __init__(self):
        df = pandas.read_csv(os.path.abspath("DescripcionDeEventos.csv"))
        seconddf = pandas.read_csv(os.path.abspath("Eventos.csv"))
        self.list = [[]]
        a = 0
        for sector in seconddf['Nombre']:
            i = 0
            for events in df['Place']:
                if sector == events:
                    x = EventType(df['Description'][i], sector)
                    self.list[a].append(x)
                    i += 1
                else:
                    i += 1
            a += 1
            self.list.append([])
        del self.list[-1]

    def eventCreator(self, location, description):
        seconddf = pandas.read_csv(os.path.abspath("Eventos.csv"))
        a = 0
        for sector in seconddf['Nombre']:
            if sector == location:
                x = EventType(description, location)
                with open(os.path.abspath("DescripcionDeEventos.csv"),mode="a",newline="") as h:
                    writer=csv.writer(h,delimiter=",")
                    writer.writerow([location,description])
                self.list[a].append(x)
                return x
            else:
                a += 1 
        return 'no existe la localizacion puesta'

eventos = eventList()

#eventos.eventCreator('Pilar','estudiar para informatica')

#print(eventos.list)