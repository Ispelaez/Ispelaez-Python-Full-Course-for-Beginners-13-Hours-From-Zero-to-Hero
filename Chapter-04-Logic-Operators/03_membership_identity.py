# Membership & Identity Operators

texto = "Python"

# Membership
print("P está en texto:", "P" in texto)
print("x no está en texto:", "x" not in texto)

# Identity
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("\nComparación de listas:")
print("a == b:", a == b)  # mismo contenido
print("a is b:", a is b)  # distinto objeto
print("a is c:", a is c)  # mismo objeto