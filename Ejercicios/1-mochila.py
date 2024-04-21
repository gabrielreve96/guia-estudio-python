"""
Dado un conjunto de elementos, cada uno con un peso y un valor, determina la cantidad máxima de valor que se puede llevar en una mochila con una capacidad máxima de peso. Este es un problema clásico de optimización.

"""
numeros=[1 , 2, 3 ,4 ,6, 12,  22,44]

totalPeso=10


def cuyaSuma_sea_meno_a_diez(numeros):
     return numeros + numeros < totalPeso

def determinarPesoTotalDelListado(listado):
     #sacamos lo numeros igual  10
     mayor_a_diez=list(filter(cuyaSuma_sea_meno_a_diez,listado))
     return print(mayor_a_diez) 



determinarPesoTotalDelListado(numeros)
