# 🧱 Chapter 7 — Python Data Structures

En este capítulo aprenderás a trabajar con **estructuras de datos**, que permiten almacenar, organizar y manipular múltiples valores en Python.

Las principales estructuras son:

- Lists (listas)
- Tuples (tuplas)
- Sets (conjuntos)
- Dictionaries (diccionarios)

Además, aprenderás:

- List comprehension
- Lambda functions

---

# 📌 ¿Qué es una estructura de datos?

Es una forma de organizar y almacenar datos para poder acceder a ellos de manera eficiente.

👉 En lugar de usar muchas variables, puedes agrupar datos relacionados.

---

# 📋 LISTS (Listas)

---

## 📌 ¿Qué es una lista?

Una lista es una colección **ordenada, mutable y permite duplicados**.

```python
numeros = [1, 2, 3, 4]
nombres = ["Ana", "Luis", "Pedro"]
mixta = [1, "Hola", True]
```

---

## 🔹 Acceso a elementos

```python
print(numeros[0])   # 1
print(numeros[-1])  # último elemento
```

---

## 🔹 Slicing

```python
print(numeros[1:3])  # [2, 3]
```

---

## 🔹 Modificar valores

```python
numeros[0] = 10
```

---

## ➕ Agregar elementos

```python
numeros.append(5)       # al final
numeros.insert(1, 99)   # en posición específica
```

---

## ❌ Eliminar elementos

```python
numeros.remove(99)  # por valor
numeros.pop()       # último elemento
numeros.pop(0)      # por índice
```

---

## 🔄 Ordenar listas

```python
numeros.sort()
numeros.sort(reverse=True)
```

---

## 🔗 Combinar listas

```python
a = [1, 2]
b = [3, 4]

c = a + b
```

---

## 🔍 Verificar elementos

```python
print(2 in numeros)
```

---

## 🔁 Iterar listas

```python
for num in numeros:
    print(num)
```

---

## 📊 Funciones útiles

```python
len(numeros)
max(numeros)
min(numeros)
sum(numeros)
```

---

# 🎯 UNPACKING

Permite asignar valores de una lista a variables.

```python
datos = ["Isis", 20, "Ecuador"]

nombre, edad, pais = datos
```

---

# 🔎 FILTERING (Filtrado)

```python
numeros = [1, 2, 3, 4, 5]

pares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
```

---

# ⚡ LIST COMPREHENSION

Forma corta de crear listas.

```python
pares = [n for n in numeros if n % 2 == 0]
```

---

# 🔥 LAMBDA FUNCTIONS

Funciones anónimas (sin nombre).

```python
cuadrado = lambda x: x ** 2
print(cuadrado(4))
```

---

## Uso con listas

```python
numeros = [1, 2, 3]

dobles = list(map(lambda x: x * 2, numeros))
```

---

# 🔒 TUPLES (Tuplas)

---

## 📌 ¿Qué es una tupla?

Es una colección **ordenada, inmutable y permite duplicados**.

```python
tupla = (1, 2, 3)
```

---

## 🔹 Características

- No se puede modificar ❌
- Más rápida que listas
- Se usa para datos constantes

---

## 🔹 Acceso

```python
print(tupla[0])
```

---

# 🧩 SETS (Conjuntos)

---

## 📌 ¿Qué es un set?

Es una colección **no ordenada, sin duplicados**.

```python
numeros = {1, 2, 3, 3}
# Resultado: {1, 2, 3}
```

---

## 🔹 Operaciones

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # unión
print(a & b)  # intersección
print(a - b)  # diferencia
```

---

# 🗂️ DICTIONARIES (Diccionarios)

---

## 📌 ¿Qué es un diccionario?

Es una colección de pares clave-valor.

```python
persona = {
    "nombre": "Isis",
    "edad": 20
}
```

---

## 🔹 Acceso

```python
print(persona["nombre"])
```

---

## 🔹 Agregar / modificar

```python
persona["edad"] = 21
persona["pais"] = "Ecuador"
```

---

## 🔹 Eliminar

```python
persona.pop("edad")
```

---

## 🔹 Recorrer diccionario

```python
for clave, valor in persona.items():
    print(clave, valor)
```

---

# ⚠️ Errores comunes

---

### ❌ Acceder a índice inexistente

```python
lista = [1, 2]
print(lista[5])  # ERROR
```

---

### ❌ Modificar tupla

```python
tupla[0] = 10  # ERROR
```

---

### ❌ Clave inexistente

```python
persona["apellido"]  # ERROR
```

---

# 🧠 Conceptos clave

- Listas → ordenadas y modificables
- Tuplas → ordenadas e inmutables
- Sets → únicos y no ordenados
- Diccionarios → clave-valor
- List comprehension → forma corta
- Lambda → funciones rápidas

---

# 🎯 Resumen

En este capítulo aprendiste:

- Listas y sus métodos
- Tuplas
- Sets
- Diccionarios
- List comprehension
- Lambda functions

---

# 🚀 Recomendación

Antes de avanzar:

- Practica CRUD en listas
- Usa diccionarios como mini bases de datos
- Practica list comprehension
- Combina estructuras

👉 Este capítulo es clave para trabajar con datos reales.
