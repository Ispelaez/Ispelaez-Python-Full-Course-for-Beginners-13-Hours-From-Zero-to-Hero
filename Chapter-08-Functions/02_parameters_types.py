# Parameter Types

# Parámetro por defecto
def saludar(nombre="Usuario"):
    return f"Hola, {nombre}"

# *args
def sumar_todos(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

# **kwargs
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

# Uso
print(saludar())
print(saludar("Isis"))

print("Suma total:", sumar_todos(1, 2, 3, 4, 5))

mostrar_info(nombre="Isis", edad=20, pais="Ecuador")