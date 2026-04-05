# Nested Conditions + Match Case

edad = int(input("Edad: "))
tiene_id = input("¿Tiene ID? (yes/no): ").lower()

if edad >= 18:
    if tiene_id == "yes":
        print("Acceso permitido")
    else:
        print("Necesitas identificación")
else:
    print("Eres menor de edad")

# Match case
opcion = int(input("\nElige una opción (1-3): "))

match opcion:
    case 1:
        print("Elegiste opción 1")
    case 2:
        print("Elegiste opción 2")
    case 3:
        print("Elegiste opción 3")
    case _:
        print("Opción inválida")