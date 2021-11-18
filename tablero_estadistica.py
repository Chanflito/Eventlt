import csv
file = open("marcadores.csv", "r")
csv_reader = csv.reader(file)

marcadores = []
for row in csv_reader:
    marcadores.append(row)

def listita(lista):
    for eventos in lista:
        del eventos[3:]
        print(eventos)

print(listita(marcadores))