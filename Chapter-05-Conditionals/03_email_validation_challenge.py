# Python Challenge - Email validation avanzada

email = input("Ingresa tu email: ").strip()

# Validaciones
no_vacio = email != ""
tiene_arroba = "@" in email
tiene_punto = "." in email
una_arroba = email.count("@") == 1
terminacion_valida = email.endswith((".com", ".org", ".net"))
longitud_valida = len(email) <= 254

# Primer y último carácter (si no está vacío)
if email:
    empieza_valido = email[0].isalnum()
    termina_valido = email[-1].isalnum()
else:
    empieza_valido = False
    termina_valido = False

# Validación final
if (
    no_vacio
    and tiene_arroba
    and tiene_punto
    and una_arroba
    and terminacion_valida
    and longitud_valida
    and empieza_valido
    and termina_valido
):
    print("Email válido")
else:
    print("Email inválido")