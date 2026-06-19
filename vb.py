baseDeDatos={
    "usuarios":[
        {
            "id": 0,
            "nombre":"creador",
            "email":"cr@gmail.com",
            "contra":"0304",
            "roles":["ceo"]
        },
        {
            "id": 1,
            "nombre":"1delegado",
            "email":"dl@gmail.com",
            "contra":"0203",
            "roles":["admin"]  
        }
    ]
}
print(baseDeDatos["usuarios"][0][2])