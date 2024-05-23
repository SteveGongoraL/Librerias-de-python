import sqlite3
from sqlite3 import Error

try:
    with sqlite3.connect('PrimerIntento.db') as conn:
        # El nombre es del archivo que quieres abrir.
        print(sqlite3.version)
except Error as e:
    print (e)