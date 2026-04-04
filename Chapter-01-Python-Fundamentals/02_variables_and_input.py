# Variables
# Sirven para almacenar informacion

nombre = "Isis"
edad = 18
altura = 1.60

print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)

# Input del usuario
user_name = input("¿Como te llamas? ")
user_age = input("¿Cuantos años tienes? ")

# Mostrar lo ingresado
print("Hola,", user_name)
print("Tienes", user_age, "años")

# Input siempre devuelve texto (string)
print(type(user_age))  # str

# Convertir a numero
user_age_int = int(user_age)

print("El proximo año tendras:", user_age_int + 1)