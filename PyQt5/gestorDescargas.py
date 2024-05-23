from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GestorDescargasDialog(object):
    def setupUi(self, GestorDescargasDialog):
        GestorDescargasDialog.setObjectName("GestorDescargasDialog")
        GestorDescargasDialog.resize(400, 127)
        self.lbl_descarga_archivos = QtWidgets.QLabel(GestorDescargasDialog)
        self.lbl_descarga_archivos.setGeometry(QtCore.QRect(160, 10, 101, 20))
        self.lbl_descarga_archivos.setObjectName("lbl_descarga_archivos")
        self.pgb_descarga_archivos = QtWidgets.QProgressBar(GestorDescargasDialog)
        self.pgb_descarga_archivos.setGeometry(QtCore.QRect(20, 40, 361, 23))
        self.pgb_descarga_archivos.setProperty("value", 0)
        self.pgb_descarga_archivos.setObjectName("pgb_descarga_archivos")
        self.btn_iniciar_descarga = QtWidgets.QPushButton(GestorDescargasDialog)
        self.btn_iniciar_descarga.setGeometry(QtCore.QRect(170, 90, 75, 23))
        self.btn_iniciar_descarga.setObjectName("btn_iniciar_descarga")

        self.retranslateUi(GestorDescargasDialog)
        QtCore.QMetaObject.connectSlotsByName(GestorDescargasDialog)

    def retranslateUi(self, GestorDescargasDialog):
        _translate = QtCore.QCoreApplication.translate
        GestorDescargasDialog.setWindowTitle(_translate("GestorDescargasDialog", "Gestor Descarga"))
        self.lbl_descarga_archivos.setText(_translate("GestorDescargasDialog", "Descarga Archivos"))
        self.btn_iniciar_descarga.setText(_translate("GestorDescargasDialog", "Iniciar"))
