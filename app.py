from PySide2.QtWidgets import QApplication
from Controles.ventanaPrincipal import Principal

if __name__ == "__main__":
    app = QApplication()
    ventana = Principal()
    ventana.show()

    app.exec_()
