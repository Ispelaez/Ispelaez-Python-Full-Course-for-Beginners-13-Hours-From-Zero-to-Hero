# Indexing & Slicing

texto = "Python"

# Indexing
print("Primera letra:", texto[0])
print("Última letra:", texto[-1])

# Slicing
print("0:3 ->", texto[0:3])
print("2:5 ->", texto[2:5])
print(":4 ->", texto[:4])
print("3: ->", texto[3:])

# Step
print("Cada 2 letras:", texto[::2])

# Invertir string
print("Invertido:", texto[::-1])