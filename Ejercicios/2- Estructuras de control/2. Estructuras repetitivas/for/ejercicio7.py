frase = input("Escribe una frase: ")
modificada = ""

for caracter in frase:
    
    caracter = caracter.upper()

    if caracter not in ["A", "E", "I", "O", "U"]:
        modificada += caracter

print(modificada)