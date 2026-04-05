# 🐍 Chapter 2 — Python Strings

En este capítulo aprenderás todo sobre **strings (cadenas de texto)** en Python.  
Los strings son uno de los tipos de datos más usados, ya que representan texto.

---

## 📌 ¿Qué es un String?

Un **string** es una secuencia de caracteres (texto) encerrada entre comillas.

```python
nombre = "Isis"
mensaje = 'Hola mundo'
```

### Tipos de comillas

```python
"Texto"
'Texto'
"""Texto largo"""
```

✔️ Todas funcionan, pero:
- Usa `' '` o `" "` para textos cortos
- Usa `""" """` para textos largos o multilínea

---

## 🔤 String Basics (Conceptos básicos)

### Concatenación

Unir strings:

```python
nombre = "Isis"
saludo = "Hola " + nombre
print(saludo)
```

---

### Repetición

```python
print("Hola " * 3)
```

---

### Longitud

```python
texto = "Python"
print(len(texto))  # 6
```

---

### Verificar si algo es string

```python
print(type(texto))
```

---

## 🔄 Transformaciones de Strings

Los strings son **inmutables** ❗  
Esto significa que **no puedes cambiarlos directamente**, sino que se crea uno nuevo.

---

### Métodos comunes

```python
texto = "hola mundo"

print(texto.upper())   # HOLA MUNDO
print(texto.lower())   # hola mundo
print(texto.title())   # Hola Mundo
print(texto.capitalize())  # Hola mundo
```

---

### Eliminar espacios

```python
texto = "  hola  "

print(texto.strip())   # "hola"
print(texto.lstrip())  # "hola  "
print(texto.rstrip())  # "  hola"
```

---

### Reemplazar texto

```python
texto = "Hola mundo"

nuevo = texto.replace("mundo", "Python")
print(nuevo)
```

---

## 🔍 Indexing (Indexación)

Cada carácter tiene una posición (índice).

```python
texto = "Python"
```

| Letra | P | y | t | h | o | n |
|------|---|---|---|---|---|---|
| Índice | 0 | 1 | 2 | 3 | 4 | 5 |

---

### Acceder a caracteres

```python
print(texto[0])  # P
print(texto[3])  # h
```

---

### Índices negativos

```python
print(texto[-1])  # n
print(texto[-2])  # o
```

---

## ✂️ Slicing (Rebanado)

Permite obtener partes del string.

```python
texto = "Python"
```

### Sintaxis

```python
texto[inicio:fin]
```

- `inicio` → incluido
- `fin` → NO incluido

---

### Ejemplos

```python
print(texto[0:3])  # Pyt
print(texto[2:5])  # tho
print(texto[:3])   # Pyt
print(texto[3:])   # hon
```

---

### Saltos (step)

```python
print(texto[::2])  # Pto
print(texto[::-1]) # nohtyP (invertir)
```

---

## 🔎 Búsqueda en Strings

---

### Buscar texto

```python
texto = "Hola mundo"

print("Hola" in texto)   # True
print("Python" in texto) # False
```

---

### Método `find()`

```python
print(texto.find("mundo"))  # posición
print(texto.find("Python")) # -1 si no existe
```

---

### Método `count()`

```python
texto = "banana"

print(texto.count("a"))  # 3
```

---

## ✅ Validación de Strings

Sirve para verificar contenido.

---

### Métodos útiles

```python
texto = "12345"
print(texto.isdigit())  # True

texto = "abc"
print(texto.isalpha())  # True

texto = "abc123"
print(texto.isalnum())  # True
```

---

### Otros métodos

```python
print("hola".islower())  # True
print("HOLA".isupper())  # True
print("Hola".istitle())  # True
```

---

## 🔤 Case Conversion (Cambio de mayúsculas/minúsculas)

---

### Métodos principales

```python
texto = "hola mundo"

print(texto.upper())     # HOLA MUNDO
print(texto.lower())     # hola mundo
print(texto.capitalize()) # Hola mundo
print(texto.title())     # Hola Mundo
print(texto.swapcase())  # HOLA MUNDO → hola mundo
```

---

## ⚠️ Errores comunes

---

### ❌ Intentar modificar un string directamente

```python
texto = "hola"
texto[0] = "H"  # ERROR
```

✔️ Solución:

```python
texto = "H" + texto[1:]
```

---

### ❌ Índice fuera de rango

```python
texto = "hola"
print(texto[10])  # ERROR
```

---

## 🧠 Conceptos clave

- Los strings son **inmutables**
- Se pueden recorrer por índices
- El slicing permite cortar texto
- Existen muchos métodos útiles
- Se pueden validar datos fácilmente

---

## 🎯 Resumen

En este capítulo aprendiste:

- Qué es un string
- Cómo manipular texto
- Indexación y slicing
- Métodos de transformación
- Búsqueda de texto
- Validación de strings
- Conversión de mayúsculas/minúsculas

---

## 🚀 Recomendación

Antes de avanzar:

- Practica slicing con diferentes textos
- Usa métodos como `.upper()`, `.strip()`
- Combina `input()` con validaciones
- Intenta invertir palabras y modificar texto

👉 Dominar strings es CLAVE para todo Python (y programación en general).
