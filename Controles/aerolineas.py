from Ventanas.registrar_aerolinea import regAerolinea
from Database.aeropuerto import *
from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Qt

class Aerolinea (QWidget, regAerolinea):

    def __init__ (self, parent = None):
        super().__init__(parent)

        self.padre_ventana = parent
        self.setupUi(self)
        self.setWindowFlag (Qt.Window)

        self.bt_saveAerolinea.clicked.connect(self.agregar_aerolinea)

    def agregar_aerolinea(self):
        
        nit = self.le_nit.text()
        nom_aerolinea = self.le_nombreAerolinea.text()
        cor_aerolinea = self.le_coraerolinea.text()
        tel_aerolinea = self.le_telaerolinea.text()

        analizar = (nit, nom_aerolinea, cor_aerolinea, tel_aerolinea)

        i=0; b= True

        while i < len(analizar) and b == True:
            if analizar[i] != "":
                i += 1
                b = True

            else:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("Para registrar la aerolínea deben estar todos\n"+
                            "los campos llenos.\n"+
                            "Por favor revise e intente de nuevo")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Critical)
                dlg.show()
                b = False

        if b == True: 
            datosAero = (nit, nom_aerolinea)
            datosCor = (nit, cor_aerolinea)
            datosTel = (nit, tel_aerolinea)

            registrar_aerolinea(datosAero)
            aerolinea_correo(datosCor)
            aerolinea_tel(datosTel)

            self.close()

            dlg = QMessageBox(self)
            dlg.setWindowTitle("Registro exitoso")
            dlg.setText("La aerolínea fue almacenada con éxito\n"+
                        "Actualice la tabla para ver los cambios realizados.")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Information)
            dlg.show()
                    
            return True        
        
    def borrar_datos_aerolinea (self, nit_aerolinea):

        eliminar_aerolinea(nit_aerolinea)
        eliminar_coraerolinea(nit_aerolinea)
        eliminar_telaerolinea(nit_aerolinea)

        return True







