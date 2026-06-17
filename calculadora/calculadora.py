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
si = "si"
no = "no"
while True:
    menu = input("bienvenido a la calculadora,quiere continuar?(si/no):")
    if menu == si:
        operacion()
    elif menu == no:
        print("gracias por usar la calculadora")
        break
    else:
        print("caracter no valido")
#que felicidad como simplifique el codigo :)


    