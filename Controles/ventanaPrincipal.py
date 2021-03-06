from PySide2.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QMessageBox
from PySide2.QtCore import Qt
from Ventanas.main_window import mainWindow
from .reprogramar_vuelos import ReprogramarVuelo
from Database.aeropuerto import *
from Database.hangares_db import traer_todos_hangares, crear_hangar, borrar_hangar, datos_factura
from Database.usuariosDB import traer_todoslos_usuarios, verificacioncontrasena , verificaciontipo, consultar_entidad
from Database.avion_db import *
from .aerolineas import Aerolinea
from .agenda import Agenda, AgendarVuelo
from .vuelos import Vuelos
from .hangares import Hangares
from .facturacion import Factura
from .usuarios import Usuarios
import datetime
from datetime import datetime
from datetime import date
from .editarusuario import Editar_usuarios
from .editaravion import Editar_Avion
from .editarvuelo import Editar_Vuelo
import time


class Principal (QWidget, mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #Cargar Tablas 
        self.c = False
        self.contra = " "
        self.tabla_aerolineas()
        self.tabla_Hangar()
        self.tabla_general_vuelos()
        self.tabla_salida_vuelos()
        self.tabla_llegada_vuelos()
        self.cargar_tabla_aerolineas(seleccionar_todas_aerolineas())
        self.cargar_tabla_hangares(traer_todos_hangares())
        self.cargar_tabla_general(seleccionar_todos_vuelos())
        self.cargar_tabla_salida(seleccionar_vuelos_salida())
        self.cargar_tabla_llegada(seleccionar_vuelos_llegada())
        self.tabla_general_vuelos_aerolinea()
        self.tabla_general_vuelos_pendientes()
        
        
        #**
        self.cargar_tabla_usuarios(traer_todoslos_usuarios ())
        self.cargar_tabla_aviones(traer_aviones())
        #**
        self.cb_pasajerosEA.setDisabled(True)
        self.cb_PropulsionEA.setDisabled(True)
        self.cb_ModeloRA.setDisabled(True)
                
        # Conectar con las multipáginas los botones del inicio
        self.bt_user.clicked.connect(lambda: self.sk_mainWindow.setCurrentWidget(self.pg_bienvenido))
        self.bt_Aerolineas.clicked.connect(lambda: self.sk_mainWindow.setCurrentWidget(self.pg_aerolinea))
        self.bt_usuarios.clicked.connect(lambda: self.sk_mainWindow.setCurrentWidget(self.pg_usuarios))
        self.bt_agendaMain.clicked.connect(lambda: self.sk_mainWindow.setCurrentWidget(self.pg_agenda))
        #&&
        
        
        # Conectar con la multipágina de inicio de sesion
        self.bt_CerrarSesion.clicked.connect(lambda: self.pag_Main.setCurrentWidget(self.Login))

        #Conectar con las multipáginas de los botones de hangar
        self.bt_agregarH.clicked.connect(lambda: self.sw_funcion_hangares.setCurrentWidget(self.pg_registrar_hg))
        self.bt_detallesHangar.clicked.connect(lambda: self.sw_funcion_hangares.setCurrentWidget(self.pg_info_hg))
        self.bt_aceptarinfhg.clicked.connect(lambda: self.sw_funcion_hangares.setCurrentWidget(self.pg_hgprincipal))
        self.bt_guardarHangar.clicked.connect(lambda: self.sw_funcion_hangares.setCurrentWidget(self.pg_hgprincipal))
        #&&
        
        #$$
        #Conectar con las multipáginas los botones de vuelos
        self.bt_aviones.clicked.connect(lambda: self.sw_vuelos_av_trip.setCurrentWidget(self.pg_aviones))
        self.bt_agregarAvion.clicked.connect(lambda: self.sw_reg_ver_avion.setCurrentWidget(self.pg_reg_avion))
        self.bt_cancelar_RA.clicked.connect(lambda: self.sw_reg_ver_avion.setCurrentWidget(self.pg_vista_aviones))
        #@@
        self.bt_nuevaTrip.clicked.connect(lambda: self.sw_reg_ver_avion.setCurrentWidget(self.pg_vista_aviones))
        
        #Conectar multipaginas agenda
        self.bt_vistaGeneral.clicked.connect(lambda: self.sk_agendaAero.setCurrentWidget(self.sk_vistaGeneral))
        self.bt_vuelosSalida.clicked.connect(lambda: self.sk_agendaAero.setCurrentWidget(self.sk_salida))
        self.bt_vuelosLlegada.clicked.connect(lambda: self.sk_agendaAero.setCurrentWidget(self.sk_llegada))

        #Conectar Nueva Tripulacion con el boton
        self.bt_nuevaTrip.clicked.connect(lambda: self.sw_vuelos_av_trip.setCurrentWidget(self.pg_newTrip))

        #Conectar Agenda Pendiente con el boton
        self.bt_agendaPendiente.clicked.connect(lambda: self.sw_vuelos_av_trip.setCurrentWidget(self.pg_agendaPendiente))

        #Conectar Agenda con el boton
        self.bt_vuelosAerolinea.clicked.connect(lambda: self.sw_vuelos_av_trip.setCurrentWidget(self.pg_agendaAerolinea))

        #Cambiar a agenda
        self.bt_Vuelos.clicked.connect(lambda: self.sk_mainWindow.setCurrentWidget(self.pg_vuelos))
        self.bt_Hangares.clicked.connect(lambda: self.sk_mainWindow.setCurrentWidget(self.pg_hangares))

        #Boton agregar (vuelos aerolinea)
        self.bt_agregarVA.clicked.connect(self.crear_vuelo)
        
        #Boton agregar aerolínea
        self.bt_addAerolinea.clicked.connect(self.reg_aerolinea)

        #Boton eliminar aerolínea
        self.bt_eliminarAerolinea.clicked.connect(self.eliminar_aerolinea)

        #Boton actualizar tabla aerolinea
        self.bt_refreshAerolinea.clicked.connect(self.actualizar_tb_aerolinea)
        
        #Boton Ocupar Hangar
        self.bt_ocuparHangar.clicked.connect(self.ocupar_hangar)

        #Boton Actualizar tabla hangares
        self.bt_refreshHangar.clicked.connect(self.actualizar_tb_hangares)

        #Crear vuelo
        #self.bt_editarAgenda.clicked.connect(self.crear_vuelo)
                
        #Boton Actualizar tabla vuelos
        self.bt_refreshAgenda.clicked.connect(self.actualizar_tb_vuelos)

        #Boton generar factura
        self.bt_generarReporte.clicked.connect(self.generar_salida)

        #Boton Crear Usuario
        self.bt_addUsuario.clicked.connect(self.reg_usuario)

        #Boton Actualizar tabla hangares
        self.bt_refreshUsuario.clicked.connect(self.actualizar_tb_usuarios)

        #&&
        #Boton Guardar hangar
        self.bt_guardarHangar.clicked.connect(self.registrar_hangar)

        #Boton Eliminar hangar
        self.bt_eliminarH.clicked.connect(self.eliminar_hangar)

        #Boton Eliminar usuario
        self.bt_eliminarUsuario.clicked.connect(self.eliminar_usuario)

        #Boton mostrar detalles de hangar
        self.bt_detallesHangar.clicked.connect(self.mostrar_detalles_hangar)
        #&&

        #$$
        #Boton verificar id avion
        self.bt_checkIDavion.clicked.connect(self.habilitar_campos_regvuelo)

        #**
        #Boton editar usuario
        self.bt_editarUsuario.clicked.connect(self.modificar_usuario)

        #**--
        #Boton guardar avion
        self.bt_aceptarAVEA.clicked.connect(self.registro_avion)

        #Boton actualizar tabla aviones
        self.bt_actualizar_avion.clicked.connect(self.actualizar_tb_aviones)

        #Boton eliminar avion
        self.bt_eliminarAvion.clicked.connect(self.eliminar_avion)

        #Boton editar avion
        self.bt_modificarAvion.clicked.connect(self.modificar_avion)
#@@
        #Boton iniciar sesion
        self.bt_ingresarlg.clicked.connect(self.iniciar_sesion)

        #Boton nueva tripulacion
        self.bt_AgregarTrip.clicked.connect(self.nueva_tripulacion)
        
        #Boton guardar tripulacion
        self.bt_GuardarTrip.clicked.connect(self.guardar_tripulacion)
        self.bt_AgregarTrip.setEnabled(True)

        #Boton modificar vuelo
        self.bt_modificarVA.clicked.connect(self.mod_vuelo)

        #Boton actualizar agenda aerolinea
        self.bt_refreshAgenda_Aerolinea.clicked.connect(self.actualizar_tb_vaerolinea)

        #Boton agenda pendiente
        self.bt_agendaPendiente.clicked.connect(self.actualizar_tb_vuelos_pendientes)

        #Boton Enviar agenda
        self.bt_enviar_agenda.clicked.connect(self.enviar_vuelos)

        #Boton Agendar vuelo
        self.bt_agendarVuelo.clicked.connect(self.agendar_en_aeropuerto)

        #Boton eliminar vuelo
        self.bt_eliminarVA.clicked.connect(self.eliminar_vuelo)

        #Boton reprogramar vuelo
        self.bt_infoVuelo.clicked.connect(self.reprogramar_vuelo)
#@@
# ///////////////////////////// AEROLINEA //////////////////////////////////////////////////////

    def reg_aerolinea (self):
        window = Aerolinea(self)
        window.show()
# --------------------------------------------------------------------------------
    def tabla_aerolineas (self):
        encabezados = ("Nit Aerolínea", "Nombre Aerolínea", "Correo", "Telefono")

        self.tb_aeroRegistradas.setColumnCount(len(encabezados))
        
        #Para mandar los encabezados
        #self.tb_aeroRegistradas.setHorizontalHeaderLabels(encabezados)
        header = self.tb_aeroRegistradas.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        self.tb_aeroRegistradas.verticalHeader().setDefaultAlignment(Qt.AlignHCenter)
        self.tb_aeroRegistradas.resizeColumnsToContents()

# --------------------------------------------------------------------------------
    def cargar_tabla_aerolineas (self, data):
        self.tb_aeroRegistradas.setRowCount(len(data))

        for(index_fila, fila) in enumerate(data):
            #indice, datos
            for (index_celda, celda) in enumerate(fila):
                self.tb_aeroRegistradas.setItem(index_fila, index_celda, 
                QTableWidgetItem(str(celda)))

# --------------------------------------------------------------------------------
    def eliminar_aerolinea (self):
        aero_seleccionada = self.tb_aeroRegistradas.selectedItems()

        if aero_seleccionada:
            nit_aerolinea = aero_seleccionada[0].text()
            print (nit_aerolinea)
            aerolinea = aero_seleccionada[0].row()

            # Mensaje de confirmación de si quiere borrar la aerolinea
            dlg = QMessageBox.question(self, "Borrar aerolínea", 
                        "¿Esta seguro que quiere eliminar esta aerolínea?", 
                        QMessageBox.Ok, QMessageBox.Cancel)

            #Si presiona Ok 
            if dlg == QMessageBox.Ok:
                if Aerolinea.borrar_datos_aerolinea(self, nit_aerolinea):
                    self.tb_aeroRegistradas.removeRow(aerolinea)
                    QMessageBox.information(self, "Eliminada", "Aerolinea eliminada con éxito", QMessageBox.Ok)

        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para eliminar una aerolínea, primero tiene que seleccionar una de ellas.\n"+
                        "Por favor revise e intente de nuevo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()

#--------------------------------------------------------------------------------
    def actualizar_tb_aerolinea(self):
        data = seleccionar_todas_aerolineas()
        self.cargar_tabla_aerolineas(data)
# -------------------------------------------------------------------------------
    def crear_vuelo (self):
        window = Vuelos(self)
        window.show()
# -------------------------------------------------------------------------------
    def cerrar_sesion(self):
        self.close()

#///////////////////////////// HANGAR //////////////////////////////////////////////////////

    def ocupar_hangar (self):
        
        hangar_seleccionado = self.tb_hangares.selectedItems()
        
        if hangar_seleccionado:
            estado = hangar_seleccionado[1].text()

            if estado == "LIBRE":
        
                hangar = hangar_seleccionado[0].text()
                print(hangar)
                window = Hangares(self, hangar)
                window.show()
            
            else:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("El hangar se encuentra ocupado.\n"+
                            "Seleccione otro.")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Critical)
                dlg.show()
        
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para alquilar un hangar, primero tiene que seleccionar uno de los hangares en estado LIBRE\n"+
                        "Por favor revise e intente de nuevo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()

#--------------------------------------------------------------------------------
    def tabla_Hangar (self):
        encabezados = ("Código", "Estado")

        self.tb_hangares.setColumnCount(len(encabezados))
        
        #Para mandar los encabezados
        #self.tb_hangares.setHorizontalHeaderLabels(encabezados)
        header = self.tb_hangares.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tb_hangares.verticalHeader().setDefaultAlignment(Qt.AlignHCenter)
        
        self.tb_hangares.resizeColumnsToContents()

# -------------------------------------------------------------------------------
    def cargar_tabla_hangares (self, data):
        self.tb_hangares.setRowCount(len(data))

        for(index_fila, fila) in enumerate(data):
            #indice, datos
            for (index_celda, celda) in enumerate(fila):
                self.tb_hangares.setItem(index_fila, index_celda, 
                QTableWidgetItem(str(celda)))

# ---------------------------------------------------------------------------------
    def actualizar_tb_hangares(self):
        data = traer_todos_hangares()
        self.cargar_tabla_hangares(data)
#--------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
    def generar_salida(self):
        hangar_seleccionado = self.tb_hangares.selectedItems()

        if hangar_seleccionado:
            estado = hangar_seleccionado[1].text()

            if estado == "OCUPADO":
                print((hangar_seleccionado[0].text()))
                self.factura_hangar(hangar_seleccionado[0].text())

            else:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("El hangar se encuentra vacio.")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Critical)
                dlg.show()

        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para liberar un hangar, primero tiene que seleccionar uno de los hangares en estado OCUPADO\n"+
                        "Por favor revise e intente de nuevo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()

# ---------------------------------------------------------------------------
    def factura_hangar(self, cod_hangar):
        window = Factura(self, cod_hangar)
        window.show()
#&&
#----------------------------------------------------------------------------
    def registrar_hangar (self):
        #Traer inf de los line edit
        codigo = self.textedit_codigoRH.text()
        capacidad = self.textedit_capacidadRH.text()
        estado ="LIBRE"

        hangar = (codigo, capacidad, estado)
        print(hangar)
        
        i=0; b= True

        while i < len(hangar) and b == True:
            if hangar[i] != "":
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

        num=1
        print (capacidad.isdigit())
        if capacidad.isdigit() == True and b==True:
            hangar = (codigo, int(capacidad), estado)
            if crear_hangar(hangar):

                dlg = QMessageBox(self)
                dlg.setWindowTitle("Nuevo hangar creado")
                dlg.setText("Hangar registrado con éxito.\n"+
                            "Actualice la tabla para visualizar los cambios.")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Information)
                dlg.show()
        
        elif b == True:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Capacidad incorrecta")
            dlg.setText("En capacidad de hangar debe introducir un valor numérico válido.\n"+
                        "Por favor revise e intente de nuevo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()
            b=False

#------------------------------------------------------------------------------------------------
    def eliminar_hangar(self):
        hangar_seleccionado = self.tb_hangares.selectedItems()

        if hangar_seleccionado:
            cod_hangar = hangar_seleccionado[0].text()
            estado = hangar_seleccionado[1].text()
            print (cod_hangar)
            hangar = hangar_seleccionado[0].row()

            if estado == "LIBRE":
                # Mensaje de confirmación de si quiere borrar el hangar
                dlg = QMessageBox.question(self, "Eliminar Hangar", 
                    "¿Esta seguro que quiere eliminar este hangar?", 
                    QMessageBox.Ok, QMessageBox.Cancel)

                #Si presiona Ok 
                if dlg == QMessageBox.Ok:
                    if borrar_hangar(cod_hangar):
                        self.tb_hangares.removeRow(hangar)
                        QMessageBox.information(self, "Eliminada", "Hangar eliminado con éxito", QMessageBox.Ok)
            
            elif estado == "OCUPADO":
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("Este hangar no puede ser eliminado porque está ocupado.\n"+
                            "Por favor revise e intente de nuevo")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Critical)
                dlg.show()

        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para eliminar un hangar, primero tiene que seleccionar uno de ellos.\n"+
                        "Por favor revise e intente de nuevo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()
# ---------------------------------------------------------------------------------------------
    def mostrar_detalles_hangar(self):
        hangar_seleccionado = self.tb_hangares.selectedItems()

        if hangar_seleccionado:
            codigo = hangar_seleccionado[0].text()
            estado = hangar_seleccionado[1].text()
            self.lb_nomHangar.setAlignment(Qt.AlignCenter|Qt.AlignVCenter)
            self.lb_nomHangar.setStyleSheet("font-size:16pt; font-weight:600; color:#1675a3")
            self.lb_ModelodeAvion.setAlignment(Qt.AlignCenter|Qt.AlignVCenter)
            self.lb_NombreAerolinea.setAlignment(Qt.AlignCenter|Qt.AlignVCenter)

            if estado =="LIBRE":
                self.lb_ModelodeAvion.setText("Vacio")
                self.lb_NombreAerolinea.setText("Vacio")
                self.lb_HoraEntrada.setText("Vacio")
                self.lb_fechaEntrada.setText("Vacio")
                self.lb_TiempoenHoras.setText("Vacio")
                self.lb_ValordelaHora.setText("Vacio")
                self.lb_nomHangar.setText("Hangar "+codigo)
                

            elif estado=="OCUPADO":
                datos = datos_factura(codigo)
                now = datetime.now()
                str_horae = datos[2].strftime('%H:%M')
                hora = now.strftime('%H:%M')
                f1 = str_horae
                f2 = hora
                fmt = '%H:%M'

                diferencia = datetime.strptime(f2, fmt) - datetime.strptime(f1, fmt)        
                print(diferencia)

                self.lb_ModelodeAvion.setText(datos[0])
                self.lb_NombreAerolinea.setText(datos[1])
                self.lb_HoraEntrada.setText(datos[2].strftime('%H:%M'))
                self.lb_fechaEntrada.setText(datos[3].strftime('%d/%m/%Y'))
                self.lb_TiempoenHoras.setText(str(diferencia))
                self.lb_ValordelaHora.setText(str(datos[4]))
                self.lb_nomHangar.setText("Hangar "+codigo)

        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para mirar un hangar, primero tiene que seleccionar uno de ellos.\n"+
                        "Por favor revise e intente de nuevo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()
#&&
# /////////////////////////////////// CREAR VUELOS /////////////////////////////////////////////
    
    def tabla_general_vuelos (self):
        header = self.tb_vistaGeneral.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        self.tb_vistaGeneral.verticalHeader().setDefaultAlignment(Qt.AlignHCenter)
        self.tb_vistaGeneral.resizeColumnsToContents()

# --------------------------------------------------------------------------------------
    def cargar_tabla_general(self, data):
        self.tb_vistaGeneral.setRowCount(len(data))

        for(index_fila, fila) in enumerate(data):
            #indice, datos
            for (index_celda, celda) in enumerate(fila):
                self.tb_vistaGeneral.setItem(index_fila, index_celda, 
                QTableWidgetItem(str(celda)))

# --------------------------------------------------------------------------------------
    def actualizar_tb_vuelos(self):
        data = seleccionar_todos_vuelos()
        self.cargar_tabla_general(data)

# ---------------------------------------------------------------------------------------
    def tabla_llegada_vuelos (self):
        self.tb_vistaLlegada.setSelectionBehavior(QAbstractItemView.SelectRows) 
        header = self.tb_vistaLlegada.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        self.tb_vistaLlegada.verticalHeader().setDefaultAlignment(Qt.AlignHCenter)
        self.tb_vistaLlegada.resizeColumnsToContents()

# --------------------------------------------------------------------------------------
    def cargar_tabla_llegada(self, data):
        self.tb_vistaLlegada.setRowCount(len(data))

        for(index_fila, fila) in enumerate(data):
            #indice, datos
            for (index_celda, celda) in enumerate(fila):
                self.tb_vistaLlegada.setItem(index_fila, index_celda, 
                QTableWidgetItem(str(celda)))

# --------------------------------------------------------------------------------------
    def actualizar_tb_llegada(self):
        data = seleccionar_vuelos_llegada()
        self.cargar_tabla_general(data)

# ---------------------------------------------------------------------------------------
    def tabla_salida_vuelos (self):
        self.tb_vistaSalida.setSelectionBehavior(QAbstractItemView.SelectRows) 
        header = self.tb_vistaSalida.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        self.tb_vistaSalida.verticalHeader().setDefaultAlignment(Qt.AlignHCenter)
        self.tb_vistaSalida.resizeColumnsToContents()

# --------------------------------------------------------------------------------------
    def cargar_tabla_salida(self, data):
        self.tb_vistaSalida.setRowCount(len(data))

        for(index_fila, fila) in enumerate(data):
            #indice, datos
            for (index_celda, celda) in enumerate(fila):
                self.tb_vistaSalida.setItem(index_fila, index_celda, 
                QTableWidgetItem(str(celda)))

# --------------------------------------------------------------------------------------
    def actualizar_tb_salida(self):
        data = seleccionar_vuelos_salida()
        self.cargar_tabla_general(data)

# ---------------------------------------------------------------------------------------
    def tabla_general_vuelos_aerolinea (self):
        self.tb_vistaAerolinea.setSelectionBehavior(QAbstractItemView.SelectRows)
        header = self.tb_vistaAerolinea.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        self.tb_vistaAerolinea.verticalHeader().setDefaultAlignment(Qt.AlignHCenter)
        self.tb_vistaAerolinea.resizeColumnsToContents()

# --------------------------------------------------------------------------------------
    def cargar_tabla_vaerolinea(self, data):

        entidad = consultar_entidad(self.contra)

        characters = "(,')"
        i=0 
        while i < len(entidad):
            entid = str(entidad [i])
            for x in range(len(characters)):
                entid = entid.replace(characters[x],"")
            i += 1
        print (entid)

        nit_aerolinea = consultar_aerolinea(entid)
        characters = "(,')"
        i=0 
        while i < len(nit_aerolinea):
            string = str(nit_aerolinea [i])
            for x in range(len(characters)):
                string = string.replace(characters[x],"")
            i += 1

        data = vuelos_entidad(string)

        self.tb_vistaAerolinea.setRowCount(len(data))

        for(index_fila, fila) in enumerate(data):
            #indice, datos
            for (index_celda, celda) in enumerate(fila):
                self.tb_vistaAerolinea.setItem(index_fila, index_celda, 
                QTableWidgetItem(str(celda)))

# --------------------------------------------------------------------------------------
    def actualizar_tb_vaerolinea(self):
        entidad = consultar_entidad(self.contra)

        characters = "(,')"
        i=0 
        while i < len(entidad):
            entid = str(entidad [i])
            for x in range(len(characters)):
                entid = entid.replace(characters[x],"")
            i += 1
        print (entid)

        nit_aerolinea = consultar_aerolinea(entid)
        characters = "(,')"
        i=0 
        while i < len(nit_aerolinea):
            string = str(nit_aerolinea [i])
            for x in range(len(characters)):
                string = string.replace(characters[x],"")
            i += 1

        data = vuelos_entidad(string)
        self.cargar_tabla_vaerolinea(data)

# ------------------------------------------------------------------------------------------------
    def tabla_general_vuelos_pendientes (self):
        header = self.tb_vistaAerolineaPendiente.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        self.tb_vistaAerolineaPendiente.verticalHeader().setDefaultAlignment(Qt.AlignHCenter)
        self.tb_vistaAerolineaPendiente.resizeColumnsToContents()

# --------------------------------------------------------------------------------------
    def cargar_tabla_vuelos_pendiente(self, data):
        
        self.tb_vistaAerolineaPendiente.setRowCount(len(data))

        for(index_fila, fila) in enumerate(data):
            #indice, datos
            for (index_celda, celda) in enumerate(fila):
                self.tb_vistaAerolineaPendiente.setItem(index_fila, index_celda, 
                QTableWidgetItem(str(celda)))

# --------------------------------------------------------------------------------------
    def actualizar_tb_vuelos_pendientes(self):
        entidad = consultar_entidad(self.contra)

        characters = "(,')"
        i=0 
        while i < len(entidad):
            entid = str(entidad [i])
            for x in range(len(characters)):
                entid = entid.replace(characters[x],"")
            i += 1
        print (entid)

        nit_aerolinea = consultar_aerolinea(entid)
        characters = "(,')"
        i=0 
        while i < len(nit_aerolinea):
            string = str(nit_aerolinea [i])
            for x in range(len(characters)):
                string = string.replace(characters[x],"")
            i += 1

        
        data = vuelos_pendientes(string)
        self.cargar_tabla_vuelos_pendiente(data)

# /////////////////////////////////////// ENVIAR VUELOS A AGENDA AEROPUERTO ////////////////////////////
    def enviar_vuelos (self):
        entidad = consultar_entidad(self.contra)

        characters = "(,')"
        i=0 
        while i < len(entidad):
            entid = str(entidad [i])
            for x in range(len(characters)):
                entid = entid.replace(characters[x],"")
            i += 1
        print (entid)

        nit_aerolinea = consultar_aerolinea(entid)
        characters = "(,')"
        i=0 
        while i < len(nit_aerolinea):
            string = str(nit_aerolinea [i])
            for x in range(len(characters)):
                string = string.replace(characters[x],"")
            i += 1

        if cambio_estado_espera(string):
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Vuelos enviados")
            dlg.setText("Los vuelos fueron enviados al aeropuerto.\n"+
                        "Cambio de estado : EN ESPERA")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Information)
            dlg.show()

# //////////////////////////// AGENDAR EN AGENDA DEL AEROPUERTO ////////////////////////////////////
    def agendar_en_aeropuerto(self):
        window = Agenda(self)
        window.show()

# ///////////////////////////// USUARIOS //////////////////////////////////////////////////////             
    def reg_usuario (self):
        window = Usuarios(self)
        window.show()
        
# ---------------------------------------------------------------------------------            
    def cargar_tabla_usuarios (self, data):
        self.tb_vistaGeneral_2.setRowCount(len(data))

        for(index_fila, fila) in enumerate(data):
            #indice, datos
            for (index_celda, celda) in enumerate(fila):
                self.tb_vistaGeneral_2.setItem(index_fila, index_celda, 
                QTableWidgetItem(str(celda)))
# --------------------------------------------------------------------------------------
    def actualizar_tb_usuarios(self):
        data = traer_todoslos_usuarios()
        self.cargar_tabla_usuarios(data) 

# --------------------------------------------------------------------------------
    def eliminar_usuario (self):
        usuario_seleccionado = self.tb_vistaGeneral_2.selectedItems()

        if usuario_seleccionado:
            id_usuario = usuario_seleccionado[0].text()
            print (id_usuario)
            usuario = usuario_seleccionado[0].row()

            # Mensaje de confirmación de si quiere borrar el usuario
            dlg = QMessageBox.question(self, "Eliminar Usuario", 
                        "¿Esta seguro que quiere eliminar el usuario?", 
                        QMessageBox.Ok, QMessageBox.Cancel)

            #Si presiona Ok 
            if dlg == QMessageBox.Ok:
                if Usuarios.borrar_datos_usuario(self, id_usuario):
                    self.tb_vistaGeneral_2.removeRow(usuario)
                    QMessageBox.information(self, "Eliminado", "Usuario eliminado con éxito.", QMessageBox.Ok)

        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para eliminar un usuario, primero tiene que seleccionar uno de ellos.\n"+
                        "Por favor revise e intente de nuevo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()
# --------------------------------------------------------------------------------------
    #**
    def modificar_usuario(self):
        usuario_seleccionado = self.tb_vistaGeneral_2.selectedItems()

        if usuario_seleccionado:
            id_usuario = usuario_seleccionado[0].text()
            print (id_usuario)
            usuario = usuario_seleccionado[0].row()

            window = Editar_usuarios(self,str(id_usuario))
            window.show()
                    
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para editar un usuario, primero tiene que seleccionar uno de ellos.\n"+
                        "Por favor revise e intente de nuevo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()
    #**
#--------------------------------------------------------------------------------
# ///////////////////////////////// AVIONES ////////////////////////////////////////////////////////
    def registro_avion (self):
        cod_avion = self.lineEdit_identificadorEA.text()
        tipo_avion = self.cb_pasajerosEA.currentText()
        # propulsion = self.cb_PropulsionEA.currentText()
        modelo = self.cb_ModeloRA.currentText()
        capacidad = self.spinBox_CapacidadEA.value()
        # motores = self.spinBox_MotoresEA.value()
        # peso = self.spinBox_pesoNomEA.value()

        #cod_avion, tipo_avion, capacidad, cod_modelo
        avion = (cod_avion, tipo_avion, modelo, capacidad)
        
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
            characters = "(,')"
            cod_modelo = str(buscar_cod_modelo(modelo))
            for x in range(len(characters)):
                cod_modelo = cod_modelo.replace(characters[x],"")

            avion = (cod_avion, tipo_avion, capacidad, cod_modelo)
            
            if registrar_avion(avion):
                self.bool = True
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Registro Exitoso")
                dlg.setText("Avión registrado con éxito.\n"+
                            " Actualice la tabla para ver los cambios realizados")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Information)
                dlg.show()

# --------------------------------------------------------------------------------------
    def actualizar_tb_aviones(self):
            data = traer_aviones()
            self.cargar_tabla_aviones(data)
# --------------------------------------------------------------------------------------
    def cargar_tabla_aviones (self, data):
        self.tb_avionesregistradosAV.setRowCount(len(data))

        for(index_fila, fila) in enumerate(data):
            #indice, datos
            for (index_celda, celda) in enumerate(fila):
                self.tb_avionesregistradosAV.setItem(index_fila, index_celda, 
                QTableWidgetItem(str(celda)))
# --------------------------------------------------------------------------------------
#**
    def modificar_avion(self):
        avion_seleccionado = self.tb_avionesregistradosAV.selectedItems()

        if avion_seleccionado:
            id_avion = avion_seleccionado[0].text()
            print (id_avion)
            avion = avion_seleccionado[0].row()

            window = Editar_Avion(self,id_avion)
            window.show()
                    
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para editar un avión, primero tiene que seleccionar uno de ellos.\n"+
                        "Por favor revise e intente de nuevo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()
    #**

#--------------------------------------------------------------------------------
    #**--
    def eliminar_avion(self):
        avion_seleccionado = self.tb_avionesregistradosAV.selectedItems()

        if avion_seleccionado:
            id_avion = avion_seleccionado[0].text()
            print (id_avion)
            avion = avion_seleccionado[0].row()

            # Mensaje de confirmación de si quiere borrar el usuario
            dlg = QMessageBox.question(self, "Eliminar Avion", 
                        "¿Esta seguro que quiere eliminar el avion?", 
                        QMessageBox.Ok, QMessageBox.Cancel)

            #Si presiona Ok 
            if dlg == QMessageBox.Ok:
                if borrar_datos_avion(id_avion):
                    self.tb_avionesregistradosAV.removeRow(avion)
                    QMessageBox.information(self, "Eliminado", "Avion eliminado con éxito", QMessageBox.Ok)
                    
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para eliminar un avion, primero tiene que seleccionar uno de ellos.\n"+
                        "Por favor revise e intente de nuevo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()
    #**--
#--------------------------------------------------------------------------------
    def local_comprobar_id (self, id_avion):
        b = True
        #Comprobación de ID
        #id_ingresado = self.lineEdit_identificadorEA.text()
        aviones = comprobar_id()
        print (id_avion)
        print (aviones)
        if len(aviones) == 0:
            b = True
        else:
            i = 0
            while i < len(aviones) and b == True:

                characters = "(,')"
                avion = str(aviones[i])
                for x in range(len(characters)):
                    avion = avion.replace(characters[x],"")

                print (avion)
                if avion != id_avion:
                    i +=1 
                    print (b)
                else:
                    b = False

        return b


# -----------------------------------------------------------------    
    def habilitar_campos_regvuelo (self):
        #Comprobación de ID
        id_ingresado = self.lineEdit_identificadorEA.text()
        b= True

        if id_ingresado == "":
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Digite el id del avion en el campo correspondiente.")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()
            b=False

        elif b == True:
            self.lb_Identificador_5.setText(" ")
            registrar = self.local_comprobar_id(id_ingresado)
            print (registrar)
        
            if registrar: 
                self.lb_Identificador_5.setText("ID Disponible")
                self.lb_Identificador_5.setStyleSheet("color:green")
                self.cb_pasajerosEA.setDisabled(False)
                self.cb_PropulsionEA.setDisabled(False)
                self.cb_ModeloRA.setDisabled(False)
                self.cargar_modelos_combo()
                
                permitir = True

            else:
                self.lb_Identificador_5.setText("ID no Disponible")
                self.lb_Identificador_5.setStyleSheet("color:red")
                permitir = False
# ---------------------------------------------------------------------------------
    def cargar_modelos_combo(self):
        modelos = traer_modelos()

        #Aquí se convierte los valores de la tupla a str y sin esos caracteres
        characters = "(,')"
        i=0 
        while i < len(modelos):
            string = str(modelos [i])
            for x in range(len(characters)):
                string = string.replace(characters[x],"")
        
        # Aquí se manda ese string ya listo al combo box    
            self.cb_ModeloRA.addItem(str(string))
            i += 1

# ----------------------------------------------------------------------------------
    def llenar_campos (self, modelo):
        
        datos_modelo = consulta_por_modelo(modelo)
        datos= []
        characters = "(,')"
        i=0 
        while i < len(datos_modelo):
            string = str(datos_modelo [i])
            for x in range(len(characters)):
                string = string.replace(characters[x],"")
            datos.append(string)

        return datos
        # Aquí se manda ese string ya listo al combo box  
        
#/////////////////////////////////Eliminar Vuelos////////////////////////////////////////////////////
    def eliminar_vuelo(self):
        vuelo_seleccionado = self.tb_vistaAerolinea.selectedItems()

        if vuelo_seleccionado:
            cod_vuelo = vuelo_seleccionado[2].text()
            print (cod_vuelo)
            vuelo = vuelo_seleccionado[0].row()

            # Mensaje de confirmación de si quiere borrar la aerolinea
            dlg = QMessageBox.question(self, "Eliminar vuelo", 
                        "¿Esta seguro que quiere eliminar este vuelo?", 
                        QMessageBox.Ok, QMessageBox.Cancel)

            #Si presiona Ok 
            if dlg == QMessageBox.Ok:
                if self.eliminar_datos_vuelo(cod_vuelo):
                    self.tb_vistaAerolinea.removeRow(vuelo)
                    QMessageBox.information(self, "Eliminado", "Vuelo eliminado con exito", QMessageBox.Ok)

        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para eliminar una aerolínea, primero tiene que seleccionar una de ellas.\n"+
                        "Por favor revise e intente de nuevo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()

    def eliminar_datos_vuelo(self, cod_vuelo):
        borrar_vuelo(cod_vuelo)
#/////////////////////////////////Reprogramar vuelo////////////////////////////////////////////////////
    def reprogramar_vuelo(self):
        vuelo_seleccionado = self.tb_vistaGeneral.selectedItems()

        if vuelo_seleccionado:
            id_vuelo = vuelo_seleccionado[2].text()
            print (id_vuelo)
            vuelo = vuelo_seleccionado[0].row()

            window = ReprogramarVuelo(self, id_vuelo)
            window.show()
                    
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para editar un vuelo, primero tiene que seleccionar uno de ellos.\n"+
                        "Por favor revise e intente de nuevo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()

#/////////////////////////////////Tripulacion////////////////////////////////////////////////////
    def local_comprobar_id_tripulante (self, cod_trip):
        b = True

        tripulaciones = comprobar_cod_tripulante()
        print (cod_trip)
        print (tripulaciones)
        if len(tripulaciones) == 0:
            b = True
        else:
            i = 0
            while i < len(tripulaciones) and b == True:

                characters = "(,')"
                tripulacion = str(tripulaciones[i])
                for x in range(len(characters)):
                    tripulacion = tripulacion.replace(characters[x],"")

                print (tripulacion)
                if tripulacion != cod_trip:
                    i +=1 
                    print (b)
                else:
                    b = False

        return b
# --------------------------------------------------------------------------------------------------
    def  nueva_tripulacion(self):
        codtripulacion = self.textedit_codTripulacion.text()
        nombre = self.textedit_nombre.text()
        apellido = self.textedit_Apellido.text()
        tipoid = self.cb_tipoID.currentText()
        numeroid = self.textedit_numeroID.text()
        licencia = self.textedit_licencia.text()
        fechaultimarev = self.date_fechaUltimaRevision.date().toPython()
        horasdevuelo = self.spinBox_HorasVuelo.value()

        if self.local_comprobar_id_tripulante(codtripulacion):

            analizar = (codtripulacion, nombre, apellido, tipoid, numeroid, licencia, fechaultimarev, horasdevuelo)

            i=0; b= True

            while i < len(analizar) and b == True:
                if analizar[i] != "":
                    i += 1
                    b = True

                else:
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("Error")
                    dlg.setText("Para agregar la tripulacion todos\n"+
                                "los campos deben estar llenos.\n")
                    dlg.setStandardButtons(QMessageBox.Ok)
                    dlg.setIcon(QMessageBox.Critical)
                    dlg.show()
                    b = False

            if b == True: 
                datostrip = (licencia, nombre, apellido, horasdevuelo, fechaultimarev, numeroid, codtripulacion )
                if nueva_trip(datostrip):
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("Tripulacion")
                    dlg.setText("Tripulante guardado con exito")
                    dlg.setStandardButtons(QMessageBox.Ok)
                    dlg.setIcon(QMessageBox.Information)
                    dlg.show()

                    self.textedit_codTripulacion.setEnabled(False)
                    self.textedit_nombre.clear()
                    self.textedit_Apellido.clear()
                    self.textedit_numeroID.clear()
                    self.textedit_licencia.clear()

                    self.bt_AgregarTrip.setEnabled(False)

                    self.c = True

        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Codigo de tripulacion ya existente")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()

# --------------------------------------------------------------------------------------------------        
    def guardar_tripulacion(self):
        codtripulacion = self.textedit_codTripulacion.text()
        nombre = self.textedit_nombre.text()
        apellido = self.textedit_Apellido.text()
        tipoid = self.cb_tipoID.currentText()
        numeroid = self.textedit_numeroID.text()
        licencia = self.textedit_licencia.text()
        fechaultimarev = self.date_fechaUltimaRevision.date().toPython()
        horasdevuelo = self.spinBox_HorasVuelo.value()
        print(self.c)
        if self.c == True:
            
            analizar = (codtripulacion, nombre, apellido, tipoid, numeroid, licencia, fechaultimarev, horasdevuelo)

            i=0; b= True

            while i < len(analizar) and b == True:
                if analizar[i] != "":
                    i += 1
                    b = True

                else:
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("Error")
                    dlg.setText("Para agregar la tripulacion todos\n"+
                                "los campos deben estar llenos.\n")
                    dlg.setStandardButtons(QMessageBox.Ok)
                    dlg.setIcon(QMessageBox.Critical)
                    dlg.show()
                    b = False

            if b == True: 
                datostrip = (licencia, nombre, apellido, horasdevuelo, fechaultimarev, numeroid, codtripulacion )
                if nueva_trip(datostrip):
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("Tripulacion")
                    dlg.setText("Tripulante guardado con exito")
                    dlg.setStandardButtons(QMessageBox.Ok)
                    dlg.setIcon(QMessageBox.Information)
                    dlg.show()

                    self.textedit_codTripulacion.clear()
                    self.textedit_codTripulacion.setEnabled(True)
                    self.textedit_nombre.clear()
                    self.textedit_Apellido.clear()
                    self.textedit_numeroID.clear()
                    self.textedit_licencia.clear()

                    self.bt_AgregarTrip.setEnabled(True)

        elif self.local_comprobar_id_tripulante(codtripulacion):

            analizar = (codtripulacion, nombre, apellido, tipoid, numeroid, licencia, fechaultimarev, horasdevuelo)

            i=0; b= True

            while i < len(analizar) and b == True:
                if analizar[i] != "":
                    i += 1
                    b = True

                else:
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("Error")
                    dlg.setText("Para agregar la tripulacion todos\n"+
                                "los campos deben estar llenos.\n")
                    dlg.setStandardButtons(QMessageBox.Ok)
                    dlg.setIcon(QMessageBox.Critical)
                    dlg.show()
                    b = False

            if b == True: 
                datostrip = (licencia, nombre, apellido, horasdevuelo, fechaultimarev, numeroid, codtripulacion )
                if nueva_trip(datostrip):
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("Tripulacion")
                    dlg.setText("Tripulante guardado con exito")
                    dlg.setStandardButtons(QMessageBox.Ok)
                    dlg.setIcon(QMessageBox.Information)
                    dlg.show()

                    self.textedit_codTripulacion.clear()
                    self.textedit_codTripulacion.setEnabled(True)
                    self.textedit_nombre.clear()
                    self.textedit_Apellido.clear()
                    self.textedit_numeroID.clear()
                    self.textedit_licencia.clear()

                    self.bt_AgregarTrip.setEnabled(True)
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Codigo de tripulacion ya existente")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()

        self.c = False

    def mod_vuelo(self):
        vuelo_seleccionado = self.tb_vistaAerolinea.selectedItems()

        if vuelo_seleccionado:
            id_vuelo = vuelo_seleccionado[3].text()
            print (id_vuelo)
            vuelo = vuelo_seleccionado[0].row()

            window = Editar_Vuelo(self, id_vuelo)
            window.show()
                    
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Para editar un vuelo, primero tiene que seleccionar uno de ellos.\n"+
                        "Por favor revise e intente de nuevo")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.show()
        

#/////////////////////////////////Inicio de Sesion////////////////////////////////////////////////////

    def iniciar_sesion (self):
        
        user = self.correo_lineEdit.text()
        print (user)
        contra = self.lgcontra_lineEdit_2.text()
        self.contra = contra  

        analizar = (user,contra)

        i=0; b= True

        
        while i < len(analizar) and b == True:
            if analizar[i] != "":
                i += 1
                b = True

            else:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("Para iniciar sesion todos los\n"+
                            "campos deben estar llenos.\n"+
                            "Por favor revise e intente de nuevo")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Critical)
                dlg.show()
                b = False

        if b == True:         
            if user != "master" :
                characters = "(,')"
                i=0 
                entidad = consultar_entidad(self.contra)

                while i < len(entidad):
                    entid = str(entidad [i])
                    for x in range(len(characters)):
                        entid = entid.replace(characters[x],"")
                    i += 1
                print (entid)

                if entid != "Campanero":
                    nit_aerolinea = consultar_aerolinea(entid)
                    characters = "(,')"
                    i=0 
                    while i < len(nit_aerolinea):
                        string = str(nit_aerolinea [i])
                        for x in range(len(characters)):
                            string = string.replace(characters[x],"")
                        i += 1

                    data = vuelos_entidad(string)
                    self.cargar_tabla_vaerolinea(data)
                    self.cargar_tabla_vuelos_pendiente(vuelos_pendientes(string))

            contraseña = verificacioncontrasena(user)
            if contraseña == None:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("Correo electronico no existente")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Critical)
                dlg.show()

                entidad = consultar_entidad(self.contra)

            else:
                characters = "(,')"
                i=0 
                while i < len(contraseña):
                    string = str(contraseña[i])
                    for x in range(len(characters)):
                        string = string.replace(characters[x],"")
                    i += 1
                if string == contra:
                    self.pag_Main.setCurrentWidget(self.Controls)
                    self.sk_mainWindow.setCurrentWidget(self.pg_bienvenido)
                    self.correo_lineEdit.clear()
                    self.lgcontra_lineEdit_2.clear()

                    self.desactivarbotoneslogin(user)
                else:
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("Error")
                    dlg.setText("Contraseña incorrecta")
                    dlg.setStandardButtons(QMessageBox.Ok)
                    dlg.setIcon(QMessageBox.Critical)
                    dlg.show()
                

                
    def desactivarbotoneslogin(self , user):
        tipouser = verificaciontipo(user)   
        characters = "(,')"
        i=0 
        while i < len(tipouser):
            string = str(tipouser[i])
            for x in range(len(characters)):
                string = string.replace(characters[x],"")
            i += 1
        print(string)

        if string == "Funcionario de vuelos ":
            self.bt_usuarios.setEnabled(False)                  
            self.bt_Hangares.setEnabled(False)
            self.bt_Vuelos.setEnabled(False)
            self.bt_Aerolineas.setEnabled(True)
            self.bt_agendaMain.setEnabled(True)
            

        if string == "Admin. Hangares":
            self.bt_usuarios.setEnabled(False)
            self.bt_Aerolineas.setEnabled(False)
            self.bt_agendaMain.setEnabled(False)
            self.bt_Vuelos.setEnabled(False)
            self.bt_Hangares.setEnabled(True)

        if string == "Admin. de aereolinea":
            self.bt_usuarios.setEnabled(False)
            self.bt_agendaMain.setEnabled(False)
            self.bt_Hangares.setEnabled(False)
            self.bt_Aerolineas.setEnabled(False)
            self.bt_Vuelos.setEnabled(True)


    
        
            