import cx_Oracle
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

def guardar_proyecto(item0,item1,item2):
    try:
        conexion = cx_Oracle.connect('HR/hr@127.0.0.1:1521/xepdb1')
        cursor= conexion.cursor()
        valores = {"MATRICULA":item0, "NOMBRE":item1, "PROMEDIO":item2}
        statement="INSERT INTO PROMEDIO(MATRICULA, NOMBRE, PROMEDIO) VALUES (:1, :2, :3)"
        cursor.execute(statement, (item0, item1, item2))
        conexion.commit()
        print("SE HAN GUARDADO LOS DATOS!!")
    except Exception as e:
        print(str(e))
    finally:
        cursor.close()
        conexion.close()

class Ui_Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("promedio.ui",self)
        self.Boton_Guardar.clicked.connect(self.guardar)

    def guardar(self):
        item0= int(self.val0.toPlainText())
        item1= str(self.val1.toPlainText())
        item2= float(self.val2.toPlainText())
        guardar_proyecto(item0,item1,item2)
        self.label_Comentario.setText("Se ha guardado la información")

app=QApplication(sys.argv)
dialogo = Ui_Dialog()
dialogo.show()
app.exec_()
