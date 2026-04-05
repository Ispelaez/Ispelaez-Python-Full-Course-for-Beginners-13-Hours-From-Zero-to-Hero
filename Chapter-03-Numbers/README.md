# 🔢 Chapter 3 — Python Numbers

En este capítulo aprenderás cómo funcionan los números en Python, incluyendo:

- Tipos numéricos
- Operaciones matemáticas
- Redondeo
- Números aleatorios
- Validación de datos numéricos

---

## 📌 Tipos de números en Python

Python tiene principalmente dos tipos numéricos básicos:

---

### 🔹 Integer (int)

Son números enteros (sin decimales):

```python
x = 10
y = -5
z = 0
```

✔️ Características:
- No tienen límite fijo de tamaño
- Pueden ser positivos, negativos o cero

---

### 🔹 Float (float)

Son números con decimales:

```python
pi = 3.14
altura = 1.65
negativo = -2.5
```

✔️ Características:
- Tienen precisión limitada
- Usan punto (`.`) para decimales

---

### 🔍 Ver tipo de dato

```python
print(type(10))     # int
print(type(3.14))   # float
```

---

## ➕ Operaciones matemáticas

Python permite realizar operaciones básicas:

---

### 🔹 Suma

```python
print(5 + 3)  # 8
```

---

### 🔹 Resta

```python
print(10 - 4)  # 6
```

---

### 🔹 Multiplicación

```python
print(6 * 2)  # 12
```

---

### 🔹 División

```python
print(10 / 2)  # 5.0 (siempre float)
```

---

### 🔹 División entera

```python
print(10 // 3)  # 3
```

---

### 🔹 Módulo (residuo)

```python
print(10 % 3)  # 1
```

---

### 🔹 Potencia

```python
print(2 ** 3)  # 8
```

---

## 📊 Jerarquía de operaciones

Python sigue el orden matemático:

1. Paréntesis `()`
2. Potencias `**`
3. Multiplicación y división `* / // %`
4. Suma y resta `+ -`

```python
resultado = 2 + 3 * 4  # 14
```

---

## 🔄 Conversión de tipos

```python
x = "10"
y = int(x)

z = 3.7
a = int(z)   # 3

b = float(5) # 5.0
```

---

## 🔢 Rounding (Redondeo)

---

### 🔹 round()

```python
print(round(3.6))    # 4
print(round(3.2))    # 3
```

---

### 🔹 Redondeo con decimales

```python
print(round(3.1416, 2))  # 3.14
```

---

### 🔹 truncar (cortar decimal)

```python
x = 3.9
print(int(x))  # 3
```

---

## 🎲 Números aleatorios (random)

Para usar números aleatorios necesitas importar:

```python
import random
```

---

### 🔹 Número entero aleatorio

```python
print(random.randint(1, 10))
```

---

### 🔹 Número decimal aleatorio

```python
print(random.random())  # entre 0 y 1
```

---

### 🔹 Elegir elemento aleatorio

```python
lista = [1, 2, 3, 4]
print(random.choice(lista))
```

---

## ✅ Validación de números

Cuando usas `input()`, el valor es texto:

```python
edad = input("Edad: ")
```

---

### 🔹 Verificar si es número

```python
print(edad.isdigit())
```

✔️ Devuelve:
- `True` si solo contiene números
- `False` si tiene letras o símbolos

---

### 🔹 Convertir con validación

```python
edad = input("Edad: ")

if edad.isdigit():
    edad = int(edad)
    print("Edad válida:", edad)
else:
    print("Entrada inválida")
```

---

## ⚠️ Errores comunes

---

### ❌ División por cero

```python
print(10 / 0)  # ERROR
```

---

### ❌ Conversión inválida

```python
int("hola")  # ERROR
```

---

### ❌ Precisión de floats

```python
print(0.1 + 0.2)  # 0.30000000000000004
```

📌 Esto es normal en computación

---

## 🧠 Conceptos clave

- `int` → números enteros
- `float` → números decimales
- `/` siempre devuelve float
- `//` devuelve entero
- `%` devuelve el residuo
- `round()` redondea números
- `random` genera valores aleatorios
- `isdigit()` ayuda a validar input

---

## 🎯 Resumen

En este capítulo aprendiste:

- Tipos numéricos (`int`, `float`)
- Operaciones matemáticas
- Jerarquía de operaciones
- Conversión de tipos
- Redondeo
- Números aleatorios
- Validación de números

---

## 🚀 Recomendación

Antes de avanzar:

- Practica operaciones matemáticas
- Usa `random` para juegos simples
- Valida inputs siempre
- Experimenta con errores

👉 Este capítulo es clave para lógica y algoritmos.
