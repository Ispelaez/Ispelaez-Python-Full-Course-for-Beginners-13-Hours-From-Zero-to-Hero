# Logical Operators

edad = 20
tiene_id = True

# AND
print("Puede entrar (AND):", edad >= 18 and tiene_id)

# OR
print("Acceso especial (OR):", edad < 18 or tiene_id)

# NOT
print("No tiene ID:", not tiene_id)

# Combinado
print("Lógica combinada:", (edad >= 18 and tiene_id) or False)