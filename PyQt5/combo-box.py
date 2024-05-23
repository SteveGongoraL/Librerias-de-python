import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

class Ui_Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("Marcas.ui",self)
        self.Boton_Aceptar.clicked.connect(self.obtenerObjeto)

    def obtenerObjeto(self):
        item=self.Opcion_Marcas.currentText()
        self.label_Lenguaje.setText("Seleccionaste la marca: "+ item)

app=QApplication(sys.argv)
dialogo = Ui_Dialog()
dialogo.show()
app.exec_()