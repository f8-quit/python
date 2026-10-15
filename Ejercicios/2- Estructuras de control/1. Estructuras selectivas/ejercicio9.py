print("¡Hola bienvenido!")
serie_fav = input("Dime, ¿cual es tu serie favorita? ")
serie_fav = serie_fav.lower()

if serie_fav == "juego de tronos" or serie_fav == "game of thrones":
    print("¡Por supuesto, Juego de Tronos es la mejor serie de todos los tiempos!")
else:
    print(f"Pues que mal gusto {serie_fav} no es Juego de Tronos.")