
#para practicar un poco de todo lo que he visto, fuera de la calculadora, un programa que le muestre las horas que haga de codigop y matematica para que asi me  muestre el acumulado y los temas que he visto en esos intervalos.


## tener en cuenta que puedo usar,diccionarios, listas funciones, bucles, dare como.

## he elegido los diccionarios como metodo para hacer este sistema asi, usemos un solo diccionario. como prueba antes de este programa 
#para actualizar update(<obj>)
diccionario = {
    "nombres":"owen",
    "edad": "21",
    "libros":"sofia"
}


ver = input("ver diccionario:")
while True:
    if ver== "si":
        print(diccionario)
    elif ver == "no":
        print("gracias por ver el diccionario")
        break
        agrd = input("cambiar algun valor?:")
        if agrd == "si":
            key=input("nombre,edad,libros?")
            if key == "libros":
                diccionario["libros"] = input(":")
                print(diccionario["libros"])


## la cuestion ahora es juntar esto con una funcion para que sea mucho mas facil.


    