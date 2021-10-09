from Ventanas.ocupar_hangar import ocuparHangar
from Database.hangares_db import *
from Database.aeropuerto import *
from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Qt


class Hangares (QWidget,ocuparHangar):

    def __init__(self,parent=None, cod_hangar=""):
        super().__init__(parent)

        self.padre_ventana = parent
        self.setupUi(self)
        self.setWindowFlag (Qt.Window)
        self.cod_hangar= cod_hangar
        self.cargar_aerolineas()

        #Boton ocupar hangar
        self.bt_ocuparHangar.clicked.connect(self.ocupar_hangar)

        
# ----------------------------------------------------------------------------------
    def cargar_aerolineas (self):
        aerolineas = traer_todas_aerolineas()
        
        #Aquí se convierte los valores de la tupla a str y sin esos caracteres
        characters = "(,')"
        i=0 
        while i < len(aerolineas):
            string = str(aerolineas [i])
            for x in range(len(characters)):
                string = string.replace(characters[x],"")
        
        # Aquí se manda ese string ya listo al combo box    
            self.cb_Aerolinea.addItem(str(string))
            i += 1
# -----------------------------------------------------------------------------------
        
    def ocupar_hangar(self):
        #print(cod_hangar)
        codigoAvion = self.lineEdit_CodigoAvion.text()
        modeloAvion = self.lineEdit_ModelodelAvion.text()
        fechaentrada = self.dateEdit_Fechaentrada.date().toPython()
        horaentrada = self.timeEdit_Horaentrada.time().toPython()
        valorhora = self.cb_Valorporhora.currentText()
        aerolinea = self.cb_Aerolinea.currentText()
        
        analizar = (self.cod_hangar, codigoAvion, modeloAvion, fechaentrada, 
                    horaentrada, valorhora, aerolinea)

        i=0; b= True

        while i < len(analizar) and b == True:
            if analizar[i] != "":
                i += 1
                b = True

            else:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("Para ocupar el hangar todos los\n"+
                            "campos deben estar llenos.\n"+
                            "Por favor revise e intente de nuevo")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Critical)
                dlg.show()
                b = False

        if b == True: 
            #Aqui va todo lo de la base de datos
            alquiler = (self.cod_hangar, codigoAvion, fechaentrada, 
                    horaentrada, valorhora, aerolinea)
            
            if alquilar_hangar(alquiler):
                self.close ()
                
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Ocupacion de Hangar")
                dlg.setText("Se ha ocupado el Hangar con exito\n"+
                            "Actualice la tabla para ver los cambios realizados.")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Information)
                dlg.show()

                self.cambiar_estado_hangar()

# ------------------------------------------------------------------------------------
    def cambiar_estado_hangar(self):
        hangar = consultar_estado_hangar(self.cod_hangar)

        string = str(hangar)
        characters = "(,')"
        
        for x in range(len(characters)):
            string = string.replace(characters[x],"")
        
        if string == "LIBRE":
            cambiar_estado_aocupado(self.cod_hangar)
        
        elif string == "OCUPADO":
            cambiar_estado_alibre(cod_hangar)

# --------------------------------------------------------------------------------------
        


