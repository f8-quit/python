numero_secreto = 3

input("Bienvenido al Torneo de los Tres Magos!\nDebes intentar adivinar el numero secreto.\nSuerte! (presiona ENTER para continuar)")
numero = int(input("Introduce el numero: "))

if numero == numero_secreto:
    print("¡Bien hecho! ¡Eres libre!")

else:
    while numero != numero_secreto:
        input("Jajaja, estás atrapado en mi bucle")
        numero = int(input("Introduce el numero: "))

        if numero == numero_secreto:
            print("¡Bien hecho! ¡Eres libre!")
            break