limite = 200000
suma = 0
numero = 1
print("¿Cuantos numeros naturales es necesario sumar consecutivamente para que el total sea 200.000 o más?")


while suma <= limite:
    suma += numero
    numero += 1

print(f'El ultimo numero de la suma consecutiva del 1 al {limite} es: {numero - 1}')