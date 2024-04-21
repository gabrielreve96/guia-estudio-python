# Definición de una función que suma dos números
def sumar(a, b):
    return a + b

# Llamada a la función y mostrar el resultado
resultado = sumar(3, 5)
print("El resultado de la suma es:", resultado)




# Definición de una función con un valor por defecto
def saludar(nombre="usuario"):
    return "Hola, " + nombre + "!"

# Llamada a la función sin especificar un nombre
mensaje = saludar()
print(mensaje)  # Output: Hola, usuario!

# Llamada a la función con un nombre especificado
mensaje_personalizado = saludar("Juan")
print(mensaje_personalizado)  # Output: Hola, Juan!




# Definición de una función con argumentos variables
def sumar_varios(*args):
    suma = 0
    for num in args:
        suma += num
    return suma

# Llamada a la función con diferentes números de argumentos
resultado1 = sumar_varios(1, 2, 3)
print("Suma 1:", resultado1)  # Output: 6

resultado2 = sumar_varios(10, 20, 30, 40, 50)
print("Suma 2:", resultado2)  # Output: 150





# Definición de una función con argumentos con palabras clave
def informacion_usuario(nombre, edad, ciudad):
    return "Nombre: {}, Edad: {}, Ciudad: {}".format(nombre, edad, ciudad)

# Llamada a la función con argumentos con palabras clave
informacion = informacion_usuario(nombre="Juan", edad=30, ciudad="Madrid")
print(informacion)  # Output: Nombre: Juan, Edad: 30, Ciudad: Madrid
