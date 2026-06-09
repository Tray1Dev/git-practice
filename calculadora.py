#hacer calculadora asi que tenego que tener en cuenta que tipo de variables tengo que establecer.

historial = []

end ="si"

while True:
    menu = input("bienvenido a la calculadora \n \n salir,si/no:").lower() 
    if menu == end:
        break
    elif menu != end:
        numero = int(input("calculadora \n \n inserta un numero: "))
        
        numero2 = int(input("inserte otro numero:"))

        operacion = input("elige la operacion:\n\n(+=suma -=resta *=multiplicacion /=division)")

        if operacion == "+":
            resultado =(numero + numero2)
            historial.append(resultado)
            print(resultado,historial)
        elif operacion == "-":
            resultado =(numero - numero2)
            historial.append(resultado)
            print(resultado,historial)
        elif operacion == "*":
            resultado = (numero * numero2)
            historial.append(resultado)
            print (resultado,historial)
        elif operacion == "/":
            resultado = (numero / numero2)
            historial.append(resultado)
            print (resultado,historial)
        else:
            print("inserta caracteres validos")
    
    else:
        print("elige un caracter valido")

    
    
    
    
    
    



    