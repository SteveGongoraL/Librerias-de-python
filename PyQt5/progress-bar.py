import sys
from PyQt5.QtWidgets import QDialog, QApplication
from gestorDescargas import Ui_GestorDescargasDialog

class GestorDescargasApplication(QDialog):
    def __init__(self):
        super().__init__()
        self.ui= Ui_GestorDescargasDialog()
        self.ui.setupUi(self)
        self.ui.btn_iniciar_descarga.clicked.connect(self.iniciar_descarga)
        self.show()

    def iniciar_descarga(self):
        x=0
        while x < 100:
            x+= 1
            self.ui.pgb_descarga_archivos.setValue(x)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ventana=GestorDescargasApplication()
    ventana.show()
    sys.exit(app.exec_())
