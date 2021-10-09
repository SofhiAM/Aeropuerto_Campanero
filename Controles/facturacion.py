from PySide2.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QMessageBox
from PySide2.QtCore import Qt
from Ventanas.factura import Facturacion
from Database.hangares_db import datos_factura, generar_salida, cambiar_estado_alibre
import datetime
from datetime import datetime
from datetime import date
import time

class Factura (QWidget, Facturacion):
    
    def __init__ (self, parent = None, cod_hangar=""):
        super().__init__(parent)

        self.padre_ventana = parent
        self.setupUi(self)
        self.setWindowFlag (Qt.Window)
        self.cod_hangar = cod_hangar

        self.generar_factura()
        self.bt_confirmar_salida.clicked.connect(self.salida)

#----------------------------------------------------------------------------
    def generar_factura (self):
#       descripcion, aero_dueña, hora_alquiler, fecha_alquiler, costo_base 
        now = datetime.now()

        datos = datos_factura(self.cod_hangar)
        self.lb_ModeloAvion.setText(datos[0])
        self.lb_NomAerolinea.setText(datos[1])

        str_horae = datos[2].strftime('%H:%M')
        self.lb_HoradeEntrada.setText(str_horae)

        str_fechae =  datos[3].strftime('%d/%m/%Y')
        self.lb_FechadeEntrada.setText(str_fechae)
        
        hora = now.strftime('%H:%M')
        self.lb_HoradeSalida.setText(hora)
        
        fecha = now.strftime('%d/%m/%Y')
        self.lb_FechadeSalida.setText(fecha)
        
        f1 = str_horae
        f2 = hora
        fmt = '%H:%M'

        diferencia = datetime.strptime(f2, fmt) - datetime.strptime(f1, fmt)        
        print(diferencia)
        self.lb_TiempoenHoras.setText(str(diferencia))

        nueva=""
        for i in str(diferencia):
            if i != ":":
                nueva = nueva + i
            else:
                break
        print (nueva)
        precio = int(nueva)*int(datos[4])
        self.lb_ValorHora.setText(str(datos[4]))
        self.lb_ValorTotal.setText(str(precio))

# -----------------------------------------------------------------------------------
    def salida (self):
        if generar_salida(self.cod_hangar):
            if cambiar_estado_alibre(self.cod_hangar):
                
                self.close()
                
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Liberado correctamente")
                dlg.setText("El hangar ha sido liberado con éxito\n"+
                            "Actualice la tabla para ver los cambios realizados")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Information)
                dlg.show()
