from Ventanas.crear_vuelo import CrearVuelo
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QMessageBox
from Database.aeropuerto import consultar_aerolinea, consultar_avion, seleccionar_avion, crear_vuelo, crear_avion, seleccionar_todos_pilotos, seleccionar_todos_vuelos, borrar_vuelo, cod_tripulacion_pasajeros, cod_tripulacion_carga, traer_tripulacion, consulta_tipo_vuelo, cod_piloto_copiloto
from Database.hangares_db import traer_todas_aerolineas
from Database.avion_db import comprobar_id, buscar_avion
from PySide2.QtCore import Qt


class Vuelos (QWidget,CrearVuelo):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        self.padre_ventana = parent
        self.setupUi(self)
        self.setWindowFlag (Qt.Window)
        #self.bt_guardarTodo.setEnabled(False)
        self.conCopiloto = False

        
        #Cargar tabla pilotos
        self.cargar_tripulacion()
        
        #Combo
        self.cargar_combo_aerolineas()
        self.cargar_combo_idaviones()

        # #Aceptar general
        self.bt_aceptarGEN.clicked.connect(self.verificacion_campos_general)

        # #Aceptar avion
        self.bt_aceptarAV.clicked.connect(self.verificacion_campos_avion)

        #Boton Guardar Vuelo
        self.bt_guardarTodo.clicked.connect(self.inf_vuelo)

        # #Evento del combo, para que cuando se seleccione llegada se bloquee destino
        # # y cuando se seleccione salida se bloquee origen.
        self.bloqueo_combo_box()
        self.event_tipo_vuelo()

        #Boton check avion
        self.bt_check.clicked.connect(self.cargar_info_avion)

# ///////////////////////////////////// CREAR VUELOS /////////////////////////////////////////
# --------------------------------------------------------------------------------------------
    def event_tipo_vuelo (self):
        self.cb_tipovuelo.activated.connect(self.bloqueo_combo_box)
    
    def bloqueo_combo_box(self):
        tipo_vuelo = self.cb_tipovuelo.currentText()
        ciudades =("Cali", "Bogota", "Cartagena", "Pasto", "Pereira")

        if tipo_vuelo == "Llegada":
            self.cb_Destino.clear()
            self.cb_Origen.clear()
            self.cb_Destino.setDisabled (True)
            self.cb_Origen.setDisabled (False)

            #Combo origen
            self.cb_Origen.addItems(ciudades)
            #Combo destino = Medellín
            self.cb_Destino.addItem("Medellín")
            
        if tipo_vuelo == "Salida":
            self.cb_Destino.clear()
            self.cb_Origen.clear()
            self.cb_Origen.setDisabled (True)
            self.cb_Destino.setDisabled (False)

            #Combo origen = Medellín
            self.cb_Origen.addItem("Medellín")
            #Combo destino 
            self.cb_Destino.addItems(ciudades)

# ===================================== GENERAL ========================================
## ------------------------------------------------------------------------------------
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
                b=False

        if b == True:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Siguiente")
            dlg.setText("Datos completamente llenos.\n"+
                        "Puede pasar a llenar los datos de avión.")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Information)
            dlg.show()
            
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para guardar la información general todos los\n"+
                        "campos deben estar llenos.\n"+
                        "Por favor revise e intente de nuevo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()
        print("revisado, pasa av")
        print (general)

# # -------------------------------------------------------------------------------------
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

            aerolinea = consultar_aerolinea(aerolinea)
            
            informacion = (cod_vuelo, tipo_vuelo, destino, origen, fsalida, hsalida, aerolinea)
            
            print("revisado, pasa")
            return informacion

# =================================== AVION =======================================
# # ------------------------------------------------------------------------------
    def verificacion_campos_avion (self):
        self.cargar_tripulacion()
        self.event_tripulacion()

        identificador = self.cb_identificador.currentText()

        if identificador == '':
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para guardar la información del avión debe seleccionar\n"+
                        "uno de ellos.\n"+
                        "Por favor revise e intente de nuevo. Puede que no haya alguno registrado")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()
            b = True

        else: 
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Siguiente")
            dlg.setText("Datos completamente llenos.\n"+
                        "Puede pasar a seleccionar tripulación.")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Information)
            dlg.show()
            
        print("revisado, pasa trip")
        #print (avion)
        
# # ------------------------------------------------------------------------------
    def info_avion (self):

        identificador = self.cb_identificador.currentText()
        tipo_avion = self.te_tipoAvion.text()
        propulsion = self.te_propulsion.text()
        modelo = self.te_modelo.text()
        capacidad = int(self.te_capacidad.text()[:-2])
        motores = int(self.te_motores.text())
        peso = int(self.te_peso.text()[:-2])

        avion = (identificador, tipo_avion, propulsion, modelo, capacidad, motores, peso)
        print(avion)
                    
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

# =================================== TRIPULACIÓN ====================================
    def cargar_combo_tripulación (self):
        if self.cb_CodigoTripulacion.count() != 0:
            self.cb_CodigoTripulacion.clear()

        #Consultar que tipo de vuelo se hará
        cod_avion = self.cb_identificador.currentText()
        tipo_vuelo = consulta_tipo_vuelo(cod_avion)
        print (tipo_vuelo)
        
        characters = "(,')"

        string = str(tipo_vuelo)
        for x in range(len(characters)):
            string = string.replace(characters[x],"")

        if string == 'Pasajeros':
            tripu = cod_tripulacion_pasajeros()
        else:
            tripu = cod_tripulacion_carga()
        
        #Aquí se convierte los valores de la tupla a str y sin esos caracteres
        
        i=0 
        while i < len(tripu):
            string = str(tripu [i])
            for x in range(len(characters)):
                string = string.replace(characters[x],"")
        
        # Aquí se manda ese string ya listo al combo box    
            self.cb_CodigoTripulacion.addItem(str(string))
            i += 1

# --------------------------------------------------------------------------------
    def event_tripulacion (self):
        self.cb_CodigoTripulacion.activated.connect(self.cargar_tripulacion)

    def cargar_tripulacion (self):

        id_trip = self.cb_CodigoTripulacion.currentText()
        print(id_trip)
        
        data = traer_tripulacion(id_trip)

        self.tableWidget.setRowCount(len(data))

        for(index_fila, fila) in enumerate(data):
            #indice, datos
            for (index_celda, celda) in enumerate(fila):
                self.tableWidget.setItem(index_fila, index_celda, 
                QTableWidgetItem(str(celda)))
# # ------------------------------------------------------------------------------
    def traer_info_piloto (self):
        
        #Consultar que tipo de vuelo se hará
        cod_avion = self.cb_identificador.currentText()
        tipo_vuelo = consulta_tipo_vuelo(cod_avion)

        characters = "(,')"
        i=0 
        while i < len(tipo_vuelo):
            stringtv = str(tipo_vuelo[i])
            for x in range(len(characters)):
                stringtv = stringtv.replace(characters[x],"")
            i += 1

        print (stringtv)

        tripulacion = cod_piloto_copiloto(self.cb_CodigoTripulacion.currentText())
        print (tripulacion)
        print(len(tripulacion))
        
        codigos=[]
        characters = "(,')"
        i=0 
        while i < len(tripulacion):
            string = str(tripulacion[i])
            for x in range(len(characters)):
                string = string.replace(characters[x],"")
            codigos.append(string)
            i +=1

        print ("codigos = ",codigos)
        print(len(codigos))

        if stringtv == "Pasajeros":
            id_piloto = float(codigos[0])
            id_copiloto = codigos[1][:-2]

        elif stringtv == "Carga": 
            id_piloto = float(codigos[0])
            id_copiloto = 0
        
        #print (id_piloto, id_copiloto)
        return (id_piloto, id_copiloto)
# # ------------------------------------------------------------------------------------
    def inf_vuelo (self):
        general = self.info_general()
        avion = self.info_avion()
        piloto = self.traer_info_piloto()
        
        print(general)
        print (avion)
        print(piloto)
        # id_vuelo, tipo_vuelo, vuelo_pascar, destino, origen, fecha_vuelo, hora_vuelo, aerolinea,
        # id_avion, id_piloto, id_copiloto, id_agenda, estado

        informacion_vuelo = (general [0],general [1], avion[1],general [2],general [3],
                            general [4],general [5],general [6],avion[0], piloto[0], piloto[1], "No Asignado", "No Enviado")
        print(informacion_vuelo)
        
        self.vuelo_crear(informacion_vuelo)
        # self.actualizar_tb_eliminar_vuelos()
        
# # ----------------------------------------------------------------------------------        
    def vuelo_crear(self, info_vuelo):
        if crear_vuelo(info_vuelo):
            self.close()            
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Vuelo Creado")
            dlg.setText("Nuevo vuelo creado con éxito")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Information)
            dlg.show()

            
        print("vuelo creado")

# # ------------------------------------------------------------------------------------
    def tabla_pilotos (self):
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        self.tableWidget.verticalHeader().setDefaultAlignment(Qt.AlignHCenter)
        self.tableWidget.resizeColumnsToContents()

# # -------------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------------
    def cargar_combo_idaviones(self):
        aviones = comprobar_id()
        
        #Aquí se convierte los valores de la tupla a str y sin esos caracteres
        characters = "(,')"
        i=0 
        while i < len(aviones):
            string = str(aviones [i])
            for x in range(len(characters)):
                string = string.replace(characters[x],"")
        
        # Aquí se manda ese string ya listo al combo box    
            self.cb_identificador.addItem(str(string))
            i += 1

# -------------------------------------------------------------------------------------
    def cargar_info_avion (self):
        self.event_tripulacion()
        self.cargar_combo_tripulación()

        identificador = self.cb_identificador.currentText()
        avion = buscar_avion(identificador)
        self.te_tipoAvion.setText(avion[1])
        self.te_propulsion.setText(avion[4])
        self.te_modelo.setText(avion[7])
        self.te_capacidad.setText(str(avion[2]))
        self.te_motores.setText(str(avion[6]))
        self.te_peso.setText(str(avion[5]))

# # -----------------------------------------------------------------------------------
#     def tabla_eliminar_vuelos (self):
#         header = self.tb_vistaGeneralED.horizontalHeader()
#         header.setSectionResizeMode(QHeaderView.ResizeToContents)       
#         self.tb_vistaGeneralED.verticalHeader().setDefaultAlignment(Qt.AlignHCenter)
#         self.tb_vistaGeneralED.resizeColumnsToContents()

# # ------------------------------------------------------------------------------------
#     def cargar_tabla_eliminar_vuelos(self,data):
#         self.tb_vistaGeneralED.setRowCount(len(data))

#         for(index_fila, fila) in enumerate(data):
#             #indice, datos
#             for (index_celda, celda) in enumerate(fila):
#                 self.tb_vistaGeneralED.setItem(index_fila, index_celda, 
#                 QTableWidgetItem(str(celda)))
    
# # -------------------------------------------------------------------------------------
#     def actualizar_tb_eliminar_vuelos(self):
#         data = seleccionar_todos_vuelos()
#         self.cargar_tabla_eliminar_vuelos(data)
    
# # ////////////////////////////////// ELIMINAR VUELOS ////////////////////////////////////////
#     def eliminar_vuelo (self):
#         vuelo_seleccionado = self.tb_vistaGeneralED.selectedItems()

#         if vuelo_seleccionado:
#             id_vuelo = vuelo_seleccionado[0].text()
#             print (id_vuelo)
#             vuelo = vuelo_seleccionado[0].row()

#             if borrar_vuelo(id_vuelo):
#                 self.tb_vistaGeneralED.removeRow(vuelo)

#         else:
#             dlg = QMessageBox(self)
#             dlg.setWindowTitle("Error")
#             dlg.setText("Para eliminar un vuelo, primero tiene que seleccionar uno de ellos.\n"+
#                         "Por favor revise e intente de nuevo")
#             dlg.setStandardButtons(QMessageBox.Ok)
#             dlg.setIcon(QMessageBox.Critical)
#             dlg.show()