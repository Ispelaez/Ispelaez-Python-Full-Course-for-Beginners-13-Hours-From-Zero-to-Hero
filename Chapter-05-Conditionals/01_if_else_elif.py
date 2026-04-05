# If / Elif / Else + Inline If

nota = int(input("Ingresa tu nota: "))

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
elif nota >= 50:
    print("Supletorio")
else:
    print("Reprobado")

# Inline if
mensaje = "Pasaste" if nota >= 70 else "No pasaste"
print(mensaje)