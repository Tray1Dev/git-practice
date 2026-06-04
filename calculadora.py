#hacer calculadora asi que tenego que tener en cuenta que tipo de variables tengo que establecer.


while True:
    numero = int(input("calculadora \n \n inserta un numero: "))
        
    numero2 = int(input("inserte otro numero:"))

    operacion = input("elige la operacion:\n\n(+=suma -=resta *=multiplicacion /=division)")

    if operacion == "+":
        resultado =(numero + numero2)
        print (resultado)
    elif operacion == "-":
        resultado2 =(numero - numero2)
        print(resultado2)
    elif operacion == "*":
        resultado3 = (numero * numero2)
        print (resultado3)
    elif operacion == "/":
        resultado4 = (numero * numero2)
        print (resultado4)
    else:
        print("inserta caracteres validos, gracias")    
    #bucle extra para ver los ultimos resultados, creo que tengo que hacerla con alguna lista o diccionario<p>
    bucle1 = input("quieres seguir,salir del menu o ver los ultimos resultados\n\n1 para salir\n2 para seguir\n3 para ver ultimos resultados")

    if bucle1 == 1:
        False
    elif bucle1 == 3:
        print(resultado,resultado2,resultado3,resultado4)
    else:
        pass 

    