import sys
import sqlite3
from sqlite3 import Error
# Agregar un registro en una tabla utilizando placeholder(?,?,...,?)

try:
    with sqlite3.connect("PrimerIntentoDemo.db") as conn:
        mi_cursor = conn.cursor() #! Conn es el puente, Cursos es el mensajero.
        valores =(2, "Segundo piloto")
        mi_cursor.execute("INSERT INTO proyecto VALUES(?,?)",valores)
        print("Registro agregado exitosamente")
except Error as e:
    print(e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")