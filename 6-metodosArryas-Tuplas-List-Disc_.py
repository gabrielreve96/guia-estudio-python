# Definir una tupla de coordenadas
coordenadas = (10, 20)

# Acceder a los elementos de la tupla por índice
print(coordenadas[0])  # Output: 10
print(coordenadas[1])  # Output: 20





# Definir una lista de números
numeros = [1, 2, 3, 4, 5]

# Agregar un elemento a la lista
numeros.append(6)

# Modificar un elemento de la lista
numeros[2] = 10

# Eliminar un elemento de la lista
del numeros[3]

print(numeros)  # Output: [1, 2, 10, 5, 6]




# Definir un diccionario de información del usuario
usuario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceder a un valor en el diccionario
print(usuario["nombre"])  # Output: Juan

# Agregar una nueva clave-valor al diccionario
usuario["profesion"] = "Ingeniero"

# Modificar un valor en el diccionario
usuario["edad"] = 31

# Eliminar una clave-valor del diccionario
del usuario["ciudad"]

print(usuario)  # Output: {'nombre': 'Juan', 'edad': 31, 'profesion': 'Ingeniero'}







# Usando la biblioteca 'array'
from array import array

# Definir un array de números enteros
mi_array = array('i', [1, 2, 3, 4, 5])

# Acceder a los elementos del array por índice
print(mi_array[0])  # Output: 1
print(mi_array[1])  # Output: 2
