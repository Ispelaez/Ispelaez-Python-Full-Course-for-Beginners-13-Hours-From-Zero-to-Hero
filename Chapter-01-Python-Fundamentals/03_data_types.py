# Tipos de datos en Python

# String
nombre = "Isis"
# Integer
edad = 18
# Float
altura = 1.60
# Boolean
es_estudiante = True

# Mostrar valores
print(nombre)
print(edad)
print(altura)
print(es_estudiante)

# Ver tipos de datos
print(type(nombre))        # str
print(type(edad))          # int
print(type(altura))        # float
print(type(es_estudiante)) # bool

# Conversion de tipos (casting)
numero_texto = "100"
numero_entero = int(numero_texto)

print(numero_entero)
print(type(numero_entero))

# Convertir numero a string
numero = 50
texto = str(numero)

print(texto)
print(type(texto))