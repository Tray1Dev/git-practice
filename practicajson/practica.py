import json

perfil={
    "nombre":[],
    "correo":"ow@gmail.com",
    "contrsenia":12345
}
add=input("agrega un numbre a el diccionario:")

perfil["nombre"].append(add)
with open("practica.json","w")as archivo:
    json.dump(perfil,archivo)


