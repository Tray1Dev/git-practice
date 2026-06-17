#elemine todos los json, quiero entender mejor como se manejan los datos.


#1 las listas [], sirven para ordenar datos de manera rigida secuenciada, osea que si tienen un orden

numeros = [1,2,3,4,5]
numeros.append(0) #append sirve para agregar un dato, lo hace en el final de la lista siempre 
numeros.insert(3,"holaaa") #insert modifica justo en la posicion que se le indique,
numeros.pop()#pop acomoda los datos, si no se le pone nada quita el ultimo de los datos, es lo inverso al append
#print(numeros)


#diccionarios {} tiene el metodo para almacenar llaves con sus valores, no tienen un orden, asi que no se pueden agregar, solo busca y modifica

diccionario ={
    "palabra":"hola",
    "significado":"saludar"
}

diccionario["palabra"]=input("ingrese una palabra:") #se llama a el diccionario en un corchete la llave que quiere acceder para asi cambiar su valor, no es acumulable solo lo reemplaza
print(diccionario)
diccionario["significado"]=input("ingrese una palabra:")
print(diccionario)
print(diccionario.keys())#muestra solo las llaves del diccionario seleccionado 
print(diccionario.values())#muestra solo los valores del diccionario seleccionado

#tuple, es la primera vez que las veo, son datos de una manera como la lista pero que su diferencia se centra en que los datos dentro de ella no se pueden cambiar

ley = ("infinito",1,2,3)
print(ley.count())
