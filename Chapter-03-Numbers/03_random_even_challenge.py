# Python Challenge
# Generar un numero aleatorio entre 1 y 100 y verificar si es par

import random

numero = random.randint(1, 100)

print("Numero generado:", numero)

# Verificar si es par
if numero % 2 == 0:
    print("Es un numero PAR")
else:
    print("Es un numero IMPAR")