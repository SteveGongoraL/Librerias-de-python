
import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "sumaresta.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.checksuma.stateChanged.connect(self.cambio)
        self.checkresta.stateChanged.connect(self.cambio)
        self.checkmultiplicacion.stateChanged.connect(self.cambio)
        self.checkdivdecimal.stateChanged.connect(self.cambio)
        self.checkdiventera.stateChanged.connect(self.cambio)

    def cambio(self):
        try:
            n1= float(self.num1.toPlainText())
            n2= float(self.num2.toPlainText())
            if self.checksuma.isChecked()==True:
                suma=n1+n2
                resultado_sum=str(suma)
                self.resultado.setText(resultado_sum)
            elif self.checkresta.isChecked()==True:
                resta=n1-n2
                resultado_res=str(resta)
                self.resultado.setText(resultado_res)
            elif self.checkmultiplicacion.isChecked()==True:
                multiplicacion=n1*n2
                resultado_mul=str(multiplicacion)
                self.resultado.setText(resultado_mul)
            elif self.checkdivdecimal.isChecked()==True:
                dividionDec=n1/n2
                resultado_div1=str(dividionDec)
                self.resultado.setText(resultado_div1)
            elif self.checkdiventera.isChecked()==True:
                divisionEnt=n1//n2
                resultado_div2=str(divisionEnt)
                self.resultado.setText(resultado_div2)
            else:
                self.resultado.setText("")
        except ValueError:
            self.resultado.setText("Dime los numeros a operar")

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
