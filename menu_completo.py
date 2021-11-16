import csv
import os
import pandas #se debe descargar esta libreria con pip install pandas en la terminal
import time
from citizen import ciudadano
import new_world
import webbrowser
import random
from listadeCuidadanos import etlist
from administrador import administrator


class MainMenu:
    @staticmethod
    def menu_o():
        try:
            print ('Bienvenido a Eventlt')
            menu_login=int(input('1.Ingresar como Admin | 2.Ingresar como usuario | 3.Ingresar como sensor | ingresar cualquier otro numero para salir:'))

            if menu_login == 1:
                MainMenu.log_adm()

            elif menu_login == 2:
                MainMenu.menu_login_citizen()

            elif menu_login == 3:
                new_world.Mapa.show_map()
                go_back = int(input("1.Volver al menu | 2. Cerrar programa: "))
                if go_back ==1 :
                    MainMenu.menu_o()
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
############################################################################################################## menu secreto autistico
            elif menu_login == 69 or menu_login == 420:
                randnum = random.randint(1, 7)
                if randnum == 1:
                    webbrowser.open('https://www.youtube.com/watch?v=auVgp3HcYaY')
                elif randnum == 2:
                    webbrowser.open('https://www.youtube.com/watch?v=R0lqowYD_Tg')
                elif randnum == 3:
                    webbrowser.open('https://www.youtube.com/watch?v=FcZd305VI60')
                elif randnum == 4:
                    webbrowser.open('https://www.youtube.com/watch?v=AJ0E87EjU0A')
                elif randnum == 5:
                    webbrowser.open('https://www.youtube.com/watch?v=uKxyLmbOc0Q')
                elif randnum == 6:
                    webbrowser.open('https://www.youtube.com/watch?v=eaDeTV-LLYA')
                elif randnum == 7:
                    webbrowser.open('https://www.youtube.com/watch?v=DAlrY0iZKwQ')
                elif randnum == 8:
                    webbrowser.open('https://www.youtube.com/watch?v=OTwJ97Q6EzI')
                MainMenu.menu_o()

#######################################################################################################################################
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
        except ValueError:
            print ('Para salir del programa debe presionar un numero.')
            time.sleep(3)
            MainMenu.menu_o()

    @staticmethod
    def register():
        phone_number=input("Ingrese su numero telefonico: (+54) ")
        try:
            int(phone_number)
        except ValueError:
            print("Debe ingresar su numero telefonico correctamente")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            MainMenu.menu_login_citizen()
        user_cuil = input("Ingrese su CUIL: ")
        try:
            int(user_cuil)
        except ValueError:
            print("El CUIL debe ser un número")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            MainMenu.menu_login_citizen()

        df = pandas.read_csv(os.path.abspath("Database.csv"))
        for numbers in df['Phonenumber']:
            if str(numbers) == str(phone_number):
                print ("Ya hay un usuario registrado con este numero telefonico")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')

                MainMenu.menu_login_citizen()
        
        for CUILnumbers in df['CUIL']:
            if str(CUILnumbers) == str(user_cuil):
                print ("Ya hay un usuario registrado con este CUIL")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')

                MainMenu.menu_login_citizen()

        counter = len(str(user_cuil))

        counter2 = len(str(phone_number))

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

            MainMenu.menu_login_citizen()

        try:
            age =input("cual es tu edad: ")
            int(age)
        except ValueError:
            print("Usted ha ingresado un caracter invalido, intentelo nuevamente")


        if counter == 11 and password == password1 and counter2==11:
            with open(os.path.abspath("Database.csv"),mode="a",newline="") as h:
                writer=csv.writer(h,delimiter=",")
                writer.writerow([user_cuil,password,phone_number,name,surname,age])
            ciudadano.create_citizen(name,surname,age, user_cuil,phone_number)
            print(etlist.getcl())
            # print("Su clase citizen fue creada exitosamente")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            h.close()
            MainMenu.menu_login_citizen()
        elif counter != 11:
            print("Has ingresado el numero incorrecto de un CUIL.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            MainMenu.register()
        elif password != password1:
            print("Contraseña Incorrecta, intentelo denuevo.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            MainMenu.register()
        elif counter2 != 11:
            print("Cantidad de digitos de su numero telefonico es incorrecta.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            MainMenu.register()

    @staticmethod
    def login ():
        df = pandas.read_csv(os.path.abspath("Database.csv"))
        user_cuil=(input("Ingrese su CUIL: ")) 
        try:
            int(user_cuil)
        except ValueError:
            print("El CUIL debe ser un número")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            MainMenu.menu_login_citizen()
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

                MainMenu.menu_login_citizen()
                return i
        password = input("Ingrese su contraseña: ")
        if str(password) == str(df['Password'][i]):
            print("Bienvenido a Eventlt.\n\n")
            MainMenu.menu_citizen(i) #<---- esto linkea al menu de las acciones del ciudadano
        else:
            print("Contraseña invalida.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            MainMenu.menu_login_citizen()

    @staticmethod
    def menu_login_citizen():
        print ("Porfavor, seleccione una de las siguentes opciones")
        try:
            user=int(input("1.Log in | 2. Registrarse | 3.Salir : "))
        except ValueError:
            print('eso no es un numero, intentelo nuevamente')
            MainMenu.menu_login_citizen()
        if user == 1:
            MainMenu.login()
        elif user==2:
            MainMenu.register()
        elif user==3:
            MainMenu.menu_o()
        else:
            print ("Debes ingresar los numeros indicados anteriormente.")
            MainMenu.menu_login_citizen()
    @staticmethod
    def menu_citizen(citizenidentifier):
        df = pandas.read_csv(os.path.abspath("Database.csv"))
        seconddf = pandas.read_csv(os.path.abspath("Eventos.csv"))
        for a in etlist.citizenlist:
            if int(df['CUIL'][citizenidentifier]) == int(a.CUIL):
                x = a
        if x.zone == -1:
            b = int(input(f'bienvenido al menu_citizen por primera vez, {x.name}!\n\nPorfavor, ingrese el numero respectivo a su zona:\n{registroDeZonas.listadoZonas(seconddf)}')) # SOLO PUEDE SER UN NUMERO
            if b > (len(seconddf['Nombre']) - 1):
                print('este numero no es valido, vuelva a intentarlo')
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                MainMenu.menu_citizen(citizenidentifier)
            else:
                print('muchas gracias!')
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
            x.zone = b
        try:
            c = int(input(f'{x.name}, elija lo que quiere hacer:\n\n1.asistir a evento | 2.dejar de asistir a evento | 3.menu de amigos | 4.cambiar zona: ')) # SOLO PUEDE SER UN NUMERO
        except ValueError:
            print ('Debe ingresar un numero')
            time.sleep(3)
            os.system('cls' if os.name== 'nt' else 'clear')
            MainMenu.menu_o()
        if c == 1:
            pass
        elif c == 2:
            pass
        elif c == 3:
            pass
        elif c == 4:
            pass
        
    @staticmethod
    def log_adm ():
        df = pandas.read_csv(os.path.abspath("Base_Adm.csv")) #va el path csv de administradores
        admin_user=input("Ingrese su nombre de usuario como admnistrador: ")
        admin_serch = 0
        for a in df['Admin_user']:
            if str(admin_user) == str(a):
                break
            admin_serch += 1
        if admin_serch == len(df["Admin_user"]):
            print('su nombre no esta como usuario, volviendo al menu principal.')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            MainMenu.menu_o()
            return admin_serch
        admin_password=input('Ingrese su contraseña: ')
        if str(admin_password) == str(df['Password'][admin_serch]):
            print(f"Usted ingreso como {admin_user}, bienvenido.")
            menu_administrador.Bienvenido()
        else:
            print("Contraseña invalida, volviendo al menu principal.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            MainMenu.menu_o()

class menu_administrador():
    @staticmethod
    def Bienvenido():
        choice = int(
            input("Elija una de las siguientes opciones:1-Volver al menu principal| 2-Bannear| 3-remover Ban:"))
        if choice == 1:
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            MainMenu.menu_o()
        if choice == 2:
            return menu_administrador.BanCitizen()
        if choice == 3:
            return menu_administrador.UnBanCitizen()

    @staticmethod
    def BanCitizen():
        usuarioseleccionado = str(input("A quien desea bannear?"))
        for usuarios in etlist.citizenlist:
            if usuarios.name == usuarioseleccionado and usuarios.citizenBan == False:
                administrator.banCitizen(usuarios)
                print(f"{usuarioseleccionado} fue banneado")
                return menu_administrador.Bienvenido()
        print("Usuario no encontrado")
        return menu_administrador.Bienvenido()

    @staticmethod
    def UnBanCitizen():
        usuarioseleccionado = str(input("A quien desea remover el ban?"))
        for users in etlist.BannedCitizenList:
            if users.name == usuarioseleccionado:
                administrator.unbanCitizen(users)
                print(f"se removio el ban de {usuarioseleccionado}")
                return menu_administrador.Bienvenido()
        print("Usuario no encontrado")
        return menu_administrador.Bienvenido()

def friends_menu(self):
    pass

class registroDeZonas:

    @staticmethod
    def listadoZonas(eventos):  
        zonitas = ''
        i = 0 
        for zona in eventos['Nombre']:
            zonitas += f'{i} |' + zona + '\n'
            i += 1
        return zonitas
