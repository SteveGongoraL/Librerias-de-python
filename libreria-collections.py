# Pila con deque. -->pop().
import collections

# biblioteca=[]
biblioteca = collections.deque()

# Agregandole valores
for cantidad in range(2):
    estudiante = input("Dime un nombre de un alumno: ")
    biblioteca.append(estudiante)
print(f"La lista con los valores agregados: \n{biblioteca}")

# Quitandole los valores
while biblioteca:
    # Quitando un valor a la vez, se utiliza LIFO
    print(biblioteca.pop())
print(f"La lista sin valores: \n{biblioteca}")
