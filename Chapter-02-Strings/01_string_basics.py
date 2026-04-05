# String Basics & Transformations

texto = "  hola mundo  "

print("Original:", texto)

# Transformaciones
print("Upper:", texto.upper())
print("Lower:", texto.lower())
print("Title:", texto.title())
print("Capitalize:", texto.capitalize())

# Eliminar espacios
print("Strip:", texto.strip())

# Reemplazar texto
nuevo_texto = texto.replace("mundo", "Python")
print("Reemplazo:", nuevo_texto)

# Longitud
print("Longitud:", len(texto))