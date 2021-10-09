from Ventanas.crear_vuelo import CrearVuelo
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QMessageBox, QTableWidget
from Database.aeropuerto import consultar_aerolinea, consultar_avion, seleccionar_avion, crear_vuelo, crear_avion, seleccionar_todos_pilotos, seleccionar_todos_vuelos, borrar_vuelo
from Database.hangares_db import traer_todas_aerolineas
from PySide2.QtCore import Qt


class Vuelos (QWidget,CrearVuelo):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        self.padre_ventana = parent
        self.setupUi(self)
        self.setWindowFlag (Qt.Window)
        self.conCopiloto = False
        self.nbt_asigCopi.setEnabled(False)
        self.bt_guardarTodo.setEnabled(False)

        #Botones multiplataforma
        self.bt_addVuelo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_agregarVuelo))
        self.bt_eliminarVuelo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_eliminarVuelo))

        #Cargar tabla pilotos
        self.tabla_pilotos()
        self.cargar_tabla_pilotos(seleccionar_todos_pilotos())

        #Cargar tabla vuelos eliminar
        self.tabla_eliminar_vuelos()
        self.cargar_tabla_eliminar_vuelos(seleccionar_todos_vuelos())

        #Combo
        self.cargar_combo_aerolineas()

        #Aceptar general
        self.bt_aceptarGEN.clicked.connect(self.verificacion_campos_general)

        #Aceptar avion
        self.bt_aceptarAV.clicked.connect(self.verificacion_campos_avion)

        #Asignar piloto
        self.bt_asigPiloto.clicked.connect(self.traer_info_piloto)

        #Asignar copiloto
        self.nbt_asigCopi.clicked.connect(self.traer_info_copiloto)

        #Boton Guardar Vuelo
        self.bt_guardarTodo.clicked.connect(self.inf_vuelo)

        #Boton Borrar vuelo
        self.bt_eliminarUNVuelo.clicked.connect(self.eliminar_vuelo)

# ///////////////////////////////////// CREAR VUELOS /////////////////////////////////////////

    def verificacion_campos_general (self):
        tipo_vuelo = self.cb_tipovuelo.currentText()
        cod_vuelo = self.textedit_codigovuelo.text()
        aerolinea = self.cb_aerolinea.currentText()

        fsalida = self.date_FechaSalida.date().toPython()
        hsalida = self.time_HoraSalida.time().toPython()
        fllegada = self.date_FechaLlegada.date().toPython()
        hllegada = self.time_HoraLlegada.time().toPython()

        destino = self.cb_Destino.currentText()
        origen = self.cb_Origen.currentText()

        general = (tipo_vuelo, cod_vuelo, aerolinea, fsalida, hsalida, fllegada, hllegada,
                    destino, origen)
        
        i=0; b= True

        while i < len(general) and b == True:
            if general[i] != "":
                i += 1
                b = True

            else:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("Para guardar la información general todos los\n"+
                            "campos deben estar llenos.\n"+
                            "Por favor revise e intente de nuevo")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Critical)
                dlg.show()
                b = False
        print("revisado, pasa av")
        print (general)
        return b

# -------------------------------------------------------------------------------------
    def info_general (self):
        
        #Recuperar Información        
        tipo_vuelo = self.cb_tipovuelo.currentText()
        cod_vuelo = self.textedit_codigovuelo.text()
        aerolinea = self.cb_aerolinea.currentText()

        fsalida = self.date_FechaSalida.date().toPython()
        hsalida = self.time_HoraSalida.time().toPython()
        fllegada = self.date_FechaLlegada.date().toPython()
        hllegada = self.time_HoraLlegada.time().toPython()

        destino = self.cb_Destino.currentText()
        origen = self.cb_Origen.currentText()

        general = (tipo_vuelo, cod_vuelo, aerolinea, fsalida, hsalida, fllegada, hllegada,
                    destino, origen)
        
        i=0; b= True

        while i < len(general) and b == True:
            if general[i] != "":
                i += 1
                b = True

            else:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("Para guardar la información general todos los\n"+
                            "campos deben estar llenos.\n"+
                            "Por favor revise e intente de nuevo")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Critical)
                dlg.show()
                b = False

        if b == True:
            nit = consultar_aerolinea(aerolinea)
            
            informacion = (cod_vuelo, tipo_vuelo, destino, origen, fsalida, hsalida, nit)
            
            print("revisado, pasa")
            return informacion
# ------------------------------------------------------------------------------
    def verificacion_campos_avion (self):
        identificador = self.textedit_identificador.text()
        tipo_avion = self.cb_tipodeAvion.currentText()
        propulsion = self.cb_Propulsion.currentText()
        modelo = self.cb_Modelo.currentText()
        capacidad = int(self.spinBox_Capacidad.value())
        motores = int(self.spinBox_Motores.value())
        peso = int(self.spinBox_pesoNom.value())

        if tipo_avion == "Pasajeros":
            self.conCopiloto = True

        avion = (identificador, tipo_avion, propulsion, modelo, capacidad, motores, peso)
                    
        i=0; b= True

        while i < len(avion) and b == True:
            if avion[i] != "":
                i += 1
                b = True

            else:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("Para guardar la información del avión todos los\n"+
                            "campos deben estar llenos.\n"+
                            "Por favor revise e intente de nuevo")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Critical)
                dlg.show()
                b = False
        print("revisado, pasa trip")
        print (avion)
        return b

# ------------------------------------------------------------------------------
    def info_avion (self):
        identificador = self.textedit_identificador.text()
        tipo_avion = self.cb_tipodeAvion.currentText()
        propulsion = self.cb_Propulsion.currentText()
        modelo = self.cb_Modelo.currentText()
        capacidad = int(self.spinBox_Capacidad.value())
        motores = int(self.spinBox_Motores.value())
        peso = int(self.spinBox_pesoNom.value())

        if tipo_avion == "Pasajeros":
            self.conCopiloto = True

        avion = (identificador, tipo_avion, propulsion, modelo, capacidad, motores, peso)
                    
        i=0; b= True

        while i < len(avion) and b == True:
            if avion[i] != "":
                i += 1
                b = True

            else:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("Para guardar la información del avión todos los\n"+
                            "campos deben estar llenos.\n"+
                            "Por favor revise e intente de nuevo")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Critical)
                dlg.show()
                b = False

        if b == True:
            return avion

# -------------------------------------------------------------------------------
    def traer_info_piloto (self):
                
        piloto_seleccionado = self.tableWidget.selectedItems()

        if self.conCopiloto == True:
            self.nbt_asigCopi.setEnabled(True)
        
        else:
            self.bt_guardarTodo.setEnabled(True)

        if piloto_seleccionado:
            id_piloto = piloto_seleccionado[0].text()

            print(id_piloto)
            return id_piloto

        else: 
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para guardar la información del piloto debe seleccionar\n"+
                        "uno de los disponibles en la tabla.\n"+
                        "Por favor revise e intente de nuevo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()
        

# -------------------------------------------------------------------------------
    def traer_info_copiloto (self):
        
        if self.conCopiloto == True:
            copiloto_seleccionado = self.tableWidget.selectedItems()

            if copiloto_seleccionado:
                id_copiloto = copiloto_seleccionado[0].text()

            else: 
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("Para guardar la información del copiloto debe seleccionar\n"+
                            "uno de los disponibles en la tabla.\n"+
                            "Por favor revise e intente de nuevo")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Critical)
                dlg.show()
        
        else:
            id_copiloto = 0
            
        self.bt_guardarTodo.setEnabled(True)
        print(id_copiloto)
        return id_copiloto

# ------------------------------------------------------------------------------------
    def inf_vuelo (self):
        general = self.info_general()
        avion = self.info_avion()
        piloto = self.traer_info_piloto()
        
        if self.conCopiloto == True:
            copiloto = self.traer_info_copiloto()
        else:
            copiloto = 0

        informacion_vuelo = (general [0],general [1], avion[1],general [2],general [3],general [4],general [5],general [6],avion[0], piloto, copiloto)
        
        self.vuelo_crear(informacion_vuelo)
        self.actualizar_tb_eliminar_vuelos()
        
# ----------------------------------------------------------------------------------        
    def vuelo_crear(self, info_vuelo):
        crear_vuelo(info_vuelo)
        print("vuelo creado")

# ------------------------------------------------------------------------------------
    def tabla_pilotos (self):
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        self.tableWidget.verticalHeader().setDefaultAlignment(Qt.AlignHCenter)
        self.tableWidget.resizeColumnsToContents()

# -------------------------------------------------------------------------------------
    def cargar_tabla_pilotos(self, data):
        self.tableWidget.setRowCount(len(data))

        for(index_fila, fila) in enumerate(data):
            #indice, datos
            for (index_celda, celda) in enumerate(fila):
                self.tableWidget.setItem(index_fila, index_celda, 
                QTableWidgetItem(str(celda)))
    
# --------------------------------------------------------------------------------------
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
            self.cb_aerolinea.addItem(str(string))
            i += 1

# -----------------------------------------------------------------------------------
    def tabla_eliminar_vuelos (self):
        header = self.tb_vistaGeneralED.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        self.tb_vistaGeneralED.verticalHeader().setDefaultAlignment(Qt.AlignHCenter)
        self.tb_vistaGeneralED.resizeColumnsToContents()

# ------------------------------------------------------------------------------------
    def cargar_tabla_eliminar_vuelos(self,data):
        self.tb_vistaGeneralED.setRowCount(len(data))

        for(index_fila, fila) in enumerate(data):
            #indice, datos
            for (index_celda, celda) in enumerate(fila):
                self.tb_vistaGeneralED.setItem(index_fila, index_celda, 
                QTableWidgetItem(str(celda)))
    
# -------------------------------------------------------------------------------------
    def actualizar_tb_eliminar_vuelos(self):
        data = seleccionar_todos_vuelos()
        self.cargar_tabla_eliminar_vuelos(data)
    
# ////////////////////////////////// ELIMINAR VUELOS ////////////////////////////////////////
    def eliminar_vuelo (self):
        vuelo_seleccionado = self.tb_vistaGeneralED.selectedItems()

        if vuelo_seleccionado:
            id_vuelo = vuelo_seleccionado[0].text()
            print (id_vuelo)
            vuelo = vuelo_seleccionado[0].row()

            if borrar_vuelo(id_vuelo):
                self.tb_vistaGeneralED.removeRow(vuelo)

        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para eliminar un vuelo, primero tiene que seleccionar uno de ellos.\n"+
                        "Por favor revise e intente de nuevo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()