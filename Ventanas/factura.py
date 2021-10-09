# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Facturación.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Facturacion(object):
    def setupUi(self, Facturacion):
        if not Facturacion.objectName():
            Facturacion.setObjectName(u"Facturacion")
        Facturacion.resize(366, 459)
        icon = QIcon()
        icon.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/Paper-Plane-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Facturacion.setWindowIcon(icon)
        self.lb_Avion = QLabel(Facturacion)
        self.lb_Avion.setObjectName(u"lb_Avion")
        self.lb_Avion.setGeometry(QRect(60, 90, 51, 21))
        font = QFont()
        font.setFamily(u"Nirmala UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lb_Avion.setFont(font)
        self.lb_Avion.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_ModeloAvion = QLabel(Facturacion)
        self.lb_ModeloAvion.setObjectName(u"lb_ModeloAvion")
        self.lb_ModeloAvion.setGeometry(QRect(200, 90, 111, 21))
        self.lb_ModeloAvion.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"font: 12pt \"Nirmala UI\";")
        self.lb_Aerolinea = QLabel(Facturacion)
        self.lb_Aerolinea.setObjectName(u"lb_Aerolinea")
        self.lb_Aerolinea.setGeometry(QRect(60, 120, 81, 21))
        self.lb_Aerolinea.setFont(font)
        self.lb_Aerolinea.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_NomAerolinea = QLabel(Facturacion)
        self.lb_NomAerolinea.setObjectName(u"lb_NomAerolinea")
        self.lb_NomAerolinea.setGeometry(QRect(210, 120, 71, 21))
        self.lb_NomAerolinea.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"font: 12pt \"Nirmala UI\";")
        self.lb_Horadeentrada = QLabel(Facturacion)
        self.lb_Horadeentrada.setObjectName(u"lb_Horadeentrada")
        self.lb_Horadeentrada.setGeometry(QRect(60, 150, 131, 21))
        self.lb_Horadeentrada.setFont(font)
        self.lb_Horadeentrada.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_HoradeEntrada = QLabel(Facturacion)
        self.lb_HoradeEntrada.setObjectName(u"lb_HoradeEntrada")
        self.lb_HoradeEntrada.setGeometry(QRect(210, 150, 81, 21))
        self.lb_HoradeEntrada.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"font: 12pt \"Nirmala UI\";")
        self.lb_Fechadeentrada = QLabel(Facturacion)
        self.lb_Fechadeentrada.setObjectName(u"lb_Fechadeentrada")
        self.lb_Fechadeentrada.setGeometry(QRect(60, 180, 141, 21))
        self.lb_Fechadeentrada.setFont(font)
        self.lb_Fechadeentrada.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_FechadeEntrada = QLabel(Facturacion)
        self.lb_FechadeEntrada.setObjectName(u"lb_FechadeEntrada")
        self.lb_FechadeEntrada.setGeometry(QRect(210, 180, 101, 21))
        self.lb_FechadeEntrada.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"font: 12pt \"Nirmala UI\";")
        self.lb_Tiempo = QLabel(Facturacion)
        self.lb_Tiempo.setObjectName(u"lb_Tiempo")
        self.lb_Tiempo.setGeometry(QRect(60, 270, 61, 21))
        self.lb_Tiempo.setFont(font)
        self.lb_Tiempo.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_TiempoenHoras = QLabel(Facturacion)
        self.lb_TiempoenHoras.setObjectName(u"lb_TiempoenHoras")
        self.lb_TiempoenHoras.setGeometry(QRect(210, 270, 71, 21))
        self.lb_TiempoenHoras.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"font: 12pt \"Nirmala UI\";")
        self.lb_valorporhora = QLabel(Facturacion)
        self.lb_valorporhora.setObjectName(u"lb_valorporhora")
        self.lb_valorporhora.setGeometry(QRect(60, 300, 121, 21))
        self.lb_valorporhora.setFont(font)
        self.lb_valorporhora.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_ValorHora = QLabel(Facturacion)
        self.lb_ValorHora.setObjectName(u"lb_ValorHora")
        self.lb_ValorHora.setGeometry(QRect(210, 300, 71, 21))
        self.lb_ValorHora.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"font: 12pt \"Nirmala UI\";")
        self.lb_ValorTotal = QLabel(Facturacion)
        self.lb_ValorTotal.setObjectName(u"lb_ValorTotal")
        self.lb_ValorTotal.setGeometry(QRect(190, 340, 121, 21))
        self.lb_ValorTotal.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"font: 12pt \"Nirmala UI\";")
        self.lb_Valortotal = QLabel(Facturacion)
        self.lb_Valortotal.setObjectName(u"lb_Valortotal")
        self.lb_Valortotal.setGeometry(QRect(60, 340, 101, 21))
        self.lb_Valortotal.setFont(font)
        self.lb_Valortotal.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.linea = QFrame(Facturacion)
        self.linea.setObjectName(u"linea")
        self.linea.setGeometry(QRect(50, 70, 271, 20))
        self.linea.setFrameShape(QFrame.HLine)
        self.linea.setFrameShadow(QFrame.Sunken)
        self.linea_3 = QFrame(Facturacion)
        self.linea_3.setObjectName(u"linea_3")
        self.linea_3.setGeometry(QRect(50, 360, 271, 20))
        self.linea_3.setFrameShape(QFrame.HLine)
        self.linea_3.setFrameShadow(QFrame.Sunken)
        self.linea_2 = QFrame(Facturacion)
        self.linea_2.setObjectName(u"linea_2")
        self.linea_2.setGeometry(QRect(310, 80, 21, 291))
        self.linea_2.setFrameShape(QFrame.VLine)
        self.linea_2.setFrameShadow(QFrame.Sunken)
        self.linea_4 = QFrame(Facturacion)
        self.linea_4.setObjectName(u"linea_4")
        self.linea_4.setGeometry(QRect(40, 80, 16, 291))
        self.linea_4.setFrameShape(QFrame.VLine)
        self.linea_4.setFrameShadow(QFrame.Sunken)
        self.lb_facturanum = QLabel(Facturacion)
        self.lb_facturanum.setObjectName(u"lb_facturanum")
        self.lb_facturanum.setGeometry(QRect(80, 20, 221, 41))
        self.lb_facturanum.setStyleSheet(u"font: 63 26pt \"Open Sans Semibold\";")
        self.linea_5 = QFrame(Facturacion)
        self.linea_5.setObjectName(u"linea_5")
        self.linea_5.setGeometry(QRect(50, 320, 271, 20))
        self.linea_5.setFrameShape(QFrame.HLine)
        self.linea_5.setFrameShadow(QFrame.Sunken)
        self.bt_confirmar_salida = QPushButton(Facturacion)
        self.bt_confirmar_salida.setObjectName(u"bt_confirmar_salida")
        self.bt_confirmar_salida.setGeometry(QRect(90, 390, 191, 41))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.bt_confirmar_salida.setFont(font1)
        self.bt_confirmar_salida.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_confirmar_salida.setStyleSheet(u"QPushButton\n"
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
        self.bt_confirmar_salida.setIcon(icon1)
        self.bt_confirmar_salida.setIconSize(QSize(30, 30))
        self.bt_confirmar_salida.setFlat(True)
        self.lb_FechadeSalida = QLabel(Facturacion)
        self.lb_FechadeSalida.setObjectName(u"lb_FechadeSalida")
        self.lb_FechadeSalida.setGeometry(QRect(210, 240, 101, 21))
        self.lb_FechadeSalida.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"font: 12pt \"Nirmala UI\";")
        self.lb_Fechadeentrada_2 = QLabel(Facturacion)
        self.lb_Fechadeentrada_2.setObjectName(u"lb_Fechadeentrada_2")
        self.lb_Fechadeentrada_2.setGeometry(QRect(60, 240, 141, 21))
        self.lb_Fechadeentrada_2.setFont(font)
        self.lb_Fechadeentrada_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Horadeentrada_2 = QLabel(Facturacion)
        self.lb_Horadeentrada_2.setObjectName(u"lb_Horadeentrada_2")
        self.lb_Horadeentrada_2.setGeometry(QRect(60, 210, 131, 21))
        self.lb_Horadeentrada_2.setFont(font)
        self.lb_Horadeentrada_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_HoradeSalida = QLabel(Facturacion)
        self.lb_HoradeSalida.setObjectName(u"lb_HoradeSalida")
        self.lb_HoradeSalida.setGeometry(QRect(210, 210, 81, 21))
        self.lb_HoradeSalida.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";\n"
"font: 12pt \"Nirmala UI\";")

        self.retranslateUi(Facturacion)

        QMetaObject.connectSlotsByName(Facturacion)
    # setupUi

    def retranslateUi(self, Facturacion):
        Facturacion.setWindowTitle(QCoreApplication.translate("Facturacion", u"Facturaci\u00f3n", None))
        self.lb_Avion.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">Avi\u00f3n</span></p></body></html>", None))
        self.lb_ModeloAvion.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Boeing 747</span></p></body></html>", None))
        self.lb_Aerolinea.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">Aerolinea</span></p></body></html>", None))
        self.lb_NomAerolinea.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Avianca</span></p></body></html>", None))
        self.lb_Horadeentrada.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">Hora de entrada</span></p></body></html>", None))
        self.lb_HoradeEntrada.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">7 : 00 A.M</span></p></body></html>", None))
        self.lb_Fechadeentrada.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">Fecha de entrada</span></p></body></html>", None))
        self.lb_FechadeEntrada.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">01/01/2021</span></p></body></html>", None))
        self.lb_Tiempo.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">Tiempo</span></p></body></html>", None))
        self.lb_TiempoenHoras.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">7 horas</span></p></body></html>", None))
        self.lb_valorporhora.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">Valor por hora $</span></p></body></html>", None))
        self.lb_ValorHora.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">30.000</span></p></body></html>", None))
        self.lb_ValorTotal.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">210.000</span></p></body></html>", None))
        self.lb_Valortotal.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">Valor total $</span></p></body></html>", None))
        self.lb_facturanum.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:400; color:#1675a3;\">Factura</span></p></body></html>", None))
        self.bt_confirmar_salida.setText(QCoreApplication.translate("Facturacion", u"CONFIRMAR SALIDA", None))
        self.lb_FechadeSalida.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">01/01/2021</span></p></body></html>", None))
        self.lb_Fechadeentrada_2.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">Fecha de salida</span></p></body></html>", None))
        self.lb_Horadeentrada_2.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">Hora de salida</span></p></body></html>", None))
        self.lb_HoradeSalida.setText(QCoreApplication.translate("Facturacion", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">7 : 00 A.M</span></p></body></html>", None))
    # retranslateUi

