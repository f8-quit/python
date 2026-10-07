print("Bienvenido al programa.")

nombre = input("Dime tu nombre: ")
apellido = input("Tu primer apellido: ")
peso_kg = float(input("Peso (en kg): "))
altura_metros = float(input("Altura (en metros): "))

kg_a_libras = peso_kg * 2.20462
metros_a_pies = altura_metros * 3.28084
imc = peso_kg / ((altura_metros)**2)

print(f"Tus datos: {nombre} {apellido}\n Peso: {kg_a_libras} libras \n Altura: {metros_a_pies} pies")
print(f"Tu IMC es: {imc}")