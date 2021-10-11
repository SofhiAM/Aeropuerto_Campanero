from Ventanas.editar_avion  import editarAvion
from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Qt
from Database.avion_db import *

class Editar_Avion (QWidget,editarAvion):
    def __init__(self,parent=None,id_avion=""):
        super().__init__(parent)
        self.padre_ventana = parent
        self.setupUi(self)
        self.setWindowFlag (Qt.Window)
        self.id_avion = id_avion
        self.traer_datos()

        self.bt_aceptarAVEA.clicked.connect(self.actualizar_datos_avion)

    def traer_datos(self):

        nuevosdatos_avion = buscar_avion(self.id_avion)
        self.lineEdit_identificadorEA.setText(nuevosdatos_avion[0])
        self.lineEdit_modeloEA.setText(nuevosdatos_avion[3])


    def actualizar_datos_avion(self):

        id_avionanterior = self.id_avion

        id_avion = self.lineEdit_identificadorEA.text()
        tipo_avion = self.cb_pasajerosEA.currentText()
        propulsion = self.cb_PropulsionEA.currentText()
        modelo_avion = self.lineEdit_modeloEA.text()
        capacidad = self.spinBox_CapacidadEA.text()
        motores = self.spinBox_MotoresEA.text()
        peso = self.spinBox_pesoNomEA.text()


        analizar = (id_avion, tipo_avion, propulsion, modelo_avion, capacidad, motores, peso)
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
                
        if b == True: 
            datosavion = (id_avion, tipo_avion, capacidad)
            print (datosavion)
            print(self.id_avion)
            actualizar_avion(self.id_avion, datosavion)
            self.close()

            dlg = QMessageBox(self)
            dlg.setWindowTitle("Actualizacion exitosa")
            dlg.setText("El avion fue actualizado con éxito")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Information)
            dlg.show()
                    
            return True 