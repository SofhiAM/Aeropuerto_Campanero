from Ventanas.Ui_login import Form
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt


class LoginControles (QWidget,Form):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.padre_ventana = parent
        self.setupUi(self)
        self.setWindowFlag (Qt.Window)
        self.bt_ingresarlg.clicked.connect(self.verificacion)

    def verificacion(self):

        correoVentana = self.correo()
        contraVentana = self.lgcontra_lineEdit_2.text()

        if contraVentana == "xx":

            self.close()
        else:
            print(correoVentana)

    def correo(self):
        correo = self.correo_lineEdit.text()
        return correo

    