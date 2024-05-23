# Ejemplo para demostrar el manejo de agregado sobre iterable. Demuestra: zip(), map(), reduce(), accumulate().

import functools # Necesario para usar reduce().
import itertools # Necesario para usar accumulate().
separador = ("°°°" * 40) + "\n"

def al_doble(valor_1):
    return valor_1 + valor_1                            # De la linea 5-12 no son necesarias para zip().
def sumar_dos(valor_1, valor_2):
    return valor_1 + valor_2

lista_numeros = [1,2,3,4,5,6]
lista_letras = "aeiou" #["a","e","i","o","u"]
# print(lista_numeros)
# print(lista_letras)

resultado_combinado = zip(lista_numeros, lista_letras)
print(f"El tipo del objeto combinado resultante es {type(resultado_combinado)}")
print(f"El resultado de combinar ambas listas es: {list(resultado_combinado)}") # Se tranforma en lista para que pueda ser un objeto iterable.
print(separador)

# Con list comprengenson= nd=[x+x]
# Demosstración de la función map() para procesar cada elemento de una lista.
numeros_al_doble = list(map(al_doble, lista_numeros))
print(f"El doble de cada elemento de la lista original: {numeros_al_doble}")
print(numeros_al_doble)
print(separador)

# Demostración de la funcion reduce() y accumulate() para agregar elementos.
print(f"La lista de numeros original es: {lista_numeros}")
sumatoria_numeros = functools.reduce(sumar_dos, lista_numeros)
print(f"La sumatoria de los datos en la lista usando 'reduce()' es: {sumatoria_numeros}")
acomulado_numeros = list(itertools.accumulate(lista_numeros, sumar_dos))
print(f"El acomulado de la lista mediante 'accumulate()' es: {acomulado_numeros}")
