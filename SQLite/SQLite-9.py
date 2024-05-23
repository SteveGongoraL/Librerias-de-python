import sys
import sqlite3
from sqlite3 import Error
# Leer todos los datos de una tabla.

try:
    with sqlite3.connect("PrimerIntentoDemo.db") as conn:
        mi_cursor = conn.cursor()
        mi_cursor.execute("SELECT * FROM proyecto")
        registros = mi_cursor.fetchall()

        print("\nClave\tNombre")
        print("°" * 20)
        for clave, nombre in registros:
            print(f"{clave}\t", end="")
            print(nombre)
except Error as e:
    print(e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")