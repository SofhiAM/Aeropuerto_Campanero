# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Registro de Usuario.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class registrodeUsuario(object):
    def setupUi(self, RegistrodeUsuario):
        if not RegistrodeUsuario.objectName():
            RegistrodeUsuario.setObjectName(u"RegistrodeUsuario")
        RegistrodeUsuario.resize(708, 332)
        font = QFont()
        font.setFamily(u"Nirmala UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        RegistrodeUsuario.setFont(font)
        icon = QIcon()
        icon.addFile(u"../Ventanas/Icons/Paper-Plane-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        RegistrodeUsuario.setWindowIcon(icon)
        RegistrodeUsuario.setStyleSheet(u"font: \"Nirmala UI\";")
        self.lb_Nombres = QLabel(RegistrodeUsuario)
        self.lb_Nombres.setObjectName(u"lb_Nombres")
        self.lb_Nombres.setGeometry(QRect(30, 70, 81, 31))
        self.lb_Nombres.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lineEdit_Nombres = QLineEdit(RegistrodeUsuario)
        self.lineEdit_Nombres.setObjectName(u"lineEdit_Nombres")
        self.lineEdit_Nombres.setGeometry(QRect(120, 70, 201, 31))
        self.lineEdit_Nombres.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lb_Apellidos = QLabel(RegistrodeUsuario)
        self.lb_Apellidos.setObjectName(u"lb_Apellidos")
        self.lb_Apellidos.setGeometry(QRect(340, 70, 101, 31))
        self.lb_Apellidos.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lineEdit_Apellidos = QLineEdit(RegistrodeUsuario)
        self.lineEdit_Apellidos.setObjectName(u"lineEdit_Apellidos")
        self.lineEdit_Apellidos.setGeometry(QRect(440, 70, 241, 31))
        self.lineEdit_Apellidos.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lb_TipodeID = QLabel(RegistrodeUsuario)
        self.lb_TipodeID.setObjectName(u"lb_TipodeID")
        self.lb_TipodeID.setGeometry(QRect(30, 120, 91, 31))
        self.lb_TipodeID.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Identificacion = QLabel(RegistrodeUsuario)
        self.lb_Identificacion.setObjectName(u"lb_Identificacion")
        self.lb_Identificacion.setGeometry(QRect(340, 120, 141, 31))
        self.lb_Identificacion.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lineEdit_Identificacion = QLineEdit(RegistrodeUsuario)
        self.lineEdit_Identificacion.setObjectName(u"lineEdit_Identificacion")
        self.lineEdit_Identificacion.setGeometry(QRect(480, 120, 201, 31))
        self.lineEdit_Identificacion.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lb_Nombres_5 = QLabel(RegistrodeUsuario)
        self.lb_Nombres_5.setObjectName(u"lb_Nombres_5")
        self.lb_Nombres_5.setGeometry(QRect(30, 170, 151, 31))
        self.lb_Nombres_5.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lineEdit_CorreoElectronico = QLineEdit(RegistrodeUsuario)
        self.lineEdit_CorreoElectronico.setObjectName(u"lineEdit_CorreoElectronico")
        self.lineEdit_CorreoElectronico.setGeometry(QRect(190, 170, 201, 31))
        self.lineEdit_CorreoElectronico.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.cb_TipodeID = QComboBox(RegistrodeUsuario)
        self.cb_TipodeID.addItem("")
        self.cb_TipodeID.addItem("")
        self.cb_TipodeID.addItem("")
        self.cb_TipodeID.addItem("")
        self.cb_TipodeID.addItem("")
        self.cb_TipodeID.addItem("")
        self.cb_TipodeID.addItem("")
        self.cb_TipodeID.addItem("")
        self.cb_TipodeID.setObjectName(u"cb_TipodeID")
        self.cb_TipodeID.setGeometry(QRect(130, 120, 191, 31))
        self.cb_TipodeID.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_TipodeID.setAcceptDrops(False)
        self.cb_TipodeID.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.cb_TipodeID.setDuplicatesEnabled(False)
        self.lb_Contrasena = QLabel(RegistrodeUsuario)
        self.lb_Contrasena.setObjectName(u"lb_Contrasena")
        self.lb_Contrasena.setGeometry(QRect(420, 170, 101, 31))
        self.lb_Contrasena.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lineEdit_Contrasena = QLineEdit(RegistrodeUsuario)
        self.lineEdit_Contrasena.setObjectName(u"lineEdit_Contrasena")
        self.lineEdit_Contrasena.setGeometry(QRect(530, 170, 151, 31))
        self.lineEdit_Contrasena.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lb_TipodeCuenta = QLabel(RegistrodeUsuario)
        self.lb_TipodeCuenta.setObjectName(u"lb_TipodeCuenta")
        self.lb_TipodeCuenta.setGeometry(QRect(30, 220, 131, 31))
        self.lb_TipodeCuenta.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.cb_TipodeCuenta = QComboBox(RegistrodeUsuario)
        self.cb_TipodeCuenta.addItem("")
        self.cb_TipodeCuenta.addItem("")
        self.cb_TipodeCuenta.addItem("")
        self.cb_TipodeCuenta.setObjectName(u"cb_TipodeCuenta")
        self.cb_TipodeCuenta.setGeometry(QRect(170, 220, 171, 31))
        self.cb_TipodeCuenta.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_TipodeCuenta.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.bt_aceptarGEN = QPushButton(RegistrodeUsuario)
        self.bt_aceptarGEN.setObjectName(u"bt_aceptarGEN")
        self.bt_aceptarGEN.setGeometry(QRect(290, 270, 141, 41))
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
        icon1.addFile(u"../Ventanas/Icons/save-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_aceptarGEN.setIcon(icon1)
        self.bt_aceptarGEN.setIconSize(QSize(40, 50))
        self.bt_aceptarGEN.setFlat(True)
        self.lb_facturanum = QLabel(RegistrodeUsuario)
        self.lb_facturanum.setObjectName(u"lb_facturanum")
        self.lb_facturanum.setGeometry(QRect(250, 10, 221, 41))
        self.lb_facturanum.setStyleSheet(u"font: 63 26pt \"Open Sans Semibold\";")

        self.retranslateUi(RegistrodeUsuario)

        self.bt_aceptarGEN.setDefault(False)


        QMetaObject.connectSlotsByName(RegistrodeUsuario)
    # setupUi

    def retranslateUi(self, RegistrodeUsuario):
        RegistrodeUsuario.setWindowTitle(QCoreApplication.translate("RegistrodeUsuario", u"Registro de Usuario", None))
        self.lb_Nombres.setText(QCoreApplication.translate("RegistrodeUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Nombres </span><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.lb_Apellidos.setText(QCoreApplication.translate("RegistrodeUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Apellidos</span><span style=\" font-weight:600; color:#0055ff;\"/><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.lb_TipodeID.setText(QCoreApplication.translate("RegistrodeUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Tipo de ID</span><span style=\" font-weight:600; color:#0055ff;\"/><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.lb_Identificacion.setText(QCoreApplication.translate("RegistrodeUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Identificaci\u00f3n </span><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.lb_Nombres_5.setText(QCoreApplication.translate("RegistrodeUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Correo Electronico</span><span style=\" font-weight:600; color:#0055ff;\"/><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.cb_TipodeID.setItemText(0, QCoreApplication.translate("RegistrodeUsuario", u"C\u00e9dula de Ciudadan\u00eda", None))
        self.cb_TipodeID.setItemText(1, QCoreApplication.translate("RegistrodeUsuario", u"Tarjeta de Identidad", None))
        self.cb_TipodeID.setItemText(2, QCoreApplication.translate("RegistrodeUsuario", u"Registro Civil", None))
        self.cb_TipodeID.setItemText(3, QCoreApplication.translate("RegistrodeUsuario", u"NIT", None))
        self.cb_TipodeID.setItemText(4, QCoreApplication.translate("RegistrodeUsuario", u"C\u00e9dula Extranjer\u00eda", None))
        self.cb_TipodeID.setItemText(5, QCoreApplication.translate("RegistrodeUsuario", u"Tarjeta Extranjer\u00eda", None))
        self.cb_TipodeID.setItemText(6, QCoreApplication.translate("RegistrodeUsuario", u"Pasaporte", None))
        self.cb_TipodeID.setItemText(7, QCoreApplication.translate("RegistrodeUsuario", u"Tipo de Documento Extranjero", None))

        self.lb_Contrasena.setText(QCoreApplication.translate("RegistrodeUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Contrase\u00f1a</span><span style=\" font-weight:600; color:#0055ff;\"/><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.lb_TipodeCuenta.setText(QCoreApplication.translate("RegistrodeUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Tipo de Cuenta</span><span style=\" font-weight:600; color:#0055ff;\"/><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.cb_TipodeCuenta.setItemText(0, QCoreApplication.translate("RegistrodeUsuario", u"Admin. de aereolinea", None))
        self.cb_TipodeCuenta.setItemText(1, QCoreApplication.translate("RegistrodeUsuario", u"Funcionario de vuelos ", None))
        self.cb_TipodeCuenta.setItemText(2, QCoreApplication.translate("RegistrodeUsuario", u"Admin. Hangares", None))

        self.bt_aceptarGEN.setText(QCoreApplication.translate("RegistrodeUsuario", u"ACEPTAR", None))
        self.lb_facturanum.setText(QCoreApplication.translate("RegistrodeUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:400; color:#1675a3;\">Crear usuario</span></p></body></html>", None))
    # retranslateUi

