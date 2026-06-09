historial = []
end = "si"
run = "no"

while True:
    menu = input("Bienvenido a la calculadora \n \n¿Salir? (si/no): ").lower() 
    
    if menu == end:
        print("Gracias por usar la calculadora. Historial final:", historial)
        break
        
    elif menu == run:  
        numero = int(input("\nInserta un numero: "))
        numero2 = int(input("Inserte otro numero: "))
        operacion = input("Elige la operacion (+, -, *, /): ")

        if operacion == "+":
            resultado = numero + numero2
        elif operacion == "-":
            resultado = numero - numero2
        elif operacion == "*":
            resultado = numero * numero2
        elif operacion == "/":
            resultado = numero / numero2
        else:
            print("Operación no válida.")
            continue # Salta al inicio del while sin guardar nada

        historial.append(resultado)
        print(f"Resultado: {resultado} | Historial: {historial}\n")
        
    else: 
        print("Por favor, introduce una opción válida ('si' o 'no').\n")
    
    
    
    
    
    



    