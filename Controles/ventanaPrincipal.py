from PySide2.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QMessageBox
from PySide2.QtCore import Qt
from Ventanas.main_window import mainWindow
from Database.aeropuerto import seleccionar_todas_aerolineas, registrar_aerolinea, aerolinea_correo, aerolinea_tel, eliminar_aerolinea, seleccionar_todos_vuelos
from Database.hangares_db import traer_todos_hangares, crear_hangar, borrar_hangar, datos_factura
from Database.usuariosDB import traer_todoslos_usuarios
from Database.avion import comprobar_id
from .aerolineas import Aerolinea
from .vuelos import Vuelos
from .hangares import Hangares
from .facturacion import Factura
from .usuarios import Usuarios
import datetime
from datetime import datetime
from datetime import date
from .editarusuario import Editar_usuarios
import time


class Principal (QWidget, mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #Cargar Tablas 
        self.tabla_aerolineas()
        self.tabla_Hangar()
        self.tabla_general_vuelos()
        self.cargar_tabla_aerolineas(seleccionar_todas_aerolineas())
        self.cargar_tabla_hangares(traer_todos_hangares())
        self.cargar_tabla_general(seleccionar_todos_vuelos())
        
        # Conectar con las multipáginas los botones del inicio
        self.bt_user.clicked.connect(lambda: self.sk_mainWindow.setCurrentWidget(self.pg_bienvenido))
        self.bt_Aerolineas.clicked.connect(lambda: self.sk_mainWindow.setCurrentWidget(self.pg_aerolinea))
        self.bt_usuarios.clicked.connect(lambda: self.sk_mainWindow.setCurrentWidget(self.pg_usuarios))
        self.bt_Vuelos.clicked.connect(lambda: self.sk_mainWindow.setCurrentWidget(self.pg_vuelos))
        self.bt_Hangares.clicked.connect(lambda: self.sk_mainWindow.setCurrentWidget(self.pg_hangares))
        
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
        self.bt_editarAgenda.clicked.connect(self.crear_vuelo)
        
        #Cerrar sesion = Cerrar la ventana principal
        self.bt_CerrarSesion.clicked.connect(self.cerrar_sesion)
        
        #Boton Actualizar tabla vuelos
        self.bt_refreshAgenda.clicked.connect(self.actualizar_tb_vuelos)

        #Boton generar factura
        self.bt_generarReporte.clicked.connect(self.generar_salida)

        #Boton Crear Usuario
        self.bt_addUsuario.clicked.connect(self.reg_usuario)

        #Boton editar usuario
        self.bt_editarUsuario.clicked.connect(self.modificar_usuario)
        
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
            dlg.setText("Para eliminar una aerolínea, primero tiene que seleccionar de ellas.\n"+
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

# ////////////////////////////////// GENERAR SALIDA //////////////////////////////////////////////

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

    def factura_hangar(self, cod_hangar):
        window = Factura(self, cod_hangar)
        window.show()

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

# //////////////////////////////// ELIMINAR VUELOS /////////////////////////////////////////////////

# ///////////////////////////// USUARIOS //////////////////////////////////////////////////////
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
# ---------------------------------------------------------------------------------              
    def reg_usuario (self):
        window = Usuarios(self)
        window.show()
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
                    QMessageBox.information(self, "Eliminado", "Usuario eliminado con éxito", QMessageBox.Ok)

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