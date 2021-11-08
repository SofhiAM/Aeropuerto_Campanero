from Ventanas.reprogramar_vuelo import reprogramarVuelo
from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Qt
from Database.aeropuerto import *

class ReprogramarVuelo (QWidget,reprogramarVuelo):
    def __init__(self,parent=None,id_vuelo=""):
        super().__init__(parent)
        self.padre_ventana = parent
        self.setupUi(self)
        self.setWindowFlag (Qt.Window)
        self.id_vuelo = id_vuelo
        self.traer_datos()

        self.bt_gagregarH_2.clicked.connect(self.actualizar_datos_vuelo)

    def traer_datos(self):
    
        self.lb_Identificador_7.setText(self.id_vuelo)

    def actualizar_datos_vuelo(self):
    
        id_vueloanterior = self.id_vuelo

        id_vuelo = id_vueloanterior
        nuevafecha = self.date_fechaUltimaRevision_6.date().toPython()
        nuevahora = self.time_HoraSalida.time().toPython()


        analizar = (id_vuelo, nuevafecha, nuevahora)
        print(analizar)
        i=0; b= True

        while i < len(analizar) and b == True:
            if analizar[i] != "":
                i += 1
                b = True

            else:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("Para editar el vuelo deben estar todos\n"+
                            "los campos llenos.\n"+
                            "Por favor revise e intente de nuevo")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Critical)
                dlg.show()
                b = False
                
        if b == True: 
            datosvuelo = (id_vuelo, nuevafecha, nuevahora)
            print (datosvuelo)
            print(self.id_vuelo )
            actualizar_vuelo(self.id_vuelo, datosvuelo)
            self.close()

            dlg = QMessageBox(self)
            dlg.setWindowTitle("Actualizacion exitosa")
            dlg.setText("El vuelo fue actualizado con éxito")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Information)
            dlg.show()
                    
            return True 
        
   
