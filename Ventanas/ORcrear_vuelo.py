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


class CrearVuelo(object):
    def setupUi(self, CrearVuelo):
        if not CrearVuelo.objectName():
            CrearVuelo.setObjectName(u"CrearVuelo")
        CrearVuelo.resize(633, 443)
        icon = QIcon()
        icon.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/Paper-Plane-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        CrearVuelo.setWindowIcon(icon)
#if QT_CONFIG(tooltip)
        CrearVuelo.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        CrearVuelo.setToolTipDuration(-1)
        self.cb_tipovuelo = QComboBox(CrearVuelo)
        self.cb_tipovuelo.addItem("")
        self.cb_tipovuelo.addItem("")
        self.cb_tipovuelo.setObjectName(u"cb_tipovuelo")
        self.cb_tipovuelo.setGeometry(QRect(80, 30, 81, 31))
        font = QFont()
        font.setFamily(u"Nirmala UI Semilight")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb_tipovuelo.setFont(font)
        self.cb_tipovuelo.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_tipovuelo.setStyleSheet(u"font: 10pt \"Nirmala UI Semilight\";\n"
"color: rgb(0, 0,0);")
        self.cb_tipovuelo.setEditable(False)
        self.cb_tipovuelo.setDuplicatesEnabled(False)
        self.cb_tipovuelo.setFrame(True)
        self.textedit_codigovuelo = QTextEdit(CrearVuelo)
        self.textedit_codigovuelo.setObjectName(u"textedit_codigovuelo")
        self.textedit_codigovuelo.setGeometry(QRect(250, 30, 104, 31))
        self.textedit_codigovuelo.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.textedit_codigovuelo.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.cb_aerolinea = QComboBox(CrearVuelo)
        self.cb_aerolinea.setObjectName(u"cb_aerolinea")
        self.cb_aerolinea.setGeometry(QRect(460, 30, 131, 31))
        self.cb_aerolinea.setFont(font)
        self.cb_aerolinea.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_aerolinea.setStyleSheet(u"font: 10pt \"Nirmala UI Semilight\";\n"
"color: rgb(0, 0,0);")
        self.lb_tipovuelo = QLabel(CrearVuelo)
        self.lb_tipovuelo.setObjectName(u"lb_tipovuelo")
        self.lb_tipovuelo.setGeometry(QRect(30, 30, 51, 31))
        self.lb_tipovuelo.setStyleSheet(u"color : rgb(22, 117, 163);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_codigo = QLabel(CrearVuelo)
        self.label_codigo.setObjectName(u"label_codigo")
        self.label_codigo.setGeometry(QRect(180, 30, 61, 31))
        self.label_codigo.setStyleSheet(u"font: 75 14pt \"Nirmala UI\";\n"
"font: 75 12pt \"Nirmala UI\";")
        self.label_aerolinea = QLabel(CrearVuelo)
        self.label_aerolinea.setObjectName(u"label_aerolinea")
        self.label_aerolinea.setGeometry(QRect(370, 30, 91, 31))
        self.label_aerolinea.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.groupBox_datosvuelo = QGroupBox(CrearVuelo)
        self.groupBox_datosvuelo.setObjectName(u"groupBox_datosvuelo")
        self.groupBox_datosvuelo.setGeometry(QRect(20, 80, 601, 351))
        font1 = QFont()
        font1.setFamily(u"Nirmala UI")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(9)
        self.groupBox_datosvuelo.setFont(font1)
        self.groupBox_datosvuelo.setStyleSheet(u"font: 75 10pt \"Nirmala UI\";")
        self.tabla_datosdevuelo = QTabWidget(self.groupBox_datosvuelo)
        self.tabla_datosdevuelo.setObjectName(u"tabla_datosdevuelo")
        self.tabla_datosdevuelo.setGeometry(QRect(10, 30, 581, 311))
        self.tabla_datosdevuelo.setCursor(QCursor(Qt.ArrowCursor))
        self.tabla_datosdevuelo.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabla_datosdevuelo.setStyleSheet(u"font: 75 11pt \"Nirmala UI\";\n"
"font: 75 10pt \"Nirmala UI\";")
        self.tabla_datosdevuelo.setMovable(False)
        self.tab_general = QWidget()
        self.tab_general.setObjectName(u"tab_general")
        self.date_FechaSalida = QDateEdit(self.tab_general)
        self.date_FechaSalida.setObjectName(u"date_FechaSalida")
        self.date_FechaSalida.setGeometry(QRect(150, 30, 110, 31))
        font2 = QFont()
        font2.setFamily(u"Nirmala UI")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.date_FechaSalida.setFont(font2)
        self.date_FechaSalida.setCursor(QCursor(Qt.IBeamCursor))
        self.date_FechaSalida.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\";")
        self.date_FechaSalida.setAlignment(Qt.AlignCenter)
        self.date_FechaLlegada = QDateEdit(self.tab_general)
        self.date_FechaLlegada.setObjectName(u"date_FechaLlegada")
        self.date_FechaLlegada.setGeometry(QRect(150, 80, 110, 31))
        self.date_FechaLlegada.setCursor(QCursor(Qt.IBeamCursor))
        self.date_FechaLlegada.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\";")
        self.date_FechaLlegada.setAlignment(Qt.AlignCenter)
        self.time_HoraSalida = QTimeEdit(self.tab_general)
        self.time_HoraSalida.setObjectName(u"time_HoraSalida")
        self.time_HoraSalida.setGeometry(QRect(400, 31, 118, 31))
        self.time_HoraSalida.setCursor(QCursor(Qt.IBeamCursor))
        self.time_HoraSalida.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\";")
        self.time_HoraSalida.setAlignment(Qt.AlignCenter)
        self.time_HoraLlegada = QTimeEdit(self.tab_general)
        self.time_HoraLlegada.setObjectName(u"time_HoraLlegada")
        self.time_HoraLlegada.setGeometry(QRect(400, 80, 118, 31))
        self.time_HoraLlegada.setCursor(QCursor(Qt.IBeamCursor))
        self.time_HoraLlegada.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\";")
        self.time_HoraLlegada.setAlignment(Qt.AlignCenter)
        self.lb_FechaSalida = QLabel(self.tab_general)
        self.lb_FechaSalida.setObjectName(u"lb_FechaSalida")
        self.lb_FechaSalida.setGeometry(QRect(30, 30, 101, 20))
        self.lb_FechaLlegada = QLabel(self.tab_general)
        self.lb_FechaLlegada.setObjectName(u"lb_FechaLlegada")
        self.lb_FechaLlegada.setGeometry(QRect(30, 80, 111, 21))
        self.lb_HoraSalida = QLabel(self.tab_general)
        self.lb_HoraSalida.setObjectName(u"lb_HoraSalida")
        self.lb_HoraSalida.setGeometry(QRect(290, 30, 91, 20))
        self.label_4 = QLabel(self.tab_general)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 80, 101, 21))
        self.lb_destino = QLabel(self.tab_general)
        self.lb_destino.setObjectName(u"lb_destino")
        self.lb_destino.setGeometry(QRect(60, 130, 61, 31))
        self.cb_Destino = QComboBox(self.tab_general)
        self.cb_Destino.addItem("")
        self.cb_Destino.setObjectName(u"cb_Destino")
        self.cb_Destino.setGeometry(QRect(130, 130, 371, 31))
        self.cb_Destino.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_Destino.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\";")
        self.lb_Origen = QLabel(self.tab_general)
        self.lb_Origen.setObjectName(u"lb_Origen")
        self.lb_Origen.setGeometry(QRect(60, 180, 61, 31))
        self.lb_Origen.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.cb_Origen = QComboBox(self.tab_general)
        self.cb_Origen.setObjectName(u"cb_Origen")
        self.cb_Origen.setGeometry(QRect(130, 180, 371, 31))
        self.cb_Origen.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_Origen.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 11pt \"Nirmala UI\";")
        self.bt_aceptarGEN = QPushButton(self.tab_general)
        self.bt_aceptarGEN.setObjectName(u"bt_aceptarGEN")
        self.bt_aceptarGEN.setGeometry(QRect(230, 230, 121, 41))
        font3 = QFont()
        font3.setFamily(u"Nirmala UI")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.bt_aceptarGEN.setFont(font3)
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
        self.bt_aceptarGEN.setIconSize(QSize(30, 30))
        self.bt_aceptarGEN.setFlat(True)
        self.tabla_datosdevuelo.addTab(self.tab_general, "")
        self.tab_Avion = QWidget()
        self.tab_Avion.setObjectName(u"tab_Avion")
        self.lb_Identificador = QLabel(self.tab_Avion)
        self.lb_Identificador.setObjectName(u"lb_Identificador")
        self.lb_Identificador.setGeometry(QRect(20, 30, 111, 31))
        font4 = QFont()
        font4.setFamily(u"Nirmala UI")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(9)
        self.lb_Identificador.setFont(font4)
        self.lb_Identificador.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.textedit_identificador = QTextEdit(self.tab_Avion)
        self.textedit_identificador.setObjectName(u"textedit_identificador")
        self.textedit_identificador.setGeometry(QRect(140, 30, 131, 31))
        self.textedit_identificador.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.textedit_identificador.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lb_TipodeAvion = QLabel(self.tab_Avion)
        self.lb_TipodeAvion.setObjectName(u"lb_TipodeAvion")
        self.lb_TipodeAvion.setGeometry(QRect(300, 30, 111, 31))
        self.lb_TipodeAvion.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.cb_tipodeAvion = QComboBox(self.tab_Avion)
        self.cb_tipodeAvion.addItem("")
        self.cb_tipodeAvion.addItem("")
        self.cb_tipodeAvion.setObjectName(u"cb_tipodeAvion")
        self.cb_tipodeAvion.setGeometry(QRect(420, 30, 121, 31))
        self.cb_tipodeAvion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_tipodeAvion.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\";")
        self.cb_tipodeAvion.setEditable(False)
        self.cb_tipodeAvion.setDuplicatesEnabled(False)
        self.cb_tipodeAvion.setFrame(True)
        self.lb_Capacidad = QLabel(self.tab_Avion)
        self.lb_Capacidad.setObjectName(u"lb_Capacidad")
        self.lb_Capacidad.setGeometry(QRect(70, 130, 91, 31))
        self.lb_Capacidad.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Modelo = QLabel(self.tab_Avion)
        self.lb_Modelo.setObjectName(u"lb_Modelo")
        self.lb_Modelo.setGeometry(QRect(300, 80, 61, 31))
        self.lb_Modelo.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Propulsion = QLabel(self.tab_Avion)
        self.lb_Propulsion.setObjectName(u"lb_Propulsion")
        self.lb_Propulsion.setGeometry(QRect(30, 80, 91, 31))
        self.lb_Propulsion.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.spinBox_Capacidad = QSpinBox(self.tab_Avion)
        self.spinBox_Capacidad.setObjectName(u"spinBox_Capacidad")
        self.spinBox_Capacidad.setGeometry(QRect(80, 170, 61, 31))
        self.spinBox_Capacidad.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 11pt \"Nirmala UI\";")
        self.cb_Propulsion = QComboBox(self.tab_Avion)
        self.cb_Propulsion.addItem("")
        self.cb_Propulsion.addItem("")
        self.cb_Propulsion.addItem("")
        self.cb_Propulsion.setObjectName(u"cb_Propulsion")
        self.cb_Propulsion.setGeometry(QRect(140, 80, 131, 31))
        self.cb_Propulsion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_Propulsion.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\";")
        self.cb_Propulsion.setEditable(False)
        self.cb_Propulsion.setDuplicatesEnabled(False)
        self.cb_Propulsion.setFrame(True)
        self.cb_Modelo = QComboBox(self.tab_Avion)
        self.cb_Modelo.setObjectName(u"cb_Modelo")
        self.cb_Modelo.setGeometry(QRect(370, 80, 171, 31))
        self.cb_Modelo.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_Modelo.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\";")
        self.cb_Modelo.setEditable(False)
        self.cb_Modelo.setDuplicatesEnabled(False)
        self.cb_Modelo.setFrame(True)
        self.lb_Motores = QLabel(self.tab_Avion)
        self.lb_Motores.setObjectName(u"lb_Motores")
        self.lb_Motores.setGeometry(QRect(250, 130, 71, 31))
        self.lb_Motores.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.spinBox_Motores = QSpinBox(self.tab_Avion)
        self.spinBox_Motores.setObjectName(u"spinBox_Motores")
        self.spinBox_Motores.setGeometry(QRect(260, 170, 51, 31))
        self.spinBox_Motores.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.spinBox_Motores_2 = QSpinBox(self.tab_Avion)
        self.spinBox_Motores_2.setObjectName(u"spinBox_Motores_2")
        self.spinBox_Motores_2.setGeometry(QRect(390, 170, 51, 31))
        self.spinBox_Motores_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.lb_Kg = QLabel(self.tab_Avion)
        self.lb_Kg.setObjectName(u"lb_Kg")
        self.lb_Kg.setGeometry(QRect(450, 170, 21, 31))
        self.lb_Kg.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_capunidades = QLabel(self.tab_Avion)
        self.lb_capunidades.setObjectName(u"lb_capunidades")
        self.lb_capunidades.setGeometry(QRect(140, 170, 71, 31))
        self.lb_capunidades.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Motores_2 = QLabel(self.tab_Avion)
        self.lb_Motores_2.setObjectName(u"lb_Motores_2")
        self.lb_Motores_2.setGeometry(QRect(370, 130, 121, 31))
        self.lb_Motores_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.bt_aceptarAV = QPushButton(self.tab_Avion)
        self.bt_aceptarAV.setObjectName(u"bt_aceptarAV")
        self.bt_aceptarAV.setGeometry(QRect(220, 220, 121, 41))
        self.bt_aceptarAV.setFont(font3)
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
        self.bt_aceptarAV.setIconSize(QSize(30, 30))
        self.bt_aceptarAV.setFlat(True)
        self.tabla_datosdevuelo.addTab(self.tab_Avion, "")
        self.tab_tripulacion = QWidget()
        self.tab_tripulacion.setObjectName(u"tab_tripulacion")
        self.lb_CodigoTripulacion = QLabel(self.tab_tripulacion)
        self.lb_CodigoTripulacion.setObjectName(u"lb_CodigoTripulacion")
        self.lb_CodigoTripulacion.setGeometry(QRect(180, 20, 151, 31))
        self.cb_CodigoTripulacion = QComboBox(self.tab_tripulacion)
        self.cb_CodigoTripulacion.setObjectName(u"cb_CodigoTripulacion")
        self.cb_CodigoTripulacion.setGeometry(QRect(340, 20, 101, 31))
        self.cb_CodigoTripulacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_CodigoTripulacion.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\";")
        self.cb_CodigoTripulacion.setEditable(False)
        self.cb_CodigoTripulacion.setDuplicatesEnabled(False)
        self.cb_CodigoTripulacion.setFrame(True)
        self.table_Tripulacion = QTableWidget(self.tab_tripulacion)
        if (self.table_Tripulacion.columnCount() < 6):
            self.table_Tripulacion.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_Tripulacion.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_Tripulacion.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_Tripulacion.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_Tripulacion.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_Tripulacion.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_Tripulacion.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.table_Tripulacion.setObjectName(u"table_Tripulacion")
        self.table_Tripulacion.setGeometry(QRect(10, 60, 551, 151))
        self.table_Tripulacion.horizontalHeader().setDefaultSectionSize(106)
        self.bt_aceptarAV_2 = QPushButton(self.tab_tripulacion)
        self.bt_aceptarAV_2.setObjectName(u"bt_aceptarAV_2")
        self.bt_aceptarAV_2.setGeometry(QRect(230, 230, 121, 41))
        self.bt_aceptarAV_2.setFont(font3)
        self.bt_aceptarAV_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_aceptarAV_2.setStyleSheet(u"QPushButton\n"
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
        self.bt_aceptarAV_2.setIcon(icon1)
        self.bt_aceptarAV_2.setIconSize(QSize(30, 30))
        self.bt_aceptarAV_2.setFlat(True)
        self.tabla_datosdevuelo.addTab(self.tab_tripulacion, "")

        self.retranslateUi(CrearVuelo)

        self.tabla_datosdevuelo.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CrearVuelo)
    # setupUi

    def retranslateUi(self, CrearVuelo):
        CrearVuelo.setWindowTitle(QCoreApplication.translate("CrearVuelo", u"Crear Vuelo", None))
#if QT_CONFIG(statustip)
        CrearVuelo.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        CrearVuelo.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.cb_tipovuelo.setItemText(0, QCoreApplication.translate("CrearVuelo", u"Llegada", None))
        self.cb_tipovuelo.setItemText(1, QCoreApplication.translate("CrearVuelo", u"Salida", None))

        self.lb_tipovuelo.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#1675a3;\">Tipo</span></p></body></html>", None))
        self.label_codigo.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#1675a3;\">C\u00f3digo</span></p></body></html>", None))
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
        self.cb_Destino.setItemText(0, QCoreApplication.translate("CrearVuelo", u"Prueba de Letra", None))

        self.lb_Origen.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Origen</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.bt_aceptarGEN.setToolTip(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p><span style=\" font-size:7pt;\">Presione cuando todos los campos esten listos</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_aceptarGEN.setText(QCoreApplication.translate("CrearVuelo", u"ACEPTAR", None))
        self.tabla_datosdevuelo.setTabText(self.tabla_datosdevuelo.indexOf(self.tab_general), QCoreApplication.translate("CrearVuelo", u"General", None))
        self.lb_Identificador.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#000000;\">Identificador</span></p></body></html>", None))
        self.lb_TipodeAvion.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#000000;\">Tipo de Avi\u00f3n</span></p></body></html>", None))
        self.cb_tipodeAvion.setItemText(0, QCoreApplication.translate("CrearVuelo", u"Pasajeros", None))
        self.cb_tipodeAvion.setItemText(1, QCoreApplication.translate("CrearVuelo", u"Carga", None))

        self.lb_Capacidad.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#000000;\">Capacidad</span></p></body></html>", None))
        self.lb_Modelo.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#000000;\">Modelo</span></p></body></html>", None))
        self.lb_Propulsion.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#000000;\">Propulsi\u00f3n</span></p></body></html>", None))
        self.cb_Propulsion.setItemText(0, QCoreApplication.translate("CrearVuelo", u"Reacci\u00f3n", None))
        self.cb_Propulsion.setItemText(1, QCoreApplication.translate("CrearVuelo", u"Turbo H\u00e9lice", None))
        self.cb_Propulsion.setItemText(2, QCoreApplication.translate("CrearVuelo", u"H\u00e9lice", None))

        self.lb_Motores.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#000000;\">Motores</span></p></body></html>", None))
        self.lb_Kg.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:400; color:#000000;\">Kg</span></p></body></html>", None))
        self.lb_capunidades.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:400; color:#000000;\">pasajeros</span></p></body></html>", None))
        self.lb_Motores_2.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#000000;\">Peso Nominal</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.bt_aceptarAV.setToolTip(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p><span style=\" font-size:7pt;\">Presione cuando todos los campos esten listos</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_aceptarAV.setText(QCoreApplication.translate("CrearVuelo", u"ACEPTAR", None))
        self.tabla_datosdevuelo.setTabText(self.tabla_datosdevuelo.indexOf(self.tab_Avion), QCoreApplication.translate("CrearVuelo", u"Avi\u00f3n", None))
        self.lb_CodigoTripulacion.setText(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">C\u00f3digo Tripulaci\u00f3n</span></p></body></html>", None))
        ___qtablewidgetitem = self.table_Tripulacion.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CrearVuelo", u"C\u00e9dula", None));
        ___qtablewidgetitem1 = self.table_Tripulacion.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CrearVuelo", u"Nombre", None));
        ___qtablewidgetitem2 = self.table_Tripulacion.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CrearVuelo", u"Apellido", None));
        ___qtablewidgetitem3 = self.table_Tripulacion.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CrearVuelo", u"Cargo", None));
        ___qtablewidgetitem4 = self.table_Tripulacion.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CrearVuelo", u"Rev Medica", None));
        ___qtablewidgetitem5 = self.table_Tripulacion.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("CrearVuelo", u"Horas de Vuelo", None));
#if QT_CONFIG(tooltip)
        self.bt_aceptarAV_2.setToolTip(QCoreApplication.translate("CrearVuelo", u"<html><head/><body><p><span style=\" font-size:7pt;\">Presione cuando todos los campos esten listos</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_aceptarAV_2.setText(QCoreApplication.translate("CrearVuelo", u"GUARDAR", None))
        self.tabla_datosdevuelo.setTabText(self.tabla_datosdevuelo.indexOf(self.tab_tripulacion), QCoreApplication.translate("CrearVuelo", u"Tripulaci\u00f3n", None))
    # retranslateUi

