numero = float(input("Dime tu nota sobre 10: "))

if numero >= 0 and numero < 5:
    print("Suspenso")
elif numero >= 5 and numero < 6:
    print("Suficiente")
elif numero >= 6 and numero < 7:
    print("Bien")
elif numero >= 7 and numero < 9:
    print("Notable")
elif numero >= 9 and numero <= 10:
    print("Sobresaliente")
else:
    print("No válido")