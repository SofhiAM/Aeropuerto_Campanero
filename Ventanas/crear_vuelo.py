# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Crear Vuelo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import datetime
import time

class CrearVuelo(object):
    def setupUi(self, CrearVuelo):
        if not CrearVuelo.objectName():
            CrearVuelo.setObjectName(u"CrearVuelo")
        CrearVuelo.resize(633, 472)
        icon = QIcon()
        icon.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/Paper-Plane-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        CrearVuelo.setWindowIcon(icon)
        self.stackedWidget = QStackedWidget(CrearVuelo)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 70, 591, 391))
        self.pg_agregarVuelo = QWidget()
        self.pg_agregarVuelo.setObjectName(u"pg_agregarVuelo")
        self.label_aerolinea = QLabel(self.pg_agregarVuelo)
        self.label_aerolinea.setObjectName(u"label_aerolinea")
        self.label_aerolinea.setGeometry(QRect(350, 10, 91, 31))
        self.label_aerolinea.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.groupBox_datosvuelo = QGroupBox(self.pg_agregarVuelo)
        self.groupBox_datosvuelo.setObjectName(u"groupBox_datosvuelo")
        self.groupBox_datosvuelo.setGeometry(QRect(20, 50, 561, 341))
        font = QFont()
        font.setFamily(u"Nirmala UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.groupBox_datosvuelo.setFont(font)
        self.groupBox_datosvuelo.setStyleSheet(u"font: 75 10pt \"Nirmala UI\";")
        self.tabla_datosdevuelo = QTabWidget(self.groupBox_datosvuelo)
        self.tabla_datosdevuelo.setObjectName(u"tabla_datosdevuelo")
        self.tabla_datosdevuelo.setGeometry(QRect(10, 30, 541, 301))
        self.tabla_datosdevuelo.setCursor(QCursor(Qt.ArrowCursor))
        self.tabla_datosdevuelo.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabla_datosdevuelo.setStyleSheet(u"color: rgb(0, 0,0);\n"
"font: 75 11pt \"Nirmala UI\";\n"
"font: 75 10pt \"Nirmala UI\";")
        self.tabla_datosdevuelo.setMovable(False)
        self.tab_general = QWidget()
        self.tab_general.setObjectName(u"tab_general")
        self.date_FechaSalida = QDateEdit(self.tab_general)
        self.date_FechaSalida.setObjectName(u"date_FechaSalida")
        self.date_FechaSalida.setGeometry(QRect(140, 20, 110, 31))
        self.date_FechaSalida.setCursor(QCursor(Qt.IBeamCursor))
        ahora = datetime.datetime.now()
        self.date_FechaSalida.setDateTime(QDateTime(ahora)) 
        self.date_FechaSalida.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.date_FechaSalida.setAlignment(Qt.AlignCenter)
        self.date_FechaLlegada = QDateEdit(self.tab_general)
        self.date_FechaLlegada.setObjectName(u"date_FechaLlegada")
        self.date_FechaLlegada.setGeometry(QRect(140, 70, 110, 31))
        self.date_FechaLlegada.setCursor(QCursor(Qt.IBeamCursor))
        self.date_FechaLlegada.setDateTime(QDateTime(ahora))
        self.date_FechaLlegada.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.date_FechaLlegada.setAlignment(Qt.AlignCenter)
        self.time_HoraSalida = QTimeEdit(self.tab_general)
        self.time_HoraSalida.setObjectName(u"time_HoraSalida")
        self.time_HoraSalida.setGeometry(QRect(390, 21, 118, 31))
        self.time_HoraSalida.setCursor(QCursor(Qt.IBeamCursor))
        self.time_HoraSalida.setDateTime(QDateTime(ahora)) 
        self.time_HoraSalida.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.time_HoraSalida.setAlignment(Qt.AlignCenter)
        self.time_HoraLlegada = QTimeEdit(self.tab_general)
        self.time_HoraLlegada.setObjectName(u"time_HoraLlegada")
        self.time_HoraLlegada.setGeometry(QRect(390, 70, 118, 31))
        self.time_HoraLlegada.setCursor(QCursor(Qt.IBeamCursor))
        self.time_HoraLlegada.setDateTime(QDateTime(ahora)) 
        self.time_HoraLlegada.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.time_HoraLlegada.setAlignment(Qt.AlignCenter)
        self.lb_FechaSalida = QLabel(self.tab_general)
        self.lb_FechaSalida.setObjectName(u"lb_FechaSalida")
        self.lb_FechaSalida.setGeometry(QRect(20, 20, 101, 20))
        self.lb_FechaLlegada = QLabel(self.tab_general)
        self.lb_FechaLlegada.setObjectName(u"lb_FechaLlegada")
        self.lb_FechaLlegada.setGeometry(QRect(20, 70, 111, 21))
        self.lb_HoraSalida = QLabel(self.tab_general)
        self.lb_HoraSalida.setObjectName(u"lb_HoraSalida")
        self.lb_HoraSalida.setGeometry(QRect(280, 20, 91, 31))
        self.label_4 = QLabel(self.tab_general)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 70, 101, 31))
        self.lb_destino = QLabel(self.tab_general)
        self.lb_destino.setObjectName(u"lb_destino")
        self.lb_destino.setGeometry(QRect(20, 130, 61, 21))
        self.cb_Destino = QComboBox(self.tab_general)
        self.cb_Destino.addItem("")
        self.cb_Destino.addItem("")
        self.cb_Destino.addItem("")
        self.cb_Destino.addItem("")
        self.cb_Destino.addItem("")
        self.cb_Destino.addItem("")
        self.cb_Destino.setObjectName(u"cb_Destino")
        self.cb_Destino.setGeometry(QRect(90, 130, 421, 31))
        self.cb_Destino.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_Destino.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.lb_Origen = QLabel(self.tab_general)
        self.lb_Origen.setObjectName(u"lb_Origen")
        self.lb_Origen.setGeometry(QRect(20, 180, 51, 21))
        self.lb_Origen.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.cb_Origen = QComboBox(self.tab_general)
        self.cb_Origen.addItem("")
        self.cb_Origen.addItem("")
        self.cb_Origen.addItem("")
        self.cb_Origen.addItem("")
        self.cb_Origen.addItem("")
        self.cb_Origen.addItem("")
        self.cb_Origen.setObjectName(u"cb_Origen")
        self.cb_Origen.setGeometry(QRect(90, 180, 421, 31))
        self.cb_Origen.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_Origen.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.bt_aceptarGEN = QPushButton(self.tab_general)
        self.bt_aceptarGEN.setObjectName(u"bt_aceptarGEN")
        self.bt_aceptarGEN.setGeometry(QRect(210, 220, 121, 41))
        font1 = QFont()
        font1.setFamily(u"Nirmala UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.bt_aceptarGEN.setFont(font1)
        self.bt_aceptarGEN.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_aceptarGEN.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/paper_plane_aceptar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_aceptarGEN.setIcon(icon1)
        self.bt_aceptarGEN.setIconSize(QSize(40, 50))
        self.bt_aceptarGEN.setFlat(True)
        self.tabla_datosdevuelo.addTab(self.tab_general, "")
        self.tab_Avion = QWidget()
        self.tab_Avion.setObjectName(u"tab_Avion")
        self.lb_Identificador = QLabel(self.tab_Avion)
        self.lb_Identificador.setObjectName(u"lb_Identificador")
        self.lb_Identificador.setGeometry(QRect(10, 20, 101, 31))
        self.lb_Identificador.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.textedit_identificador = QLineEdit(self.tab_Avion)
        self.textedit_identificador.setObjectName(u"textedit_identificador")
        self.textedit_identificador.setGeometry(QRect(120, 20, 101, 31))
        self.textedit_identificador.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lb_TipodeAvion = QLabel(self.tab_Avion)
        self.lb_TipodeAvion.setObjectName(u"lb_TipodeAvion")
        self.lb_TipodeAvion.setGeometry(QRect(280, 20, 111, 31))
        self.lb_TipodeAvion.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.cb_tipodeAvion = QComboBox(self.tab_Avion)
        self.cb_tipodeAvion.addItem("")
        self.cb_tipodeAvion.addItem("")
        self.cb_tipodeAvion.setObjectName(u"cb_tipodeAvion")
        self.cb_tipodeAvion.setGeometry(QRect(400, 20, 121, 31))
        self.cb_tipodeAvion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_tipodeAvion.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.cb_tipodeAvion.setEditable(False)
        self.cb_tipodeAvion.setDuplicatesEnabled(False)
        self.cb_tipodeAvion.setFrame(True)
        self.lb_Capacidad = QLabel(self.tab_Avion)
        self.lb_Capacidad.setObjectName(u"lb_Capacidad")
        self.lb_Capacidad.setGeometry(QRect(40, 130, 81, 31))
        self.lb_Capacidad.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Modelo = QLabel(self.tab_Avion)
        self.lb_Modelo.setObjectName(u"lb_Modelo")
        self.lb_Modelo.setGeometry(QRect(280, 70, 61, 31))
        self.lb_Modelo.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Propulsion = QLabel(self.tab_Avion)
        self.lb_Propulsion.setObjectName(u"lb_Propulsion")
        self.lb_Propulsion.setGeometry(QRect(20, 70, 91, 31))
        self.lb_Propulsion.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.spinBox_Capacidad = QSpinBox(self.tab_Avion)
        self.spinBox_Capacidad.setObjectName(u"spinBox_Capacidad")
        self.spinBox_Capacidad.setGeometry(QRect(50, 170, 81, 31))
        self.spinBox_Capacidad.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 12pt \"Nirmala UI\"")
        self.cb_Propulsion = QComboBox(self.tab_Avion)
        self.cb_Propulsion.addItem("")
        self.cb_Propulsion.addItem("")
        self.cb_Propulsion.addItem("")
        self.cb_Propulsion.setObjectName(u"cb_Propulsion")
        self.cb_Propulsion.setGeometry(QRect(120, 70, 131, 31))
        self.cb_Propulsion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_Propulsion.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.cb_Propulsion.setEditable(False)
        self.cb_Propulsion.setDuplicatesEnabled(False)
        self.cb_Propulsion.setFrame(True)
        self.cb_Modelo = QComboBox(self.tab_Avion)
        self.cb_Modelo.addItem("")
        self.cb_Modelo.addItem("")
        self.cb_Modelo.addItem("")
        self.cb_Modelo.addItem("")
        self.cb_Modelo.addItem("")
        self.cb_Modelo.setObjectName(u"cb_Modelo")
        self.cb_Modelo.setGeometry(QRect(350, 70, 171, 31))
        self.cb_Modelo.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_Modelo.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.cb_Modelo.setEditable(False)
        self.cb_Modelo.setDuplicatesEnabled(False)
        self.cb_Modelo.setFrame(True)
        self.lb_Motores = QLabel(self.tab_Avion)
        self.lb_Motores.setObjectName(u"lb_Motores")
        self.lb_Motores.setGeometry(QRect(230, 130, 71, 31))
        self.lb_Motores.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.spinBox_Motores = QSpinBox(self.tab_Avion)
        self.spinBox_Motores.setObjectName(u"spinBox_Motores")
        self.spinBox_Motores.setGeometry(QRect(240, 170, 51, 31))
        self.spinBox_Motores.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 12pt \"Nirmala UI\"")
        self.lb_PesoNominal = QLabel(self.tab_Avion)
        self.lb_PesoNominal.setObjectName(u"lb_PesoNominal")
        self.lb_PesoNominal.setGeometry(QRect(350, 130, 111, 31))
        self.lb_PesoNominal.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.spinBox_pesoNom = QSpinBox(self.tab_Avion)
        self.spinBox_pesoNom.setObjectName(u"spinBox_pesoNom")
        self.spinBox_pesoNom.setGeometry(QRect(370, 170, 51, 31))
        self.spinBox_pesoNom.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 12pt \"Nirmala UI\"")
        self.lb_Kg = QLabel(self.tab_Avion)
        self.lb_Kg.setObjectName(u"lb_Kg")
        self.lb_Kg.setGeometry(QRect(430, 170, 21, 31))
        self.lb_Kg.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_capacidad = QLabel(self.tab_Avion)
        self.lb_capacidad.setObjectName(u"lb_capacidad")
        self.lb_capacidad.setGeometry(QRect(140, 170, 61, 31))
        self.lb_capacidad.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.bt_aceptarAV = QPushButton(self.tab_Avion)
        self.bt_aceptarAV.setObjectName(u"bt_aceptarAV")
        self.bt_aceptarAV.setGeometry(QRect(210, 220, 131, 41))
        font2 = QFont()
        font2.setFamily(u"Nirmala UI")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.bt_aceptarAV.setFont(font2)
        self.bt_aceptarAV.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_aceptarAV.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        self.bt_aceptarAV.setIcon(icon1)
        self.bt_aceptarAV.setIconSize(QSize(40, 50))
        self.bt_aceptarAV.setFlat(True)
        self.bt_check = QPushButton(self.tab_Avion)
        self.bt_check.setObjectName(u"bt_check")
        self.bt_check.setGeometry(QRect(220, 20, 41, 31))
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_check.setIcon(icon2)
        self.bt_check.setIconSize(QSize(30, 30))
        self.bt_check.setFlat(True)
        self.tabla_datosdevuelo.addTab(self.tab_Avion, "")
        self.tab_tripulacion = QWidget()
        self.tab_tripulacion.setObjectName(u"tab_tripulacion")
        self.lb_CodigoTripulacion = QLabel(self.tab_tripulacion)
        self.lb_CodigoTripulacion.setObjectName(u"lb_CodigoTripulacion")
        self.lb_CodigoTripulacion.setGeometry(QRect(10, 20, 151, 31))
        self.cb_CodigoTripulacion = QComboBox(self.tab_tripulacion)
        self.cb_CodigoTripulacion.addItem("")
        self.cb_CodigoTripulacion.addItem("")
        self.cb_CodigoTripulacion.addItem("")
        self.cb_CodigoTripulacion.setObjectName(u"cb_CodigoTripulacion")
        self.cb_CodigoTripulacion.setGeometry(QRect(170, 20, 101, 31))
        self.cb_CodigoTripulacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_CodigoTripulacion.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.cb_CodigoTripulacion.setEditable(False)
        self.cb_CodigoTripulacion.setDuplicatesEnabled(False)
        self.cb_CodigoTripulacion.setFrame(True)
        self.tableWidget = QTableWidget(self.tab_tripulacion)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        brush = QBrush(QColor(22, 117, 163, 255))
        brush.setStyle(Qt.SolidPattern)
        font3 = QFont()
        font3.setFamily(u"Nirmala UI")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        __qtablewidgetitem1.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        __qtablewidgetitem2.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        __qtablewidgetitem3.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        __qtablewidgetitem4.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        __qtablewidgetitem5.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 70, 501, 131))
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        font4 = QFont()
        font4.setFamily(u"Open Sans")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(1)
        self.tableWidget.setFont(font4)
        self.tableWidget.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 9 pt \"Open Sans\"")
        self.bt_guardarTodo = QPushButton(self.tab_tripulacion)
        self.bt_guardarTodo.setObjectName(u"bt_guardarTodo")
        self.bt_guardarTodo.setGeometry(QRect(130, 220, 131, 41))
        self.bt_guardarTodo.setFont(font2)
        self.bt_guardarTodo.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_guardarTodo.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        self.bt_guardarTodo.setIcon(icon1)
        self.bt_guardarTodo.setIconSize(QSize(40, 50))
        self.bt_guardarTodo.setFlat(True)
        self.bt_asigPiloto = QPushButton(self.tab_tripulacion)
        self.bt_asigPiloto.setObjectName(u"bt_asigPiloto")
        self.bt_asigPiloto.setGeometry(QRect(290, 20, 101, 31))
        self.nbt_asigCopi = QPushButton(self.tab_tripulacion)
        self.nbt_asigCopi.setObjectName(u"nbt_asigCopi")
        self.nbt_asigCopi.setGeometry(QRect(400, 20, 111, 31))
        self.bt_refreshTrip = QPushButton(self.tab_tripulacion)
        self.bt_refreshTrip.setObjectName(u"bt_refreshTrip")
        self.bt_refreshTrip.setGeometry(QRect(280, 220, 131, 41))
        self.bt_refreshTrip.setFont(font1)
        self.bt_refreshTrip.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_refreshTrip.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/recarga.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_refreshTrip.setIcon(icon2)
        self.bt_refreshTrip.setIconSize(QSize(30, 40))
        self.bt_refreshTrip.setFlat(True)
        self.tabla_datosdevuelo.addTab(self.tab_tripulacion, "")
        self.cb_tipovuelo = QComboBox(self.pg_agregarVuelo)
        self.cb_tipovuelo.addItem("")
        self.cb_tipovuelo.addItem("")
        self.cb_tipovuelo.setObjectName(u"cb_tipovuelo")
        self.cb_tipovuelo.setGeometry(QRect(60, 10, 81, 31))
        self.cb_tipovuelo.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_tipovuelo.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.cb_tipovuelo.setEditable(False)
        self.cb_tipovuelo.setDuplicatesEnabled(False)
        self.cb_tipovuelo.setFrame(True)
        self.label_codigo = QLabel(self.pg_agregarVuelo)
        self.label_codigo.setObjectName(u"label_codigo")
        self.label_codigo.setGeometry(QRect(160, 10, 61, 31))
        self.label_codigo.setStyleSheet(u"font: 75 14pt \"Nirmala UI\";\n"
"font: 75 12pt \"Nirmala UI\";")
        self.textedit_codigovuelo = QLineEdit(self.pg_agregarVuelo)
        self.textedit_codigovuelo.setObjectName(u"textedit_codigovuelo")
        self.textedit_codigovuelo.setGeometry(QRect(230, 10, 113, 31))
        self.textedit_codigovuelo.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.cb_aerolinea = QComboBox(self.pg_agregarVuelo)
        self.cb_aerolinea.setObjectName(u"cb_aerolinea")
        self.cb_aerolinea.setGeometry(QRect(440, 10, 131, 31))
        self.cb_aerolinea.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_aerolinea.setStyleSheet(u"color : rgb(0,0,0); font: 10pt \"Nirmala UI\"")
        self.lb_tipovuelo = QLabel(self.pg_agregarVuelo)
        self.lb_tipovuelo.setObjectName(u"lb_tipovuelo")
        self.lb_tipovuelo.setGeometry(QRect(10, 10, 51, 31))
        self.lb_tipovuelo.setStyleSheet(u"font: 14pt \"Nirmala UI\";")
        self.stackedWidget.addWidget(self.pg_agregarVuelo)
        self.pg_eliminarVuelo = QWidget()
        self.pg_eliminarVuelo.setObjectName(u"pg_eliminarVuelo")
        self.groupBox_2 = QGroupBox(self.pg_eliminarVuelo)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 70, 561, 261))
        self.groupBox_2.setFont(font3)
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.tb_vistaGeneralED = QTableWidget(self.groupBox_2)
        if (self.tb_vistaGeneralED.columnCount() < 11):
            self.tb_vistaGeneralED.setColumnCount(11)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        __qtablewidgetitem6.setForeground(brush);
        self.tb_vistaGeneralED.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font3);
        __qtablewidgetitem7.setForeground(brush);
        self.tb_vistaGeneralED.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font3);
        __qtablewidgetitem8.setForeground(brush);
        self.tb_vistaGeneralED.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font3);
        __qtablewidgetitem9.setForeground(brush);
        self.tb_vistaGeneralED.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font3);
        __qtablewidgetitem10.setForeground(brush);
        self.tb_vistaGeneralED.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font3);
        __qtablewidgetitem11.setForeground(brush);
        self.tb_vistaGeneralED.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font3);
        __qtablewidgetitem12.setForeground(brush);
        self.tb_vistaGeneralED.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font3);
        __qtablewidgetitem13.setForeground(brush);
        self.tb_vistaGeneralED.setHorizontalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font3);
        __qtablewidgetitem14.setForeground(brush);
        self.tb_vistaGeneralED.setHorizontalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font3);
        __qtablewidgetitem15.setForeground(brush);
        self.tb_vistaGeneralED.setHorizontalHeaderItem(9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font3);
        __qtablewidgetitem16.setForeground(brush);
        self.tb_vistaGeneralED.setHorizontalHeaderItem(10, __qtablewidgetitem16)
        self.tb_vistaGeneralED.setObjectName(u"tb_vistaGeneralED")
        self.tb_vistaGeneralED.setGeometry(QRect(10, 30, 531, 221))
        font5 = QFont()
        font5.setFamily(u"Open Sans")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.tb_vistaGeneralED.setFont(font5)
        self.tb_vistaGeneralED.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.le_buscarVuelo = QLineEdit(self.pg_eliminarVuelo)
        self.le_buscarVuelo.setObjectName(u"le_buscarVuelo")
        self.le_buscarVuelo.setGeometry(QRect(220, 20, 181, 31))
        font6 = QFont()
        font6.setFamily(u"Open Sans")
        font6.setPointSize(9)
        self.le_buscarVuelo.setFont(font6)
        self.bt_buscarVuelo = QPushButton(self.pg_eliminarVuelo)
        self.bt_buscarVuelo.setObjectName(u"bt_buscarVuelo")
        self.bt_buscarVuelo.setGeometry(QRect(400, 20, 91, 31))
        self.bt_buscarVuelo.setFont(font1)
        self.bt_buscarVuelo.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_buscarVuelo.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:#0069c0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/buscar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_buscarVuelo.setIcon(icon3)
        self.bt_buscarVuelo.setIconSize(QSize(30, 50))
        self.bt_buscarVuelo.setFlat(True)
        self.label_cerrarsesion_7 = QLabel(self.pg_eliminarVuelo)
        self.label_cerrarsesion_7.setObjectName(u"label_cerrarsesion_7")
        self.label_cerrarsesion_7.setGeometry(QRect(70, 20, 141, 31))
        font7 = QFont()
        font7.setFamily(u"Nirmala UI")
        font7.setPointSize(9)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_cerrarsesion_7.setFont(font7)
        self.bt_eliminarUNVuelo = QPushButton(self.pg_eliminarVuelo)
        self.bt_eliminarUNVuelo.setObjectName(u"bt_eliminarUNVuelo")
        self.bt_eliminarUNVuelo.setGeometry(QRect(230, 340, 131, 41))
        self.bt_eliminarUNVuelo.setFont(font1)
        self.bt_eliminarUNVuelo.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_eliminarUNVuelo.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/borrarVuelo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_eliminarUNVuelo.setIcon(icon4)
        self.bt_eliminarUNVuelo.setIconSize(QSize(30, 50))
        self.bt_eliminarUNVuelo.setFlat(True)
        self.stackedWidget.addWidget(self.pg_eliminarVuelo)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.bt_addVuelo = QPushButton(CrearVuelo)
        self.bt_addVuelo.setObjectName(u"bt_addVuelo")
        self.bt_addVuelo.setGeometry(QRect(40, 10, 161, 41))
        self.bt_addVuelo.setFont(font1)
        self.bt_addVuelo.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_addVuelo.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:#0069c0;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/agregar-aero.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_addVuelo.setIcon(icon5)
        self.bt_addVuelo.setIconSize(QSize(30, 50))
        self.bt_addVuelo.setFlat(True)
        self.bt_eliminarVuelo = QPushButton(CrearVuelo)
        self.bt_eliminarVuelo.setObjectName(u"bt_eliminarVuelo")
        self.bt_eliminarVuelo.setGeometry(QRect(230, 10, 161, 41))
        self.bt_eliminarVuelo.setFont(font1)
        self.bt_eliminarVuelo.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_eliminarVuelo.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:#0069c0;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_eliminarVuelo.setIcon(icon6)
        self.bt_eliminarVuelo.setIconSize(QSize(30, 50))
        self.bt_eliminarVuelo.setFlat(True)
        self.linea_2 = QFrame(CrearVuelo)
        self.linea_2.setObjectName(u"linea_2")
        self.linea_2.setGeometry(QRect(0, 50, 631, 21))
        self.linea_2.setFrameShape(QFrame.HLine)
        self.linea_2.setFrameShadow(QFrame.Sunken)
        self.bt_nuevoPiloto = QPushButton(CrearVuelo)
        self.bt_nuevoPiloto.setObjectName(u"bt_nuevoPiloto")
        self.bt_nuevoPiloto.setGeometry(QRect(420, 10, 161, 41))
        self.bt_nuevoPiloto.setFont(font1)
        self.bt_nuevoPiloto.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_nuevoPiloto.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:#0069c0;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/piloto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_nuevoPiloto.setIcon(icon7)
        self.bt_nuevoPiloto.setIconSize(QSize(30, 50))
        self.bt_nuevoPiloto.setFlat(True)

        self.retranslateUi(CrearVuelo)

        self.stackedWidget.setCurrentIndex(2)
        self.tabla_datosdevuelo.setCurrentIndex(0)
        self.bt_aceptarGEN.setDefault(False)
        self.bt_aceptarAV.setDefault(True)
        self.bt_guardarTodo.setDefault(True)


        QMetaObject.connectSlotsByName(CrearVuelo)
    # setupUi

    def retranslateUi(self, CrearVuelo):
        CrearVuelo.setWindowTitle(QCoreApplication.translate("CrearVuelo", u"Crear Vuelo", None))
        self.label_aerolinea.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#1675a3;\">Aerolinea</span></p></body></html>", None))
        self.groupBox_datosvuelo.setTitle(QCoreApplication.translate("CrearVuelo", u"Datos de Vuelo", None))
#if QT_CONFIG(tooltip)
        self.tabla_datosdevuelo.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tabla_datosdevuelo.setWhatsThis(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p>General</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lb_FechaSalida.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Fecha de Salida</span></p></body></html>", None))
        self.lb_FechaLlegada.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Fecha de Llegada</span></p></body></html>", None))
        self.lb_HoraSalida.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Hora de Salida</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Hora de Llegada</span></p></body></html>", None))
        self.lb_destino.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Destino</span></p></body></html>", None))
        self.cb_Destino.setItemText(0, QCoreApplication.translate("CrearVuelo", u"Cali", None))
        self.cb_Destino.setItemText(1, QCoreApplication.translate("CrearVuelo", u"Bogota", None))
        self.cb_Destino.setItemText(2, QCoreApplication.translate("CrearVuelo", u"Pasto", None))
        self.cb_Destino.setItemText(3, QCoreApplication.translate("CrearVuelo", u"Medell\u00edn", None))
        self.cb_Destino.setItemText(4, QCoreApplication.translate("CrearVuelo", u"Cartagena", None))
        self.cb_Destino.setItemText(5, QCoreApplication.translate("CrearVuelo", u"Pereira", None))
        self.lb_Origen.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Origen</span></p></body></html>", None))
        self.bt_aceptarGEN.setText(QCoreApplication.translate("CrearVuelo", u"ACEPTAR", None))
        self.cb_Origen.setItemText(0, QCoreApplication.translate("CrearVuelo", u"Cali", None))
        self.cb_Origen.setItemText(1, QCoreApplication.translate("CrearVuelo", u"Bogota", None))
        self.cb_Origen.setItemText(2, QCoreApplication.translate("CrearVuelo", u"Pasto", None))
        self.cb_Origen.setItemText(3, QCoreApplication.translate("CrearVuelo", u"Medell\u00edn", None))
        self.cb_Origen.setItemText(4, QCoreApplication.translate("CrearVuelo", u"Cartagena", None))
        self.cb_Origen.setItemText(5, QCoreApplication.translate("CrearVuelo", u"Pereira", None))
        self.tabla_datosdevuelo.setTabText(self.tabla_datosdevuelo.indexOf(self.tab_general), QCoreApplication.translate("CrearVuelo", u"General", None))
        self.lb_Identificador.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Identificador</span></p></body></html>", None))
        self.lb_TipodeAvion.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Tipo de Avi\u00f3n</span></p></body></html>", None))
        self.cb_tipodeAvion.setItemText(0, QCoreApplication.translate("CrearVuelo", u"Pasajeros", None))
        self.cb_tipodeAvion.setItemText(1, QCoreApplication.translate("CrearVuelo", u"Carga", None))

        self.lb_Capacidad.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Capacidad</span></p></body></html>", None))
        self.lb_Modelo.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Modelo</span></p></body></html>", None))
        self.lb_Propulsion.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Propulsi\u00f3n</span></p></body></html>", None))
        self.cb_Propulsion.setItemText(0, QCoreApplication.translate("CrearVuelo", u"Reacci\u00f3n", None))
        self.cb_Propulsion.setItemText(1, QCoreApplication.translate("CrearVuelo", u"Turbo H\u00e9lice", None))
        self.cb_Propulsion.setItemText(2, QCoreApplication.translate("CrearVuelo", u"H\u00e9lice", None))
        self.cb_Modelo.setItemText(0, QCoreApplication.translate("CrearVuelo", u"Airbus 330", None))
        self.cb_Modelo.setItemText(1, QCoreApplication.translate("CrearVuelo", u"Boeing 737", None))
        self.cb_Modelo.setItemText(2, QCoreApplication.translate("CrearVuelo", u"Airbus 234", None))
        self.cb_Modelo.setItemText(3, QCoreApplication.translate("CrearVuelo", u"Airbus 323", None))
        self.cb_Modelo.setItemText(4, QCoreApplication.translate("CrearVuelo", u"Boeing 657", None))

        self.lb_Motores.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Motores</span></p></body></html>", None))
        self.lb_PesoNominal.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Peso Nominal</span></p></body></html>", None))
        self.lb_Kg.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:400; color:#000000;\">Kg</span></p></body></html>", None))
        self.lb_capacidad.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:400; color:#000000;\">pasajeros</span></p></body></html>", None))
        self.bt_aceptarAV.setText(QCoreApplication.translate("CrearVuelo", u"ACEPTAR", None))
        self.tabla_datosdevuelo.setTabText(self.tabla_datosdevuelo.indexOf(self.tab_Avion), QCoreApplication.translate("CrearVuelo", u"Avi\u00f3n", None))
        self.lb_CodigoTripulacion.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">C\u00f3digo Tripulaci\u00f3n</span></p></body></html>", None))
        self.cb_CodigoTripulacion.setItemText(0, QCoreApplication.translate("CrearVuelo", u"TRIP1234", None))
        self.cb_CodigoTripulacion.setItemText(1, QCoreApplication.translate("CrearVuelo", u"TRIP6743", None))
        self.cb_CodigoTripulacion.setItemText(2, QCoreApplication.translate("CrearVuelo", u"TRIP4321", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CrearVuelo", u"C\u00e9dula", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CrearVuelo", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CrearVuelo", u"Apellido", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CrearVuelo", u"Licencia", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CrearVuelo", u"Rev Medica", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("CrearVuelo", u"Horas Vuelo", None));
        self.bt_guardarTodo.setText(QCoreApplication.translate("CrearVuelo", u"GUARDAR", None))
        self.bt_asigPiloto.setText(QCoreApplication.translate("CrearVuelo", u"Asignar Piloto", None))
        self.nbt_asigCopi.setText(QCoreApplication.translate("CrearVuelo", u"Asignar Copiloto", None))
        self.bt_refreshTrip.setText(QCoreApplication.translate("CrearVuelo", u"ACTUALIZAR", None))
        self.tabla_datosdevuelo.setTabText(self.tabla_datosdevuelo.indexOf(self.tab_tripulacion), QCoreApplication.translate("CrearVuelo", u"Tripulaci\u00f3n", None))
        self.cb_tipovuelo.setItemText(0, QCoreApplication.translate("CrearVuelo", u"Llegada", None))
        self.cb_tipovuelo.setItemText(1, QCoreApplication.translate("CrearVuelo", u"Salida", None))

        self.label_codigo.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#1675a3;\">C\u00f3digo</span></p></body></html>", None))
        self.lb_tipovuelo.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#1675a3;\">Tipo</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("CrearVuelo", u"Vuelos disponibles", None))
        ___qtablewidgetitem6 = self.tb_vistaGeneralED.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("CrearVuelo", u"Codigo", None));
        ___qtablewidgetitem7 = self.tb_vistaGeneralED.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("CrearVuelo", u"Tipo", None));
        ___qtablewidgetitem8 = self.tb_vistaGeneralED.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("CrearVuelo", u"Vuelo", None));
        ___qtablewidgetitem9 = self.tb_vistaGeneralED.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("CrearVuelo", u"Destino", None));
        ___qtablewidgetitem10 = self.tb_vistaGeneralED.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("CrearVuelo", u"Origen", None));
        ___qtablewidgetitem11 = self.tb_vistaGeneralED.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("CrearVuelo", u"Fecha", None));
        ___qtablewidgetitem12 = self.tb_vistaGeneralED.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("CrearVuelo", u"Hora", None));
        ___qtablewidgetitem13 = self.tb_vistaGeneralED.horizontalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("CrearVuelo", u"Avi\u00f3n", None));
        ___qtablewidgetitem14 = self.tb_vistaGeneralED.horizontalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("CrearVuelo", u"Aerolinea", None));
        ___qtablewidgetitem15 = self.tb_vistaGeneralED.horizontalHeaderItem(9)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("CrearVuelo", u"Nombre Piloto", None));
        ___qtablewidgetitem16 = self.tb_vistaGeneralED.horizontalHeaderItem(10)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("CrearVuelo", u"Apellido Piloto", None));
#if QT_CONFIG(tooltip)
        self.le_buscarVuelo.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.le_buscarVuelo.setInputMask("")
        self.le_buscarVuelo.setText("")
        self.le_buscarVuelo.setPlaceholderText("")
        self.bt_buscarVuelo.setText(QCoreApplication.translate("CrearVuelo", u"Buscar", None))
        self.label_cerrarsesion_7.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">C\u00f3digo de Vuelo</span></p></body></html>", None))
        self.bt_eliminarUNVuelo.setText(QCoreApplication.translate("CrearVuelo", u"Eliminar", None))
        self.bt_addVuelo.setText(QCoreApplication.translate("CrearVuelo", u"Agregar Vuelo ", None))
        self.bt_eliminarVuelo.setText(QCoreApplication.translate("CrearVuelo", u"Eliminar Vuelo", None))
        self.bt_nuevoPiloto.setText(QCoreApplication.translate("CrearVuelo", u"Nuevo piloto", None))
    # retranslateUi

