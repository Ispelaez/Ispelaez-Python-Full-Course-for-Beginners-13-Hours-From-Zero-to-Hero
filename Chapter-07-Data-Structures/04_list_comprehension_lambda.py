# List Comprehension & Lambda

numbers = [1, 2, 3, 4, 5]

# List comprehension
pares = [n for n in numbers if n % 2 == 0]
print("Pares:", pares)

# Lambda
cuadrados = list(map(lambda x: x**2, numbers))
print("Cuadrados:", cuadrados)