# Clean Functions Example

def es_mayor_de_edad(edad):
    return edad >= 18


def tiene_nombre_valido(nombre):
    return isinstance(nombre, str) and nombre.strip() != ""


def validar_usuario(nombre, edad):
    if not tiene_nombre_valido(nombre):
        return "Nombre inválido"

    if not isinstance(edad, int):
        return "Edad inválida"

    if es_mayor_de_edad(edad):
        return "Usuario válido"
    else:
        return "Usuario menor de edad"


# Uso
print(validar_usuario("Isis", 20))
print(validar_usuario("", 20))
print(validar_usuario("Juan", 15))