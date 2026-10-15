num_mayor = int(input("Introduce un numero mayor: "))
num_menor = int(input("Introduce un numero menor: "))

if num_mayor <= num_menor:
    print("Valores introducidos no válidos, el primero debe ser mayor y el segundo menor.")

else:
    for salida in range(num_mayor, (num_menor -1), -1):
        print(salida)