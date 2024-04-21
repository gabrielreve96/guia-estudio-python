# Definir una lista de números
numeros = [1, 2, 3, 4, 5]

# Iterar sobre la lista e imprimir cada elemento
print("Recorriendo la lista con un bucle for:")
for numero in numeros:
    print(numero)

# Sumar todos los elementos de la lista usando un bucle for
suma = 0
for numero in numeros:
    suma += numero
print("Suma de los elementos:", suma)





# Definir un diccionario de información de un estudiante
estudiante = {
    "nombre": "Juan",
    "edad": 20,
    "curso": "Python"
}

# Iterar sobre las claves del diccionario e imprimir cada clave y su valor
print("Recorriendo el diccionario con un bucle for:")
for clave in estudiante:
    valor = estudiante[clave]
    print(clave + ":", valor)





# Definir una tupla de colores
colores = ("rojo", "verde", "azul")

# Iterar sobre la tupla e imprimir cada color
print("Recorriendo la tupla con un bucle for:")
for color in colores:
    print(color)
