#hoy aprendi a usar for asi que vamos a ver si si me quedo en el cerebro la informacion 
#variales menu
op1=1
op2=2
op3=3
coleccion ={
    "juegos":[
        {
            "nombre":"fortnite",
            "tipo":"shooter",
            "calificacion":0
        },
        {
            "nombre":"liga de leyendas",
            "tipo":"moba",
            "calificacion":0,
        },
        {
            "nombre":"liga de leyendas",
            "tipo":"moba",
            "calificacion":0,
        }
    ],
    "musica":[
        {
            "genero":"grunge",
            "artista":"kurt",
            "cancion":"smell like shit"    
        },
        {
            "genero":"pop",
            "artista":"mgmt",
            "cancion":"little dark age"    
        },
        {
            "genero":"black metal",
            "artista":"summoning",
            "cancion":"morthond"    
        },
        {
            "genero":"clasica",
            "artista":"bach",
            "cancion":"chelo suite 01"    
        }
    ]
}
#la idea es hacer un pequeno menu que permita ingresar y ver tu coleccion, al verla elgies los datos y agregas algo

while True:

    print("bienvenido a la coleccion personal:)")
    print(coleccion)
    menu = int(input("te gustaria agregar algo a juegos(1) a musica(2) o salir(3) "))
    if menu == op1:
        print(coleccion["juegos"])
        nJuego=input("nombre del juego: ")
        nTipo=input("tipo del juego: ")
        nCali=int(input("calificacion del juego 0-10: "))
        coleccion["juegos"].append({"nombre":nJuego,"tipo":nTipo,"calificacion":nCali})
        print(coleccion["juegos"])



    break