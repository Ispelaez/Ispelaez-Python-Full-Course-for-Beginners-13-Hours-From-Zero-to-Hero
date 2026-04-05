# 🧠 Chapter 4 — Logic & Operators

En este capítulo aprenderás cómo tomar decisiones en Python usando lógica.

Aquí se introducen conceptos fundamentales como:

- Valores booleanos
- Operadores de comparación
- Operadores lógicos
- Operadores de pertenencia
- Operadores de identidad

👉 Este capítulo es la base para estructuras como `if`, `while`, etc.

---

## 🔘 Boolean Values (Valores booleanos)

Un **booleano** es un tipo de dato que solo puede tener dos valores:

```python
True
False
```

---

### Ejemplos

```python
es_mayor = True
tiene_permiso = False
```

---

### Convertir a booleano

```python
print(bool(1))    # True
print(bool(0))    # False
print(bool(""))   # False
print(bool("Hi")) # True
```

---

### Valores considerados False (Falsy)

- `0`
- `0.0`
- `""` (string vacío)
- `None`
- `False`

Todo lo demás es `True`

---

## ⚖️ Comparison Operators (Operadores de comparación)

Se usan para comparar valores y siempre devuelven `True` o `False`.

---

### Operadores

| Operador | Significado |
|---------|------------|
| `==` | Igual |
| `!=` | Diferente |
| `>` | Mayor que |
| `<` | Menor que |
| `>=` | Mayor o igual |
| `<=` | Menor o igual |

---

### Ejemplos

```python
print(5 == 5)   # True
print(5 != 3)   # True
print(10 > 3)   # True
print(2 < 1)    # False
```

---

## 🔗 Logical Operators (Operadores lógicos)

Se usan para combinar condiciones.

---

### 🔹 AND

Devuelve `True` si **ambas condiciones son verdaderas**

```python
print(True and True)   # True
print(True and False)  # False
```

---

### 🔹 OR

Devuelve `True` si **al menos una condición es verdadera**

```python
print(True or False)  # True
```

---

### 🔹 NOT

Invierte el valor

```python
print(not True)   # False
print(not False)  # True
```

---

### Ejemplo combinado

```python
edad = 20
tiene_id = True

print(edad >= 18 and tiene_id)  # True
```

---

## 📊 Orden de evaluación

1. `not`
2. `and`
3. `or`

```python
print(True or False and False)  # True
```

---

## 📦 Membership Operators (Pertenencia)

Se usan para verificar si un valor está dentro de una colección.

---

### 🔹 `in`

```python
texto = "Python"

print("P" in texto)   # True
print("x" in texto)   # False
```

---

### 🔹 `not in`

```python
print("x" not in texto)  # True
```

---

## 🆔 Identity Operators (Identidad)

Comparan si dos variables apuntan al mismo objeto en memoria.

---

### 🔹 `is`

```python
a = 5
b = 5

print(a is b)  # True (en muchos casos)
```

---

### 🔹 `is not`

```python
a = [1, 2]
b = [1, 2]

print(a is b)      # False (distintos objetos)
print(a == b)      # True (mismo contenido)
```

---

## ⚠️ Diferencia importante

| Operador | Qué compara |
|----------|------------|
| `==` | Valor |
| `is` | Identidad (memoria) |

---

## ⚠️ Errores comunes

---

### ❌ Confundir `=` con `==`

```python
if x = 5:  # ERROR
```

✔️ Correcto:

```python
if x == 5:
```

---

### ❌ Usar `is` en vez de `==`

```python
a = 10
b = 10

print(a is b)  # puede funcionar pero no es buena práctica
```

✔️ Usa:

```python
print(a == b)
```

---

## 🧠 Conceptos clave

- `True` y `False` controlan la lógica
- Comparaciones devuelven booleanos
- `and`, `or`, `not` combinan condiciones
- `in` verifica pertenencia
- `is` verifica identidad
- `==` compara valores

---

## 🎯 Resumen

En este capítulo aprendiste:

- Valores booleanos
- Operadores de comparación
- Operadores lógicos
- Membership operators
- Identity operators

---

## 🚀 Recomendación

Antes de avanzar:

- Practica combinando condiciones
- Usa `and` y `or` en ejemplos reales
- Entiende bien la diferencia entre `==` y `is`
- Experimenta con `in` en strings

👉 Este capítulo es la base de TODA la lógica en programación.
