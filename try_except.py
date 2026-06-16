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
        horas=int(input("cuantas horas?:"))
        tablero["horas"].append(horas)
    except ValueError:
        print("ingrese solo numeros")
        return
def datos ():
    d=input("que estuidiaste hoy?(mate/cod):")
    if d == cod:
        tab =input("que tema?:")
        tablero["codigo"].append(tab) #corregir el fallo de la misma manera que, con las horas, crear variable para almacenar en la lista del diccionario
        verror()
        print(tablero)
    elif d == mate:
        tab =input("que tema?:")
        tablero["matematica"].append(tab)
        verror()
        print(tablero)
    else:
        print("seleciona'mate'o'cod'")
        return
while True:
    menu = input("bienvenido a el tablero,quiere continuar?(si/no):")
    if menu == si:
        datos()
    elif menu == no:
        print("gracias por usar el tablero")
        break
    else:
        print("caracter no valido")

#para hoy tenia pendiente arreglar unos detalles, con los append, ya que solo la lista de los numeros es la unica que se queda

        










    