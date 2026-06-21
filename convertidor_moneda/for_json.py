import json

empresa = {
    "usuarios":[
        {
            "id":0,
            "nombre":"owen",
            "correo":"owen@gmail.com",
            "contrasena":12345,
            "cargo":["ceo"]
        },
        {
            "id":1,
            "nombre":"jhonatan",
            "correo":"jhon@gmail.com",
            "contrasena":54321,
            "cargo":["monitor"]
        },
        {
            "id":2,
            "nombre":"diana",
            "correo":"diana@gmail.com",
            "contrasena":23344,
            "cargo":["disenadora"]
        },
        {
            "id":3,
            "nombre":"allan",
            "correo":"allan@gmail.com",
            "contrasena":98765,
            "cargo":["publicista"]
        }
    ],
    "lugares":[
        {
            "sede principal":"centro",
            "sede secundaria":"sur",
            "acceso":0
        }
    ]   
}
def pedirDatos ():
    correo = input("cual es su correo:")
    try:
        contrasena = int(input("cual es su contrasena:"))
    except:
        UnboundLocalError
        print("solo numeros")
    return correo,contrasena 
  
def verificarDatos(correo,contrasena):
    encontrado=False
    for correos in empresa["usuarios"]:
        if correo == correos["correo"] and contrasena == correos["contrasena"]:
            encontrado=True
            print("bienvenido")
    if not encontrado:
        print("error") 
        return
        
correo,contrasena = pedirDatos() 

verificarDatos(correo,contrasena)

    