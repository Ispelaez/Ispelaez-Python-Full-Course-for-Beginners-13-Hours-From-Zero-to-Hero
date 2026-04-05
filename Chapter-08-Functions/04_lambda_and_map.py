# Lambda & Map

numeros = [1, 2, 3, 4, 5]

# Lambda simple
cuadrado = lambda x: x ** 2
print("Cuadrado de 4:", cuadrado(4))

# map
cuadrados = list(map(lambda x: x ** 2, numeros))
print("Lista de cuadrados:", cuadrados)

# filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)
