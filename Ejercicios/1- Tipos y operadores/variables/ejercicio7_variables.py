print("Cálculo de hipotenusa")

a = float(input("Longitud primer cateto (en cm): "))
b = float(input("Longitud segundo cateto (en cm): "))

h = round(float((a**2 + b**2) ** 0.5), 2)

print(f"La hipotenusa mide: {h}")