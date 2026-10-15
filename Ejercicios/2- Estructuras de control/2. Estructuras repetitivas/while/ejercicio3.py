numero = int(input("Introduce un número para ver sus múltiplos: "))
contador = 1
multiplo = numero * contador
print(f"{multiplo}")

while contador <= 999999:
    contador += 1
    multiplo = numero * contador

    continuar = input("¿Quieres continuar? (s/n)").lower()
    if continuar == "s":
        print(f"{multiplo}")
    elif continuar == "n":
        print("Adiós")
        break
    else:
        print("No válido")
        break