# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main Window - Login Inicio.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1042, 606)
        icon = QIcon()
        icon.addFile(u"../Ventanas/Icons/Paper-Plane-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.pag_Main = QStackedWidget(mainWindow)
        self.pag_Main.setObjectName(u"pag_Main")
        self.pag_Main.setGeometry(QRect(0, 0, 1041, 601))
        self.Login = QWidget()
        self.Login.setObjectName(u"Login")
        self.correo_lineEdit = QLineEdit(self.Login)
        self.correo_lineEdit.setObjectName(u"correo_lineEdit")
        self.correo_lineEdit.setGeometry(QRect(390, 320, 321, 41))
        self.correo_lineEdit.setStyleSheet(u"font: 12pt \"Nirmala UI Semilight\";")
        self.correo_lineEdit.setFrame(True)
        self.correo_lineEdit.setEchoMode(QLineEdit.Normal)
        self.correo_lineEdit.setDragEnabled(False)
        self.bt_ingresarlg = QPushButton(self.Login)
        self.bt_ingresarlg.setObjectName(u"bt_ingresarlg")
        self.bt_ingresarlg.setGeometry(QRect(500, 460, 121, 41))
        self.bt_ingresarlg.setCursor(QCursor(Qt.ArrowCursor))
        self.bt_ingresarlg.setStyleSheet(u"font: 63 13pt \"Open Sans Semibold\";\n"
"color: rgb(22, 117, 163);")
        self.label_13 = QLabel(self.Login)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(430, 40, 231, 211))
        self.label_13.setPixmap(QPixmap(u"../Ventanas/Icons/Avion.png"))
        self.label_13.setScaledContents(True)
        self.lgcontra_lineEdit_2 = QLineEdit(self.Login)
        self.lgcontra_lineEdit_2.setObjectName(u"lgcontra_lineEdit_2")
        self.lgcontra_lineEdit_2.setGeometry(QRect(390, 380, 321, 41))
        self.lgcontra_lineEdit_2.setStyleSheet(u"font: 12pt \"Nirmala UI Semilight\";")
        self.lgcontra_lineEdit_2.setFrame(True)
        self.lgcontra_lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lgcontra_lineEdit_2.setDragEnabled(False)
        self.label_14 = QLabel(self.Login)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(310, 250, 471, 51))
        self.label_14.setStyleSheet(u"font: 63 26pt \"Open Sans Semibold\";")
        self.pag_Main.addWidget(self.Login)
        font8 = QFont()
        font8.setFamily(u"Open Sans")
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setWeight(50)
        self.Controls = QWidget()
        self.Controls.setObjectName(u"Controls")
        self.sk_mainWindow = QStackedWidget(self.Controls)
        self.sk_mainWindow.setObjectName(u"sk_mainWindow")
        self.sk_mainWindow.setGeometry(QRect(250, 10, 781, 581))
        self.pg_bienvenido = QWidget()
        self.pg_bienvenido.setObjectName(u"pg_bienvenido")
        self.label_cerrarsesion_2 = QLabel(self.pg_bienvenido)
        self.label_cerrarsesion_2.setObjectName(u"label_cerrarsesion_2")
        self.label_cerrarsesion_2.setGeometry(QRect(110, 430, 571, 51))
        font = QFont()
        font.setFamily(u"Open Sans Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_cerrarsesion_2.setFont(font)
        self.label_11 = QLabel(self.pg_bienvenido)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(240, 150, 301, 301))
        self.label_11.setPixmap(QPixmap(u"../Ventanas/Icons/Avion.png"))
        self.label_11.setScaledContents(True)
        self.label_cerrarsesion_97 = QLabel(self.pg_bienvenido)
        self.label_cerrarsesion_97.setObjectName(u"label_cerrarsesion_97")
        self.label_cerrarsesion_97.setGeometry(QRect(290, 110, 221, 41))
        font1 = QFont()
        font1.setFamily(u"Franklin Gothic Heavy")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_cerrarsesion_97.setFont(font1)
        self.sk_mainWindow.addWidget(self.pg_bienvenido)
        self.pg_usuarios = QWidget()
        self.pg_usuarios.setObjectName(u"pg_usuarios")
        self.bt_refreshUsuario = QPushButton(self.pg_usuarios)
        self.bt_refreshUsuario.setObjectName(u"bt_refreshUsuario")
        self.bt_refreshUsuario.setGeometry(QRect(600, 520, 131, 41))
        font2 = QFont()
        font2.setFamily(u"Nirmala UI")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.bt_refreshUsuario.setFont(font2)
        self.bt_refreshUsuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_refreshUsuario.setStyleSheet(u"QPushButton:hover\n"
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
        icon1.addFile(u"../Ventanas/Icons/recarga.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_refreshUsuario.setIcon(icon1)
        self.bt_refreshUsuario.setIconSize(QSize(30, 40))
        self.bt_refreshUsuario.setFlat(True)
        self.bt_buscarUsuario = QPushButton(self.pg_usuarios)
        self.bt_buscarUsuario.setObjectName(u"bt_buscarUsuario")
        self.bt_buscarUsuario.setGeometry(QRect(510, 30, 91, 31))
        self.bt_buscarUsuario.setFont(font2)
        self.bt_buscarUsuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_buscarUsuario.setStyleSheet(u"QPushButton:hover\n"
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
        icon2 = QIcon()
        icon2.addFile(u"../Ventanas/Icons/buscar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_buscarUsuario.setIcon(icon2)
        self.bt_buscarUsuario.setIconSize(QSize(30, 50))
        self.bt_buscarUsuario.setFlat(True)
        self.groupBox_4 = QGroupBox(self.pg_usuarios)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(40, 100, 701, 401))
        self.groupBox_4.setFont(font2)
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.tb_vistaGeneral_2 = QTableWidget(self.groupBox_4)
        if (self.tb_vistaGeneral_2.columnCount() < 6):
            self.tb_vistaGeneral_2.setColumnCount(6)
        brush = QBrush(QColor(22, 117, 163, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        __qtablewidgetitem.setForeground(brush);
        self.tb_vistaGeneral_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        __qtablewidgetitem1.setForeground(brush);
        self.tb_vistaGeneral_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        __qtablewidgetitem2.setForeground(brush);
        self.tb_vistaGeneral_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        __qtablewidgetitem3.setForeground(brush);
        self.tb_vistaGeneral_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        __qtablewidgetitem4.setForeground(brush);
        self.tb_vistaGeneral_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        __qtablewidgetitem5.setForeground(brush);
        self.tb_vistaGeneral_2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tb_vistaGeneral_2.setObjectName(u"tb_vistaGeneral_2")
        self.tb_vistaGeneral_2.setGeometry(QRect(10, 30, 681, 361))
        font3 = QFont()
        font3.setFamily(u"Open Sans")
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(1)
        self.tb_vistaGeneral_2.setFont(font8)
        self.tb_vistaGeneral_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        header = self.tb_vistaGeneral_2.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tb_vistaGeneral_2.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 9 pt \"Open Sans\"")
        self.bt_eliminarUsuario = QPushButton(self.pg_usuarios)
        self.bt_eliminarUsuario.setObjectName(u"bt_eliminarUsuario")
        self.bt_eliminarUsuario.setGeometry(QRect(220, 520, 171, 41))
        self.bt_eliminarUsuario.setFont(font2)
        self.bt_eliminarUsuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_eliminarUsuario.setStyleSheet(u"QPushButton:hover\n"
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
        icon3.addFile(u"../Ventanas/Icons/eliminar_usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_eliminarUsuario.setIcon(icon3)
        self.bt_eliminarUsuario.setIconSize(QSize(30, 50))
        self.bt_eliminarUsuario.setFlat(True)
        self.le_buscarUsuario = QLineEdit(self.pg_usuarios)
        self.le_buscarUsuario.setObjectName(u"le_buscarUsuario")
        self.le_buscarUsuario.setGeometry(QRect(270, 30, 221, 31))
        font4 = QFont()
        font4.setFamily(u"Open Sans")
        font4.setPointSize(9)
        self.le_buscarUsuario.setFont(font4)
        self.bt_editarUsuario = QPushButton(self.pg_usuarios)
        self.bt_editarUsuario.setObjectName(u"bt_editarUsuario")
        self.bt_editarUsuario.setGeometry(QRect(420, 520, 151, 41))
        self.bt_editarUsuario.setFont(font2)
        self.bt_editarUsuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_editarUsuario.setStyleSheet(u"QPushButton:hover\n"
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
        icon4 = QIcon()
        icon4.addFile(u"../Ventanas/Icons/editar_usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_editarUsuario.setIcon(icon4)
        self.bt_editarUsuario.setIconSize(QSize(30, 50))
        self.bt_editarUsuario.setFlat(True)
        self.bt_addUsuario = QPushButton(self.pg_usuarios)
        self.bt_addUsuario.setObjectName(u"bt_addUsuario")
        self.bt_addUsuario.setGeometry(QRect(20, 520, 171, 41))
        self.bt_addUsuario.setFont(font2)
        self.bt_addUsuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_addUsuario.setStyleSheet(u"QPushButton:hover\n"
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
        icon5.addFile(u"../Ventanas/Icons/nuevo_usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_addUsuario.setIcon(icon5)
        self.bt_addUsuario.setIconSize(QSize(30, 50))
        self.bt_addUsuario.setFlat(True)
        self.label_cerrarsesion_98 = QLabel(self.pg_usuarios)
        self.label_cerrarsesion_98.setObjectName(u"label_cerrarsesion_98")
        self.label_cerrarsesion_98.setGeometry(QRect(140, 30, 101, 31))
        font5 = QFont()
        font5.setFamily(u"Nirmala UI")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_cerrarsesion_98.setFont(font5)
        self.sk_mainWindow.addWidget(self.pg_usuarios)
        self.pg_aerolinea = QWidget()
        self.pg_aerolinea.setObjectName(u"pg_aerolinea")
        self.groupBox = QGroupBox(self.pg_aerolinea)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 80, 711, 441))
        self.groupBox.setFont(font2)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.tb_aeroRegistradas = QTableWidget(self.groupBox)
        if (self.tb_aeroRegistradas.columnCount() < 4):
            self.tb_aeroRegistradas.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font2);
        __qtablewidgetitem6.setForeground(brush);
        self.tb_aeroRegistradas.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font2);
        __qtablewidgetitem7.setForeground(brush);
        self.tb_aeroRegistradas.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font2);
        __qtablewidgetitem8.setForeground(brush);
        self.tb_aeroRegistradas.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font2);
        __qtablewidgetitem9.setForeground(brush);
        self.tb_aeroRegistradas.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        self.tb_aeroRegistradas.setObjectName(u"tb_aeroRegistradas")
        self.tb_aeroRegistradas.setGeometry(QRect(20, 40, 671, 381))
        font6 = QFont()
        font6.setFamily(u"Open Sans")
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setWeight(50)
        self.tb_aeroRegistradas.setFont(font8)
        self.tb_aeroRegistradas.setSelectionBehavior(QAbstractItemView.SelectRows)
        header = self.tb_aeroRegistradas.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.le_buscarAero = QLineEdit(self.pg_aerolinea)
        self.le_buscarAero.setObjectName(u"le_buscarAero")
        self.le_buscarAero.setGeometry(QRect(130, 20, 351, 31))
        self.le_buscarAero.setFont(font4)
        self.bt_buscarAerolinea = QPushButton(self.pg_aerolinea)
        self.bt_buscarAerolinea.setObjectName(u"bt_buscarAerolinea")
        self.bt_buscarAerolinea.setGeometry(QRect(500, 20, 91, 31))
        self.bt_buscarAerolinea.setFont(font2)
        self.bt_buscarAerolinea.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_buscarAerolinea.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_buscarAerolinea.setIcon(icon2)
        self.bt_buscarAerolinea.setIconSize(QSize(30, 50))
        self.bt_buscarAerolinea.setFlat(True)
        self.bt_addAerolinea = QPushButton(self.pg_aerolinea)
        self.bt_addAerolinea.setObjectName(u"bt_addAerolinea")
        self.bt_addAerolinea.setGeometry(QRect(20, 530, 171, 31))
        self.bt_addAerolinea.setFont(font2)
        self.bt_addAerolinea.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_addAerolinea.setStyleSheet(u"QPushButton:hover\n"
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
        icon6.addFile(u"../Ventanas/Icons/agregar-aero.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_addAerolinea.setIcon(icon6)
        self.bt_addAerolinea.setIconSize(QSize(30, 50))
        self.bt_addAerolinea.setFlat(True)
        self.bt_editarAerolinea = QPushButton(self.pg_aerolinea)
        self.bt_editarAerolinea.setObjectName(u"bt_editarAerolinea")
        self.bt_editarAerolinea.setGeometry(QRect(430, 530, 161, 31))
        self.bt_editarAerolinea.setFont(font2)
        self.bt_editarAerolinea.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_editarAerolinea.setStyleSheet(u"QPushButton:hover\n"
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
        icon7.addFile(u"../Ventanas/Icons/editar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_editarAerolinea.setIcon(icon7)
        self.bt_editarAerolinea.setIconSize(QSize(30, 50))
        self.bt_editarAerolinea.setFlat(True)
        self.bt_refreshAerolinea = QPushButton(self.pg_aerolinea)
        self.bt_refreshAerolinea.setObjectName(u"bt_refreshAerolinea")
        self.bt_refreshAerolinea.setGeometry(QRect(620, 530, 131, 31))
        self.bt_refreshAerolinea.setFont(font2)
        self.bt_refreshAerolinea.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_refreshAerolinea.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_refreshAerolinea.setIcon(icon1)
        self.bt_refreshAerolinea.setIconSize(QSize(30, 40))
        self.bt_refreshAerolinea.setFlat(True)
        self.bt_eliminarAerolinea = QPushButton(self.pg_aerolinea)
        self.bt_eliminarAerolinea.setObjectName(u"bt_eliminarAerolinea")
        self.bt_eliminarAerolinea.setGeometry(QRect(230, 530, 171, 31))
        self.bt_eliminarAerolinea.setFont(font2)
        self.bt_eliminarAerolinea.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_eliminarAerolinea.setStyleSheet(u"QPushButton:hover\n"
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
        icon8 = QIcon()
        icon8.addFile(u"../Ventanas/Icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_eliminarAerolinea.setIcon(icon8)
        self.bt_eliminarAerolinea.setIconSize(QSize(30, 50))
        self.bt_eliminarAerolinea.setFlat(True)
        self.sk_mainWindow.addWidget(self.pg_aerolinea)
        self.pg_agenda = QWidget()
        self.pg_agenda.setObjectName(u"pg_agenda")
        self.groupBox_2 = QGroupBox(self.pg_agenda)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 80, 721, 391))
        self.groupBox_2.setFont(font2)
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.sk_agendaAero = QStackedWidget(self.groupBox_2)
        self.sk_agendaAero.setObjectName(u"sk_agendaAero")
        self.sk_agendaAero.setGeometry(QRect(20, 30, 681, 341))
        self.sk_vistaGeneral = QWidget()
        self.sk_vistaGeneral.setObjectName(u"sk_vistaGeneral")
        self.tb_vistaGeneral = QTableWidget(self.sk_vistaGeneral)
        if (self.tb_vistaGeneral.columnCount() < 8):
            self.tb_vistaGeneral.setColumnCount(8)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font2);
        __qtablewidgetitem10.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font2);
        __qtablewidgetitem11.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font2);
        __qtablewidgetitem12.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font2);
        __qtablewidgetitem13.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font2);
        __qtablewidgetitem14.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font2);
        __qtablewidgetitem15.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font2);
        __qtablewidgetitem16.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font2);
        __qtablewidgetitem17.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(7, __qtablewidgetitem17)
        self.tb_vistaGeneral.setObjectName(u"tb_vistaGeneral")
        self.tb_vistaGeneral.setGeometry(QRect(0, 0, 681, 341))
        self.tb_vistaGeneral.setFont(font8)
        self.tb_vistaGeneral.setSelectionBehavior(QAbstractItemView.SelectRows)
        header = self.tb_vistaGeneral.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tb_vistaGeneral.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 9 pt \"Open Sans\"")
        self.sk_agendaAero.addWidget(self.sk_vistaGeneral)
        self.sk_salida = QWidget()
        self.sk_salida.setObjectName(u"sk_salida")
        self.tb_vistaSalida = QTableWidget(self.sk_salida)
        if (self.tb_vistaSalida.columnCount() < 6):
            self.tb_vistaSalida.setColumnCount(6)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font2);
        __qtablewidgetitem18.setForeground(brush);
        self.tb_vistaSalida.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font2);
        __qtablewidgetitem19.setForeground(brush);
        self.tb_vistaSalida.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font2);
        __qtablewidgetitem20.setForeground(brush);
        self.tb_vistaSalida.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font2);
        __qtablewidgetitem21.setForeground(brush);
        self.tb_vistaSalida.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font2);
        __qtablewidgetitem22.setForeground(brush);
        self.tb_vistaSalida.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font2);
        __qtablewidgetitem23.setForeground(brush);
        self.tb_vistaSalida.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        self.tb_vistaSalida.setObjectName(u"tb_vistaSalida")
        self.tb_vistaSalida.setGeometry(QRect(0, 0, 681, 341))
        self.tb_vistaSalida.setFont(font3)
        self.tb_vistaSalida.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 9 pt \"Open Sans\"")
        self.sk_agendaAero.addWidget(self.sk_salida)
        self.sk_llegada = QWidget()
        self.sk_llegada.setObjectName(u"sk_llegada")
        self.tb_vistaLlegada = QTableWidget(self.sk_llegada)
        if (self.tb_vistaLlegada.columnCount() < 6):
            self.tb_vistaLlegada.setColumnCount(6)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font2);
        __qtablewidgetitem24.setForeground(brush);
        self.tb_vistaLlegada.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font2);
        __qtablewidgetitem25.setForeground(brush);
        self.tb_vistaLlegada.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font2);
        __qtablewidgetitem26.setForeground(brush);
        self.tb_vistaLlegada.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font2);
        __qtablewidgetitem27.setForeground(brush);
        self.tb_vistaLlegada.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font2);
        __qtablewidgetitem28.setForeground(brush);
        self.tb_vistaLlegada.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font2);
        __qtablewidgetitem29.setForeground(brush);
        self.tb_vistaLlegada.setHorizontalHeaderItem(5, __qtablewidgetitem29)
        self.tb_vistaLlegada.setObjectName(u"tb_vistaLlegada")
        self.tb_vistaLlegada.setGeometry(QRect(0, 0, 681, 341))
        self.tb_vistaLlegada.setFont(font3)
        self.tb_vistaLlegada.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 9 pt \"Open Sans\"")
        self.sk_agendaAero.addWidget(self.sk_llegada)
        self.le_buscarAgenda = QLineEdit(self.pg_agenda)
        self.le_buscarAgenda.setObjectName(u"le_buscarAgenda")
        self.le_buscarAgenda.setGeometry(QRect(270, 30, 201, 31))
        self.le_buscarAgenda.setFont(font4)
        self.bt_buscarAgenda = QPushButton(self.pg_agenda)
        self.bt_buscarAgenda.setObjectName(u"bt_buscarAgenda")
        self.bt_buscarAgenda.setGeometry(QRect(490, 30, 91, 31))
        self.bt_buscarAgenda.setFont(font2)
        self.bt_buscarAgenda.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_buscarAgenda.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_buscarAgenda.setIcon(icon2)
        self.bt_buscarAgenda.setIconSize(QSize(30, 50))
        self.bt_buscarAgenda.setFlat(True)
        self.bt_refreshAgenda = QPushButton(self.pg_agenda)
        self.bt_refreshAgenda.setObjectName(u"bt_refreshAgenda")
        self.bt_refreshAgenda.setGeometry(QRect(590, 30, 111, 31))
        self.bt_refreshAgenda.setFont(font2)
        self.bt_refreshAgenda.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_refreshAgenda.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_refreshAgenda.setIcon(icon1)
        self.bt_refreshAgenda.setIconSize(QSize(30, 40))
        self.bt_refreshAgenda.setFlat(True)
        self.label_cerrarsesion_99 = QLabel(self.pg_agenda)
        self.label_cerrarsesion_99.setObjectName(u"label_cerrarsesion_99")
        self.label_cerrarsesion_99.setGeometry(QRect(330, 540, 121, 21))
        font7 = QFont()
        font7.setFamily(u"Nirmala UI")
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_cerrarsesion_99.setFont(font7)
        self.bt_vuelosSalida = QPushButton(self.pg_agenda)
        self.bt_vuelosSalida.setObjectName(u"bt_vuelosSalida")
        self.bt_vuelosSalida.setGeometry(QRect(220, 490, 51, 51))
        self.bt_vuelosSalida.setFont(font7)
        self.bt_vuelosSalida.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_vuelosSalida.setStyleSheet(u"QPushButton:hover\n"
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
        icon9 = QIcon()
        icon9.addFile(u"../Ventanas/Icons/Despegue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_vuelosSalida.setIcon(icon9)
        self.bt_vuelosSalida.setIconSize(QSize(50, 61))
        self.bt_vuelosSalida.setFlat(True)
        self.bt_agendarVuelo = QPushButton(self.pg_agenda)
        self.bt_agendarVuelo.setObjectName(u"bt_agendarVuelo")
        self.bt_agendarVuelo.setGeometry(QRect(630, 490, 61, 51))
        self.bt_agendarVuelo.setFont(font7)
        self.bt_agendarVuelo.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_agendarVuelo.setStyleSheet(u"QPushButton:hover\n"
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
        icon10 = QIcon()
        icon10.addFile(u"../Ventanas/Icons/agendar_vuelo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_agendarVuelo.setIcon(icon10)
        self.bt_agendarVuelo.setIconSize(QSize(50, 61))
        self.bt_agendarVuelo.setFlat(True)
        self.bt_vuelosLlegada = QPushButton(self.pg_agenda)
        self.bt_vuelosLlegada.setObjectName(u"bt_vuelosLlegada")
        self.bt_vuelosLlegada.setGeometry(QRect(360, 490, 51, 51))
        self.bt_vuelosLlegada.setFont(font7)
        self.bt_vuelosLlegada.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_vuelosLlegada.setStyleSheet(u"QPushButton:hover\n"
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
        icon11 = QIcon()
        icon11.addFile(u"../Ventanas/Icons/Aterrizaje.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_vuelosLlegada.setIcon(icon11)
        self.bt_vuelosLlegada.setIconSize(QSize(50, 61))
        self.bt_vuelosLlegada.setFlat(True)
        self.label_cerrarsesion_100 = QLabel(self.pg_agenda)
        self.label_cerrarsesion_100.setObjectName(u"label_cerrarsesion_100")
        self.label_cerrarsesion_100.setGeometry(QRect(490, 540, 91, 21))
        self.label_cerrarsesion_100.setFont(font7)
        self.bt_infoVuelo = QPushButton(self.pg_agenda)
        self.bt_infoVuelo.setObjectName(u"bt_infoVuelo")
        self.bt_infoVuelo.setGeometry(QRect(510, 490, 51, 51))
        self.bt_infoVuelo.setFont(font7)
        self.bt_infoVuelo.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_infoVuelo.setStyleSheet(u"QPushButton:hover\n"
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
        icon12 = QIcon()
        icon12.addFile(u"../Ventanas/Icons/Informaci\u00f3n.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_infoVuelo.setIcon(icon12)
        self.bt_infoVuelo.setIconSize(QSize(50, 61))
        self.bt_infoVuelo.setFlat(True)
        self.label_cerrarsesion_101 = QLabel(self.pg_agenda)
        self.label_cerrarsesion_101.setObjectName(u"label_cerrarsesion_101")
        self.label_cerrarsesion_101.setGeometry(QRect(610, 540, 101, 21))
        self.label_cerrarsesion_101.setFont(font7)
        self.label_cerrarsesion_102 = QLabel(self.pg_agenda)
        self.label_cerrarsesion_102.setObjectName(u"label_cerrarsesion_102")
        self.label_cerrarsesion_102.setGeometry(QRect(50, 540, 91, 21))
        self.label_cerrarsesion_102.setFont(font7)
        self.bt_vistaGeneral = QPushButton(self.pg_agenda)
        self.bt_vistaGeneral.setObjectName(u"bt_vistaGeneral")
        self.bt_vistaGeneral.setGeometry(QRect(70, 490, 51, 51))
        self.bt_vistaGeneral.setFont(font7)
        self.bt_vistaGeneral.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_vistaGeneral.setStyleSheet(u"QPushButton:hover\n"
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
        icon13 = QIcon()
        icon13.addFile(u"../Ventanas/Icons/Agenda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_vistaGeneral.setIcon(icon13)
        self.bt_vistaGeneral.setIconSize(QSize(50, 61))
        self.bt_vistaGeneral.setFlat(True)
        self.label_cerrarsesion_103 = QLabel(self.pg_agenda)
        self.label_cerrarsesion_103.setObjectName(u"label_cerrarsesion_103")
        self.label_cerrarsesion_103.setGeometry(QRect(190, 540, 111, 21))
        self.label_cerrarsesion_103.setFont(font7)
        self.bt_vuelos = QPushButton(self.pg_agenda)
        self.bt_vuelos.setObjectName(u"bt_vuelos")
        self.bt_vuelos.setGeometry(QRect(40, 20, 211, 41))
        self.bt_vuelos.setFont(font2)
        self.bt_vuelos.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_vuelos.setStyleSheet(u"QPushButton:hover\n"
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
        icon14 = QIcon()
        icon14.addFile(u"../Ventanas/Icons/crear agenda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_vuelos.setIcon(icon14)
        self.bt_vuelos.setIconSize(QSize(40, 50))
        self.bt_vuelos.setFlat(True)
        self.sk_mainWindow.addWidget(self.pg_agenda)
        self.pg_vuelos = QWidget()
        self.pg_vuelos.setObjectName(u"pg_vuelos")
        self.bt_aviones = QPushButton(self.pg_vuelos)
        self.bt_aviones.setObjectName(u"bt_aviones")
        self.bt_aviones.setGeometry(QRect(210, 530, 131, 41))
        self.bt_aviones.setFont(font2)
        self.bt_aviones.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_aviones.setStyleSheet(u"QPushButton:hover\n"
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
        icon15 = QIcon()
        icon15.addFile(u"../Ventanas/Icons/agregar_avion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_aviones.setIcon(icon15)
        self.bt_aviones.setIconSize(QSize(40, 50))
        self.bt_aviones.setFlat(True)
        self.bt_vuelosAerolinea = QPushButton(self.pg_vuelos)
        self.bt_vuelosAerolinea.setObjectName(u"bt_vuelosAerolinea")
        self.bt_vuelosAerolinea.setGeometry(QRect(80, 530, 121, 41))
        self.bt_vuelosAerolinea.setFont(font2)
        self.bt_vuelosAerolinea.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_vuelosAerolinea.setStyleSheet(u"QPushButton:hover\n"
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
        icon16 = QIcon()
        icon16.addFile(u"../Ventanas/Icons/vuelo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_vuelosAerolinea.setIcon(icon16)
        self.bt_vuelosAerolinea.setIconSize(QSize(40, 50))
        self.bt_vuelosAerolinea.setFlat(True)
        self.bt_nuevaTrip = QPushButton(self.pg_vuelos)
        self.bt_nuevaTrip.setObjectName(u"bt_nuevaTrip")
        self.bt_nuevaTrip.setGeometry(QRect(370, 530, 181, 41))
        self.bt_nuevaTrip.setFont(font2)
        self.bt_nuevaTrip.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_nuevaTrip.setStyleSheet(u"QPushButton:hover\n"
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
        icon17 = QIcon()
        icon17.addFile(u"../Ventanas/Icons/piloto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_nuevaTrip.setIcon(icon17)
        self.bt_nuevaTrip.setIconSize(QSize(30, 50))
        self.bt_nuevaTrip.setFlat(True)
        self.sw_vuelos_av_trip = QStackedWidget(self.pg_vuelos)
        self.sw_vuelos_av_trip.setObjectName(u"sw_vuelos_av_trip")
        self.sw_vuelos_av_trip.setGeometry(QRect(30, 20, 731, 511))
        self.pg_agendaAerolinea = QWidget()
        self.pg_agendaAerolinea.setObjectName(u"pg_agendaAerolinea")
        self.groupBox_39 = QGroupBox(self.pg_agendaAerolinea)
        self.groupBox_39.setObjectName(u"groupBox_39")
        self.groupBox_39.setGeometry(QRect(0, 80, 731, 421))
        self.groupBox_39.setFont(font2)
        self.groupBox_39.setAlignment(Qt.AlignCenter)
        self.tb_vistaAerolinea = QTableWidget(self.groupBox_39)
        if (self.tb_vistaAerolinea.columnCount() < 8):
            self.tb_vistaAerolinea.setColumnCount(8)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font2);
        __qtablewidgetitem30.setForeground(brush);
        self.tb_vistaAerolinea.setHorizontalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font2);
        __qtablewidgetitem31.setForeground(brush);
        self.tb_vistaAerolinea.setHorizontalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font2);
        __qtablewidgetitem32.setForeground(brush);
        self.tb_vistaAerolinea.setHorizontalHeaderItem(2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font2);
        __qtablewidgetitem33.setForeground(brush);
        self.tb_vistaAerolinea.setHorizontalHeaderItem(3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font2);
        __qtablewidgetitem34.setForeground(brush);
        self.tb_vistaAerolinea.setHorizontalHeaderItem(4, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font2);
        __qtablewidgetitem35.setForeground(brush);
        self.tb_vistaAerolinea.setHorizontalHeaderItem(5, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font2);
        __qtablewidgetitem36.setForeground(brush);
        self.tb_vistaAerolinea.setHorizontalHeaderItem(6, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font2);
        __qtablewidgetitem37.setForeground(brush);
        self.tb_vistaAerolinea.setHorizontalHeaderItem(7, __qtablewidgetitem37)
        self.tb_vistaAerolinea.setObjectName(u"tb_vistaAerolinea")
        self.tb_vistaAerolinea.setGeometry(QRect(20, 40, 691, 321))
        self.tb_vistaAerolinea.setFont(font8)
        self.tb_vistaAerolinea.setSelectionBehavior(QAbstractItemView.SelectRows)
        header = self.tb_vistaAerolinea.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tb_vistaAerolinea.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 9 pt \"Open Sans\"")
        self.bt_agregarVA = QPushButton(self.groupBox_39)
        self.bt_agregarVA.setObjectName(u"bt_agregarVA")
        self.bt_agregarVA.setGeometry(QRect(170, 380, 111, 31))
        self.bt_agregarVA.setFont(font2)
        self.bt_agregarVA.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_agregarVA.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_agregarVA.setIconSize(QSize(40, 50))
        self.bt_agregarVA.setFlat(False)
        self.bt_modificarVA = QPushButton(self.groupBox_39)
        self.bt_modificarVA.setObjectName(u"bt_modificarVA")
        self.bt_modificarVA.setGeometry(QRect(320, 380, 111, 31))
        self.bt_modificarVA.setFont(font2)
        self.bt_modificarVA.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_modificarVA.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_modificarVA.setIconSize(QSize(40, 50))
        self.bt_modificarVA.setFlat(False)
        self.bt_eliminarVA = QPushButton(self.groupBox_39)
        self.bt_eliminarVA.setObjectName(u"bt_eliminarVA")
        self.bt_eliminarVA.setGeometry(QRect(470, 380, 111, 31))
        self.bt_eliminarVA.setFont(font2)
        self.bt_eliminarVA.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_eliminarVA.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_eliminarVA.setIconSize(QSize(40, 50))
        self.bt_eliminarVA.setFlat(False)
        self.label_cerrarsesion_104 = QLabel(self.pg_agendaAerolinea)
        self.label_cerrarsesion_104.setObjectName(u"label_cerrarsesion_104")
        self.label_cerrarsesion_104.setGeometry(QRect(90, 20, 81, 31))
        self.label_cerrarsesion_104.setFont(font2)
        self.bt_buscarAgenda_Aerolinea = QPushButton(self.pg_agendaAerolinea)
        self.bt_buscarAgenda_Aerolinea.setObjectName(u"bt_buscarAgenda_Aerolinea")
        self.bt_buscarAgenda_Aerolinea.setGeometry(QRect(460, 20, 91, 31))
        self.bt_buscarAgenda_Aerolinea.setFont(font2)
        self.bt_buscarAgenda_Aerolinea.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_buscarAgenda_Aerolinea.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_buscarAgenda_Aerolinea.setIcon(icon2)
        self.bt_buscarAgenda_Aerolinea.setIconSize(QSize(30, 50))
        self.bt_buscarAgenda_Aerolinea.setFlat(True)
        self.le_buscarAgendaAerolinea = QLineEdit(self.pg_agendaAerolinea)
        self.le_buscarAgendaAerolinea.setObjectName(u"le_buscarAgendaAerolinea")
        self.le_buscarAgendaAerolinea.setGeometry(QRect(170, 20, 271, 31))
        self.le_buscarAgendaAerolinea.setFont(font4)
        self.bt_refreshAgenda_Aerolinea = QPushButton(self.pg_agendaAerolinea)
        self.bt_refreshAgenda_Aerolinea.setObjectName(u"bt_refreshAgenda_Aerolinea")
        self.bt_refreshAgenda_Aerolinea.setGeometry(QRect(560, 20, 111, 31))
        self.bt_refreshAgenda_Aerolinea.setFont(font2)
        self.bt_refreshAgenda_Aerolinea.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_refreshAgenda_Aerolinea.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_refreshAgenda_Aerolinea.setIcon(icon1)
        self.bt_refreshAgenda_Aerolinea.setIconSize(QSize(30, 40))
        self.bt_refreshAgenda_Aerolinea.setFlat(True)
        self.sw_vuelos_av_trip.addWidget(self.pg_agendaAerolinea)
        self.pg_agendaPendiente = QWidget()
        self.pg_agendaPendiente.setObjectName(u"pg_agendaPendiente")
        self.groupBox_40 = QGroupBox(self.pg_agendaPendiente)
        self.groupBox_40.setObjectName(u"groupBox_40")
        self.groupBox_40.setGeometry(QRect(0, 30, 731, 411))
        self.groupBox_40.setFont(font2)
        self.groupBox_40.setAlignment(Qt.AlignCenter)
        self.tb_vistaAerolineaPendiente = QTableWidget(self.groupBox_40)
        if (self.tb_vistaAerolineaPendiente.columnCount() < 8):
            self.tb_vistaAerolineaPendiente.setColumnCount(8)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font2);
        __qtablewidgetitem38.setForeground(brush);
        self.tb_vistaAerolineaPendiente.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font2);
        __qtablewidgetitem39.setForeground(brush);
        self.tb_vistaAerolineaPendiente.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font2);
        __qtablewidgetitem40.setForeground(brush);
        self.tb_vistaAerolineaPendiente.setHorizontalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFont(font2);
        __qtablewidgetitem41.setForeground(brush);
        self.tb_vistaAerolineaPendiente.setHorizontalHeaderItem(3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFont(font2);
        __qtablewidgetitem42.setForeground(brush);
        self.tb_vistaAerolineaPendiente.setHorizontalHeaderItem(4, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setFont(font2);
        __qtablewidgetitem43.setForeground(brush);
        self.tb_vistaAerolineaPendiente.setHorizontalHeaderItem(5, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setFont(font2);
        __qtablewidgetitem44.setForeground(brush);
        self.tb_vistaAerolineaPendiente.setHorizontalHeaderItem(6, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setFont(font2);
        __qtablewidgetitem45.setForeground(brush);
        self.tb_vistaAerolineaPendiente.setHorizontalHeaderItem(7, __qtablewidgetitem45)
        self.tb_vistaAerolineaPendiente.setObjectName(u"tb_vistaAerolineaPendiente")
        self.tb_vistaAerolineaPendiente.setGeometry(QRect(20, 40, 691, 351))
        self.tb_vistaAerolineaPendiente.setFont(font8)
        self.tb_vistaAerolineaPendiente.setSelectionBehavior(QAbstractItemView.SelectRows)
        header = self.tb_vistaAerolineaPendiente.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tb_vistaAerolineaPendiente.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 9 pt \"Open Sans\"")
        self.bt_agregar_avion = QPushButton(self.pg_agendaPendiente)
        self.bt_agregar_avion.setObjectName(u"bt_agregar_avion")
        self.bt_agregar_avion.setGeometry(QRect(320, 460, 141, 31))
        self.bt_agregar_avion.setFont(font2)
        self.bt_agregar_avion.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_agregar_avion.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_agregar_avion.setIconSize(QSize(40, 50))
        self.bt_agregar_avion.setFlat(False)
        self.sw_vuelos_av_trip.addWidget(self.pg_agendaPendiente)
        self.pg_newTrip = QWidget()
        self.pg_newTrip.setObjectName(u"pg_newTrip")
        self.lb_NumeroID = QLabel(self.pg_newTrip)
        self.lb_NumeroID.setObjectName(u"lb_NumeroID")
        self.lb_NumeroID.setGeometry(QRect(370, 290, 91, 31))
        
        self.lb_NumeroID.setFont(font8)
        self.textedit_licencia = QLineEdit(self.pg_newTrip)
        self.textedit_licencia.setObjectName(u"textedit_licencia")
        self.textedit_licencia.setGeometry(QRect(460, 290, 161, 31))
        self.textedit_licencia.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.date_fechaUltimaRevision = QDateEdit(self.pg_newTrip)
        self.date_fechaUltimaRevision.setObjectName(u"date_fechaUltimaRevision")
        self.date_fechaUltimaRevision.setGeometry(QRect(410, 360, 110, 31))
        self.date_fechaUltimaRevision.setCursor(QCursor(Qt.IBeamCursor))
        self.date_fechaUltimaRevision.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.date_fechaUltimaRevision.setAlignment(Qt.AlignCenter)
        self.lb_tipoID = QLabel(self.pg_newTrip)
        self.lb_tipoID.setObjectName(u"lb_tipoID")
        self.lb_tipoID.setGeometry(QRect(80, 230, 81, 31))
        self.lb_tipoID.setFont(font8)
        self.lb_codTripulacion = QLabel(self.pg_newTrip)
        self.lb_codTripulacion.setObjectName(u"lb_codTripulacion")
        self.lb_codTripulacion.setGeometry(QRect(80, 110, 141, 31))
        self.lb_codTripulacion.setFont(font8)
        self.lb_NumeroID_2 = QLabel(self.pg_newTrip)
        self.lb_NumeroID_2.setObjectName(u"lb_NumeroID_2")
        self.lb_NumeroID_2.setGeometry(QRect(360, 230, 91, 31))
        self.lb_NumeroID_2.setFont(font8)
        self.lb_tipoID_2 = QLabel(self.pg_newTrip)
        self.lb_tipoID_2.setObjectName(u"lb_tipoID_2")
        self.lb_tipoID_2.setGeometry(QRect(90, 290, 121, 31))
        self.lb_tipoID_2.setFont(font8)
        self.lb_Nombre = QLabel(self.pg_newTrip)
        self.lb_Nombre.setObjectName(u"lb_Nombre")
        self.lb_Nombre.setGeometry(QRect(80, 170, 81, 31))
        self.lb_Nombre.setFont(font8)
        self.textedit_codTripulacion = QLineEdit(self.pg_newTrip)
        self.textedit_codTripulacion.setObjectName(u"textedit_codTripulacion")
        self.textedit_codTripulacion.setGeometry(QRect(220, 110, 121, 31))
        self.textedit_codTripulacion.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lb_tipoID_18 = QLabel(self.pg_newTrip)
        self.lb_tipoID_18.setObjectName(u"lb_tipoID_18")
        self.lb_tipoID_18.setGeometry(QRect(160, 360, 211, 31))
        self.lb_tipoID_18.setFont(font8)
        self.bt_GuardarTrip = QPushButton(self.pg_newTrip)
        self.bt_GuardarTrip.setObjectName(u"bt_GuardarTrip")
        self.bt_GuardarTrip.setGeometry(QRect(390, 420, 131, 41))
        font9 = QFont()
        font9.setFamily(u"Nirmala UI")
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setWeight(75)
        self.bt_GuardarTrip.setFont(font9)
        self.bt_GuardarTrip.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_GuardarTrip.setStyleSheet(u"QPushButton\n"
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
        icon18 = QIcon()
        icon18.addFile(u"../Ventanas/Icons/save-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_GuardarTrip.setIcon(icon18)
        self.bt_GuardarTrip.setIconSize(QSize(40, 50))
        self.bt_GuardarTrip.setFlat(True)
        self.textedit_numeroID = QLineEdit(self.pg_newTrip)
        self.textedit_numeroID.setObjectName(u"textedit_numeroID")
        self.textedit_numeroID.setGeometry(QRect(460, 230, 161, 31))
        self.textedit_numeroID.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.cb_tipoID = QComboBox(self.pg_newTrip)
        self.cb_tipoID.addItem("")
        self.cb_tipoID.addItem("")
        self.cb_tipoID.addItem("")
        self.cb_tipoID.setObjectName(u"cb_tipoID")
        self.cb_tipoID.setGeometry(QRect(180, 230, 161, 31))
        self.cb_tipoID.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_tipoID.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.cb_tipoID.setEditable(False)
        self.cb_tipoID.setDuplicatesEnabled(False)
        self.cb_tipoID.setFrame(True)
        self.textedit_nombre = QLineEdit(self.pg_newTrip)
        self.textedit_nombre.setObjectName(u"textedit_nombre")
        self.textedit_nombre.setGeometry(QRect(180, 170, 161, 31))
        self.textedit_nombre.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.spinBox_HorasVuelo = QSpinBox(self.pg_newTrip)
        self.spinBox_HorasVuelo.setObjectName(u"spinBox_HorasVuelo")
        self.spinBox_HorasVuelo.setGeometry(QRect(250, 290, 91, 31))
        self.spinBox_HorasVuelo.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 12pt \"Nirmala UI\"")
        self.lb_apellido = QLabel(self.pg_newTrip)
        self.lb_apellido.setObjectName(u"lb_apellido")
        self.lb_apellido.setGeometry(QRect(370, 170, 81, 31))
        self.lb_apellido.setFont(font8)
        self.textedit_Apellido = QLineEdit(self.pg_newTrip)
        self.textedit_Apellido.setObjectName(u"textedit_Apellido")
        self.textedit_Apellido.setGeometry(QRect(460, 170, 161, 31))
        self.textedit_Apellido.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lb_facturanum = QLabel(self.pg_newTrip)
        self.lb_facturanum.setObjectName(u"lb_facturanum")
        self.lb_facturanum.setGeometry(QRect(180, 40, 391, 41))
        self.lb_facturanum.setStyleSheet(u"font: 63 26pt \"Open Sans Semibold\";")
        self.bt_AgregarTrip = QPushButton(self.pg_newTrip)
        self.bt_AgregarTrip.setObjectName(u"bt_AgregarTrip")
        self.bt_AgregarTrip.setGeometry(QRect(190, 420, 161, 41))
        self.bt_AgregarTrip.setFont(font9)
        self.bt_AgregarTrip.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_AgregarTrip.setStyleSheet(u"QPushButton\n"
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
        icon19 = QIcon()
        icon19.addFile(u"../Ventanas/Icons/agregar_tripulacion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_AgregarTrip.setIcon(icon19)
        self.bt_AgregarTrip.setIconSize(QSize(40, 50))
        self.bt_AgregarTrip.setFlat(True)
        self.sw_vuelos_av_trip.addWidget(self.pg_newTrip)
        self.pg_aviones = QWidget()
        self.pg_aviones.setObjectName(u"pg_aviones")
        self.sw_reg_ver_avion = QStackedWidget(self.pg_aviones)
        self.sw_reg_ver_avion.setObjectName(u"sw_reg_ver_avion")
        self.sw_reg_ver_avion.setGeometry(QRect(30, 10, 671, 481))
        self.pg_reg_avion = QWidget()
        self.pg_reg_avion.setObjectName(u"pg_reg_avion")
        self.lb_Modelo_7 = QLabel(self.pg_reg_avion)
        self.lb_Modelo_7.setObjectName(u"lb_Modelo_7")
        self.lb_Modelo_7.setGeometry(QRect(380, 120, 61, 31))
        font10 = QFont()
        font10.setFamily(u"Nirmala UI")
        font10.setPointSize(12)
        font10.setBold(False)
        font10.setItalic(False)
        font10.setWeight(9)
        self.lb_Modelo_7.setFont(font10)
        self.lb_Modelo_7.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_PesoNominal_7 = QLabel(self.pg_reg_avion)
        self.lb_PesoNominal_7.setObjectName(u"lb_PesoNominal_7")
        self.lb_PesoNominal_7.setGeometry(QRect(400, 260, 111, 31))
        self.lb_PesoNominal_7.setFont(font10)
        self.lb_PesoNominal_7.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.spinBox_MotoresEA = QSpinBox(self.pg_reg_avion)
        self.spinBox_MotoresEA.setObjectName(u"spinBox_MotoresEA")
        self.spinBox_MotoresEA.setGeometry(QRect(280, 300, 71, 31))
        self.spinBox_MotoresEA.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 12pt \"Nirmala UI\"")
        self.spinBox_MotoresEA.setMinimum(1)
        self.spinBox_MotoresEA.setMaximum(4)
        self.bt_checkIDavion = QPushButton(self.pg_reg_avion)
        self.bt_checkIDavion.setObjectName(u"bt_checkIDavion")
        self.bt_checkIDavion.setGeometry(QRect(260, 120, 41, 31))
        icon20 = QIcon()
        icon20.addFile(u"../Ventanas/Icons/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_checkIDavion.setIcon(icon20)
        self.bt_checkIDavion.setIconSize(QSize(30, 30))
        self.bt_checkIDavion.setFlat(True)
        self.spinBox_CapacidadEA = QSpinBox(self.pg_reg_avion)
        self.spinBox_CapacidadEA.setObjectName(u"spinBox_CapacidadEA")
        self.spinBox_CapacidadEA.setGeometry(QRect(140, 300, 81, 31))
        self.spinBox_CapacidadEA.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 12pt \"Nirmala UI\"")
        self.spinBox_CapacidadEA.setMinimum(1)
        self.cb_PropulsionEA = QComboBox(self.pg_reg_avion)
        self.cb_PropulsionEA.addItem("")
        self.cb_PropulsionEA.addItem("")
        self.cb_PropulsionEA.addItem("")
        self.cb_PropulsionEA.setObjectName(u"cb_PropulsionEA")
        self.cb_PropulsionEA.setGeometry(QRect(150, 190, 131, 31))
        self.cb_PropulsionEA.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_PropulsionEA.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.cb_PropulsionEA.setEditable(False)
        self.cb_PropulsionEA.setDuplicatesEnabled(False)
        self.cb_PropulsionEA.setFrame(True)
        self.bt_aceptarAVEA = QPushButton(self.pg_reg_avion)
        self.bt_aceptarAVEA.setObjectName(u"bt_aceptarAVEA")
        self.bt_aceptarAVEA.setGeometry(QRect(170, 380, 171, 41))
        self.bt_aceptarAVEA.setFont(font9)
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
        self.bt_aceptarAVEA.setIcon(icon15)
        self.bt_aceptarAVEA.setIconSize(QSize(40, 50))
        self.bt_aceptarAVEA.setFlat(True)
        self.lb_TipodeAvion_7 = QLabel(self.pg_reg_avion)
        self.lb_TipodeAvion_7.setObjectName(u"lb_TipodeAvion_7")
        self.lb_TipodeAvion_7.setGeometry(QRect(380, 190, 111, 31))
        self.lb_TipodeAvion_7.setFont(font10)
        self.lb_TipodeAvion_7.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Capacidad = QLabel(self.pg_reg_avion)
        self.lb_Capacidad.setObjectName(u"lb_Capacidad")
        self.lb_Capacidad.setGeometry(QRect(140, 260, 81, 31))
        self.lb_Capacidad.setFont(font10)
        self.lb_Capacidad.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Motores_7 = QLabel(self.pg_reg_avion)
        self.lb_Motores_7.setObjectName(u"lb_Motores_7")
        self.lb_Motores_7.setGeometry(QRect(280, 260, 71, 31))
        self.lb_Motores_7.setFont(font10)
        self.lb_Motores_7.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_facturanum_17 = QLabel(self.pg_reg_avion)
        self.lb_facturanum_17.setObjectName(u"lb_facturanum_17")
        self.lb_facturanum_17.setGeometry(QRect(160, 50, 391, 41))
        self.lb_facturanum_17.setStyleSheet(u"font: 63 26pt \"Open Sans Semibold\";")
        self.lineEdit_identificadorEA = QLineEdit(self.pg_reg_avion)
        self.lineEdit_identificadorEA.setObjectName(u"lineEdit_identificadorEA")
        self.lineEdit_identificadorEA.setGeometry(QRect(160, 120, 101, 31))
        self.lineEdit_identificadorEA.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lb_Propulsion_7 = QLabel(self.pg_reg_avion)
        self.lb_Propulsion_7.setObjectName(u"lb_Propulsion_7")
        self.lb_Propulsion_7.setGeometry(QRect(50, 190, 91, 31))
        self.lb_Propulsion_7.setFont(font10)
        self.lb_Propulsion_7.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Identificador_22 = QLabel(self.pg_reg_avion)
        self.lb_Identificador_22.setObjectName(u"lb_Identificador_22")
        self.lb_Identificador_22.setGeometry(QRect(150, 140, 101, 31))
        self.lb_Identificador_22.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.cb_pasajerosEA = QComboBox(self.pg_reg_avion)
        self.cb_pasajerosEA.addItem("")
        self.cb_pasajerosEA.addItem("")
        self.cb_pasajerosEA.setObjectName(u"cb_pasajerosEA")
        self.cb_pasajerosEA.setGeometry(QRect(500, 190, 121, 31))
        self.cb_pasajerosEA.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_pasajerosEA.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.cb_pasajerosEA.setEditable(False)
        self.cb_pasajerosEA.setDuplicatesEnabled(False)
        self.cb_pasajerosEA.setFrame(True)
        self.spinBox_pesoNomEA = QSpinBox(self.pg_reg_avion)
        self.spinBox_pesoNomEA.setObjectName(u"spinBox_pesoNomEA")
        self.spinBox_pesoNomEA.setGeometry(QRect(420, 300, 81, 31))
        self.spinBox_pesoNomEA.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 12pt \"Nirmala UI\"")
        self.spinBox_pesoNomEA.setMaximum(1000)
        self.lb_Identificador_23 = QLabel(self.pg_reg_avion)
        self.lb_Identificador_23.setObjectName(u"lb_Identificador_23")
        self.lb_Identificador_23.setGeometry(QRect(50, 120, 101, 31))
        self.lb_Identificador_23.setFont(font10)
        self.lb_Identificador_23.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.cb_ModeloRA = QComboBox(self.pg_reg_avion)
        self.cb_ModeloRA.setObjectName(u"cb_ModeloRA")
        self.cb_ModeloRA.setGeometry(QRect(460, 120, 161, 31))
        self.cb_ModeloRA.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_ModeloRA.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.cb_ModeloRA.setEditable(False)
        self.cb_ModeloRA.setDuplicatesEnabled(False)
        self.cb_ModeloRA.setFrame(True)
        self.bt_cancelar_RA = QPushButton(self.pg_reg_avion)
        self.bt_cancelar_RA.setObjectName(u"bt_cancelar_RA")
        self.bt_cancelar_RA.setGeometry(QRect(370, 380, 131, 41))
        self.bt_cancelar_RA.setFont(font9)
        self.bt_cancelar_RA.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_cancelar_RA.setStyleSheet(u"QPushButton\n"
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
        self.bt_cancelar_RA.setIconSize(QSize(40, 50))
        self.bt_cancelar_RA.setFlat(True)
        self.sw_reg_ver_avion.addWidget(self.pg_reg_avion)
        self.pg_vista_aviones = QWidget()
        self.pg_vista_aviones.setObjectName(u"pg_vista_aviones")
        self.label_cerrarsesion_105 = QLabel(self.pg_vista_aviones)
        self.label_cerrarsesion_105.setObjectName(u"label_cerrarsesion_105")
        self.label_cerrarsesion_105.setGeometry(QRect(110, 10, 141, 31))
        self.label_cerrarsesion_105.setFont(font8)
        self.groupBox_41 = QGroupBox(self.pg_vista_aviones)
        self.groupBox_41.setObjectName(u"groupBox_41")
        self.groupBox_41.setGeometry(QRect(0, 60, 671, 411))
        self.groupBox_41.setFont(font2)
        self.groupBox_41.setAlignment(Qt.AlignCenter)
        self.tb_avionesregistradosAV = QTableWidget(self.groupBox_41)
        if (self.tb_avionesregistradosAV.columnCount() < 7):
            self.tb_avionesregistradosAV.setColumnCount(7)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setFont(font2);
        __qtablewidgetitem46.setForeground(brush);
        self.tb_avionesregistradosAV.setHorizontalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setFont(font2);
        __qtablewidgetitem47.setForeground(brush);
        self.tb_avionesregistradosAV.setHorizontalHeaderItem(1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setFont(font2);
        __qtablewidgetitem48.setForeground(brush);
        self.tb_avionesregistradosAV.setHorizontalHeaderItem(2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setFont(font2);
        __qtablewidgetitem49.setForeground(brush);
        self.tb_avionesregistradosAV.setHorizontalHeaderItem(3, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setFont(font2);
        __qtablewidgetitem50.setForeground(brush);
        self.tb_avionesregistradosAV.setHorizontalHeaderItem(4, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setFont(font2);
        __qtablewidgetitem51.setForeground(brush);
        self.tb_avionesregistradosAV.setHorizontalHeaderItem(5, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setFont(font2);
        __qtablewidgetitem52.setForeground(brush);
        self.tb_avionesregistradosAV.setHorizontalHeaderItem(6, __qtablewidgetitem52)
        self.tb_avionesregistradosAV.setObjectName(u"tb_avionesregistradosAV")
        self.tb_avionesregistradosAV.setGeometry(QRect(20, 40, 631, 321))
        self.tb_avionesregistradosAV.setFont(font8)
        self.tb_avionesregistradosAV.setSelectionBehavior(QAbstractItemView.SelectRows)
        header = self.tb_avionesregistradosAV.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tb_avionesregistradosAV.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 9 pt \"Open Sans\"")
        self.bt_eliminarAvion = QPushButton(self.groupBox_41)
        self.bt_eliminarAvion.setObjectName(u"bt_eliminarAvion")
        self.bt_eliminarAvion.setGeometry(QRect(360, 370, 111, 31))
        self.bt_eliminarAvion.setFont(font2)
        self.bt_eliminarAvion.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_eliminarAvion.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_eliminarAvion.setIconSize(QSize(40, 50))
        self.bt_eliminarAvion.setFlat(False)
        self.bt_agregarAvion = QPushButton(self.groupBox_41)
        self.bt_agregarAvion.setObjectName(u"bt_agregarAvion")
        self.bt_agregarAvion.setGeometry(QRect(50, 370, 111, 31))
        self.bt_agregarAvion.setFont(font2)
        self.bt_agregarAvion.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_agregarAvion.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_agregarAvion.setIconSize(QSize(40, 50))
        self.bt_agregarAvion.setFlat(False)
        self.bt_modificarAvion = QPushButton(self.groupBox_41)
        self.bt_modificarAvion.setObjectName(u"bt_modificarAvion")
        self.bt_modificarAvion.setGeometry(QRect(200, 370, 111, 31))
        self.bt_modificarAvion.setFont(font2)
        self.bt_modificarAvion.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_modificarAvion.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_modificarAvion.setIconSize(QSize(40, 50))
        self.bt_modificarAvion.setFlat(False)
        self.bt_actualizar_avion = QPushButton(self.groupBox_41)
        self.bt_actualizar_avion.setObjectName(u"bt_actualizar_avion")
        self.bt_actualizar_avion.setGeometry(QRect(510, 370, 111, 31))
        self.bt_actualizar_avion.setFont(font2)
        self.bt_actualizar_avion.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_actualizar_avion.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_actualizar_avion.setIconSize(QSize(40, 50))
        self.bt_actualizar_avion.setFlat(False)
        self.bt_buscarVuelo = QPushButton(self.pg_vista_aviones)
        self.bt_buscarVuelo.setObjectName(u"bt_buscarVuelo")
        self.bt_buscarVuelo.setGeometry(QRect(440, 10, 91, 31))
        self.bt_buscarVuelo.setFont(font7)
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
        self.bt_buscarVuelo.setIcon(icon2)
        self.bt_buscarVuelo.setIconSize(QSize(30, 50))
        self.bt_buscarVuelo.setFlat(True)
        self.cb_codigoavionAV = QComboBox(self.pg_vista_aviones)
        self.cb_codigoavionAV.setObjectName(u"cb_codigoavionAV")
        self.cb_codigoavionAV.setGeometry(QRect(270, 10, 171, 31))
        self.cb_codigoavionAV.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_codigoavionAV.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.cb_codigoavionAV.setEditable(False)
        self.cb_codigoavionAV.setDuplicatesEnabled(False)
        self.cb_codigoavionAV.setFrame(True)
        self.sw_reg_ver_avion.addWidget(self.pg_vista_aviones)
        self.sw_vuelos_av_trip.addWidget(self.pg_aviones)
        self.bt_agendaPendiente = QPushButton(self.pg_vuelos)
        self.bt_agendaPendiente.setObjectName(u"bt_agendaPendiente")
        self.bt_agendaPendiente.setGeometry(QRect(570, 530, 171, 41))
        self.bt_agendaPendiente.setFont(font2)
        self.bt_agendaPendiente.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_agendaPendiente.setStyleSheet(u"QPushButton:hover\n"
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
        icon21 = QIcon()
        icon21.addFile(u"../Ventanas/Icons/enviar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_agendaPendiente.setIcon(icon21)
        self.bt_agendaPendiente.setIconSize(QSize(30, 50))
        self.bt_agendaPendiente.setFlat(True)
        self.sk_mainWindow.addWidget(self.pg_vuelos)
        self.pg_hangares = QWidget()
        self.pg_hangares.setObjectName(u"pg_hangares")
        self.groupBox_42 = QGroupBox(self.pg_hangares)
        self.groupBox_42.setObjectName(u"groupBox_42")
        self.groupBox_42.setGeometry(QRect(20, 70, 741, 441))
        self.groupBox_42.setFont(font2)
        self.groupBox_42.setAlignment(Qt.AlignCenter)
        self.tb_hangares = QTableWidget(self.groupBox_42)
        if (self.tb_hangares.columnCount() < 2):
            self.tb_hangares.setColumnCount(2)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setFont(font2);
        __qtablewidgetitem53.setForeground(brush);
        self.tb_hangares.setHorizontalHeaderItem(0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setFont(font2);
        __qtablewidgetitem54.setForeground(brush);
        self.tb_hangares.setHorizontalHeaderItem(1, __qtablewidgetitem54)
        self.tb_hangares.setObjectName(u"tb_hangares")
        self.tb_hangares.setGeometry(QRect(40, 40, 241, 341))
        font11 = QFont()
        font11.setFamily(u"Open Sans")
        font11.setPointSize(10)
        self.tb_hangares.setFont(font8)
        self.tb_hangares.setSelectionBehavior(QAbstractItemView.SelectRows)
        header = self.tb_hangares.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tb_hangares.setGridStyle(Qt.SolidLine)
        self.sw_funcion_hangares = QStackedWidget(self.groupBox_42)
        self.sw_funcion_hangares.setObjectName(u"sw_funcion_hangares")
        self.sw_funcion_hangares.setGeometry(QRect(300, 30, 421, 401))
        font12 = QFont()
        font12.setBold(False)
        font12.setWeight(50)
        self.sw_funcion_hangares.setFont(font12)
        self.pg_hgprincipal = QWidget()
        self.pg_hgprincipal.setObjectName(u"pg_hgprincipal")
        self.label_12 = QLabel(self.pg_hgprincipal)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(70, 30, 291, 261))
        self.label_12.setPixmap(QPixmap(u"../Ventanas/Icons/image_hangar.png"))
        self.label_12.setScaledContents(True)
        self.label_cerrarsesion_106 = QLabel(self.pg_hgprincipal)
        self.label_cerrarsesion_106.setObjectName(u"label_cerrarsesion_106")
        self.label_cerrarsesion_106.setGeometry(QRect(40, 270, 361, 51))
        self.label_cerrarsesion_106.setFont(font)
        self.sw_funcion_hangares.addWidget(self.pg_hgprincipal)
        self.pg_registrar_hg = QWidget()
        self.pg_registrar_hg.setObjectName(u"pg_registrar_hg")
        self.lb_Identificador = QLabel(self.pg_registrar_hg)
        self.lb_Identificador.setObjectName(u"lb_Identificador")
        self.lb_Identificador.setGeometry(QRect(80, 200, 111, 31))
        self.lb_Identificador.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.textedit_codigoRH = QLineEdit(self.pg_registrar_hg)
        self.textedit_codigoRH.setObjectName(u"textedit_codigoRH")
        self.textedit_codigoRH.setGeometry(QRect(200, 150, 121, 31))
        self.textedit_codigoRH.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lb_facturanum_18 = QLabel(self.pg_registrar_hg)
        self.lb_facturanum_18.setObjectName(u"lb_facturanum_18")
        self.lb_facturanum_18.setGeometry(QRect(80, 80, 251, 41))
        self.lb_facturanum_18.setStyleSheet(u"font: 63 26pt \"Open Sans Semibold\";")
        self.lb_Identificador_ = QLabel(self.pg_registrar_hg)
        self.lb_Identificador_.setObjectName(u"lb_Identificador_")
        self.lb_Identificador_.setGeometry(QRect(80, 150, 101, 31))
        self.lb_Identificador_.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.textedit_capacidadRH = QLineEdit(self.pg_registrar_hg)
        self.textedit_capacidadRH.setObjectName(u"textedit_capacidadRH")
        self.textedit_capacidadRH.setGeometry(QRect(200, 200, 121, 31))
        self.textedit_capacidadRH.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.bt_guardarHangar = QPushButton(self.pg_registrar_hg)
        self.bt_guardarHangar.setObjectName(u"bt_guardarHangar")
        self.bt_guardarHangar.setGeometry(QRect(140, 270, 121, 41))
        self.bt_guardarHangar.setFont(font9)
        self.bt_guardarHangar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_guardarHangar.setStyleSheet(u"QPushButton\n"
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
        self.bt_guardarHangar.setIcon(icon18)
        self.bt_guardarHangar.setIconSize(QSize(40, 50))
        self.bt_guardarHangar.setFlat(True)
        self.sw_funcion_hangares.addWidget(self.pg_registrar_hg)
        self.pg_info_hg = QWidget()
        self.pg_info_hg.setObjectName(u"pg_info_hg")
        self.lb_nomHangar = QLabel(self.pg_info_hg)
        self.lb_nomHangar.setObjectName(u"lb_nomHangar")
        self.lb_nomHangar.setGeometry(QRect(100, 10, 231, 41))
        font13 = QFont()
        font13.setFamily(u"Open Sans")
        font13.setPointSize(12)
        self.lb_nomHangar.setFont(font13)
        self.lb_nomHangar.setTextFormat(Qt.RichText)
        self.label_cerrarsesion_107 = QLabel(self.pg_info_hg)
        self.label_cerrarsesion_107.setObjectName(u"label_cerrarsesion_107")
        self.label_cerrarsesion_107.setGeometry(QRect(90, 60, 71, 31))
        self.label_cerrarsesion_107.setFont(font2)
        self.lb_ModelodeAvion = QLabel(self.pg_info_hg)
        self.lb_ModelodeAvion.setObjectName(u"lb_ModelodeAvion")
        self.lb_ModelodeAvion.setGeometry(QRect(60, 90, 131, 31))
        font14 = QFont()
        font14.setFamily(u"Nirmala UI")
        font14.setPointSize(11)
        self.lb_ModelodeAvion.setFont(font14)
        self.label_cerrarsesion_108 = QLabel(self.pg_info_hg)
        self.label_cerrarsesion_108.setObjectName(u"label_cerrarsesion_108")
        self.label_cerrarsesion_108.setGeometry(QRect(230, 60, 101, 31))
        self.label_cerrarsesion_108.setFont(font7)
        self.lb_NombreAerolinea = QLabel(self.pg_info_hg)
        self.lb_NombreAerolinea.setObjectName(u"lb_NombreAerolinea")
        self.lb_NombreAerolinea.setGeometry(QRect(220, 90, 121, 31))
        font15 = QFont()
        font15.setFamily(u"Nirmala UI")
        font15.setPointSize(12)
        self.lb_NombreAerolinea.setFont(font15)
        self.label_cerrarsesion_109 = QLabel(self.pg_info_hg)
        self.label_cerrarsesion_109.setObjectName(u"label_cerrarsesion_109")
        self.label_cerrarsesion_109.setGeometry(QRect(80, 160, 121, 31))
        self.label_cerrarsesion_109.setFont(font8)
        self.lb_fechaEntrada = QLabel(self.pg_info_hg)
        self.lb_fechaEntrada.setObjectName(u"lb_fechaEntrada")
        self.lb_fechaEntrada.setGeometry(QRect(230, 200, 101, 31))
        font16 = QFont()
        font16.setPointSize(12)
        self.lb_fechaEntrada.setFont(font16)
        self.label_cerrarsesion_110 = QLabel(self.pg_info_hg)
        self.label_cerrarsesion_110.setObjectName(u"label_cerrarsesion_110")
        self.label_cerrarsesion_110.setGeometry(QRect(80, 200, 121, 31))
        self.label_cerrarsesion_110.setFont(font8)
        self.lb_HoraEntrada = QLabel(self.pg_info_hg)
        self.lb_HoraEntrada.setObjectName(u"lb_HoraEntrada")
        self.lb_HoraEntrada.setGeometry(QRect(230, 160, 71, 31))
        font17 = QFont()
        font17.setFamily(u"Nirmala UI")
        self.lb_HoraEntrada.setFont(font17)
        self.lb_TiempoenHoras = QLabel(self.pg_info_hg)
        self.lb_TiempoenHoras.setObjectName(u"lb_TiempoenHoras")
        self.lb_TiempoenHoras.setGeometry(QRect(230, 240, 91, 31))
        self.lb_TiempoenHoras.setFont(font14)
        self.label_cerrarsesion_111 = QLabel(self.pg_info_hg)
        self.label_cerrarsesion_111.setObjectName(u"label_cerrarsesion_111")
        self.label_cerrarsesion_111.setGeometry(QRect(140, 240, 61, 31))
        self.label_cerrarsesion_111.setFont(font7)
        self.lb_ValordelaHora = QLabel(self.pg_info_hg)
        self.lb_ValordelaHora.setObjectName(u"lb_ValordelaHora")
        self.lb_ValordelaHora.setGeometry(QRect(230, 280, 71, 31))
        self.lb_ValordelaHora.setFont(font14)
        self.label_cerrarsesion_112 = QLabel(self.pg_info_hg)
        self.label_cerrarsesion_112.setObjectName(u"label_cerrarsesion_112")
        self.label_cerrarsesion_112.setGeometry(QRect(100, 280, 111, 31))
        self.label_cerrarsesion_112.setFont(font2)
        self.line_32 = QFrame(self.pg_info_hg)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setGeometry(QRect(20, 10, 20, 371))
        self.line_32.setFrameShape(QFrame.VLine)
        self.line_32.setFrameShadow(QFrame.Sunken)
        self.line_33 = QFrame(self.pg_info_hg)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setGeometry(QRect(380, 10, 20, 371))
        self.line_33.setFrameShape(QFrame.VLine)
        self.line_33.setFrameShadow(QFrame.Sunken)
        self.line_34 = QFrame(self.pg_info_hg)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setGeometry(QRect(30, 0, 361, 20))
        self.line_34.setFrameShape(QFrame.HLine)
        self.line_34.setFrameShadow(QFrame.Sunken)
        self.line_35 = QFrame(self.pg_info_hg)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setGeometry(QRect(30, 40, 361, 20))
        self.line_35.setFrameShape(QFrame.HLine)
        self.line_35.setFrameShadow(QFrame.Sunken)
        self.line_36 = QFrame(self.pg_info_hg)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setGeometry(QRect(30, 130, 361, 20))
        self.line_36.setFrameShape(QFrame.HLine)
        self.line_36.setFrameShadow(QFrame.Sunken)
        self.bt_aceptarinfhg = QPushButton(self.pg_info_hg)
        self.bt_aceptarinfhg.setObjectName(u"bt_aceptarinfhg")
        self.bt_aceptarinfhg.setGeometry(QRect(170, 330, 101, 31))
        font18 = QFont()
        font18.setPointSize(11)
        font18.setBold(True)
        font18.setWeight(75)
        self.bt_aceptarinfhg.setFont(font18)
        self.line_37 = QFrame(self.pg_info_hg)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setGeometry(QRect(30, 370, 361, 20))
        self.line_37.setFrameShape(QFrame.HLine)
        self.line_37.setFrameShadow(QFrame.Sunken)
        self.bt_cerrar_infohg = QPushButton(self.pg_info_hg)
        self.bt_cerrar_infohg.setObjectName(u"bt_cerrar_infohg")
        self.bt_cerrar_infohg.setGeometry(QRect(360, 20, 21, 21))
        self.bt_cerrar_infohg.setFont(font7)
        self.bt_cerrar_infohg.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_cerrar_infohg.setStyleSheet(u"QPushButton:hover\n"
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
        icon22 = QIcon()
        icon22.addFile(u"../Ventanas/Icons/cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cerrar_infohg.setIcon(icon22)
        self.bt_cerrar_infohg.setIconSize(QSize(50, 61))
        self.bt_cerrar_infohg.setFlat(True)
        self.sw_funcion_hangares.addWidget(self.pg_info_hg)
        self.bt_eliminarH = QPushButton(self.groupBox_42)
        self.bt_eliminarH.setObjectName(u"bt_eliminarH")
        self.bt_eliminarH.setGeometry(QRect(40, 390, 111, 31))
        self.bt_eliminarH.setFont(font2)
        self.bt_eliminarH.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_eliminarH.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_eliminarH.setIconSize(QSize(40, 50))
        self.bt_eliminarH.setFlat(False)
        self.bt_agregarH = QPushButton(self.groupBox_42)
        self.bt_agregarH.setObjectName(u"bt_agregarH")
        self.bt_agregarH.setGeometry(QRect(160, 390, 111, 31))
        self.bt_agregarH.setFont(font2)
        self.bt_agregarH.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_agregarH.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_agregarH.setIconSize(QSize(40, 50))
        self.bt_agregarH.setFlat(False)
        self.bt_buscarHangar = QPushButton(self.pg_hangares)
        self.bt_buscarHangar.setObjectName(u"bt_buscarHangar")
        self.bt_buscarHangar.setGeometry(QRect(480, 20, 91, 31))
        self.bt_buscarHangar.setFont(font2)
        self.bt_buscarHangar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_buscarHangar.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_buscarHangar.setIcon(icon2)
        self.bt_buscarHangar.setIconSize(QSize(30, 50))
        self.bt_buscarHangar.setFlat(True)
        self.label_cerrarsesion_113 = QLabel(self.pg_hangares)
        self.label_cerrarsesion_113.setObjectName(u"label_cerrarsesion_113")
        self.label_cerrarsesion_113.setGeometry(QRect(190, 20, 141, 31))
        self.label_cerrarsesion_113.setFont(font7)
        self.cb_codHangar = QComboBox(self.pg_hangares)
        self.cb_codHangar.setObjectName(u"cb_codHangar")
        self.cb_codHangar.setGeometry(QRect(340, 20, 131, 31))
        self.bt_detallesHangar = QPushButton(self.pg_hangares)
        self.bt_detallesHangar.setObjectName(u"bt_detallesHangar")
        self.bt_detallesHangar.setGeometry(QRect(20, 520, 111, 41))
        self.bt_detallesHangar.setFont(font2)
        self.bt_detallesHangar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_detallesHangar.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_detallesHangar.setIcon(icon12)
        self.bt_detallesHangar.setIconSize(QSize(40, 50))
        self.bt_detallesHangar.setFlat(True)
        self.bt_ocuparHangar = QPushButton(self.pg_hangares)
        self.bt_ocuparHangar.setObjectName(u"bt_ocuparHangar")
        self.bt_ocuparHangar.setGeometry(QRect(290, 520, 121, 41))
        self.bt_ocuparHangar.setFont(font2)
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
        icon23 = QIcon()
        icon23.addFile(u"../Ventanas/Icons/hangar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_ocuparHangar.setIcon(icon23)
        self.bt_ocuparHangar.setIconSize(QSize(40, 50))
        self.bt_ocuparHangar.setFlat(True)
        self.bt_refreshHangar = QPushButton(self.pg_hangares)
        self.bt_refreshHangar.setObjectName(u"bt_refreshHangar")
        self.bt_refreshHangar.setGeometry(QRect(640, 520, 121, 41))
        self.bt_refreshHangar.setFont(font2)
        self.bt_refreshHangar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_refreshHangar.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_refreshHangar.setIcon(icon1)
        self.bt_refreshHangar.setIconSize(QSize(30, 40))
        self.bt_refreshHangar.setFlat(True)
        self.bt_generarReporte = QPushButton(self.pg_hangares)
        self.bt_generarReporte.setObjectName(u"bt_generarReporte")
        self.bt_generarReporte.setGeometry(QRect(440, 520, 171, 41))
        self.bt_generarReporte.setFont(font2)
        self.bt_generarReporte.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_generarReporte.setStyleSheet(u"QPushButton:hover\n"
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
        icon24 = QIcon()
        icon24.addFile(u"../Ventanas/Icons/Facturaci\u00f3n.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_generarReporte.setIcon(icon24)
        self.bt_generarReporte.setIconSize(QSize(40, 50))
        self.bt_generarReporte.setFlat(True)
        self.bt_detallesHangar_2 = QPushButton(self.pg_hangares)
        self.bt_detallesHangar_2.setObjectName(u"bt_detallesHangar_2")
        self.bt_detallesHangar_2.setGeometry(QRect(150, 520, 121, 41))
        self.bt_detallesHangar_2.setFont(font2)
        self.bt_detallesHangar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_detallesHangar_2.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_detallesHangar_2.setIcon(icon7)
        self.bt_detallesHangar_2.setIconSize(QSize(40, 50))
        self.bt_detallesHangar_2.setFlat(True)
        self.sk_mainWindow.addWidget(self.pg_hangares)
        self.line = QFrame(self.Controls)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(230, 0, 21, 601))
        self.line.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.Frameizq_menu = QFrame(self.Controls)
        self.Frameizq_menu.setObjectName(u"Frameizq_menu")
        self.Frameizq_menu.setGeometry(QRect(10, 10, 221, 591))
        self.Frameizq_menu.setStyleSheet(u"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Frameizq_menu.setFrameShape(QFrame.StyledPanel)
        self.Frameizq_menu.setFrameShadow(QFrame.Raised)
        self.label_tipousuari = QLabel(self.Frameizq_menu)
        self.label_tipousuari.setObjectName(u"label_tipousuari")
        self.label_tipousuari.setGeometry(QRect(20, 150, 181, 31))
        font19 = QFont()
        font19.setFamily(u"Open Sans")
        self.label_tipousuari.setFont(font19)
        self.label_tipousuari.setTextFormat(Qt.RichText)
        self.bt_usuarios = QPushButton(self.Frameizq_menu)
        self.bt_usuarios.setObjectName(u"bt_usuarios")
        self.bt_usuarios.setGeometry(QRect(40, 200, 141, 41))
        self.bt_usuarios.setFont(font)
        self.bt_usuarios.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_usuarios.setStyleSheet(u"color: rgb(22, 117, 163)")
        self.bt_usuarios.setAutoRepeatDelay(309)
        self.bt_usuarios.setAutoDefault(False)
        self.bt_usuarios.setFlat(False)
        self.bt_Vuelos = QPushButton(self.Frameizq_menu)
        self.bt_Vuelos.setObjectName(u"bt_Vuelos")
        self.bt_Vuelos.setGeometry(QRect(40, 350, 141, 41))
        self.bt_Vuelos.setFont(font)
        self.bt_Vuelos.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_Vuelos.setStyleSheet(u"color:rgb(22, 117, 163)")
        self.bt_Vuelos.setAutoRepeatDelay(309)
        self.bt_Vuelos.setAutoDefault(False)
        self.bt_Vuelos.setFlat(False)
        self.bt_Aerolineas = QPushButton(self.Frameizq_menu)
        self.bt_Aerolineas.setObjectName(u"bt_Aerolineas")
        self.bt_Aerolineas.setGeometry(QRect(40, 250, 141, 41))
        self.bt_Aerolineas.setFont(font)
        self.bt_Aerolineas.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_Aerolineas.setStyleSheet(u"color: rgb(22, 117, 163);")
        self.bt_Aerolineas.setAutoRepeatDelay(309)
        self.bt_Aerolineas.setAutoDefault(False)
        self.bt_Aerolineas.setFlat(False)
        self.bt_Hangares = QPushButton(self.Frameizq_menu)
        self.bt_Hangares.setObjectName(u"bt_Hangares")
        self.bt_Hangares.setGeometry(QRect(40, 400, 141, 41))
        self.bt_Hangares.setFont(font)
        self.bt_Hangares.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_Hangares.setStyleSheet(u"color:rgb(22, 117, 163)\n"
"")
        self.bt_Hangares.setAutoRepeatDelay(309)
        self.bt_Hangares.setAutoDefault(False)
        self.bt_Hangares.setFlat(False)
        self.bt_CerrarSesion = QPushButton(self.Frameizq_menu)
        self.bt_CerrarSesion.setObjectName(u"bt_CerrarSesion")
        self.bt_CerrarSesion.setGeometry(QRect(70, 470, 71, 81))
        font20 = QFont()
        font20.setFamily(u"HoloLens MDL2 Assets")
        font20.setPointSize(16)
        self.bt_CerrarSesion.setFont(font20)
        self.bt_CerrarSesion.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_CerrarSesion.setAcceptDrops(False)
        self.bt_CerrarSesion.setStyleSheet(u"QPushButton:hover\n"
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
        icon25 = QIcon()
        icon25.addFile(u"../Ventanas/Icons/cerrar_sesion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_CerrarSesion.setIcon(icon25)
        self.bt_CerrarSesion.setIconSize(QSize(80, 80))
        self.bt_CerrarSesion.setCheckable(False)
        self.bt_CerrarSesion.setAutoRepeat(False)
        self.bt_CerrarSesion.setAutoExclusive(False)
        self.bt_CerrarSesion.setAutoRepeatDelay(309)
        self.bt_CerrarSesion.setAutoDefault(False)
        self.bt_CerrarSesion.setFlat(True)
        self.label_cerrarsesion = QLabel(self.Frameizq_menu)
        self.label_cerrarsesion.setObjectName(u"label_cerrarsesion")
        self.label_cerrarsesion.setGeometry(QRect(50, 550, 111, 16))
        self.label_cerrarsesion.setFont(font)
        self.bt_user = QPushButton(self.Frameizq_menu)
        self.bt_user.setObjectName(u"bt_user")
        self.bt_user.setGeometry(QRect(40, 20, 141, 121))
        icon26 = QIcon()
        icon26.addFile(u"../Ventanas/Icons/persona_.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_user.setIcon(icon26)
        self.bt_user.setIconSize(QSize(131, 121))
        self.bt_user.setFlat(True)
        self.bt_agendaMain = QPushButton(self.Frameizq_menu)
        self.bt_agendaMain.setObjectName(u"bt_agendaMain")
        self.bt_agendaMain.setGeometry(QRect(40, 300, 141, 41))
        self.bt_agendaMain.setFont(font)
        self.bt_agendaMain.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_agendaMain.setStyleSheet(u"color:rgb(22, 117, 163)")
        self.bt_agendaMain.setAutoRepeatDelay(309)
        self.bt_agendaMain.setAutoDefault(False)
        self.bt_agendaMain.setFlat(False)
        self.pag_Main.addWidget(self.Controls)

        self.retranslateUi(mainWindow)

        self.pag_Main.setCurrentIndex(1)
        self.sk_mainWindow.setCurrentIndex(0)
        self.sk_agendaAero.setCurrentIndex(2)
        self.sw_vuelos_av_trip.setCurrentIndex(0)
        self.bt_modificarVA.setDefault(False)
        self.bt_eliminarVA.setDefault(False)
        self.bt_GuardarTrip.setDefault(True)
        self.bt_AgregarTrip.setDefault(True)
        self.sw_reg_ver_avion.setCurrentIndex(1)
        self.bt_aceptarAVEA.setDefault(True)
        self.bt_cancelar_RA.setDefault(True)
        self.bt_eliminarAvion.setDefault(False)
        self.bt_modificarAvion.setDefault(False)
        self.bt_actualizar_avion.setDefault(False)
        self.sw_funcion_hangares.setCurrentIndex(2)
        self.bt_guardarHangar.setDefault(True)
        self.bt_eliminarH.setDefault(False)
        self.bt_usuarios.setDefault(False)
        self.bt_Vuelos.setDefault(False)
        self.bt_Aerolineas.setDefault(False)
        self.bt_Hangares.setDefault(False)
        self.bt_CerrarSesion.setDefault(False)
        self.bt_agendaMain.setDefault(False)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Bienvenido - Aeropuerto el Campanero", None))
        self.correo_lineEdit.setText("")
        self.correo_lineEdit.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Correo Electronico", None))
        self.bt_ingresarlg.setText(QCoreApplication.translate("mainWindow", u"Ingresar", None))
        self.label_13.setText("")
        self.lgcontra_lineEdit_2.setText("")
        self.lgcontra_lineEdit_2.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Contrase\u00f1a", None))
        self.label_14.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:400; color:#1675a3;\">Aeropuerto el Campanero</span></p></body></html>", None))
        self.label_cerrarsesion_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#000000;\">Sistema de Gesti\u00f3n Aeropuerto el Campanero</span></p></body></html>", None))
        self.label_11.setText("")
        self.label_cerrarsesion_97.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#000000;\">BIENVENIDO</span></p></body></html>", None))
        self.bt_refreshUsuario.setText(QCoreApplication.translate("mainWindow", u"Actualizar", None))
        self.bt_buscarUsuario.setText(QCoreApplication.translate("mainWindow", u"Buscar", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("mainWindow", u"Usuarios Registrados", None))
        ___qtablewidgetitem = self.tb_vistaGeneral_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tb_vistaGeneral_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mainWindow", u"Tipo ID", None));
        ___qtablewidgetitem2 = self.tb_vistaGeneral_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("mainWindow", u"Nombre", None));
        ___qtablewidgetitem3 = self.tb_vistaGeneral_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("mainWindow", u"Apellido", None));
        ___qtablewidgetitem4 = self.tb_vistaGeneral_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("mainWindow", u"Correo", None));
        ___qtablewidgetitem5 = self.tb_vistaGeneral_2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("mainWindow", u"Cuenta", None));
        self.bt_eliminarUsuario.setText(QCoreApplication.translate("mainWindow", u"Eliminar Usuario", None))
#if QT_CONFIG(tooltip)
        self.le_buscarUsuario.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.le_buscarUsuario.setInputMask("")
        self.le_buscarUsuario.setText("")
        self.le_buscarUsuario.setPlaceholderText("")
        self.bt_editarUsuario.setText(QCoreApplication.translate("mainWindow", u"Editar Usuario", None))
        self.bt_addUsuario.setText(QCoreApplication.translate("mainWindow", u"Agregar Usuario ", None))
        self.label_cerrarsesion_98.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Id de Usuario</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("mainWindow", u"Aerol\u00edneas Registradas", None))
        ___qtablewidgetitem6 = self.tb_aeroRegistradas.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("mainWindow", u"NIT", None));
        ___qtablewidgetitem7 = self.tb_aeroRegistradas.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("mainWindow", u"Nombre Aerol\u00ednea", None));
        ___qtablewidgetitem8 = self.tb_aeroRegistradas.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("mainWindow", u"Correo ", None));
        ___qtablewidgetitem9 = self.tb_aeroRegistradas.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("mainWindow", u"Tel\u00e9fono", None));
#if QT_CONFIG(tooltip)
        self.le_buscarAero.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.le_buscarAero.setInputMask("")
        self.le_buscarAero.setText("")
        self.le_buscarAero.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Ingrese el nombre de su aerolinea", None))
        self.bt_buscarAerolinea.setText(QCoreApplication.translate("mainWindow", u"Buscar", None))
        self.bt_addAerolinea.setText(QCoreApplication.translate("mainWindow", u"Agregar Aerol\u00ednea ", None))
        self.bt_editarAerolinea.setText(QCoreApplication.translate("mainWindow", u"Editar Aerol\u00ednea", None))
        self.bt_refreshAerolinea.setText(QCoreApplication.translate("mainWindow", u"Actualizar", None))
        self.bt_eliminarAerolinea.setText(QCoreApplication.translate("mainWindow", u"Eliminar Aerol\u00ednea", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("mainWindow", u"Agenda del D\u00eda", None))
        ___qtablewidgetitem10 = self.tb_vistaGeneral.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("mainWindow", u"Fecha", None));
        ___qtablewidgetitem11 = self.tb_vistaGeneral.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("mainWindow", u"Hora", None));
        ___qtablewidgetitem12 = self.tb_vistaGeneral.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("mainWindow", u"Codigo", None));
        ___qtablewidgetitem13 = self.tb_vistaGeneral.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("mainWindow", u"Tipo", None));
        ___qtablewidgetitem14 = self.tb_vistaGeneral.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("mainWindow", u"Vuelo", None));
        ___qtablewidgetitem15 = self.tb_vistaGeneral.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("mainWindow", u"Destino", None));
        ___qtablewidgetitem16 = self.tb_vistaGeneral.horizontalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("mainWindow", u"Origen", None));
        ___qtablewidgetitem17 = self.tb_vistaGeneral.horizontalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("mainWindow", u"Estado", None));
        ___qtablewidgetitem18 = self.tb_vistaSalida.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("mainWindow", u"Fecha", None));
        ___qtablewidgetitem19 = self.tb_vistaSalida.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("mainWindow", u"Hora", None));
        ___qtablewidgetitem20 = self.tb_vistaSalida.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("mainWindow", u"Codigo", None));
        ___qtablewidgetitem21 = self.tb_vistaSalida.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("mainWindow", u"Vuelo", None));
        ___qtablewidgetitem22 = self.tb_vistaSalida.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("mainWindow", u"Destino", None));
        ___qtablewidgetitem23 = self.tb_vistaSalida.horizontalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("mainWindow", u"Estado", None));
        ___qtablewidgetitem24 = self.tb_vistaLlegada.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("mainWindow", u"Fecha", None));
        ___qtablewidgetitem25 = self.tb_vistaLlegada.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("mainWindow", u"Hora", None));
        ___qtablewidgetitem26 = self.tb_vistaLlegada.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("mainWindow", u"Codigo", None));
        ___qtablewidgetitem27 = self.tb_vistaLlegada.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("mainWindow", u"Vuelo", None));
        ___qtablewidgetitem28 = self.tb_vistaLlegada.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("mainWindow", u"Origen", None));
        ___qtablewidgetitem29 = self.tb_vistaLlegada.horizontalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("mainWindow", u"Estado", None));
#if QT_CONFIG(tooltip)
        self.le_buscarAgenda.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.le_buscarAgenda.setInputMask("")
        self.le_buscarAgenda.setText("")
        self.le_buscarAgenda.setPlaceholderText("")
        self.bt_buscarAgenda.setText(QCoreApplication.translate("mainWindow", u"Buscar", None))
        self.bt_refreshAgenda.setText(QCoreApplication.translate("mainWindow", u"Actualizar", None))
        self.label_cerrarsesion_99.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Vuelos de Llegada</span></p></body></html>", None))
        self.bt_vuelosSalida.setText("")
        self.bt_agendarVuelo.setText("")
        self.bt_vuelosLlegada.setText("")
        self.label_cerrarsesion_100.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Info. Vuelo</span></p></body></html>", None))
        self.bt_infoVuelo.setText("")
        self.label_cerrarsesion_101.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Agendar Vuelo</span></p></body></html>", None))
        self.label_cerrarsesion_102.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\">Vista General</p></body></html>", None))
        self.bt_vistaGeneral.setText("")
        self.label_cerrarsesion_103.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Vuelos de Salida</span></p></body></html>", None))
        self.bt_vuelos.setText(QCoreApplication.translate("mainWindow", u"Crear Nueva Agenda ", None))
        self.bt_aviones.setText(QCoreApplication.translate("mainWindow", u"Aviones", None))
        self.bt_vuelosAerolinea.setText(QCoreApplication.translate("mainWindow", u"Vuelos", None))
        self.bt_nuevaTrip.setText(QCoreApplication.translate("mainWindow", u"Nueva Tripulaci\u00f3n", None))
        self.groupBox_39.setTitle(QCoreApplication.translate("mainWindow", u"Agenda de Aerolinea", None))
        ___qtablewidgetitem30 = self.tb_vistaAerolinea.horizontalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("mainWindow", u"Fecha", None));
        ___qtablewidgetitem31 = self.tb_vistaAerolinea.horizontalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("mainWindow", u"Hora", None));
        ___qtablewidgetitem32 = self.tb_vistaAerolinea.horizontalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("mainWindow", u"Codigo", None));
        ___qtablewidgetitem33 = self.tb_vistaAerolinea.horizontalHeaderItem(3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("mainWindow", u"Tipo", None));
        ___qtablewidgetitem34 = self.tb_vistaAerolinea.horizontalHeaderItem(4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("mainWindow", u"Vuelo", None));
        ___qtablewidgetitem35 = self.tb_vistaAerolinea.horizontalHeaderItem(5)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("mainWindow", u"Destino", None));
        ___qtablewidgetitem36 = self.tb_vistaAerolinea.horizontalHeaderItem(6)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("mainWindow", u"Origen", None));
        ___qtablewidgetitem37 = self.tb_vistaAerolinea.horizontalHeaderItem(7)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("mainWindow", u"Estado", None));
        self.bt_agregarVA.setText(QCoreApplication.translate("mainWindow", u"Agregar", None))
        self.bt_modificarVA.setText(QCoreApplication.translate("mainWindow", u"Modificar", None))
        self.bt_eliminarVA.setText(QCoreApplication.translate("mainWindow", u"Eliminar ", None))
        self.label_cerrarsesion_104.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Buscar </span></p></body></html>", None))
        self.bt_buscarAgenda_Aerolinea.setText(QCoreApplication.translate("mainWindow", u"Buscar", None))
#if QT_CONFIG(tooltip)
        self.le_buscarAgendaAerolinea.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.le_buscarAgendaAerolinea.setInputMask("")
        self.le_buscarAgendaAerolinea.setText("")
        self.le_buscarAgendaAerolinea.setPlaceholderText("")
        self.bt_refreshAgenda_Aerolinea.setText(QCoreApplication.translate("mainWindow", u"Actualizar", None))
        self.groupBox_40.setTitle(QCoreApplication.translate("mainWindow", u"Agenda Pendiente por enviar", None))
        ___qtablewidgetitem38 = self.tb_vistaAerolineaPendiente.horizontalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("mainWindow", u"Fecha", None));
        ___qtablewidgetitem39 = self.tb_vistaAerolineaPendiente.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("mainWindow", u"Hora", None));
        ___qtablewidgetitem40 = self.tb_vistaAerolineaPendiente.horizontalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("mainWindow", u"Codigo", None));
        ___qtablewidgetitem41 = self.tb_vistaAerolineaPendiente.horizontalHeaderItem(3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("mainWindow", u"Tipo", None));
        ___qtablewidgetitem42 = self.tb_vistaAerolineaPendiente.horizontalHeaderItem(4)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("mainWindow", u"Vuelo", None));
        ___qtablewidgetitem43 = self.tb_vistaAerolineaPendiente.horizontalHeaderItem(5)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("mainWindow", u"Destino", None));
        ___qtablewidgetitem44 = self.tb_vistaAerolineaPendiente.horizontalHeaderItem(6)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("mainWindow", u"Origen", None));
        ___qtablewidgetitem45 = self.tb_vistaAerolineaPendiente.horizontalHeaderItem(7)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("mainWindow", u"Estado", None));
        self.bt_agregar_avion.setText(QCoreApplication.translate("mainWindow", u"Enviar agenda", None))
        self.lb_NumeroID.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Licencia</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.lb_tipoID.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Tipo ID</span></p></body></html>", None))
        self.lb_codTripulacion.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Cod Tripulaci\u00f3n</span></p></body></html>", None))
        self.lb_NumeroID_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Numero ID</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.lb_tipoID_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Horas de vuelo</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.lb_Nombre.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Nombre</span></p></body></html>", None))
        self.lb_tipoID_18.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Fecha \u00faltima rev. m\u00e9dica</span></p></body></html>", None))
        self.bt_GuardarTrip.setText(QCoreApplication.translate("mainWindow", u"GUARDAR", None))
        self.cb_tipoID.setItemText(0, QCoreApplication.translate("mainWindow", u"C\u00e9dula", None))
        self.cb_tipoID.setItemText(1, QCoreApplication.translate("mainWindow", u"C\u00e9dula Extranjer\u00eda ", None))
        self.cb_tipoID.setItemText(2, QCoreApplication.translate("mainWindow", u"NIT", None))

        self.lb_apellido.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Apellido</span></p></body></html>", None))
        self.lb_facturanum.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:400; color:#1675a3;\">Registrar Tripulaci\u00f3n</span></p></body></html>", None))
        self.bt_AgregarTrip.setText(QCoreApplication.translate("mainWindow", u"AGREGAR TRIP.", None))
        self.lb_Modelo_7.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Modelo</span></p></body></html>", None))
        self.lb_PesoNominal_7.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Peso Nominal</span></p></body></html>", None))
        self.bt_checkIDavion.setText("")
        self.cb_PropulsionEA.setItemText(0, QCoreApplication.translate("mainWindow", u"Reacci\u00f3n", None))
        self.cb_PropulsionEA.setItemText(1, QCoreApplication.translate("mainWindow", u"Turbo H\u00e9lice", None))
        self.cb_PropulsionEA.setItemText(2, QCoreApplication.translate("mainWindow", u"H\u00e9lice", None))

        self.bt_aceptarAVEA.setText(QCoreApplication.translate("mainWindow", u"GUARDAR AVION", None))
        self.lb_TipodeAvion_7.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Tipo de Avi\u00f3n</span></p></body></html>", None))
        self.lb_Capacidad.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Capacidad</span></p></body></html>", None))
        self.lb_Motores_7.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Motores</span></p></body></html>", None))
        self.lb_facturanum_17.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:400; color:#1675a3;\">Registrar avion</span></p></body></html>", None))
        self.lb_Propulsion_7.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Propulsi\u00f3n</span></p></body></html>", None))
        self.lb_Identificador_22.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.cb_pasajerosEA.setItemText(0, QCoreApplication.translate("mainWindow", u"Pasajeros", None))
        self.cb_pasajerosEA.setItemText(1, QCoreApplication.translate("mainWindow", u"Carga", None))

        self.lb_Identificador_23.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Identificador</span></p></body></html>", None))
        self.bt_cancelar_RA.setText(QCoreApplication.translate("mainWindow", u"VOLVER", None))
        self.label_cerrarsesion_105.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">C\u00f3digo de Avi\u00f3n</span></p></body></html>", None))
        self.groupBox_41.setTitle(QCoreApplication.translate("mainWindow", u"Aviones registrados", None))
        ___qtablewidgetitem46 = self.tb_avionesregistradosAV.horizontalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("mainWindow", u"Identificador ", None));
        ___qtablewidgetitem47 = self.tb_avionesregistradosAV.horizontalHeaderItem(1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("mainWindow", u"Tipo", None));
        ___qtablewidgetitem48 = self.tb_avionesregistradosAV.horizontalHeaderItem(2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("mainWindow", u"Modelo", None));
        ___qtablewidgetitem49 = self.tb_avionesregistradosAV.horizontalHeaderItem(3)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("mainWindow", u"Propulsi\u00f3n", None));
        ___qtablewidgetitem50 = self.tb_avionesregistradosAV.horizontalHeaderItem(4)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("mainWindow", u"Capacidad", None));
        ___qtablewidgetitem51 = self.tb_avionesregistradosAV.horizontalHeaderItem(5)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("mainWindow", u"Peso", None));
        ___qtablewidgetitem52 = self.tb_avionesregistradosAV.horizontalHeaderItem(6)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("mainWindow", u"Motores", None));
        self.bt_eliminarAvion.setText(QCoreApplication.translate("mainWindow", u"Eliminar ", None))
        self.bt_agregarAvion.setText(QCoreApplication.translate("mainWindow", u"Agregar", None))
        self.bt_modificarAvion.setText(QCoreApplication.translate("mainWindow", u"Modificar", None))
        self.bt_actualizar_avion.setText(QCoreApplication.translate("mainWindow", u"Actualizar", None))
        self.bt_buscarVuelo.setText(QCoreApplication.translate("mainWindow", u"Buscar", None))
        self.bt_agendaPendiente.setText(QCoreApplication.translate("mainWindow", u"Agenda Pendiente", None))
        self.groupBox_42.setTitle(QCoreApplication.translate("mainWindow", u"Hangares ", None))
        ___qtablewidgetitem53 = self.tb_hangares.horizontalHeaderItem(0)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("mainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem54 = self.tb_hangares.horizontalHeaderItem(1)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("mainWindow", u"Estado", None));
        self.label_12.setText("")
        self.label_cerrarsesion_106.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Sistema de Gesti\u00f3n Aeropuerto el Campanero</span></p></body></html>", None))
        self.lb_Identificador.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Capacidad m</span><span style=\" font-weight:600; color:#000000; vertical-align:super;\">2</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.lb_facturanum_18.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:400; color:#1675a3;\">Registrar de hangares</span></p></body></html>", None))
        self.lb_Identificador_.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">C\u00f3digo</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.bt_guardarHangar.setText(QCoreApplication.translate("mainWindow", u"GUARDAR", None))
        self.lb_nomHangar.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#1675a3;\">Hangar</span></p></body></html>", None))
        self.label_cerrarsesion_107.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\">Avi\u00f3n</p></body></html>", None))
        self.lb_ModelodeAvion.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_cerrarsesion_108.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Aerol\u00ednea</span></p></body></html>", None))
        self.lb_NombreAerolinea.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_cerrarsesion_109.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Hora de Entrada</span></p></body></html>", None))
        self.lb_fechaEntrada.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_cerrarsesion_110.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Fecha de Entrada</span></p></body></html>", None))
        self.lb_HoraEntrada.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lb_TiempoenHoras.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_cerrarsesion_111.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Tiempo</span></p></body></html>", None))
        self.lb_ValordelaHora.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_cerrarsesion_112.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\">Valor por Hora</p></body></html>", None))
        self.bt_aceptarinfhg.setText(QCoreApplication.translate("mainWindow", u"Aceptar", None))
        self.bt_cerrar_infohg.setText("")
        self.bt_eliminarH.setText(QCoreApplication.translate("mainWindow", u"Eliminar ", None))
        self.bt_agregarH.setText(QCoreApplication.translate("mainWindow", u"Agregar", None))
        self.bt_buscarHangar.setText(QCoreApplication.translate("mainWindow", u"Buscar", None))
        self.label_cerrarsesion_113.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">C\u00f3digo de Hangar</span></p></body></html>", None))
        self.bt_detallesHangar.setText(QCoreApplication.translate("mainWindow", u"Detalles", None))
        self.bt_ocuparHangar.setText(QCoreApplication.translate("mainWindow", u"Ocupar", None))
        self.bt_refreshHangar.setText(QCoreApplication.translate("mainWindow", u"Actualizar", None))
        self.bt_generarReporte.setText(QCoreApplication.translate("mainWindow", u"Generar Reporte", None))
        self.bt_detallesHangar_2.setText(QCoreApplication.translate("mainWindow", u"Modificar", None))
        self.label_tipousuari.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#1675a3;\">Administrador</span></p></body></html>", None))
        self.bt_usuarios.setText(QCoreApplication.translate("mainWindow", u"Usuarios", None))
        self.bt_Vuelos.setText(QCoreApplication.translate("mainWindow", u"Vuelos", None))
        self.bt_Aerolineas.setText(QCoreApplication.translate("mainWindow", u"Aerolineas", None))
        self.bt_Hangares.setText(QCoreApplication.translate("mainWindow", u"Hangares", None))
#if QT_CONFIG(tooltip)
        self.bt_CerrarSesion.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bt_CerrarSesion.setText("")
        self.label_cerrarsesion.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#000000;\">Cerrar Sesi\u00f3n</span></p></body></html>", None))
        self.bt_user.setText("")
        self.bt_agendaMain.setText(QCoreApplication.translate("mainWindow", u"Agenda", None))
    # retranslateUi

