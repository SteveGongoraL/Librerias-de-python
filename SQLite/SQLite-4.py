import sys
import sqlite3
from sqlite3 import Error
# Agrega un registro en una tabla

try:
    with sqlite3.connect("PrimerIntentoDemo.db") as conn:
        mi_cursor = conn.cursor() #! Conn es el puente, Cursos es el mensajero.
        mi_cursor.execute("INSERT INTO proyecto VALUES(1,'Piloto')")
        print("Registro agregado exitosamente")
except Error as e:
    print(e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")