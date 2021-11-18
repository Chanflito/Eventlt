import csv
import os
import pandas #se debe descargar esta libreria con pip install pandas en la terminal
import time
from citizen import ciudadano
# from listaDeEventos import eventos
import new_world
from listadeCuidadanos import etlist
from administrador import administrator
from revisionlist import defualt_revision_list

class MainMenu:
    @staticmethod
    def menu_o():
        
        seconddf = pandas.read_csv(os.path.abspath("zona.csv"))
        try:
            print ('Bienvenido a Eventlt')
            menu_login=int(input('1.Ingresar como Admin | 2.Ingresar como usuario | 3.Ingresar como sensor | ingresar cualquier otro numero para salir:'))

            if menu_login == 1:
                MainMenu.log_adm()

            elif menu_login == 2:
                MainMenu.menu_login_citizen()

            elif menu_login == 3:
                print('Zonas disponibles: ')
                print(registroDeZonas.listadoZonas(seconddf))
                num = int(input("Elija su zona: "))
                if num <= len(seconddf['Nombre']):
                    new_world.Mapa.show_map(seconddf['Latitud'][num],seconddf['Longitud'][num])
                    os.system('cls' if os.name == 'nt' else 'clear')
                    MainMenu.menu_o()
                else:
                    print('numero invalido')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    MainMenu.menu_o()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
        except ValueError:
            print ('Para salir del programa debe presionar un numero.')
            time.sleep(3)
            MainMenu.menu_o()

    @staticmethod
    def register():
        seconddf = pandas.read_csv(os.path.abspath("zona.csv"))
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
        print('en que zona esta?')
        print(registroDeZonas.listadoZonas(seconddf))
        zona_user = int(input('respuesta: '))
        if zona_user > (len(seconddf['Nombre']) - 1):
            print('este numero no es valido')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            return MainMenu.menu_o

        if counter == 11 and password == password1 and counter2==11:
            with open(os.path.abspath("Database.csv"),mode="a",newline="") as h:
                writer=csv.writer(h,delimiter=",")
                writer.writerow([user_cuil,password,phone_number,name,surname,age,zona_user])
            ciudadano.create_citizen(name,surname,age, user_cuil,phone_number,zona_user)
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
        seconddf = pandas.read_csv(os.path.abspath("zona.csv"))
        for a in etlist.citizenlist:
            if int(df['CUIL'][citizenidentifier]) == int(a.CUIL):
                ciudadanos = a
        if ciudadanos.citizenBan == True:    # si la cuenta esta baneada no pasa
            print('su cuenta esta bloqueada, no puede ingresar')
            return MainMenu.menu_o
        try:
            c = int(input(f'{ciudadanos.name}, elija lo que quiere hacer:\n\n1.asistir a evento | 2.dejar de asistir a evento | 3.menu de amigos | 4.cambiar zona: ')) # SOLO PUEDE SER UN NUMERO
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
            menu_amigos.friends_menu(citizenidentifier)
        elif c == 4:
            registroDeZonas.listadoZonas(seconddf)
            print(registroDeZonas.listadoZonas(seconddf))
            num = int(input("a que zona quiere cambiar?\n"))
            ciudadanos.change_zone(num)
            print('su zona se actualizo correctamente')
            MainMenu.menu_citizen(citizenidentifier)
        else:
            return MainMenu.menu_o()
        
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
    revisionlist=[]

    @staticmethod
    def Bienvenido():
        choice = int(input("Elija una de las siguientes opciones:1-agregar evento| 2-Bannear| 3-remover Ban| 4-Ver lista de revisión: "))
        if choice == 1:
            zona = input('dime la zona del evento: ')
            nombre = input('titulo de evento: ')
            descripcion = input('descripcion del evento: ')
            latitud = input('latitud: ')
            longitud = input('longitud: ')
            administrator.addEvent(zona, nombre, descripcion, latitud, longitud )
            return menu_administrador.Bienvenido()
        elif choice == 2:
            return menu_administrador.BanCitizen()
        elif choice == 3:
            return menu_administrador.UnBanCitizen()
        elif choice == 4:
            defualt_revision_list.update_revision_list()
            return menu_administrador.check_revisionList()
        else:
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            MainMenu.menu_o()

    @staticmethod
    def check_revisionList():
        print(defualt_revision_list.getlist())
        citizenindex=int(input("seleccione la posicion del ciudadano al que quiere revisar (empezando desde el 0): "))
        ban_choice = str(input("Quiere remover el ban del citizen? si/no: "))
        chosen_citizen=defualt_revision_list.revision_list[citizenindex]
        if ban_choice=="si":
            administrator.unbanCitizen(chosen_citizen)
            print("El usuario fue des-banneado")
            return menu_administrador.Bienvenido()
        else:
            defualt_revision_list.removecitizen(chosen_citizen)
            chosen_citizen.quien_me_rechazo=[]
            print("El ciudadano fue removido de la lista de revision y automaticamente fue baneado")
            return menu_administrador.Bienvenido()

    @staticmethod
    def BanCitizen():
        usuarioseleccionado = int(input("A quien desea bannear? "))
        for usuarios in etlist.citizenlist:
            if usuarios.CUIL == usuarioseleccionado and usuarios.citizenBan == False:
                administrator.banCitizen(usuarios)
                print(f"el usuario con CUIL {usuarioseleccionado} fue banneado")
                return menu_administrador.Bienvenido()
        print("Usuario no encontrado")
        return menu_administrador.Bienvenido()

    @staticmethod
    def UnBanCitizen():
        usuarioseleccionado = int(input("A quien desea remover el ban? CUIL: "))
        for users in etlist.BannedCitizenList:
            if users.CUIL == usuarioseleccionado:
                administrator.unbanCitizen(users)
                print(f"se removio el ban de la persona con el CUIL: {usuarioseleccionado}")
                return menu_administrador.Bienvenido()
        print("Usuario no encontrado")
        return menu_administrador.Bienvenido()

    @classmethod
    def update_revision_list(cls):
        for citizen in etlist.citizenlist:
            if len(citizen.quien_me_rechazo)==5:
                cls.revisionlist.append(citizen)
                administrator.banCitizen(citizen)


class menu_amigos:

    @staticmethod
    def friends_menu(user):
        df = pandas.read_csv(os.path.abspath("Database.csv"))
        for ciudadanos in etlist.citizenlist:
            if int(df['CUIL'][user]) == int(ciudadanos.CUIL):
                x = ciudadanos
        menu_choice = int(input(f"{x.name}, bienvenido a sus contactos:\n\n1.Ver solicitudes | 2.Enviar solicitud | 3.Ver contactos | Volver menu"))
        if menu_choice == 1:
            print(x.ver_solicitudes())
            acciones_disponibles = int(input('1.Aceptar una solicitud | 2.Rechazar una solicitud '))
            if acciones_disponibles == 1:
                solicitud_choice = input('dime el numero de el que quieres agregar: ')
                print(x.aceptar_solicitud(solicitud_choice))
                return menu_amigos.friends_menu(user)
            elif acciones_disponibles == 2:
                solicitud_choice = input('dime el numero de el que quieres rechazar: ')
                print(x.aceptar_solicitud(solicitud_choice))
                return menu_amigos.friends_menu(user)
            else:
                return menu_amigos.friends_menu(user)
        elif menu_choice == 2:
            friend_cuil = int(input("dime el cuil de tu amigo"))
            print(x.enviar_solicitud(friend_cuil))
            return menu_amigos.friends_menu(user)
        elif menu_choice == 3:
            if len(x.friends) == 0:
                print('usted no tiene amigos')
                return menu_amigos.friends_menu(user)
            for friend in x.friends:
                print(f"{friend.name} {friend.lastName} | {friend.CUIL}")
            return menu_amigos.friends_menu(user)
        else:
            MainMenu.menu_citizen(user)

class registroDeZonas:

    @staticmethod
    def listadoZonas(eventos):  
        zonitas = ''
        i = 0 
        for zona in eventos['Nombre']:
            zonitas += f'{i} |' + zona + '\n'
            i += 1
        return zonitas
