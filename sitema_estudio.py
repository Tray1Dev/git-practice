#voy a hacer un tablero digital, para tener un mejor control de mi flujo de estudio,con esto practico el nuevo concepto que estoy aprendiendo que son los diccionarios.
sistema_de_estudio = {
    "codigo": "",
    "matematica":""
}
while True:
    print("bienvenido al tablero de estudio digital",sistema_de_estudio)

    m = "mate"
    c = "codigo"

    p = input("estudiaste mate o codigo?:")
    if p == m:
        print("que estudiaste en mate y cuantas horas?")
        sistema_de_estudio["matematica"] = input()
    elif p == c:
        print("que estudiaste en codigo y cuantas horas?")
        sistema_de_estudio["codigo"] = input()
    else:
        print("caracteres no validos")

    
# obtuvo forma, ahora quiero darl algo mas de complejidad, pero me gusta :)


