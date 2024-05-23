import random
separador ="\n" + ("°°°" * 30) + "\n"

print(f"Obteniendo un numero entero aleatorio que puede ir del 0 al 19:\n {random.randrange(20)}")
print(f"Obteniendo un multiplo de 2 aleatorio que puede ir del 2 al 20:\n {random.randrange(2, 21, 2)}")
print(f"Obteniendo un valor numérico entre 0.0 y 1.0:\n {random.random()}")
print(separador)


lista_de_prueba = [10, 20, 30, 40, 15, 25, 35, 45]
print(f"La lista de prueba es:\n {lista_de_prueba}")
random.shuffle(lista_de_prueba)
print(f"La lista ya 'barajeada' es:\n {lista_de_prueba}")
print(f"El valor seleccionado aleatoriamente de la lista es:\n {random.choice(lista_de_prueba)}")
