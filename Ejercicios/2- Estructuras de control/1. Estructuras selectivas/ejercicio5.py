numero1 = int(input("Dime un número: "))
numero2 = int(input("Dime otro número: "))
numero3 = int(input("Dime otro número: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2}")
else:
    print(f"{numero3}")

# Optimizado:
# Añadir cuando se tienen varios valores (en este caso numeros),
# un valor que indique cual es mayor
# Ejemplo: mayor = max(numero1, numero2, numero3)