# ALL Python Challenges

print("----- Challenge 1 -----")
name = input("Nombre: ").strip()
age = input("Edad: ")

if age.isdigit() and name and int(age) >= 18:
    print("Acceso permitido")
else:
    print("Acceso denegado")


print("\n----- Challenge 2 -----")
password = input("Password: ")

if len(password) >= 8 and " " not in password:
    print("Contraseña válida")
else:
    print("Contraseña inválida")


print("\n----- Challenge 3 -----")
email = input("Email: ").strip()

if email and "@" in email and email.endswith(".com"):
    print("Email válido")
else:
    print("Email inválido")


print("\n----- Challenge 4 -----")
username = input("Username: ").strip()

if isinstance(username, str) and len(username) > 5:
    print("Username válido")
else:
    print("Username inválido")


print("\n----- Challenge 5 -----")
role = input("Rol (admin/moderator/user): ").lower()
is_banned = input("¿Baneado? (yes/no): ").lower() == "yes"
is_verified = input("¿Email verificado? (yes/no): ").lower() == "yes"

if (role in ["admin", "moderator"]) and (not is_banned or is_verified):
    print("Acceso permitido")
else:
    print("Acceso denegado")