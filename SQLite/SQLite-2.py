import sys
import sqlite3
from sqlite3 import Error
# Crea una tabla en SQLite3

try:
    with sqlite3.connect("PrimerIntentoDemo.db") as conn:
        c= conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS proyecto (clave INTEGER PRIMARY KEY, nombre TEXT NOT NULL);")
        print("Tabla creada exitosamente ")
except Error as e:
    print(e)
except:
    print(f'Se produjo el siguiente error: {sys.exc_info()[0]}')