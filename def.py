


def calculadora ():
    historial = []
    end = "si"
    run = "no"
    def suma ():
        numero = int(input("insterte un numero:"))
        numero2 = int(input("insterte otro numero:"))
        resultado = numero + numero2
        print(resultado)
        historial.append(resultado)
        print(f"Resultado: {resultado} | Historial: {historial}\n")

        ## suma()
    def resta ():
        numero = int(input("insterte un numero:"))
        numero2 = int(input("insterte un numero:"))
        resultado = numero - numero2
        print(resultado)
        historial.append(resultado)
        print(f"Resultado: {resultado} | Historial: {historial}\n")

    ## resta ()
    def multiplicacion ():
        numero = int(input("insterte un numero:"))
        numero2 = int(input("insterte un numero:"))
        resultado = numero * numero2
        print(resultado)
        historial.append(resultado)
        print(f"Resultado: {resultado} | Historial: {historial}\n")

## multiplicacion ()
    def division ():
        numero = int(input("insterte un numero:"))
        numero2 = int(input("insterte un numero:"))
        resultado = numero / numero2
        print(resultado)
        historial.append(resultado)
        print(f"Resultado: {resultado} | Historial: {historial}\n")

## division ()
    while True:
        menu = input("Bienvenido a la calculadora \n \n¿Salir? (si/no): ").lower() 
    
        if menu == end:
            print("Gracias por usar la calculadora. Historial final:", historial)
            break
        
        elif menu == run:  
        
            operacion = input("Elige la operacion (+, -, *, /): ")

            if operacion == "+":
                suma()
            elif operacion == "-":
                resta()
            elif operacion == "*":
             multiplicacion()
            elif operacion == "/":
                division()
            else:
                print("Operación no válida.")
                continue # Salta al inicio del while sin guardar nada       
    else: 
        print("Por favor, introduce una opción válida ('si' o 'no').\n")


var1 = input("correr calculadora? si?")

if var1 == "si":
    calculadora()
else:
    print("pronto mas aplicaciones.....")




    

    