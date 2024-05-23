import sys
import os
separador = ("°°°" * 40) + "\n"

# Comparar el peso entre una lista y una tupla
lista = list()
for numero in range (1,1001):
    lista.append(numero)
print(f"La lista tiene {len(lista)} elementos, y tiene un tamaño de {sys.getsizeof(lista)} bytes")

tupla =tuple(lista)
print(f"La tupla tiene {len(tupla)} elementos, y tiene un tamaño de {sys.getsizeof(tupla)} bytes")
print(separador)


print(f"El directorio actual de trabajo es: {os.getcwd()}")
for raiz, dirs, archivos in os.walk(".", topdown= False):
    for nombre in archivos:
        print(os.path.join(raiz, nombre))
    for nombre in dirs:
        print(os.path.join(raiz, nombre))
print(separador)
