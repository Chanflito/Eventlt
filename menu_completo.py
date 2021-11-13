import csv
import os
import pandas #se debe descargar esta libreria con pip install pandas en la terminal
import time
from citizen import ciudadano
from listadeCuidadanos import etlist
import new_world


def menu_o():
    print ('Bienvenido a Eventlt')
    menu_login=int(input('1.Ingresar como Admin | 2.Ingresar como usuario | 3.Ingresar como sensor | ingresar cualquier otro numero para salir:'))

    if menu_login == 1:
        log_adm()

    elif menu_login == 2:
        menu_login_citizen()

    elif menu_login == 3:
        new_world.Mapa.show_map()
        volver=int(input("1.Volver al menu | 2. Cerrar programa: "))
        if volver==1:
            menu_o()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

def register():
    phonenumber=input("Ingrese su numero telefonico: (+54) ")
    try:
        int(phonenumber)
    except ValueError:
        print("Debe ingresar su numero telefonico correctamente")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

        menu_login_citizen()
    user_cuil = input("Ingrese su CUIL: ")
    try:
        int(user_cuil)
    except ValueError:
        print("El CUIL debe ser un número")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

        menu_login_citizen()

    df = pandas.read_csv(os.path.abspath("Database.csv"))
    for i in df['Phonenumber']:
        if str(i) == str(phonenumber):
            print ("Ya hay un usuario registrado con este numero telefonico")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            menu_login_citizen()
    
    for i in df['CUIL']:
        if str(i) == str(user_cuil):
            print ("Ya hay un usuario registrado con este CUIL")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            menu_login_citizen()

    counter = len(str(user_cuil))

    counter2 = len(str(phonenumber))

    password = input("Ingrese su contraseña,porfavor: ")

    password1 = input("Confirme su contraseña,nuevamente: ")

    name = input('Ingrese su nombre: ')

    surname = input('Ingrese su apellido: ')

    try:
        if str(name).isdigit() == True or str(surname).isdigit() == True:
            raise ValueError()
    except ValueError:
        print ('Ingresaste numeros en tu nombre o apellido, intentelo denuevo')
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

        menu_login_citizen()

    try:
        age =input("cual es tu edad: ")
        int(age)
    except ValueError:
        print("Usted ha ingresado un caracter invalido, intentelo nuevamente")


    if counter == 11 and password == password1 and counter2==11:
        with open(os.path.abspath("Database.csv"),mode="a",newline="") as h:
            writer=csv.writer(h,delimiter=",")
            writer.writerow([user_cuil,password,phonenumber,name,surname,age])
        ciudadano.create_citizen(name,surname,age, user_cuil,phonenumber)
        print(etlist.getcl())
        print("Su clase citizen fue creada exitosamente")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

        h.close()
        menu_login_citizen()    
    elif counter != 11:
        print("Has ingresado el numero incorrecto de un CUIL.")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

        register()
    elif password != password1:
        print("Contraseña Incorrecta, intentelo denuevo.")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

        register()
    elif counter2 != 11:
        print("Cantidad de digitos de su numero telefonico es incorrecta.")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

        register()

def login():
    df = pandas.read_csv(os.path.abspath("Database.csv"))
    user_cuil=(input("Ingrese su CUIL: ")) 
    try:
        int(user_cuil)
    except ValueError:
        print("El CUIL debe ser un número")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

        menu_login_citizen()
    user_cuil=int(user_cuil)
    i = 0
    for a in df['CUIL']:
        if str(user_cuil) == str(a):
            break
        i += 1
        if i ==len(df["CUIL"]):
            print('Su CUIL no fue encontrado')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            menu_login_citizen()
            return i
    password = input("Ingrese su contraseña: ")
    if str(password) == str(df['Password'][i]):
        print("Bienvenido a Eventlt.\n\n")
        menu_citizen(i) #<---- esto linkea al menu de las acciones del ciudadano
    else:
        print("Contraseña invalida.")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

        menu_login_citizen()

def menu_login_citizen():
    print ("Porfavor, seleccione una de las siguentes opciones")
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

def listadoZonas(eventos):
    
    zonitas = ''
    i = 0 
    for zona in eventos['Nombre']:
        zonitas += f'{i} |' + zona + '\n'
        i += 1
    return zonitas

def menu_citizen(i):
    df = pandas.read_csv(os.path.abspath("Database.csv"))
    seconddf = pandas.read_csv(os.path.abspath("Eventos.csv"))
    for a in etlist.citizenlist:
        if int(df['CUIL'][i]) == int(a.CUIL):
            x = a
    if x.zone == -1:
        b = int(input(f'bienvenido al menu_citizen por primera vez, {x.name}!\n\nPorfavor, ingrese el numero respectivo a su zona:\n{listadoZonas(seconddf)}')) # SOLO PUEDE SER UN NUMERO
        if b > (len(seconddf['Nombre']) - 1):
            print('este numero no es valido, vuelva a intentarlo')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            menu_citizen(i)
        else:
            print('muchas gracias!')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
        x.zone = b
    c = int(input(f'{x.name}, elija lo que quiere hacer:\n\n1.asistir a evento | 2.dejar de asistir a evento | 3.menu de amigos')) # SOLO PUEDE SER UN NUMERO


def log_adm():
    df = pandas.read_csv(os.path.abspath("Base_Adm.csv")) #va el path csv de administradores
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
        print(f"Usted ingreso como {admin_user}, bienvenido.")
    else:
        print("Contraseña invalida, volviendo al menu principal.")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_o()

def menu_administrador():
    pass

def friends_menu():
    pass

menu_o()
