# Métodos de Listas (Arrays)

# Método append(): Agrega un elemento al final de la lista.
mi_lista = [1, 2, 3]
mi_lista.append(4)
print("append():", mi_lista)

# Método extend(): Extiende la lista agregando elementos de otra lista.
mi_lista = [1, 2, 3]
otra_lista = [4, 5, 6]
mi_lista.extend(otra_lista)
print("extend():", mi_lista)

# Método insert(): Inserta un elemento en una posición específica de la lista.
mi_lista = [1, 2, 3]
mi_lista.insert(1, 10)
print("insert():", mi_lista)

# Método remove(): Elimina el primer elemento con el valor especificado de la lista.
mi_lista = [1, 2, 3, 4, 3]
mi_lista.remove(3)
print("remove():", mi_lista)

# Método pop(): Elimina y devuelve el elemento en la posición especificada de la lista.
mi_lista = [1, 2, 3]
elemento_eliminado = mi_lista.pop(1)
print("pop():", elemento_eliminado, mi_lista)

# Método index(): Devuelve el índice del primer elemento con el valor especificado.
mi_lista = [1, 2, 3, 4, 3]
indice = mi_lista.index(3)
print("index():", indice)

# Método count(): Devuelve el número de veces que aparece un elemento en la lista.
mi_lista = [1, 2, 3, 4, 3]
conteo = mi_lista.count(3)
print("count():", conteo)

# Método sort(): Ordena los elementos de la lista.
mi_lista = [3, 1, 4, 1, 5, 9, 2]
mi_lista.sort()
print("sort():", mi_lista)

# Método reverse(): Invierte el orden de los elementos en la lista.
mi_lista = [1, 2, 3, 4, 5]
mi_lista.reverse()
print("reverse():", mi_lista)

# Método copy(): Retorna una copia superficial de la lista.
mi_lista = [1, 2, 3]
copia = mi_lista.copy()
print("copy():", copia)

# Método clear(): Elimina todos los elementos de la lista.
mi_lista = [1, 2, 3]
mi_lista.clear()
print("clear():", mi_lista)



# Método find(): Encuentra el índice del primer elemento con el valor especificado.
mi_lista = [10, 20, 30, 40, 50]
indice = mi_lista.index(30)
print("find():", indice)

# Método sort(): Ordena los elementos de la lista.
mi_lista = [50, 10, 30, 20, 40]
mi_lista.sort()
print("sort():", mi_lista)

# Método replace(): Reemplaza todos los elementos en la lista con otro valor.
mi_lista = [1, 2, 3, 4, 5]
mi_lista = [elemento * 2 for elemento in mi_lista]  # Multiplica todos los elementos por 2
print("replace():", mi_lista)
