contraseña = "password123"
intento_contraseña = input("Introduce una contraseña: ")
while intento_contraseña != contraseña:
    print("Contraseña incorrecta")
    intento_contraseña = input("Introduce una contraseña: ")
print("Fino señores")