# 🐍 Chapter 1 — Python Fundamentals

Este capítulo cubre los fundamentos esenciales de Python.  
Aquí se construyen las bases necesarias para poder programar correctamente.

---

## 📌 ¿Qué es Python?

Python es un lenguaje de programación:

- 🧠 De alto nivel (fácil de leer y escribir)
- 🔄 Interpretado (no necesita compilación previa)
- 🌍 Multipropósito (web, data, IA, automatización, etc.)
- 👨‍💻 Orientado a objetos (pero también soporta otros estilos)

---

## ⚙️ ¿Cómo funciona Python?

Cuando ejecutas un programa en Python:

1. Escribes código en un archivo `.py`
2. El intérprete de Python lee ese código
3. Lo traduce a instrucciones que la computadora puede entender
4. Ejecuta línea por línea

📌 Importante:
- Python se ejecuta **de arriba hacia abajo**
- Si hay un error, el programa se detiene

---

## 🛠️ Instalación de Python

Pasos generales:

1. Descargar desde: https://www.python.org
2. Instalar Python
3. (Muy importante) Activar:
   - ✅ *Add Python to PATH*
4. Verificar instalación:

```bash
python --version
```

---

## 💬 Comentarios en Python

Los comentarios son líneas que Python **ignora**.

Sirven para:
- Explicar código
- Dejar notas
- Evitar ejecutar ciertas líneas

### Tipos de comentarios

```python
# Comentario de una sola línea

"""
Comentario
de varias líneas
"""
```

---

## 🖨️ Función `print()`

Se usa para mostrar información en consola.

```python
print("Hola mundo")
```

### Ejemplos

```python
print("Hola")
print(10)
print("Hola", "Mundo")
```

### Características

- Puede imprimir texto, números, variables
- Separa elementos con comas
- Siempre muestra salida al usuario

---

## 📦 Variables

Una variable es un espacio donde se almacena información.

```python
nombre = "Juan"
edad = 20
```

### Reglas para nombrar variables

- Deben empezar con letra o `_`
- No pueden empezar con número ❌
- No usar espacios
- Son sensibles a mayúsculas (`Edad` ≠ `edad`)

### Buenas prácticas

```python
user_name = "Ana"   # snake_case
```

---

## ⌨️ Entrada de usuario `input()`

Permite al usuario ingresar datos.

```python
nombre = input("Ingresa tu nombre: ")
```

### Importante

- `input()` siempre devuelve un **string**

```python
edad = input("Edad: ")
print(type(edad))  # str
```

### Convertir datos

```python
edad = int(input("Edad: "))
altura = float(input("Altura: "))
```

---

## 🔢 Tipos de datos en Python

Python tiene varios tipos de datos básicos:

---

### 🧵 String (str)

Texto entre comillas:

```python
nombre = "Isis"
```

---

### 🔢 Integer (int)

Números enteros:

```python
edad = 21
```

---

### 🔣 Float (float)

Números decimales:

```python
altura = 1.65
```

---

### 🔘 Boolean (bool)

Valores lógicos:

```python
es_mayor = True
es_menor = False
```

---

## 🔍 Ver tipo de dato

```python
print(type(nombre))
```

---

## 🔄 Conversión de tipos (Casting)

Convertir de un tipo a otro:

```python
x = "10"
y = int(x)

z = 3.5
a = int(z)
```

---

## ⚠️ Errores comunes

### ❌ TypeError
Cuando mezclas tipos incompatibles:

```python
print("Edad: " + 20)  # ERROR
```

✔️ Solución:

```python
print("Edad:", 20)
```

---

### ❌ ValueError

```python
int("hola")  # ERROR
```

---

### ❌ NameError

```python
print(nombre)  # variable no definida
```

---

## 🧠 Conceptos clave

- Python es interpretado
- El código se ejecuta en orden
- Las variables almacenan datos
- `input()` recibe datos del usuario
- `print()` muestra resultados
- Todo en Python tiene un tipo de dato

---

## 🎯 Resumen

En este capítulo aprendiste:

- Qué es Python
- Cómo funciona internamente
- Cómo instalarlo
- Uso de comentarios
- Uso de `print()`
- Variables
- Entrada de usuario
- Tipos de datos
- Conversión de tipos
- Errores básicos

---

## 🚀 Recomendación

Antes de avanzar:

- Practica creando variables
- Usa `input()` y `print()`
- Experimenta con tipos de datos
- Comete errores y entiéndelos

👉 Este capítulo es la base de TODO Python.
