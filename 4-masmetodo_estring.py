# Métodos de Cadena (String)

# Método capitalize(): Convierte el primer carácter a mayúscula.
cadena = "hola mundo"
capitalizada = cadena.capitalize()
print("capitalize():", capitalizada)

# Método upper(): Convierte toda la cadena a mayúsculas.
cadena = "hola mundo"
mayusculas = cadena.upper()
print("upper():", mayusculas)

# Método lower(): Convierte toda la cadena a minúsculas.
cadena = "HOLA MUNDO"
minusculas = cadena.lower()
print("lower():", minusculas)

# Método title(): Convierte la primera letra de cada palabra a mayúscula.
cadena = "hola mundo"
titulo = cadena.title()
print("title():", titulo)

# Método strip(): Elimina los espacios en blanco al principio y al final de la cadena.
cadena = "   hola mundo   "
sin_espacios = cadena.strip()
print("strip():", sin_espacios)

# Método split(): Divide la cadena en subcadenas utilizando un separador y devuelve una lista de subcadenas.
cadena = "hola,mundo,python"
subcadenas = cadena.split(",")
print("split():", subcadenas)

# Método join(): Une una lista de cadenas utilizando la cadena de llamada como separador.
lista = ["hola", "mundo", "python"]
cadena_unida = ",".join(lista)
print("join():", cadena_unida)

# Método replace(): Reemplaza una subcadena con otra en la cadena.
cadena = "hola mundo"
reemplazada = cadena.replace("mundo", "Python")
print("replace():", reemplazada)

# Método find(): Encuentra la primera aparición de una subcadena dentro de la cadena y devuelve su índice.
cadena = "hola mundo"
indice = cadena.find("mundo")
print("find():", indice)

# Método count(): Cuenta cuántas veces aparece una subcadena en la cadena.
cadena = "hola mundo mundo"
conteo = cadena.count("mundo")
print("count():", conteo)

# Método startswith(): Comprueba si la cadena comienza con la subcadena especificada.
cadena = "hola mundo"
comienza_con = cadena.startswith("hola")
print("startswith():", comienza_con)

# Método endswith(): Comprueba si la cadena termina con la subcadena especificada.
cadena = "hola mundo"
termina_con = cadena.endswith("mundo")
print("endswith():", termina_con)
