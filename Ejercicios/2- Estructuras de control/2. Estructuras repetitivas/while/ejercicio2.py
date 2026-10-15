numero_salida = 3
opcion = 0 

while opcion != numero_salida:
    opcion = int(input("Escoge (1 para Hola, 2 para Adiós, 3 para Salir): "))
    
    if opcion == 1:
        print("Hola")
    elif opcion == 2:
        print("Adiós")
    elif opcion == 3:
        print("Ta luego")
    else:
        print("No válido")