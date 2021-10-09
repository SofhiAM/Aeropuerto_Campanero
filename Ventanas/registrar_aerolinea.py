# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Registrar Aerolínea.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class regAerolinea(object):
    def setupUi(self, regAerolinea):
        if not regAerolinea.objectName():
            regAerolinea.setObjectName(u"regAerolinea")
        regAerolinea.resize(361, 382)
        icon = QIcon()
        icon.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/Paper-Plane-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        regAerolinea.setWindowIcon(icon)

        font = QFont()
        font.setPointSize(10)
        regAerolinea.setFont(font)
        self.label_2 = QLabel(regAerolinea)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 30, 221, 41))
        self.label_2.setStyleSheet(u"font: 63 26pt \"Open Sans Semibold\";")
        self.le_nit = QLineEdit(regAerolinea)
        self.le_nit.setObjectName(u"le_nit")
        self.le_nit.setGeometry(QRect(60, 110, 151, 21))
        font1 = QFont()
        font1.setFamily(u"Nirmala UI Semilight")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.le_nit.setFont(font1)
        self.le_nit.setStyleSheet(u"font: 10pt \"Nirmala UI Semilight\";")
        self.le_nit.setFrame(True)
        self.le_nit.setEchoMode(QLineEdit.Normal)
        self.le_nit.setDragEnabled(False)
        self.label = QLabel(regAerolinea)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 90, 47, 13))
        font2 = QFont()
        font2.setFamily(u"Nirmala UI Semilight")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label_3 = QLabel(regAerolinea)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 140, 81, 16))
        self.label_3.setFont(font2)
        self.le_nombreAerolinea = QLineEdit(regAerolinea)
        self.le_nombreAerolinea.setObjectName(u"le_nombreAerolinea")
        self.le_nombreAerolinea.setGeometry(QRect(60, 160, 251, 21))
        self.le_nombreAerolinea.setFont(font1)
        self.le_nombreAerolinea.setStyleSheet(u"font: 10pt \"Nirmala UI Semilight\";")
        self.le_nombreAerolinea.setFrame(True)
        self.le_nombreAerolinea.setEchoMode(QLineEdit.Normal)
        self.le_nombreAerolinea.setDragEnabled(False)
        self.le_coraerolinea = QLineEdit(regAerolinea)
        self.le_coraerolinea.setObjectName(u"le_coraerolinea")
        self.le_coraerolinea.setGeometry(QRect(60, 210, 251, 21))
        self.le_coraerolinea.setStyleSheet(u"font: 10pt \"Nirmala UI Semilight\";")
        self.le_coraerolinea.setFrame(True)
        self.le_coraerolinea.setEchoMode(QLineEdit.Normal)
        self.le_coraerolinea.setDragEnabled(False)
        self.label_4 = QLabel(regAerolinea)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 190, 131, 16))
        self.label_4.setFont(font2)
        self.le_telaerolinea = QLineEdit(regAerolinea)
        self.le_telaerolinea.setObjectName(u"le_telaerolinea")
        self.le_telaerolinea.setGeometry(QRect(60, 260, 161, 21))
        self.le_telaerolinea.setStyleSheet(u"font: 10pt \"Nirmala UI Semilight\";")
        self.le_telaerolinea.setFrame(True)
        self.le_telaerolinea.setEchoMode(QLineEdit.Normal)
        self.le_telaerolinea.setDragEnabled(False)
        self.label_5 = QLabel(regAerolinea)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 240, 81, 16))
        self.label_5.setFont(font2)
        self.bt_saveAerolinea = QPushButton(regAerolinea)
        self.bt_saveAerolinea.setObjectName(u"bt_saveAerolinea")
        self.bt_saveAerolinea.setGeometry(QRect(120, 310, 121, 41))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.bt_saveAerolinea.setFont(font3)
        self.bt_saveAerolinea.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_saveAerolinea.setStyleSheet(u"QPushButton\n"
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
        icon.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/save-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_saveAerolinea.setIcon(icon)
        self.bt_saveAerolinea.setIconSize(QSize(30, 30))
        self.bt_saveAerolinea.setFlat(True)

        self.retranslateUi(regAerolinea)

        QMetaObject.connectSlotsByName(regAerolinea)
    # setupUi

    def retranslateUi(self, regAerolinea):
        regAerolinea.setWindowTitle(QCoreApplication.translate("regAerolinea", u"Registrar Aerol\u00ednea", None))
        self.label_2.setText(QCoreApplication.translate("regAerolinea", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:400; color:#1675a3;\">Registrar Aerol\u00ednea</span></p></body></html>", None))
        self.le_nit.setText("")
        self.le_nit.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("regAerolinea", u"NIT", None))
        self.label_3.setText(QCoreApplication.translate("regAerolinea", u"Nombre ", None))
        self.le_nombreAerolinea.setText("")
        self.le_nombreAerolinea.setPlaceholderText("")
        self.le_coraerolinea.setText("")
        self.le_coraerolinea.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("regAerolinea", u"Correo Electr\u00f3nico", None))
        self.le_telaerolinea.setText("")
        self.le_telaerolinea.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("regAerolinea", u"Tel\u00e9fono", None))
        self.bt_saveAerolinea.setText(QCoreApplication.translate("regAerolinea", u"GUARDAR", None))
    # retranslateUi

