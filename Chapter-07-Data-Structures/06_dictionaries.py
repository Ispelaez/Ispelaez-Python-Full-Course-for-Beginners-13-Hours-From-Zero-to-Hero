# Dictionaries

persona = {
    "nombre": "Isis",
    "edad": 20,
    "pais": "Ecuador"
}

# Acceso
print("Nombre:", persona["nombre"])

# Modificar
persona["edad"] = 21

# Agregar
persona["email"] = "isis@email.com"

# Recorrer
for clave, valor in persona.items():
    print(clave, ":", valor)