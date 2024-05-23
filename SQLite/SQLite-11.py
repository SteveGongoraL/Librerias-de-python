import sys
import sqlite3
from sqlite3 import Error
# Leer todos los datos de una tabla con una condición.
valor_clave=int(input("Clave del proyecto a consultar: "))

try:
    with sqlite3.connect("PrimerIntentoDemo.db") as conn:
        mi_cursor = conn.cursor()
        valores = {"clave":valor_clave}
        mi_cursor.execute("SELECT * FROM proyecto WHERE clave = :clave", valores)
        registro = mi_cursor.fetchall()

        if registro:
            for clave, nombre in registro:
                print(f"{clave} \t", end="")
                print(nombre)
        else:
            print(f"No se encontro un proyecto asociado con la clave {valor_clave}")

except Error as e:
    print(e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")