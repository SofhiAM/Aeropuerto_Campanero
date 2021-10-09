from Ventanas.Ui_usuarios import usuarios
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt


class Usuarios (QWidget,usuarios):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.padre_ventana = parent
        self.setupUi(self)
        self.setWindowFlag (Qt.Window)

        