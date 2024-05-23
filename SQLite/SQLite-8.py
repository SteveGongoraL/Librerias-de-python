import sys
import sqlite3
from sqlite3 import Error
# Agregar un registro en una tabla utilizando una funcion definida por el usuario (udf).

def guardaProyecto(clave,nombre):
    try:
        with sqlite3.connect("PrimerIntentoDemo.db") as conn:
            mi_cursor = conn.cursor() #! Conn es el puente, Cursos es el mensajero.
            valores ={"clave":campoClave,"nombre":campoNombre}
            mi_cursor.execute("INSERT INTO proyecto VALUES(:clave,:nombre)",valores)
    except Error as e:
        print(e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

continuar=True
while continuar:
    print()
    print("Dime los datos del proyecyp, pon 0 para terminar")
    print()
    campoClave=int(input("Clave de proyecto a agregar: "))
    if campoClave==0:
        continuar=False
    else:
        campoNombre=input("Nombre del proyecto a agregar: ")
        guardaProyecto(campoClave,campoNombre)
print("Se concluyo la carga de registros")