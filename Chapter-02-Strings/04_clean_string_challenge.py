# Python Challenge - Clean the string

texto = "968-Maria, ( Data Engineer ) ;; 27y "

# Paso 1: limpiar espacios extremos
texto = texto.strip()

# Paso 2: separar partes
# Eliminamos caracteres innecesarios
texto = texto.replace("(", "").replace(")", "")
texto = texto.replace(";;", "").replace(",", "")

# Paso 3: separar por espacios
partes = texto.split()

# partes = ['968-Maria', 'Data', 'Engineer', '27y']

# Extraer nombre
nombre = partes[0].split("-")[1].lower()

# Extraer rol
rol = (partes[1] + " " + partes[2]).lower()

# Extraer edad
edad = partes[3].replace("y", "")

# Resultado final
print(f"name: {nombre} | role: {rol} | age: {edad}")