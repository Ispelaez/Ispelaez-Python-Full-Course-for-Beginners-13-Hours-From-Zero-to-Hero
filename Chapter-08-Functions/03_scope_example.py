# Scope Example

x = 10  # variable global

def cambiar_valor():
    x = 5  # variable local
    print("Dentro de la función:", x)

def usar_global():
    global x
    x = 20

print("Antes:", x)

cambiar_valor()
print("Después de cambiar_valor:", x)

usar_global()
print("Después de usar_global:", x)