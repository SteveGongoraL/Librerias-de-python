import sys
from PyQt5.QtWidgets import *

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Usando QRadioButton")
        self: setGeometry(50, 50, 350, 350)
        self.UI()

    def UI(self):
        self.nombre = QLineEdit(self)
        self.nombre.move(100, 50)
        self.nombre.setPlaceholderText("Introduce tu nombre")
        self.hombre = QRadioButton("hombre", self)
        self.hombre.move(100, 100)
        self.mujer = QRadioButton("mujer", self)
        self.mujer.move(200, 100)
        self.mujer.setChecked(True)
        botonPush = QPushButton("Enviar ", self)
        botonPush.move(140, 140)
        botonPush.clicked.connect(self.getEjecutar)

    def getEjecutar(self):
        minombre = self.nombre.text()
        if self.hombre.isChecked():
            print("Mi nombre es: " + minombre + ", tu sexo es: Hombre")
        else:
            print("Mi nombre es: " + minombre + ", tu sexo es: Mujer")

if __name__ == "__main__":
    app =  QApplication(sys.argv)
    window = Ventana()
    window.show()
    sys.exit(app.exec_())