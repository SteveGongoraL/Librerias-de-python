import cx_Oracle

def guardar_proyecto(val0,val1,val2):
    try:
        conexion = cx_Oracle.connect('HR/hr@127.0.0.1:1521/xepdb1') # (xepdb1) nombre usuario-pasword-ip-esquema que usaremos.
        cursor= conexion.cursor()
        valores = {"matricula":val0, "nombre":val1, "promedio":val2}
        cursor.execute("INSERT INTO PROMEDIO2 VALUES(:matricula,:nombre,:promedio)", valores)
        print("SE HAN GUARDADO LOS DATOS")
    except Exception as e:
        print(str(e))
    finally:
        cursor.close()
        conexion.close()


def guardar_proyecto1(val0,val1,val2):
    try:
        conn_str='HR/HR@127.0.0.1:1521/XE'
        db_conn = cx_Oracle.connect(conn_str)
        cursor = db_conn.cursor()
        valores = {"matricula":val0, "nombre":val1, "promedio":val2}
        cursor.execute("INSERT INTO promedio VALUES(:matricula,:nombre,:promedio)", valores)
        print("SE HAN GUARDADO LOS DATOS")
    except Exception as e:
        print(str(e))
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        cursor.close()
        conexion.close()


#Funciona.
def guardar_proyecto(item0,item1,item2):
    try:
        conexion = cx_Oracle.connect('HR/hr@127.0.0.1:1521/xepdb1') # (xepdb1) nombre usuario-pasword-ip-esquema que usaremos.
        cursor= conexion.cursor()
        valores = {"MATRICULA":item0, "NOMBRE":item1, "PROMEDIO":item2}
        #cursor.execute("INSERT INTO PROMEDIO2 VALUES(:matricula,:promedio)",valores)
        statement="INSERT INTO PROMEDIO(MATRICULA, NOMBRE, PROMEDIO) VALUES (:1, :2, :3)"
        cursor.execute(statement, (item0, item1, item2))
        conexion.commit()
        #cursor.execute("CREATE TABLE Materias (Clave INT PRIMARY KEY, NombreMateria INT NOT NULL)")
        print("SE HAN GUARDADO LOS DATOS")
    except Exception as e:
        print(str(e))
    finally:
        cursor.close()
        conexion.close()
