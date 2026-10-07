print("Bienvenido al programa de conversión de euros a dólar.")

euros = float(input("Dime la cantidad de euros: "))

euros_a_dolar = euros * 1.13
resultado = round(euros_a_dolar, 2)

print(f"{euros}€ = {resultado}$")