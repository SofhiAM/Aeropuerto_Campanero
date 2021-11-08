from PySide2.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QMessageBox
from Ventanas.agendar_vuelo import AgendarVuelo
from Database.aeropuerto import *
from Database.hangares_db import traer_todas_aerolineas
from PySide2.QtCore import Qt
import datetime
from datetime import datetime
from datetime import date
import time

class Agenda (QWidget, AgendarVuelo):

    def __init__ (self, parent = None):
        super().__init__(parent)

        self.padre_ventana = parent
        self.setupUi(self)
        self.setWindowFlag (Qt.Window)

        #Cargar combo aerolineas
        self.tabla_general_vuelos()
        self.cargar_combo_aerolineas()
        self.event_tabla_vuelo()
        
        self.bt_guardarAereolinea.clicked.connect(self.aceptar_vuelo)
        self.bt_regresarAereolinea.clicked.connect(self.denegar_vuelo)

# -----------------------------------------------------------------------------
    def cargar_combo_aerolineas(self):
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

# -------------------------------------------------------------------------------
    def tabla_general_vuelos (self):
        self.tb_agendAereolinea.setSelectionBehavior(QAbstractItemView.SelectRows) 
        header = self.tb_agendAereolinea.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        self.tb_agendAereolinea.verticalHeader().setDefaultAlignment(Qt.AlignHCenter)
        self.tb_agendAereolinea.resizeColumnsToContents()

# -------------------------------------------------------------------------------
    def cargar_tabla_vuelos (self):
        aerolinea = self.cb_Aerolinea.currentText()
        print(aerolinea)
        nit = consultar_aerolinea(aerolinea)
        print(nit)

        characters = "(,')"
        i=0 
        while i < len(nit):
            string = str(nit [i])
            for x in range(len(characters)):
                string = string.replace(characters[x],"")
            i += 1

        print(string)
        datos = traer_vuelos_espera(string)
        print (datos)

        self.tb_agendAereolinea.setRowCount(len(datos))

        for(index_fila, fila) in enumerate(datos):
            #indice, datos
            for (index_celda, celda) in enumerate(fila):
                self.tb_agendAereolinea.setItem(index_fila, index_celda, 
                QTableWidgetItem(str(celda)))

# ---------------------------------------------------------------------------------
    def event_tabla_vuelo (self):
        self.cb_Aerolinea.activated.connect(self.cargar_tabla_vuelos)
# ---------------------------------------------------------------------------------
    def aceptar_vuelo (self):
        vuelo_seleccionado = self.tb_agendAereolinea.selectedItems()

        if vuelo_seleccionado:
            id_vuelo= vuelo_seleccionado[2].text()
            print (id_vuelo)
            vuelo = vuelo_seleccionado[0].row()

            # Mensaje de confirmación de si quiere borrar la aerolinea
            dlg = QMessageBox.question(self, "Guardar Vuelo", 
                        "¿Esta seguro que quiere agendar este vuelo?", 
                        QMessageBox.Ok, QMessageBox.Cancel)

            #Si presiona Ok 
            if dlg == QMessageBox.Ok:
                if aceptar_vuelo(id_vuelo):
                    self.tb_agendAereolinea.removeRow(vuelo)
                    QMessageBox.information(self, "Agendado", "Vuelo agendado con éxito", QMessageBox.Ok)

        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para agendar un vuelo primero debe seleccionarlo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()

# ---------------------------------------------------------------------------------
    def denegar_vuelo (self):
        vuelo_seleccionado = self.tb_agendAereolinea.selectedItems()

        if vuelo_seleccionado:
            id_vuelo= vuelo_seleccionado[2].text()
            print (id_vuelo)
            vuelo = vuelo_seleccionado[0].row()

            # Mensaje de confirmación de si quiere borrar la aerolinea
            dlg = QMessageBox.question(self, "Regresar Vuelo", 
                        "¿Esta seguro que quiere regresar este vuelo?", 
                        QMessageBox.Ok, QMessageBox.Cancel)

            #Si presiona Ok 
            if dlg == QMessageBox.Ok:
                if rechazar_vuelo(id_vuelo):
                    self.tb_agendAereolinea.removeRow(vuelo)
                    QMessageBox.information(self, "Denegado", "Vuelo regresado a la aerolinea", QMessageBox.Ok)

        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para regresar un vuelo primero debe seleccionarlo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()


