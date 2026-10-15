numero = int(input("Dime un año: "))

if numero % 4 != 0 or (numero % 100 == 0 and numero % 400 != 0):
    print("No es bisiesto")
else:
    print("Es bisiesto")