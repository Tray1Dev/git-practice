#voy a hacer un tablero digital, para tener un mejor control de mi flujo de estudio,con esto practico el nuevo concepto que estoy aprendiendo que son los diccionarios.
sistema_de_estudio = {
    "codigo": [],
    "matematica":[]
    
}
while True:
    print("bienvenido al tablero de estudio digital",sistema_de_estudio)

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

    
# obtuvo forma, ahora quiero darl algo mas de complejidad, pero me gusta :)

# voy a darle mas complejidad entre dias y horas para ser mas especifica, ya no es un diccionario de solo el sistema de estudio si no que ese sea el menu, los diccionarios son solo dos, ya que asi puedo acceder a los dias 
