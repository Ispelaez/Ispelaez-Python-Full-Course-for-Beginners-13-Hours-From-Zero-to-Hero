# Python Challenge - Filtrar estudiantes que empiezan con 'M'

students = [
    ["Maria", 85],
    ["Kumar", 90],
    ["Max", 60]
]

# Solución con list comprehension
filtered_students = [s for s in students if s[0].startswith("M")]

print("Estudiantes filtrados:")
for student in filtered_students:
    print(student)
    