import csv
import os
import pandas #se debe descargar esta libreria con pip install pandas en la terminal
import time
from citizen import ciudadano
from listadeCuidadanos import etlist


def menu_o():
    print ('Bienvenido a Eventlt')
    menu_login=int(input('1.Ingresar como Admin | 2.Ingresar como usuario | 3.Ingresar como sensor: '))

    if menu_login == 1:
        pass

    elif menu_login == 2:
        menu_login_citizen()

    elif menu_login == 3:
        pass


def register():
    phonenumber=input("Ingrese su numero telefonico: (+54) ")
    try:
        int(phonenumber)
    except ValueError:
        print("Debe ingresar su numero telefonico correctamente")
        time.sleep(3)
        os.system("cls")
        menu_login_citizen()
    user_cuil = input("Ingrese su CUIL: ")
    try:
        int(user_cuil)
    except ValueError:
        print("El CUIL debe ser un número")
        time.sleep(3)
        os.system("cls")
        menu_login_citizen()

    df = pandas.read_csv(r"D:\Codigos\TP1Prog\Database.csv")
    for i in df['Phonenumber']:
        if str(i) == str(phonenumber):
            print ("Ya hay un usuario registrado con este numero telefonico")
            time.sleep(3)
            os.system("cls")
            menu_login_citizen()
    
    for i in df['CUIL']:
        if str(i) == str(user_cuil):
            print ("Ya hay un usuario registrado con este CUIL")
            time.sleep(3)
            os.system("cls")
            menu_login_citizen()

    counter = len(str(user_cuil))

    counter2 = len(str(phonenumber))

    password = input("Ingrese su contraseña,porfavor: ")

    password1 = input("Confirme su contraseña,nuevamente: ")

    name = input('Ingrese su nombre ')

    surname = input('Ingrese su apellido ')

    try:
        if str(name).isdigit() == True or str(surname).isdigit() == True:
            raise ValueError()
    except ValueError:
        print ('Ingresaste numeros en tu nombre o apellido, intentelo denuevo')
        time.sleep(3)
        os.system("cls")
        menu_login_citizen()

    try:
        age =input("cual es tu edad: ")
        int(age)
    except ValueError:
        print("usted ha ingresado un caracter invalido, intentelo nuevamente")


    if counter == 11 and password == password1 and counter2==11:
        with open(r"D:\Codigos\TP1Prog\Database.csv",mode="a",newline="") as h:
            writer=csv.writer(h,delimiter=",")
            writer.writerow([user_cuil,password,phonenumber,name,surname,age])
        ciudadano.create_citizen(name,surname,age, user_cuil,phonenumber)
        print(etlist.getcl())
        print("su clase citizen fue creada exitosamente")
        time.sleep(3)
        os.system("cls")
        h.close()
        menu_login_citizen()    
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
    elif counter2 != 11:
        print("Cantidad de digitos de su numero telefonico es incorrecta.")
        time.sleep(3)
        os.system("cls")
        register()


def login():
    df = pandas.read_csv(r"D:\Codigos\TP1Prog\Database.csv")
    user_cuil=(input("Ingrese su CUIL: ")) 
    try:
        int(user_cuil)
    except ValueError:
        print("El CUIL debe ser un número")
        time.sleep(3)
        os.system("cls")
        menu_login_citizen()
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
            menu_login_citizen()
            return i
    password = input("Ingrese su contraseña: ")
    if str(password) == str(df['Password'][i]):
        print("Bienvenido a Eventlt.")
    else:
        print("Contraseña invalida.")
        time.sleep(3)
        os.system("cls")
        menu_login_citizen()


def menu_login_citizen():
    print ("porfavor, seleccione una de las siguentes opciones")
    try:
        user=int(input("1.Log in | 2. Registrarse | 3.Salir : "))
    except ValueError:
        print('eso no es un numero, intentelo nuevamente')
        menu_login_citizen()
    if user == 1:
        login()
    elif user==2:
        register()
    elif user==3:
        menu_o()
    else:
        print ("Debes ingresar los numeros indicados anteriormente.")
        menu_login_citizen()


def log_adm():
    df = pandas.read_csv(r"D:\Codigos\TP1Prog\Base_Adm.csv") #va el path csv de administradores
    admin_user=input("Ingrese su nombre de usuario como admnistrador: ")
    i = 0
    for a in df['Admin_user']:
        if str(admin_user) == str(a):
            break
        i += 1
    if i == len(df["Admin_user"]):
        print('su nombre no esta como usuario, volviendo al menu principal.')
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_o()
        return i
    admin_password=input('Ingrese su contraseña: ')
    if str(admin_password) == str(df['Password'][i]):
        print(f"usted ingreso como {admin_user}, bienvenido")
    else:
        print("Contraseña invalida, volviendo al menu principal.")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_o()


menu_o()
