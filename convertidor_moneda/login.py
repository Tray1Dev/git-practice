#importar el json
import json
#crear variables para menu
 
incioSesion = "1"
salir = "2"
crear = "3"
#variables que puedan buscar el perfil dentro del json 
perfiles={
    "nombre":"owen",
    "saldo": [300]
}
contrasenia={
    "contra":"0304"
}

def baseDatos():
    d=input("esta seguro que quiere crear la base de datos\n\n\n si(1) no(2)")
    if d == incioSesion:
        pw=input("ingrese la contrasenia:")
        if pw == contrasenia["contra"]:
            print("orden consedida")
            with open("base de datos/convertidor_moneda""w")as base:
                json.dump(base)
        else:
            print("orden denegada")
    elif d == salir:
        menuBanco()
        return
def agregarSaldo ():
    
    print(perfiles["saldo"])
    t=input("desesa agregar dinero al saldo total(1)\nvolver al banco(2)")
    if t == incioSesion:
        perfiles["saldo"].append(input(""))
        print(perfiles["saldo"])
        menuBanco()
    elif t == salir:
        menuBanco()
        return False
    else:
        print("caracteres no validos,recuerde (1)(2)")
        return False


def menuBanco ():
    mb=input("ahora que quiere hacer?\n mirar saldo (1)\n volver(2)\n crear base de datos para que mas personas puedan entrar?....(3)")
    if mb == incioSesion:
        agregarSaldo()
        return True
    elif mb == salir:
        sesion()
        return
    elif mb == crear:
        baseDatos()
        return

def sesion ():
    b=input("ingresar al banco(1)::\n salir(2):\n inserte una opcion:")
    if b == incioSesion:
        n=input("cual es su nombre:")
        if n == perfiles["nombre"]:
            print("bienvenido de nuevo creador")
            menuBanco()
        else:
            print("usuario incorrecto")
    elif b == salir:
        menu()
        return
#def validar ():
    #try:
        #menu
    #except:
def menu():        
    while True:
        menu = str(input("banco de intercambio\n""inicio de sesion(1):\n""salir(2):\n""inserte una opcion:"))
        if menu == incioSesion:
            sesion()
        elif menu == salir:
            print("gracias por creer en mi dios")
            break
        else:
            print("caracteres invalidos.\n recuerde inicio sesion(1)   salir(2)")
        

menu()

