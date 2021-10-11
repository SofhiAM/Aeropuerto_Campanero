from Ventanas.editar_usuario  import editarUsuario
from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Qt
from Database.usuariosDB import *

class Editar_usuarios (QWidget,editarUsuario):
    def __init__(self,parent=None,id_usuario=""):
        super().__init__(parent)
        self.padre_ventana = parent
        self.setupUi(self)
        self.setWindowFlag (Qt.Window)
        self.id_usuario = id_usuario
        self.traer_datos()

        self.bt_Guardar.clicked.connect(self.actualizar_datos_usuario)

    def traer_datos(self):
        self.lineEdit_Contrasena.setDisabled(True)

        nuevosdatos_usuario = buscar_usuario(self.id_usuario)
        self.lineEdit_Nombres.setText(nuevosdatos_usuario[2])
        self.lineEdit_Apellidos.setText(nuevosdatos_usuario[3])
        self.lineEdit_Identificacion.setText(str(nuevosdatos_usuario[0]))
        self.lineEdit_CorreoElectronico.setText(nuevosdatos_usuario[4])
        self.lineEdit_Contrasena.setText(nuevosdatos_usuario[5])

    def actualizar_datos_usuario(self):

        id_usuarioanterior = self.id_usuario

        nom_usuario = self.lineEdit_Nombres.text()
        apell_usuario = self.lineEdit_Apellidos.text()
        tipoid_usuario = self.cb_TipodeID.currentText()
        id_usuario = self.lineEdit_Identificacion.text()
        correo_usuario = self.lineEdit_CorreoElectronico.text()
        nuevacontra_usuario = self.lineEdit_nuevacontrasena.text()
        tipocuenta_usuario = self.cb_TipodeCuenta.currentText()

        analizar = (nom_usuario, apell_usuario, tipoid_usuario, id_usuario, correo_usuario, tipocuenta_usuario)
        print(analizar)
        i=0; b= True

        while i < len(analizar) and b == True:
            if analizar[i] != "":
                i += 1
                b = True

            else:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("Para editar el usuario deben estar todos\n"+
                            "los campos marcados llenos.\n"+
                            "Por favor revise e intente de nuevo")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Critical)
                dlg.show()
                b = False

        if nuevacontra_usuario == "":
            nuevacontra_usuario = self.lineEdit_Contrasena.text()

        if b == True: 
            datosusuario = (id_usuario, tipoid_usuario, nom_usuario, apell_usuario, correo_usuario, nuevacontra_usuario, tipocuenta_usuario)
            print (datosusuario)
            print(self.id_usuario)
            actualizar_usuario(self.id_usuario, datosusuario)
            self.close()

            dlg = QMessageBox(self)
            dlg.setWindowTitle("Actualizacion exitosa")
            dlg.setText("El usuario fue actualizado con éxito")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Information)
            dlg.show()
                    
            return True 

        