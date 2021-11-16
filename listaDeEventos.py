import os, csv, pandas
from creadorDeEventos import EventType

class eventList:
    
    def __init__(self):
        df = pandas.read_csv(os.path.abspath("marcadores.csv"))
        seconddf = pandas.read_csv(os.path.abspath("Eventos.csv"))
        self.list = [[]]
        a = 0
        for sector in seconddf['Nombre']:
            i = 0
            for events in df['Zona']:
                if sector == events:
                    x = EventType(df['Descripcion'][i], sector)
                    self.list[a].append(x)
                    i += 1
                else:
                    i += 1
            a += 1
            self.list.append([])
        del self.list[-1]

    def eventCreator(self, zona, nombre, descripcion, latitud, longitud):
        seconddf = pandas.read_csv(os.path.abspath("Eventos.csv"))
        a = 0
        for sector in seconddf['Nombre']:
            if sector == zona:
                x = EventType(descripcion, zona)
                if int(seconddf["min_Lat"][a]) > latitud or (int(seconddf["min_Lat"][a])+2*(int(seconddf['Latitud'])-int(seconddf['min_Lat']))):
                    return 'usted no esta dentro de los limites de la zona'
                elif int(seconddf["min_Lon"][a]) > latitud or (int(seconddf["min_Lon"][a])+2*(int(seconddf['Longitud'])-int(seconddf['min_Lon']))):
                    return 'usted no esta dentro de los limites de la zona'
                with open(os.path.abspath("marcadores.csv"),mode="a",newline="") as h:
                    writer=csv.writer(h,delimiter=",")
                    writer.writerow([zona,nombre,descripcion, latitud, longitud])
                self.list[a].append(x)
                return x
            else:
                a += 1 
        return 'no existe la localizacion puesta'

eventos = eventList()

#eventos.eventCreator('Pilar','estudiar para informatica')

#print(eventos.list)