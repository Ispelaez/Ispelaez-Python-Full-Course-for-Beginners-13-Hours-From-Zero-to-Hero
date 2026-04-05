# Search, Validation & Case Conversion

texto = "Hola Python 123"

# Busqueda
print("Python" in texto)
print("Java" in texto)

print("Posición de Python:", texto.find("Python"))

# Conteo
print("Cantidad de 'o':", texto.count("o"))

#Validacion
print("Es alfanumérico:", texto.isalnum())
print("Es solo letras:", texto.isalpha())
print("Es solo números:", texto.isdigit())

# Case conversion
print("Upper:", texto.upper())
print("Lower:", texto.lower())
print("Swapcase:", texto.swapcase())