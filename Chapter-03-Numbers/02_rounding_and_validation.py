# Rounding & Validation

# Redondeo
numero = 3.1416

print("Numero original:", numero)
print("Redondeado:", round(numero))
print("Redondeado a 2 decimales:", round(numero, 2))

# Validación de input
edad = input("\nIngresa tu edad: ")

if edad.isdigit():
    edad = int(edad)
    print("Edad valida:", edad)
else:
    print("Error: Debes ingresar un numero valido")