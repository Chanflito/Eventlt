import csv
import pandas
import os
import pandas as pd
import listaDeEventos
from matplotlib import pyplot


class Stats_Board:
    def show_p_per_zone(self):
        pyplot.title("Cantidad de personas por zona")
        pyplot.xlabel("Zonas",labelpad=6)
        pyplot.ylabel("Personas",labelpad=6)
        df = pandas.read_csv(os.path.abspath("Database.csv"))
        seconddf = pandas.read_csv(os.path.abspath("zona.csv"))
        users = open("Database.csv","r") 
        file = csv.DictReader(users)
        zonas=list(seconddf['Nombre'])
        nombres = []
        i = 0
        for col in file:
            nombres.append(col['Name'])
            i += 1

        p_x_zona = [[]]
        new=[]
        a = 0
        for sector in seconddf['Nombre']:
            i = 0
            for zona in df['Zona']:
                if a == zona:
                    p_x_zona[a].append(nombres[i])
                    i += 1
                else:
                    i += 1
            new.append(len(p_x_zona[a]))
            a += 1
            p_x_zona.append([]) 
        pyplot.bar(zonas,new)
        pyplot.show()

    def top_per_zone(self):
        pass

