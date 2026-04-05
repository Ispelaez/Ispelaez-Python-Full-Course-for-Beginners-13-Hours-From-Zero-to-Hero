# 🧩 Chapter 8 — Python Functions

En este capítulo aprenderás a crear y utilizar **funciones**, una de las herramientas más importantes en programación.

Las funciones permiten:

- Reutilizar código
- Organizar programas
- Hacer código más limpio y mantenible
- Evitar repetición (DRY: Don't Repeat Yourself)

---

# 📌 ¿Qué es una función?

Una función es un bloque de código que realiza una tarea específica y puede ser reutilizado múltiples veces.

---

## 🔹 Sintaxis básica

```python
def nombre_funcion():
    # código
```

---

### Ejemplo simple

```python
def saludar():
    print("Hola mundo")

saludar()
```

👉 `saludar()` ejecuta la función

---

# 🔹 Funciones con parámetros

Los parámetros permiten pasar datos a la función.

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Isis")
```

---

## 🔹 Múltiples parámetros

```python
def sumar(a, b):
    print(a + b)

sumar(5, 3)
```

---

# 🔙 Return (retorno de valores)

Las funciones pueden devolver valores usando `return`.

---

## 🔹 Ejemplo

```python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)
```

---

## ⚠️ Diferencia clave

```python
def suma1(a, b):
    print(a + b)

def suma2(a, b):
    return a + b
```

👉 `print()` solo muestra  
👉 `return` devuelve el valor para usarlo después

---

# 🔄 Tipos de funciones

---

## 1️⃣ Funciones sin parámetros

```python
def saludo():
    print("Hola")
```

---

## 2️⃣ Funciones con parámetros

```python
def saludo(nombre):
    print(nombre)
```

---

## 3️⃣ Funciones con retorno

```python
def cuadrado(x):
    return x ** 2
```

---

## 4️⃣ Funciones con parámetros por defecto

```python
def saludar(nombre="Usuario"):
    print("Hola", nombre)

saludar()
saludar("Isis")
```

---

## 5️⃣ Funciones con múltiples retornos

```python
def datos():
    return "Isis", 20

nombre, edad = datos()
```

---

# 🧠 Scope (alcance de variables)

---

## 🔹 Variable local

```python
def funcion():
    x = 10
    print(x)
```

---

## 🔹 Variable global

```python
x = 5

def mostrar():
    print(x)
```

---

## ⚠️ Importante

Las variables dentro de funciones NO afectan las externas (a menos que uses `global`).

---

# 🔧 Argumentos avanzados

---

## 🔹 Argumentos por posición

```python
def resta(a, b):
    return a - b

resta(5, 3)
```

---

## 🔹 Argumentos por nombre

```python
resta(a=5, b=3)
```

---

## 🔹 `*args` (múltiples valores)

```python
def suma(*numeros):
    return sum(numeros)

print(suma(1, 2, 3, 4))
```

---

## 🔹 `**kwargs` (clave-valor)

```python
def mostrar_info(**datos):
    print(datos)

mostrar_info(nombre="Isis", edad=20)
```

---

# ⚡ Funciones lambda

Funciones anónimas en una sola línea.

```python
cuadrado = lambda x: x * x
print(cuadrado(4))
```

---

## Uso común

```python
numeros = [1, 2, 3]

dobles = list(map(lambda x: x * 2, numeros))
```

---

# 🧼 Clean Code (Código limpio)

---

## 📌 ¿Por qué es importante?

- Facilita la lectura
- Reduce errores
- Hace el código mantenible

---

## 🔹 Buenas prácticas

---

### ✔️ Nombres claros

```python
def calcular_total():
```

❌ Evita:

```python
def ct():
```

---

### ✔️ Funciones pequeñas

Una función debe hacer UNA cosa.

---

### ✔️ Evitar duplicación

❌

```python
print(5 + 3)
print(10 + 2)
```

✔️

```python
def sumar(a, b):
    return a + b
```

---

### ✔️ Uso de return en vez de print

✔️ Mejor práctica:

```python
def calcular(a, b):
    return a + b
```

---

### ✔️ Separación de responsabilidades

Cada función debe tener un propósito claro.

---

# ⚠️ Errores comunes

---

### ❌ Olvidar return

```python
def suma(a, b):
    a + b
```

---

### ❌ Confundir print con return

---

### ❌ Variables fuera de scope

---

### ❌ Funciones muy largas

---

# 🧠 Conceptos clave

- Funciones reutilizan código
- `def` define funciones
- Parámetros reciben datos
- `return` devuelve valores
- Lambda crea funciones rápidas
- Clean code mejora calidad

---

# 🎯 Resumen

En este capítulo aprendiste:

- Crear funciones
- Usar parámetros
- Usar return
- Tipos de funciones
- Lambda
- Buenas prácticas

---

# 🚀 Recomendación

Antes de avanzar:

- Practica creando funciones propias
- Usa funciones en tus ejercicios anteriores
- Divide problemas grandes en funciones pequeñas
- Aplica clean code siempre

👉 Este capítulo es el paso a programar como profesional.
