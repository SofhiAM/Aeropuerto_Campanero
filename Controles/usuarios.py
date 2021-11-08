from Ventanas.registro_usuario import registrodeUsuario
from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Qt
from Database.usuariosDB import *


class Usuarios (QWidget,registrodeUsuario):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.padre_ventana = parent
        self.setupUi(self)
        self.setWindowFlag (Qt.Window)

        self.bt_guardarRU.clicked.connect(self.agregar_usuario)

        print("h")
        
    def agregar_usuario(self):

        nom_usuario = self.lineEdit_Nombres.text()
        apell_usuario = self.lineEdit_Apellidos.text()
        tipoid_usuario = self.cb_TipodeID.currentText()
        id_usuario = self.lineEdit_Identificacion.text()
        correo_usuario = self.lineEdit_CorreoElectronico.text()
        contra_usuario = self.lineEdit_Contrasena.text()
        tipocuenta_usuario = self.cb_TipodeCuenta.currentText()

        analizar = (nom_usuario, apell_usuario, tipoid_usuario, id_usuario, correo_usuario, contra_usuario, tipocuenta_usuario)

        i=0; b= True

        while i < len(analizar) and b == True:
            if analizar[i] != "":
                i += 1
                b = True

            else:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("Para registrar el usuario deben estar todos\n"+
                            "los campos llenos.\n"+
                            "Por favor revise e intente de nuevo")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Critical)
                dlg.show()
                b = False

        if b == True: 
            datosusuario = (id_usuario, tipoid_usuario, nom_usuario, apell_usuario, correo_usuario, contra_usuario, tipocuenta_usuario)
            registrar_usuario(datosusuario)
            self.close()

            dlg = QMessageBox(self)
            dlg.setWindowTitle("Registro exitoso")
            dlg.setText("El usuario fue registrado con éxito. Actualice para ver los cambios")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Information)
            dlg.show()
                    
            return True
#-------------------------------------------------------------------------------------------------
    def borrar_datos_usuario (self, id_usuario):
        
        eliminar_id_usuario(id_usuario)

        return True
#-------------------------------------------------------------------------------------------------