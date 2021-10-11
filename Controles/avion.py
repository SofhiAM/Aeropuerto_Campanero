from Database.avion import *
from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Qt
from Database.avion import *

class Avion (QWidget):
   def borrar_datos_usuario (self, id_avion):
      
      eliminar_id_avion(id_avion)

      return True 