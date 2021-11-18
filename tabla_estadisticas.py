# AGREGAR AL CODIGO DENTRO DE LOS METODOS
# ORDENA LA LISTA DEPENDIENDO DE LAS PERSONAS EN LA ZONA 
# HAY QUE BUSCAR LA FORMA DE REPRESENTARLO COMO ZONAS
from collections import UserString
import csv
from time import process_time_ns
import pandas
import os
df = pandas.read_csv(os.path.abspath("Database.csv"))
seconddf = pandas.read_csv(os.path.abspath("zona.csv"))
users = open("Database.csv","r") 
file = csv.DictReader(users)

nombres = []
i = 0
for col in file:
    nombres.append(col['Name'])
    i += 1


p_x_zona = [[]]
a = 0
for sector in seconddf['Nombre']:
    i = 0
    for zona in df['Zona']:
        if a == zona:
            p_x_zona[a].append(nombres[i])
            i += 1
        else:
            i += 1
    a += 1
    p_x_zona.append([]) 

print(p_x_zona)





