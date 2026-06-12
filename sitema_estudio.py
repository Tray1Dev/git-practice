#voy a hacer un tablero digital, para tener un mejor control de mi flujo de estudio,con esto practico el nuevo concepto que estoy aprendiendo que son los diccionarios.
sistema_de_estudio = {
    "codigo": [],
    "matematica":[]
    
}
while True:
    print("bienvenido al tablero de estudio digital",sistema_de_estudio)
    salir = "si"
    seguir = "no"

    s = input("salir? (si/no):").lower()
    if s == salir:
        print("gracias por usar el tablero digital :)")
        break
    elif s == seguir:
        pass
    else:
        print("caracteres no validos")
        continue
    m = "mate"
    c = "codigo"

    p = input("estudiaste mate o codigo?:")
    
    if p == m:
        print("que estudiaste en mate y cuantas horas?")
        sistema_de_estudio["matematica"].append(input()) 
        
    elif p == c:
        print("que estudiaste en codigo y cuantas horas?")
        sistema_de_estudio["codigo"].append(input())
    else:
        print("caracteres no validos")

#estoy mas orgulloso de este resultado ya quedo mejor, tiene menos posibles errores.
#     
