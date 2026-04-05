# 🔀 Chapter 5 — Python Conditional Statements

En este capítulo aprenderás a tomar decisiones en Python utilizando estructuras condicionales.

Las condicionales permiten que tu programa ejecute diferentes acciones dependiendo de ciertas condiciones.

---

## 📌 ¿Qué son las condicionales?

Son estructuras que permiten evaluar una condición (True o False) y ejecutar código dependiendo del resultado.

👉 Se basan en lógica booleana (`True` / `False`)

---

## 🔹 Estructura básica: `if`

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
```

✔️ Si la condición es `True`, se ejecuta el bloque  
❌ Si es `False`, se ignora

---

## 🔹 `if / else`

Permite ejecutar una alternativa si la condición no se cumple.

```python
edad = 16

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
```

---

## 🔹 `if / elif / else`

Permite evaluar múltiples condiciones.

```python
nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")
```

📌 Python evalúa de arriba hacia abajo  
👉 Solo se ejecuta el primer caso verdadero

---

## ⚠️ Importancia de la indentación

Python usa indentación (espacios) para definir bloques.

```python
if True:
    print("Correcto")
```

❌ Incorrecto:

```python
if True:
print("Error")  # ERROR de indentación
```

---

## 🔁 Nested Conditions (Condiciones anidadas)

Son condicionales dentro de otras.

```python
edad = 20
tiene_id = True

if edad >= 18:
    if tiene_id:
        print("Puedes entrar")
    else:
        print("Necesitas identificación")
else:
    print("Eres menor de edad")
```

---

## 🔀 Inline If (Operador ternario)

Permite escribir una condición en una sola línea.

```python
edad = 18

mensaje = "Mayor" if edad >= 18 else "Menor"
print(mensaje)
```

---

### Otro ejemplo:

```python
numero = 10

resultado = "Par" if numero % 2 == 0 else "Impar"
```

---

## 🧩 `match case` (Python 3.10+)

Es similar a un switch en otros lenguajes.

```python
dia = "lunes"

match dia:
    case "lunes":
        print("Inicio de semana")
    case "viernes":
        print("Fin de semana cerca")
    case _:
        print("Día normal")
```

---

### Ejemplo con números

```python
opcion = 2

match opcion:
    case 1:
        print("Elegiste 1")
    case 2:
        print("Elegiste 2")
    case _:
        print("Opción no válida")
```

---

## ⚠️ Errores comunes

---

### ❌ Olvidar indentación

```python
if True:
print("Error")
```

---

### ❌ Condiciones mal ordenadas

```python
nota = 95

if nota >= 70:
    print("Aprobado")
elif nota >= 90:
    print("Excelente")  # nunca se ejecuta
```

✔️ Correcto:

```python
if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
```

---

### ❌ Comparaciones incorrectas

```python
if x = 5:  # ERROR
```

✔️ Correcto:

```python
if x == 5:
```

---

## 🧠 Buenas prácticas

- Mantén condiciones claras y simples
- Evita anidar demasiado (puede complicar el código)
- Usa nombres de variables descriptivos
- Ordena condiciones de mayor a menor relevancia

---

## 🧠 Conceptos clave

- `if` ejecuta código si la condición es verdadera
- `else` maneja el caso contrario
- `elif` permite múltiples condiciones
- La indentación es obligatoria
- `match case` es útil para múltiples opciones
- Inline if simplifica condiciones cortas

---

## 🎯 Resumen

En este capítulo aprendiste:

- Estructura `if`
- Uso de `else` y `elif`
- Condiciones anidadas
- Operador ternario (inline if)
- `match case`
- Errores comunes

---

## 🚀 Recomendación

Antes de avanzar:

- Practica con decisiones simples
- Combina condiciones con `and` y `or`
- Crea mini programas (ej: login, validaciones)
- Experimenta con `match case`

👉 Este capítulo es donde Python empieza a volverse realmente poderoso.
