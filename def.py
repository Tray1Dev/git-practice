#definir funciones y entenderlas realmente como son y que despenian 
    
#entendamos que una funcion compone todo el codigo de el lenguaje escrito adentro de si, es decir, cualquier secunecia cualquer variable puede estar adentro de una funcion.

#creare una funcion que apartir de ciertos nombres que se indique en la consola, los muestre en el mismo orden de mencion en una lista
datos = []
def ponerDatos (datos):
    mensaje = input("hola que datos quieres listar:")
    datos.append(mensaje)
    print(datos)
    return mensaje #la funcion ya queda creada, no se usa hasta que sea llamada, abajo se combina con un bucle .
def borrarDatos (datos):
    mensaje1 = input("quieres borrar los datos?:")
    datos.clear
    print (datos)
    return mensaje1
while True:
    ponerDatos(datos)
    borrarDatos(datos)
    
    


    