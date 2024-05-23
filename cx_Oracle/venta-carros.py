import cx_Oracle
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

def guardar_proyecto(item0, item1, item2):
    try:
        conexion = cx_Oracle.connect("HR/hr@127.0.0.1:1521/xepdb1") #Usuario,Contraseña,IP,Puerto,Servicio.
        cursor = conexion.cursor()
        valores = {"MODELO": item0, "PRECIO": item1, "COLOR": item2}
        statement = "INSERT INTO AUTOS(MODELO, PRECIO, COLOR) VALUES (:1, :2, :3)"
        cursor.execute(statement, (item0, item1, item2))
        conexion.commit()
        print("Se han guardado los datos!!")
    except Exception as e:
        print(str(e))
    finally:
        cursor.close()
        conexion.close()

class Ui_Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("carros.ui", self)
        self.Boton_Guardar.clicked.connect(self.guardar)

    def guardar(self):
        item0 = str(self.val0.toPlainText())
        item1 = float(self.val1.toPlainText())
        item2 = str(self.val2.toPlainText())
        guardar_proyecto(item0, item1, item2)
        self.label_Comentario.setText("Los datos fueron guardados con exito!")

app = QApplication(sys.argv)
dialogo = Ui_Dialog()
dialogo.show()
app.exec_()
