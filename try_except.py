
#practica de try/except'


















#pracitca de funciones de nuevo :P
historial = []
def operacion ():
    try:
        n1= int(input("ingrese numero:"))
        n2=int(input("ingrese otro numero:"))
    except ValueError:
        print("ingresa solo numeros")
        return
    op= input("que operacion desea hacer?(*,/,+/-):")
    if op == "+":
        resultado = n1 + n2
        print (resultado)
    elif op == "-":
        resultado = n1 - n2
        print (resultado)
    elif op == "*":
        resultado = n1 * n2
        print (resultado)
    elif op == "/":
        try:
            resultado = n1 / n2
            print(resultado)
        except ZeroDivisionError:
            print("no es divisible el 0")
            return
    else:
        print("operacion no valida")
        return
    historial.append(resultado)
    print(f"Resultado: {resultado} | Historial: {historial}\n")
    return resultado


operacion()




        










    