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

correo = input("cual es su correo:")
for correos in empresa["usuarios"]:
    if correo == correos["correo"]:
        print(correos["contrasena"])
        contrasena = int(input("cual es su contrasena:"))    
        if contrasena == correos["contrasena"]:
            print("bienvenido de nuevo")
        else:
            print("contrasena incorrecta")

    