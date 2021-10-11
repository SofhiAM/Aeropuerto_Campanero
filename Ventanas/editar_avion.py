# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editar informacion de avion .ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class editarAvion(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(557, 360)
        icon = QIcon()
        icon.addFile(u"../Ventanas/Icons/Paper-Plane-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.spinBox_CapacidadEA = QSpinBox(Form)
        self.spinBox_CapacidadEA.setObjectName(u"spinBox_CapacidadEA")
        self.spinBox_CapacidadEA.setGeometry(QRect(80, 230, 81, 31))
        self.spinBox_CapacidadEA.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 12pt \"Nirmala UI\"")
        self.spinBox_CapacidadEA.setMinimum(1)
        self.lb_Propulsion_2 = QLabel(Form)
        self.lb_Propulsion_2.setObjectName(u"lb_Propulsion_2")
        self.lb_Propulsion_2.setGeometry(QRect(30, 140, 91, 31))
        self.lb_Propulsion_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.spinBox_pesoNomEA = QSpinBox(Form)
        self.spinBox_pesoNomEA.setObjectName(u"spinBox_pesoNomEA")
        self.spinBox_pesoNomEA.setGeometry(QRect(360, 230, 81, 31))
        self.spinBox_pesoNomEA.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 12pt \"Nirmala UI\"")
        self.spinBox_pesoNomEA.setMaximum(1000)
        self.lb_Identificador_2 = QLabel(Form)
        self.lb_Identificador_2.setObjectName(u"lb_Identificador_2")
        self.lb_Identificador_2.setGeometry(QRect(20, 70, 101, 31))
        self.lb_Identificador_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_PesoNominal_2 = QLabel(Form)
        self.lb_PesoNominal_2.setObjectName(u"lb_PesoNominal_2")
        self.lb_PesoNominal_2.setGeometry(QRect(340, 190, 111, 31))
        self.lb_PesoNominal_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Modelo_2 = QLabel(Form)
        self.lb_Modelo_2.setObjectName(u"lb_Modelo_2")
        self.lb_Modelo_2.setGeometry(QRect(290, 140, 61, 31))
        self.lb_Modelo_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.spinBox_MotoresEA = QSpinBox(Form)
        self.spinBox_MotoresEA.setObjectName(u"spinBox_MotoresEA")
        self.spinBox_MotoresEA.setGeometry(QRect(220, 230, 71, 31))
        self.spinBox_MotoresEA.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 12pt \"Nirmala UI\"")
        self.spinBox_MotoresEA.setMinimum(1)
        self.spinBox_MotoresEA.setMaximum(4)
        self.lb_Kg_2 = QLabel(Form)
        self.lb_Kg_2.setObjectName(u"lb_Kg_2")
        self.lb_Kg_2.setGeometry(QRect(450, 230, 21, 31))
        self.lb_Kg_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Capacidad_2 = QLabel(Form)
        self.lb_Capacidad_2.setObjectName(u"lb_Capacidad_2")
        self.lb_Capacidad_2.setGeometry(QRect(80, 190, 81, 31))
        self.lb_Capacidad_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.cb_PropulsionEA = QComboBox(Form)
        self.cb_PropulsionEA.addItem("")
        self.cb_PropulsionEA.addItem("")
        self.cb_PropulsionEA.addItem("")
        self.cb_PropulsionEA.setObjectName(u"cb_PropulsionEA")
        self.cb_PropulsionEA.setGeometry(QRect(130, 140, 131, 31))
        self.cb_PropulsionEA.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_PropulsionEA.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.cb_PropulsionEA.setEditable(False)
        self.cb_PropulsionEA.setDuplicatesEnabled(False)
        self.cb_PropulsionEA.setFrame(True)
        self.lb_Motores_2 = QLabel(Form)
        self.lb_Motores_2.setObjectName(u"lb_Motores_2")
        self.lb_Motores_2.setGeometry(QRect(220, 190, 71, 31))
        self.lb_Motores_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_TipodeAvion_2 = QLabel(Form)
        self.lb_TipodeAvion_2.setObjectName(u"lb_TipodeAvion_2")
        self.lb_TipodeAvion_2.setGeometry(QRect(290, 70, 111, 31))
        self.lb_TipodeAvion_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.cb_pasajerosEA = QComboBox(Form)
        self.cb_pasajerosEA.addItem("")
        self.cb_pasajerosEA.addItem("")
        self.cb_pasajerosEA.setObjectName(u"cb_pasajerosEA")
        self.cb_pasajerosEA.setGeometry(QRect(410, 70, 121, 31))
        self.cb_pasajerosEA.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_pasajerosEA.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.cb_pasajerosEA.setEditable(False)
        self.cb_pasajerosEA.setDuplicatesEnabled(False)
        self.cb_pasajerosEA.setFrame(True)
        self.bt_aceptarAVEA = QPushButton(Form)
        self.bt_aceptarAVEA.setObjectName(u"bt_aceptarAVEA")
        self.bt_aceptarAVEA.setGeometry(QRect(190, 300, 171, 41))
        font = QFont()
        font.setFamily(u"Nirmala UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bt_aceptarAVEA.setFont(font)
        self.bt_aceptarAVEA.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_aceptarAVEA.setStyleSheet(u"QPushButton\n"
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
        icon1.addFile(u"../Ventanas/Icons/agregar_avion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_aceptarAVEA.setIcon(icon1)
        self.bt_aceptarAVEA.setIconSize(QSize(40, 50))
        self.bt_aceptarAVEA.setFlat(True)
        self.lb_facturanum = QLabel(Form)
        self.lb_facturanum.setObjectName(u"lb_facturanum")
        self.lb_facturanum.setGeometry(QRect(100, 10, 391, 41))
        self.lb_facturanum.setStyleSheet(u"font: 63 26pt \"Open Sans Semibold\";")
        self.lineEdit_identificadorEA = QLineEdit(Form)
        self.lineEdit_identificadorEA.setObjectName(u"lineEdit_identificadorEA")
        self.lineEdit_identificadorEA.setEnabled(False)
        self.lineEdit_identificadorEA.setGeometry(QRect(130, 70, 121, 31))
        self.lineEdit_identificadorEA.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lineEdit_modeloEA = QLineEdit(Form)
        self.lineEdit_modeloEA.setObjectName(u"lineEdit_modeloEA")
        self.lineEdit_modeloEA.setGeometry(QRect(380, 140, 151, 31))
        self.lineEdit_modeloEA.setStyleSheet(u"font: 12pt \"Nirmala UI\";")

        self.retranslateUi(Form)

        self.bt_aceptarAVEA.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Editar informacion de avion ", None))
        self.lb_Propulsion_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Propulsi\u00f3n</span></p></body></html>", None))
        self.lb_Identificador_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Identificador</span></p></body></html>", None))
        self.lb_PesoNominal_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Peso Nominal</span></p></body></html>", None))
        self.lb_Modelo_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Modelo</span></p></body></html>", None))
        self.lb_Kg_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:400; color:#000000;\">Kg</span></p></body></html>", None))
        self.lb_Capacidad_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Capacidad</span></p></body></html>", None))
        self.cb_PropulsionEA.setItemText(0, QCoreApplication.translate("Form", u"Reacci\u00f3n", None))
        self.cb_PropulsionEA.setItemText(1, QCoreApplication.translate("Form", u"Turbo H\u00e9lice", None))
        self.cb_PropulsionEA.setItemText(2, QCoreApplication.translate("Form", u"H\u00e9lice", None))

        self.lb_Motores_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Motores</span></p></body></html>", None))
        self.lb_TipodeAvion_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Tipo de Avi\u00f3n</span></p></body></html>", None))
        self.cb_pasajerosEA.setItemText(0, QCoreApplication.translate("Form", u"Pasajeros", None))
        self.cb_pasajerosEA.setItemText(1, QCoreApplication.translate("Form", u"Carga", None))

        self.bt_aceptarAVEA.setText(QCoreApplication.translate("Form", u"GUARDAR AVION", None))
        self.lb_facturanum.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:400; color:#1675a3;\">Editar informacion de avi\u00f3n </span></p></body></html>", None))
    # retranslateUi

