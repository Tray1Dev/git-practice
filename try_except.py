#variables
si="si"
no="no"
mate="mate"
cod="cod"
#diccionario
tablero={
    "codigo":[] ,
    "matematica":[] ,
    "horas":[]
}
#funciones
def verror ():
    try:
        horas=int(input("cuantas horas estudiaste hoy?:"))
        if horas == 0:
            print("tiempo de estudio valido desde 1 hora.")
            return False
        else:
            tablero["horas"].append(horas)
            return True
    except ValueError:
        print("ingrese solo numeros")
        return False    
def datos ():
    d=input("que estuidiaste hoy?(mate/cod):")
    if d == cod:
        tab =input("que tema?:")
        tablero["codigo"].append(tab) 
        print(tablero)
    elif d == mate:
        tab =input("que tema?:")
        tablero["matematica"].append(tab)
        print(tablero)
    else:
        print("seleciona'mate'o'cod'")
        return
while True:
    
    menu = input("bienvenido a el tablero,quiere continuar?(si/no):")
    if menu == si:
        if verror() == False:
            continue
        else:
            datos()   
    elif menu == no:
        print("gracias por usar el tablero")
        break
    else:
        print("caracter no valido")

#ahora tengo que encontrar la manera de que se puedan vincular directamente las horas con los teemas por que no se va a saber especificamente de que tema se estudia.


        










    