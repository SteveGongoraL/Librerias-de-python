import numpy as np
separador = ("°°°" * 40) + "\n"

a = np.array([[2,0],[2,0],[3,1],[5,0],[5,1],[5,2]])
print(a)
print(type(a))
print(separador)

# Se cambio el primer valor de cada lista por 8
a[:,0] = 8
print(a)
print(separador)

# Se cambio el segundo valor de cada lista por 28
a[:,1] = 28
print(a)
print(separador)

# Creando un arreglo NumPy bidimensional con 2 filas y 4 columnas
print("Arreglo2: \nTiene 2 filas y 4 columnas")
# shape() especifica el numero de filas y columnas. dtype=int establece el tipo de dato que tendra este arreglo
arreglo2 = np.zeros(shape = (2,4), dtype = int)
print(arreglo2)
# Shape te muestra cuantas filas y columnas tiene.
print(arreglo2.shape)
print(separador)

# Con arrange()
# El primer valor es el de inicio (incluido)
# El segundo valor es el de fin -1 osea llegara hasta 24
# El tercer valor es el de incremento
dosEnDos = np.arange(10,25,2)
print(dosEnDos)
# Shape muestra cuantos valores imprimio. # Unidimensional
print(dosEnDos.shape)
print(separador)
