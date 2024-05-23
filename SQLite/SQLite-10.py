import sys
import sqlite3
from sqlite3 import Error
# Leer todos los datos de una tabala.
valor_clave=int(input("Clave del proyecto a consultar: "))

try:
    with sqlite3.connect("PrimerIntentoDemo.db") as conn:
        mi_cursor = conn.cursor()
        valores = {"clave":valor_clave}
        mi_cursor.execute("SELECT * FROM proyecto WHERE clave = :clave", valores)
        registros = mi_cursor.fetchall()

        for registro in registros:
            print(registro)

except Error as e:
    print(e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")