archivo = open("nota.txt", "r")

contenido = archivo.read()

print(contenido)

archivo.close()

palabras = contenido.split()
print(palabras)