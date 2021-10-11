# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Modificar Usuario.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class editarUsuario(object):
    def setupUi(self, EditarUsuario):
        if not EditarUsuario.objectName():
            EditarUsuario.setObjectName(u"EditarUsuario")
        EditarUsuario.resize(709, 330)
        self.lb_Contrasena = QLabel(EditarUsuario)
        self.lb_Contrasena.setObjectName(u"lb_Contrasena")
        self.lb_Contrasena.setGeometry(QRect(420, 170, 101, 31))
        self.lb_Contrasena.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lineEdit_Contrasena = QLineEdit(EditarUsuario)
        self.lineEdit_Contrasena.setObjectName(u"lineEdit_Contrasena")
        self.lineEdit_Contrasena.setGeometry(QRect(530, 170, 151, 31))
        self.lineEdit_Contrasena.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.cb_TipodeID = QComboBox(EditarUsuario)
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
        self.lb_Nombres = QLabel(EditarUsuario)
        self.lb_Nombres.setObjectName(u"lb_Nombres")
        self.lb_Nombres.setGeometry(QRect(30, 70, 81, 31))
        self.lb_Nombres.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.bt_Guardar = QPushButton(EditarUsuario)
        self.bt_Guardar.setObjectName(u"bt_Guardar")
        self.bt_Guardar.setGeometry(QRect(290, 270, 141, 41))
        font = QFont()
        font.setFamily(u"Nirmala UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_Guardar.setFont(font)
        self.bt_Guardar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_Guardar.setStyleSheet(u"QPushButton\n"
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
        icon = QIcon()
        icon.addFile(u"../Ventanas/Icons/save-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_Guardar.setIcon(icon)
        self.bt_Guardar.setIconSize(QSize(40, 50))
        self.bt_Guardar.setFlat(True)
        self.lb_Nombres_5 = QLabel(EditarUsuario)
        self.lb_Nombres_5.setObjectName(u"lb_Nombres_5")
        self.lb_Nombres_5.setGeometry(QRect(30, 170, 151, 31))
        self.lb_Nombres_5.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_TipodeCuenta = QLabel(EditarUsuario)
        self.lb_TipodeCuenta.setObjectName(u"lb_TipodeCuenta")
        self.lb_TipodeCuenta.setGeometry(QRect(30, 220, 131, 31))
        self.lb_TipodeCuenta.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lineEdit_Nombres = QLineEdit(EditarUsuario)
        self.lineEdit_Nombres.setObjectName(u"lineEdit_Nombres")
        self.lineEdit_Nombres.setGeometry(QRect(120, 70, 201, 31))
        self.lineEdit_Nombres.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lb_Apellidos = QLabel(EditarUsuario)
        self.lb_Apellidos.setObjectName(u"lb_Apellidos")
        self.lb_Apellidos.setGeometry(QRect(340, 70, 101, 31))
        self.lb_Apellidos.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lineEdit_Identificacion = QLineEdit(EditarUsuario)
        self.lineEdit_Identificacion.setObjectName(u"lineEdit_Identificacion")
        self.lineEdit_Identificacion.setGeometry(QRect(480, 120, 201, 31))
        self.lineEdit_Identificacion.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lineEdit_CorreoElectronico = QLineEdit(EditarUsuario)
        self.lineEdit_CorreoElectronico.setObjectName(u"lineEdit_CorreoElectronico")
        self.lineEdit_CorreoElectronico.setGeometry(QRect(190, 170, 201, 31))
        self.lineEdit_CorreoElectronico.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lb_Identificacion = QLabel(EditarUsuario)
        self.lb_Identificacion.setObjectName(u"lb_Identificacion")
        self.lb_Identificacion.setGeometry(QRect(340, 120, 141, 31))
        self.lb_Identificacion.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_modificarusuario = QLabel(EditarUsuario)
        self.lb_modificarusuario.setObjectName(u"lb_modificarusuario")
        self.lb_modificarusuario.setGeometry(QRect(250, 10, 221, 41))
        self.lb_modificarusuario.setStyleSheet(u"font: 63 26pt \"Open Sans Semibold\";")
        self.lb_TipodeID = QLabel(EditarUsuario)
        self.lb_TipodeID.setObjectName(u"lb_TipodeID")
        self.lb_TipodeID.setGeometry(QRect(30, 120, 91, 31))
        self.lb_TipodeID.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.cb_TipodeCuenta = QComboBox(EditarUsuario)
        self.cb_TipodeCuenta.addItem("")
        self.cb_TipodeCuenta.addItem("")
        self.cb_TipodeCuenta.addItem("")
        self.cb_TipodeCuenta.setObjectName(u"cb_TipodeCuenta")
        self.cb_TipodeCuenta.setGeometry(QRect(170, 220, 171, 31))
        self.cb_TipodeCuenta.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_TipodeCuenta.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lineEdit_Apellidos = QLineEdit(EditarUsuario)
        self.lineEdit_Apellidos.setObjectName(u"lineEdit_Apellidos")
        self.lineEdit_Apellidos.setGeometry(QRect(440, 70, 241, 31))
        self.lineEdit_Apellidos.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lb_nuevacontrasena = QLabel(EditarUsuario)
        self.lb_nuevacontrasena.setObjectName(u"lb_nuevacontrasena")
        self.lb_nuevacontrasena.setGeometry(QRect(370, 220, 151, 31))
        self.lb_nuevacontrasena.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lineEdit_nuevacontrasena = QLineEdit(EditarUsuario)
        self.lineEdit_nuevacontrasena.setObjectName(u"lineEdit_nuevacontrasena")
        self.lineEdit_nuevacontrasena.setGeometry(QRect(530, 220, 151, 31))
        self.lineEdit_nuevacontrasena.setStyleSheet(u"font: 12pt \"Nirmala UI\";")

        self.retranslateUi(EditarUsuario)

        self.bt_Guardar.setDefault(False)


        QMetaObject.connectSlotsByName(EditarUsuario)
    # setupUi

    def retranslateUi(self, EditarUsuario):
        EditarUsuario.setWindowTitle(QCoreApplication.translate("EditarUsuario", u"Modificar Usuario", None))
        self.lb_Contrasena.setText(QCoreApplication.translate("EditarUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Contrase\u00f1a</span><span style=\" font-weight:600; color:#0055ff;\"/><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.cb_TipodeID.setItemText(0, QCoreApplication.translate("EditarUsuario", u"C\u00e9dula de Ciudadan\u00eda", None))
        self.cb_TipodeID.setItemText(1, QCoreApplication.translate("EditarUsuario", u"Tarjeta de Identidad", None))
        self.cb_TipodeID.setItemText(2, QCoreApplication.translate("EditarUsuario", u"Registro Civil", None))
        self.cb_TipodeID.setItemText(3, QCoreApplication.translate("EditarUsuario", u"NIT", None))
        self.cb_TipodeID.setItemText(4, QCoreApplication.translate("EditarUsuario", u"C\u00e9dula Extranjer\u00eda", None))
        self.cb_TipodeID.setItemText(5, QCoreApplication.translate("EditarUsuario", u"Tarjeta Extranjer\u00eda", None))
        self.cb_TipodeID.setItemText(6, QCoreApplication.translate("EditarUsuario", u"Pasaporte", None))
        self.cb_TipodeID.setItemText(7, QCoreApplication.translate("EditarUsuario", u"Tipo de Documento Extranjero", None))

        self.lb_Nombres.setText(QCoreApplication.translate("EditarUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Nombres </span><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.bt_Guardar.setText(QCoreApplication.translate("EditarUsuario", u"GUARDAR", None))
        self.lb_Nombres_5.setText(QCoreApplication.translate("EditarUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Correo Electronico</span><span style=\" font-weight:600; color:#0055ff;\"/><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.lb_TipodeCuenta.setText(QCoreApplication.translate("EditarUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Tipo de Cuenta</span><span style=\" font-weight:600; color:#0055ff;\"/><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.lb_Apellidos.setText(QCoreApplication.translate("EditarUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Apellidos</span><span style=\" font-weight:600; color:#0055ff;\"/><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.lb_Identificacion.setText(QCoreApplication.translate("EditarUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Identificaci\u00f3n </span><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.lb_modificarusuario.setText(QCoreApplication.translate("EditarUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:400; color:#1675a3;\">Modificar Usuario</span></p></body></html>", None))
        self.lb_TipodeID.setText(QCoreApplication.translate("EditarUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Tipo de ID</span><span style=\" font-weight:600; color:#0055ff;\"/><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.cb_TipodeCuenta.setItemText(0, QCoreApplication.translate("EditarUsuario", u"Admin. de aereolinea", None))
        self.cb_TipodeCuenta.setItemText(1, QCoreApplication.translate("EditarUsuario", u"Funcionario de vuelos ", None))
        self.cb_TipodeCuenta.setItemText(2, QCoreApplication.translate("EditarUsuario", u"Admin. Hangares", None))

        self.lb_nuevacontrasena.setText(QCoreApplication.translate("EditarUsuario", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Nueva contrase\u00f1a</span><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
    # retranslateUi

