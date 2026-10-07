import math

print("Cálculo del área y el volumen de un cilindro dado el radio")

radio = float(input("Dime el radio (en cm): "))
altura = float(input("Dime la altura (en cm): "))

area = round(float(2 * math.pi * radio * (radio + altura)), 2)
volumen = round(float(math.pi * (radio ** 2) * altura), 2)

print(f"El área es: {area} \n El volumen es: {volumen}")