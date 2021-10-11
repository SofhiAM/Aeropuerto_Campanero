# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ocupar Hangar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ocuparHangar(object):
    def setupUi(self, OcuparHangar):
        if not OcuparHangar.objectName():
            OcuparHangar.setObjectName(u"OcuparHangar")
        OcuparHangar.resize(643, 305)
        icon = QIcon()
        icon.addFile(u"D:/Sofia/Documents/AERO Campanero/Backend/Backend/Ventanas/Icons/Paper-Plane-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        OcuparHangar.setWindowIcon(icon)
        self.lineEdit_ModelodelAvion = QLineEdit(OcuparHangar)
        self.lineEdit_ModelodelAvion.setObjectName(u"lineEdit_ModelodelAvion")
        self.lineEdit_ModelodelAvion.setEnabled(False)
        self.lineEdit_ModelodelAvion.setGeometry(QRect(470, 80, 151, 31))
        self.lineEdit_ModelodelAvion.setStyleSheet(u"font: 9pt  \"Open Sans\";\n"
"")
        self.dateEdit_Fechaentrada = QDateEdit(OcuparHangar)
        self.dateEdit_Fechaentrada.setObjectName(u"dateEdit_Fechaentrada")
        self.dateEdit_Fechaentrada.setGeometry(QRect(170, 130, 121, 31))
        self.dateEdit_Fechaentrada.setCursor(QCursor(Qt.IBeamCursor))
        self.dateEdit_Fechaentrada.setStyleSheet(u"font: 9pt  \"Open Sans\";\n"
"")
        self.timeEdit_Horaentrada = QTimeEdit(OcuparHangar)
        self.timeEdit_Horaentrada.setObjectName(u"timeEdit_Horaentrada")
        self.timeEdit_Horaentrada.setGeometry(QRect(470, 130, 151, 31))
        self.timeEdit_Horaentrada.setCursor(QCursor(Qt.IBeamCursor))
        self.timeEdit_Horaentrada.setStyleSheet(u"font: 9pt  \"Open Sans\";\n"
"")
        self.cb_Valorporhora = QComboBox(OcuparHangar)
        self.cb_Valorporhora.addItem("")
        self.cb_Valorporhora.addItem("")
        self.cb_Valorporhora.addItem("")
        self.cb_Valorporhora.setObjectName(u"cb_Valorporhora")
        self.cb_Valorporhora.setGeometry(QRect(160, 180, 131, 31))
        self.cb_Valorporhora.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_Valorporhora.setStyleSheet(u"font: 9pt  \"Open Sans\";\n"
"")
        self.cb_Aerolinea = QComboBox(OcuparHangar)
        self.cb_Aerolinea.addItem("")
        self.cb_Aerolinea.setObjectName(u"cb_Aerolinea")
        self.cb_Aerolinea.setGeometry(QRect(420, 180, 201, 31))
        self.cb_Aerolinea.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_Aerolinea.setStyleSheet(u"font: 9pt  \"Open Sans\";\n"
"")
        self.lb_titleOcuparHangar = QLabel(OcuparHangar)
        self.lb_titleOcuparHangar.setObjectName(u"lb_titleOcuparHangar")
        self.lb_titleOcuparHangar.setGeometry(QRect(140, 20, 371, 41))
        self.lb_titleOcuparHangar.setStyleSheet(u"font: 63 26pt \"Open Sans Semibold\";")
        self.label_cerrarsesion_7 = QLabel(OcuparHangar)
        self.label_cerrarsesion_7.setObjectName(u"label_cerrarsesion_7")
        self.label_cerrarsesion_7.setGeometry(QRect(20, 80, 121, 31))
        font = QFont()
        font.setFamily(u"Nirmala UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_cerrarsesion_7.setFont(font)
        self.label_cerrarsesion_8 = QLabel(OcuparHangar)
        self.label_cerrarsesion_8.setObjectName(u"label_cerrarsesion_8")
        self.label_cerrarsesion_8.setGeometry(QRect(330, 80, 121, 31))
        self.label_cerrarsesion_8.setFont(font)
        self.label_cerrarsesion_9 = QLabel(OcuparHangar)
        self.label_cerrarsesion_9.setObjectName(u"label_cerrarsesion_9")
        self.label_cerrarsesion_9.setGeometry(QRect(30, 130, 121, 31))
        self.label_cerrarsesion_9.setFont(font)
        self.label_cerrarsesion_10 = QLabel(OcuparHangar)
        self.label_cerrarsesion_10.setObjectName(u"label_cerrarsesion_10")
        self.label_cerrarsesion_10.setGeometry(QRect(330, 130, 121, 31))
        self.label_cerrarsesion_10.setFont(font)
        self.label_cerrarsesion_11 = QLabel(OcuparHangar)
        self.label_cerrarsesion_11.setObjectName(u"label_cerrarsesion_11")
        self.label_cerrarsesion_11.setGeometry(QRect(30, 180, 121, 31))
        self.label_cerrarsesion_11.setFont(font)
        self.label_cerrarsesion_12 = QLabel(OcuparHangar)
        self.label_cerrarsesion_12.setObjectName(u"label_cerrarsesion_12")
        self.label_cerrarsesion_12.setGeometry(QRect(320, 180, 101, 31))
        self.label_cerrarsesion_12.setFont(font)
        self.bt_ocuparHangar = QPushButton(OcuparHangar)
        self.bt_ocuparHangar.setObjectName(u"bt_ocuparHangar")
        self.bt_ocuparHangar.setGeometry(QRect(260, 240, 131, 41))
        font1 = QFont()
        font1.setFamily(u"Nirmala UI")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.bt_ocuparHangar.setFont(font1)
        self.bt_ocuparHangar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_ocuparHangar.setStyleSheet(u"QPushButton:hover\n"
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
        icon1 = QIcon()
        icon1.addFile(u"D:/Sofia/Documents/AERO Campanero/Backend/Backend/Ventanas/Icons/save-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_ocuparHangar.setIcon(icon1)
        self.bt_ocuparHangar.setIconSize(QSize(30, 50))
        self.bt_ocuparHangar.setFlat(False)
        self.cb_cod_avion = QComboBox(OcuparHangar)
        self.cb_cod_avion.setObjectName(u"cb_cod_avion")
        self.cb_cod_avion.setGeometry(QRect(150, 80, 141, 31))
        self.cb_cod_avion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_cod_avion.setStyleSheet(u"font: 9pt  \"Open Sans\";\n"
"")

        self.retranslateUi(OcuparHangar)

        QMetaObject.connectSlotsByName(OcuparHangar)
    # setupUi

    def retranslateUi(self, OcuparHangar):
        OcuparHangar.setWindowTitle(QCoreApplication.translate("OcuparHangar", u"Ocupar Hangar", None))
        self.cb_Valorporhora.setItemText(0, QCoreApplication.translate("OcuparHangar", u"30.000", None))
        self.cb_Valorporhora.setItemText(1, QCoreApplication.translate("OcuparHangar", u"50.000", None))
        self.cb_Valorporhora.setItemText(2, QCoreApplication.translate("OcuparHangar", u"25.000", None))

        self.cb_Aerolinea.setItemText(0, "")

        self.lb_titleOcuparHangar.setText(QCoreApplication.translate("OcuparHangar", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:400; color:#1675a3;\">Ocupar Hangar</span></p></body></html>", None))
        self.label_cerrarsesion_7.setText(QCoreApplication.translate("OcuparHangar", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">C\u00f3digo Avi\u00f3n</span></p></body></html>", None))
        self.label_cerrarsesion_8.setText(QCoreApplication.translate("OcuparHangar", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Modelo de Avi\u00f3n</span></p></body></html>", None))
        self.label_cerrarsesion_9.setText(QCoreApplication.translate("OcuparHangar", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Fecha de Entrada</span></p></body></html>", None))
        self.label_cerrarsesion_10.setText(QCoreApplication.translate("OcuparHangar", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Hora de Entrada</span></p></body></html>", None))
        self.label_cerrarsesion_11.setText(QCoreApplication.translate("OcuparHangar", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Valor por hora $</span></p></body></html>", None))
        self.label_cerrarsesion_12.setText(QCoreApplication.translate("OcuparHangar", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Aerolinea</span></p></body></html>", None))
        self.bt_ocuparHangar.setText(QCoreApplication.translate("OcuparHangar", u"Guardar", None))
    # retranslateUi

