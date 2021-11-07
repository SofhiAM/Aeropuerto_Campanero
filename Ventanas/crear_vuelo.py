# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Crear Vuelo - poner.ui'
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
        CrearVuelo.resize(633, 516)
        icon = QIcon()
        icon.addFile(u"../Ventanas/Icons/Paper-Plane-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        CrearVuelo.setWindowIcon(icon)
        self.lb_tipovuelo = QLabel(CrearVuelo)
        self.lb_tipovuelo.setObjectName(u"lb_tipovuelo")
        self.lb_tipovuelo.setGeometry(QRect(40, 90, 51, 31))
        self.lb_tipovuelo.setStyleSheet(u"font: 14pt \"Nirmala UI\";")
        self.label_aerolinea = QLabel(CrearVuelo)
        self.label_aerolinea.setObjectName(u"label_aerolinea")
        self.label_aerolinea.setGeometry(QRect(380, 90, 91, 31))
        self.label_aerolinea.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.groupBox_datosvuelo = QGroupBox(CrearVuelo)
        self.groupBox_datosvuelo.setObjectName(u"groupBox_datosvuelo")
        self.groupBox_datosvuelo.setGeometry(QRect(50, 140, 561, 341))
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
        icon1.addFile(u"../Ventanas/Icons/paper_plane_aceptar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_aceptarGEN.setIcon(icon1)
        self.bt_aceptarGEN.setIconSize(QSize(40, 50))
        self.bt_aceptarGEN.setFlat(True)
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
        self.tabla_datosdevuelo.addTab(self.tab_general, "")
        self.tab_Avion = QWidget()
        self.tab_Avion.setObjectName(u"tab_Avion")
        self.lb_Identificador = QLabel(self.tab_Avion)
        self.lb_Identificador.setObjectName(u"lb_Identificador")
        self.lb_Identificador.setGeometry(QRect(10, 20, 101, 31))
        self.lb_Identificador.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_TipodeAvion = QLabel(self.tab_Avion)
        self.lb_TipodeAvion.setObjectName(u"lb_TipodeAvion")
        self.lb_TipodeAvion.setGeometry(QRect(280, 20, 111, 31))
        self.lb_TipodeAvion.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Capacidad = QLabel(self.tab_Avion)
        self.lb_Capacidad.setObjectName(u"lb_Capacidad")
        self.lb_Capacidad.setGeometry(QRect(70, 130, 81, 31))
        self.lb_Capacidad.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Modelo = QLabel(self.tab_Avion)
        self.lb_Modelo.setObjectName(u"lb_Modelo")
        self.lb_Modelo.setGeometry(QRect(280, 70, 61, 31))
        self.lb_Modelo.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Propulsion = QLabel(self.tab_Avion)
        self.lb_Propulsion.setObjectName(u"lb_Propulsion")
        self.lb_Propulsion.setGeometry(QRect(20, 70, 91, 31))
        self.lb_Propulsion.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Motores = QLabel(self.tab_Avion)
        self.lb_Motores.setObjectName(u"lb_Motores")
        self.lb_Motores.setGeometry(QRect(230, 130, 71, 31))
        self.lb_Motores.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_PesoNominal = QLabel(self.tab_Avion)
        self.lb_PesoNominal.setObjectName(u"lb_PesoNominal")
        self.lb_PesoNominal.setGeometry(QRect(350, 130, 111, 31))
        self.lb_PesoNominal.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Kg = QLabel(self.tab_Avion)
        self.lb_Kg.setObjectName(u"lb_Kg")
        self.lb_Kg.setGeometry(QRect(450, 170, 21, 31))
        self.lb_Kg.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
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
        icon2.addFile(u"../Ventanas/Icons/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_check.setIcon(icon2)
        self.bt_check.setIconSize(QSize(30, 30))
        self.bt_check.setFlat(True)
        self.cb_identificador = QComboBox(self.tab_Avion)
        self.cb_identificador.setObjectName(u"cb_identificador")
        self.cb_identificador.setGeometry(QRect(120, 20, 101, 31))
        self.cb_identificador.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_identificador.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.cb_identificador.setEditable(False)
        self.cb_identificador.setDuplicatesEnabled(False)
        self.cb_identificador.setFrame(True)
        self.te_tipoAvion = QLineEdit(self.tab_Avion)
        self.te_tipoAvion.setObjectName(u"te_tipoAvion")
        self.te_tipoAvion.setEnabled(False)
        self.te_tipoAvion.setGeometry(QRect(400, 20, 113, 31))
        self.te_tipoAvion.setStyleSheet(u"font: 11pt \"Nirmala UI\";")
        self.te_propulsion = QLineEdit(self.tab_Avion)
        self.te_propulsion.setObjectName(u"te_propulsion")
        self.te_propulsion.setEnabled(False)
        self.te_propulsion.setGeometry(QRect(120, 70, 141, 31))
        self.te_propulsion.setStyleSheet(u"font: 11pt \"Nirmala UI\";")
        self.te_modelo = QLineEdit(self.tab_Avion)
        self.te_modelo.setObjectName(u"te_modelo")
        self.te_modelo.setEnabled(False)
        self.te_modelo.setGeometry(QRect(360, 70, 151, 31))
        self.te_modelo.setStyleSheet(u"font: 11pt \"Nirmala UI\";")
        self.te_capacidad = QLineEdit(self.tab_Avion)
        self.te_capacidad.setObjectName(u"te_capacidad")
        self.te_capacidad.setEnabled(False)
        self.te_capacidad.setGeometry(QRect(60, 170, 101, 31))
        self.te_capacidad.setStyleSheet(u"font: 11pt \"Nirmala UI\";")
        self.te_motores = QLineEdit(self.tab_Avion)
        self.te_motores.setObjectName(u"te_motores")
        self.te_motores.setEnabled(False)
        self.te_motores.setGeometry(QRect(220, 170, 91, 31))
        self.te_motores.setStyleSheet(u"font: 11pt \"Nirmala UI\";")
        self.te_peso = QLineEdit(self.tab_Avion)
        self.te_peso.setObjectName(u"te_peso")
        self.te_peso.setEnabled(False)
        self.te_peso.setGeometry(QRect(360, 170, 81, 31))
        self.te_peso.setStyleSheet(u"font: 11pt \"Nirmala UI\";")
        self.tabla_datosdevuelo.addTab(self.tab_Avion, "")
        self.tab_tripulacion = QWidget()
        self.tab_tripulacion.setObjectName(u"tab_tripulacion")
        self.lb_CodigoTripulacion = QLabel(self.tab_tripulacion)
        self.lb_CodigoTripulacion.setObjectName(u"lb_CodigoTripulacion")
        self.lb_CodigoTripulacion.setGeometry(QRect(130, 20, 151, 31))
        self.cb_CodigoTripulacion = QComboBox(self.tab_tripulacion)
        self.cb_CodigoTripulacion.setObjectName(u"cb_CodigoTripulacion")
        self.cb_CodigoTripulacion.setGeometry(QRect(290, 20, 101, 31))
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
        self.tableWidget.setGeometry(QRect(20, 70, 501, 141))
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
        self.bt_guardarTodo.setGeometry(QRect(200, 220, 131, 41))
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
        self.tabla_datosdevuelo.addTab(self.tab_tripulacion, "")
        self.cb_tipovuelo = QComboBox(CrearVuelo)
        self.cb_tipovuelo.addItem("")
        self.cb_tipovuelo.addItem("")
        self.cb_tipovuelo.setObjectName(u"cb_tipovuelo")
        self.cb_tipovuelo.setGeometry(QRect(90, 90, 81, 31))
        self.cb_tipovuelo.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_tipovuelo.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.cb_tipovuelo.setEditable(False)
        self.cb_tipovuelo.setDuplicatesEnabled(False)
        self.cb_tipovuelo.setFrame(True)
        self.textedit_codigovuelo = QLineEdit(CrearVuelo)
        self.textedit_codigovuelo.setObjectName(u"textedit_codigovuelo")
        self.textedit_codigovuelo.setGeometry(QRect(260, 90, 113, 31))
        self.textedit_codigovuelo.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.cb_aerolinea = QComboBox(CrearVuelo)
        self.cb_aerolinea.setObjectName(u"cb_aerolinea")
        self.cb_aerolinea.setGeometry(QRect(470, 90, 131, 31))
        self.cb_aerolinea.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_aerolinea.setStyleSheet(u"color : rgb(0,0,0); font: 10pt \"Nirmala UI\"")
        self.label_codigo = QLabel(CrearVuelo)
        self.label_codigo.setObjectName(u"label_codigo")
        self.label_codigo.setGeometry(QRect(190, 90, 61, 31))
        self.label_codigo.setStyleSheet(u"font: 75 14pt \"Nirmala UI\";\n"
"font: 75 12pt \"Nirmala UI\";")
        self.label_2 = QLabel(CrearVuelo)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 30, 371, 41))
        font5 = QFont()
        font5.setFamily(u"Open Sans Semibold")
        font5.setPointSize(26)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(7)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"font: 63 26pt \"Open Sans Semibold\";")

        self.retranslateUi(CrearVuelo)

        self.tabla_datosdevuelo.setCurrentIndex(0)
        self.bt_aceptarGEN.setDefault(False)
        self.bt_aceptarAV.setDefault(True)
        self.bt_guardarTodo.setDefault(True)


        QMetaObject.connectSlotsByName(CrearVuelo)
    # setupUi

    def retranslateUi(self, CrearVuelo):
        CrearVuelo.setWindowTitle(QCoreApplication.translate("CrearVuelo", u"Crear Vuelo", None))
        self.lb_tipovuelo.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#1675a3;\">Tipo</span></p></body></html>", None))
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
        self.lb_Capacidad.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Capacidad</span></p></body></html>", None))
        self.lb_Modelo.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Modelo</span></p></body></html>", None))
        self.lb_Propulsion.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Propulsi\u00f3n</span></p></body></html>", None))
        self.lb_Motores.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Motores</span></p></body></html>", None))
        self.lb_PesoNominal.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Peso Nominal</span></p></body></html>", None))
        self.lb_Kg.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:400; color:#000000;\">Kg</span></p></body></html>", None))
        self.bt_aceptarAV.setText(QCoreApplication.translate("CrearVuelo", u"ACEPTAR", None))
        self.bt_check.setText("")
        self.te_tipoAvion.setText("")
        self.te_propulsion.setText("")
        self.te_modelo.setText("")
        self.te_capacidad.setText("")
        self.te_motores.setText("")
        self.te_peso.setText("")
        self.tabla_datosdevuelo.setTabText(self.tabla_datosdevuelo.indexOf(self.tab_Avion), QCoreApplication.translate("CrearVuelo", u"Avi\u00f3n", None))
        self.lb_CodigoTripulacion.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">C\u00f3digo Tripulaci\u00f3n</span></p></body></html>", None))
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
        self.tabla_datosdevuelo.setTabText(self.tabla_datosdevuelo.indexOf(self.tab_tripulacion), QCoreApplication.translate("CrearVuelo", u"Tripulaci\u00f3n", None))
        self.cb_tipovuelo.setItemText(0, QCoreApplication.translate("CrearVuelo", u"Llegada", None))
        self.cb_tipovuelo.setItemText(1, QCoreApplication.translate("CrearVuelo", u"Salida", None))

        self.label_codigo.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#1675a3;\">C\u00f3digo</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:400; color:#1675a3;\">Crear Vuelo</span></p></body></html>", None))
    # retranslateUi

