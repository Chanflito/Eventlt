import csv
import os
import pandas #se debe descargar esta libreria con pip install pandas en la terminal
import time
def register():
    user_cuil = input("Ingrese su CUIL: ")
    try:
        int(user_cuil)
    except ValueError:
            print("El CUIL debe ser un número")
            time.sleep(3)
            os.system("cls")
            menu()
    user_cuil=int(user_cuil)
    with open("Database.csv","r",newline="") as t: 
        reader=csv.reader(t,delimiter=",")
        for i in reader:
            for j in i:
                if j== str(user_cuil):
                    print ("Ya hay un usuario registrado con este CUIL")
                    time.sleep(3)
                    os.system("cls")
                    menu()
        counter = len(str(user_cuil))
        password = input("Ingrese su contraseña,porfavor: ")
        password1 = input("Confirme su contraseña,nuevamente: ")
        if counter == 11 and password == password1:
            print("Te has registrado correctamente.")
            with open("Database.csv",mode="a",newline="") as h:
                writer=csv.writer(h,delimiter=",")
                writer.writerow([user_cuil,password])
                print ("Bienvenido")
                h.close()
        elif counter != 11:
            print("Has ingresado el numero incorrecto de un CUIL.")
            time.sleep(3)
            os.system("cls")
            register()
        elif password != password1:
            print("Contraseña Incorrecta, intentelo denuevo.")
            time.sleep(3)
            os.system("cls")
            register()
df = pandas.read_csv(r"Database.csv")
def login():
    user_cuil=(input("Ingrese su CUIL: ")) 
    try:
        int(user_cuil)
    except ValueError:
            print("El CUIL debe ser un número")
            time.sleep(3)
            os.system("cls")
            menu()
    user_cuil=int(user_cuil)
    i = 0
    for a in df['CUIL']:
        if str(user_cuil) == str(a):
            break
        i += 1
        if i ==len(df["CUIL"]):
            print('su CUIL no fue encontrado')
            time.sleep(3)
            os.system("cls")
            menu()
            return i
    password = input("Ingrese su contraseña: ")
    if str(password) == str(df['Password'][i]):
        print("Bienvenido a Eventlt.")
    else:
        print("Contraseña invalida.")
        time.sleep(3)
        os.system("cls")
        menu()

def menu():
    print ("Bienvenido a Eventlt")
    user=int(input("1.Log in | 2. Registrarse | 3.Salir : "))
    if user == 1:
        login()
    elif user==2:
        register()
    elif user==3:
        return "salir"
    else:
        print ("Debes ingresar los numeros indicados anteriormente.")
        menu()
menu()
