import sys
from PyQt5.QtGui import QIcon, QRegExpValidator, QFont
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit


class ventanaPrincipal(QMainWindow):
    def __init__(self, parent=None):
        super(ventanaPrincipal, self).__init__(parent)

        self.setWindowTitle("QLineEdit en PyQt5 por: Jackers")
        self.setWindowIcon(QIcon("icono.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 400)
        self.initUI()

    def initUI(self):
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(20, 20, 360, 24)
        self.lineEdit.setText("Jackers")
        self.lineEdit.setAlignment(Qt.AlignLeft)
        self.lineEdit.setClearButtonEnabled(True)
        print(self.lineEdit.text())

        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setCapitalization(QFont.Capitalize)

        self.lineEdit.setFont(fuente)
        self.lineEdit.returnPressed.connect(
            lambda: print("Se presiono la tecla Enter..."))
        self.lineEdit.textChanged.connect(lambda: print("El texto cambio..."))
        self.lineEdit.textEdited.connect(
            lambda: print("El texto fue editado..."))

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    ventana = ventanaPrincipal()
    ventana.show()
    sys.exit(aplicacion.exec_())
