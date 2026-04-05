# 🔁 Chapter 6 — Python Loops

En este capítulo aprenderás a repetir acciones automáticamente usando bucles (loops).

Los loops permiten ejecutar un bloque de código múltiples veces sin tener que escribirlo repetidamente.

---

## 📌 ¿Qué es un loop?

Un **loop (bucle)** es una estructura que repite un bloque de código mientras se cumpla una condición o sobre una colección de datos.

---

## 🔹 Tipos de loops en Python

- `for` → recorre elementos
- `while` → se ejecuta mientras una condición sea verdadera

---

# 🔁 FOR LOOPS

---

## 📌 ¿Qué es un `for`?

El loop `for` se usa para recorrer secuencias como:

- Strings
- Listas
- Rangos (`range()`)

---

### Sintaxis

```python
for variable in iterable:
    # código
```

---

### Ejemplo básico

```python
for i in range(5):
    print(i)
```

👉 Salida:
```
0
1
2
3
4
```

---

### Usando strings

```python
for letra in "Python":
    print(letra)
```

---

### Usando listas

```python
numeros = [1, 2, 3]

for num in numeros:
    print(num)
```

---

## 🔢 Función `range()`

Genera secuencias de números.

---

### Formas de usarla

```python
range(5)        # 0 a 4
range(1, 5)     # 1 a 4
range(1, 10, 2) # salto de 2
```

---

# ⛔ BREAK, CONTINUE, PASS

---

## 🔹 `break`

Detiene el loop completamente.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

## 🔹 `continue`

Salta una iteración.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## 🔹 `pass`

No hace nada (placeholder).

```python
for i in range(5):
    if i == 2:
        pass
    print(i)
```

---

# 🔁 WHILE LOOPS

---

## 📌 ¿Qué es un `while`?

Se ejecuta mientras una condición sea `True`.

---

### Sintaxis

```python
while condicion:
    # código
```

---

### Ejemplo

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

---

## ⚠️ Bucle infinito

```python
while True:
    print("Esto nunca termina")
```

👉 Usa `break` para detenerlo

---

# 🔂 NESTED LOOPS (Bucles anidados)

Un loop dentro de otro.

---

### Ejemplo

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

---

### Uso común

- Tablas
- Matrices
- Patrones

---

# 🔚 FOR-ELSE

---

## 📌 ¿Qué es?

El `else` se ejecuta cuando el loop termina normalmente (sin `break`).

---

### Ejemplo

```python
for i in range(5):
    print(i)
else:
    print("Loop terminado")
```

---

### Con `break`

```python
for i in range(5):
    if i == 3:
        break
else:
    print("Nunca se ejecuta")
```

---

# ⚠️ Errores comunes

---

### ❌ Olvidar actualizar el `while`

```python
while x < 5:
    print(x)  # loop infinito
```

---

### ❌ Mal uso de break

```python
for i in range(5):
    break  # termina inmediatamente
```

---

### ❌ Indentación incorrecta

```python
for i in range(5):
print(i)  # ERROR
```

---

# 🧠 Buenas prácticas

- Usa `for` cuando conozcas el rango
- Usa `while` cuando dependa de una condición
- Evita loops infinitos
- Mantén el código claro

---

# 🧠 Conceptos clave

- `for` recorre secuencias
- `while` depende de condiciones
- `break` detiene el loop
- `continue` salta iteraciones
- `pass` no hace nada
- `nested loops` permiten estructuras complejas
- `for-else` tiene comportamiento especial

---

# 🎯 Resumen

En este capítulo aprendiste:

- For loops
- While loops
- Break / Continue / Pass
- Nested loops
- For-else

---

# 🚀 Recomendación

Antes de avanzar:

- Practica con `range()`
- Haz loops con condiciones reales
- Crea patrones (triángulos, etc.)
- Combina loops con `if`

👉 Este capítulo es esencial para automatizar tareas.
