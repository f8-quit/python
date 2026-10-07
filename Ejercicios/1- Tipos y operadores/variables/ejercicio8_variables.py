import math

print("Cálculo del área y el volumen de una esfera dado el radio")

radio = float(input("Dime el radio (en cm): "))

area = round(float(4 * math.pi * radio ** 2), 2)
volumen = round(float((4 / 3) * math.pi * (radio ** 3)), 2)

print(f"El área es: {area} \n El volumen es: {volumen}")