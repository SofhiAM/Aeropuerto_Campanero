# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main Window.ui'
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
        mainWindow.resize(1032, 606)
        icon = QIcon()
        icon.addFile(u"../Ventanas/Icons/Paper-Plane-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.Frameizq_menu = QFrame(mainWindow)
        self.Frameizq_menu.setObjectName(u"Frameizq_menu")
        self.Frameizq_menu.setGeometry(QRect(0, 10, 221, 591))
        self.Frameizq_menu.setStyleSheet(u"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Frameizq_menu.setFrameShape(QFrame.StyledPanel)
        self.Frameizq_menu.setFrameShadow(QFrame.Raised)
        self.label_tipousuario = QLabel(self.Frameizq_menu)
        self.label_tipousuario.setObjectName(u"label_tipousuario")
        self.label_tipousuario.setGeometry(QRect(20, 150, 181, 31))
        font = QFont()
        font.setFamily(u"Open Sans")
        self.label_tipousuario.setFont(font)
        self.label_tipousuario.setTextFormat(Qt.RichText)
        self.bt_usuarios = QPushButton(self.Frameizq_menu)
        self.bt_usuarios.setObjectName(u"bt_usuarios")
        self.bt_usuarios.setGeometry(QRect(40, 200, 141, 41))
        font1 = QFont()
        font1.setFamily(u"Open Sans Semibold")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.bt_usuarios.setFont(font1)
        self.bt_usuarios.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_usuarios.setStyleSheet(u"color: rgb(22, 117, 163)")
        self.bt_usuarios.setAutoRepeatDelay(309)
        self.bt_usuarios.setAutoDefault(False)
        self.bt_usuarios.setFlat(False)
        self.bt_Vuelos = QPushButton(self.Frameizq_menu)
        self.bt_Vuelos.setObjectName(u"bt_Vuelos")
        self.bt_Vuelos.setGeometry(QRect(40, 350, 141, 41))
        self.bt_Vuelos.setFont(font1)
        self.bt_Vuelos.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_Vuelos.setStyleSheet(u"color:rgb(22, 117, 163)")
        self.bt_Vuelos.setAutoRepeatDelay(309)
        self.bt_Vuelos.setAutoDefault(False)
        self.bt_Vuelos.setFlat(False)
        self.bt_Aerolineas = QPushButton(self.Frameizq_menu)
        self.bt_Aerolineas.setObjectName(u"bt_Aerolineas")
        self.bt_Aerolineas.setGeometry(QRect(40, 250, 141, 41))
        self.bt_Aerolineas.setFont(font1)
        self.bt_Aerolineas.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_Aerolineas.setStyleSheet(u"color: rgb(22, 117, 163);")
        self.bt_Aerolineas.setAutoRepeatDelay(309)
        self.bt_Aerolineas.setAutoDefault(False)
        self.bt_Aerolineas.setFlat(False)
        self.bt_Hangares = QPushButton(self.Frameizq_menu)
        self.bt_Hangares.setObjectName(u"bt_Hangares")
        self.bt_Hangares.setGeometry(QRect(40, 400, 141, 41))
        self.bt_Hangares.setFont(font1)
        self.bt_Hangares.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_Hangares.setStyleSheet(u"color:rgb(22, 117, 163)\n"
"")
        self.bt_Hangares.setAutoRepeatDelay(309)
        self.bt_Hangares.setAutoDefault(False)
        self.bt_Hangares.setFlat(False)
        self.bt_CerrarSesion = QPushButton(self.Frameizq_menu)
        self.bt_CerrarSesion.setObjectName(u"bt_CerrarSesion")
        self.bt_CerrarSesion.setGeometry(QRect(70, 470, 71, 81))
        font2 = QFont()
        font2.setFamily(u"HoloLens MDL2 Assets")
        font2.setPointSize(16)
        self.bt_CerrarSesion.setFont(font2)
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
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/cerrar_sesion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_CerrarSesion.setIcon(icon1)
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
        self.label_cerrarsesion.setFont(font1)
        self.bt_user = QPushButton(self.Frameizq_menu)
        self.bt_user.setObjectName(u"bt_user")
        self.bt_user.setGeometry(QRect(40, 20, 141, 121))
        icon2 = QIcon()
        icon2.addFile(u"../Ventanas/Icons/persona_.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_user.setIcon(icon2)
        self.bt_user.setIconSize(QSize(131, 121))
        self.bt_user.setFlat(True)
        self.bt_agendaMain = QPushButton(self.Frameizq_menu)
        self.bt_agendaMain.setObjectName(u"bt_agendaMain")
        self.bt_agendaMain.setGeometry(QRect(40, 300, 141, 41))
        self.bt_agendaMain.setFont(font1)
        self.bt_agendaMain.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_agendaMain.setStyleSheet(u"color:rgb(22, 117, 163)")
        self.bt_agendaMain.setAutoRepeatDelay(309)
        self.bt_agendaMain.setAutoDefault(False)
        self.bt_agendaMain.setFlat(False)
        self.line = QFrame(mainWindow)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(213, 0, 21, 601))
        self.line.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.sk_mainWindow = QStackedWidget(mainWindow)
        self.sk_mainWindow.setObjectName(u"sk_mainWindow")
        self.sk_mainWindow.setGeometry(QRect(240, 10, 781, 581))
        self.pg_bienvenido = QWidget()
        self.pg_bienvenido.setObjectName(u"pg_bienvenido")
        self.label_cerrarsesion_8 = QLabel(self.pg_bienvenido)
        self.label_cerrarsesion_8.setObjectName(u"label_cerrarsesion_8")
        self.label_cerrarsesion_8.setGeometry(QRect(110, 430, 571, 51))
        self.label_cerrarsesion_8.setFont(font1)
        self.label = QLabel(self.pg_bienvenido)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 150, 301, 301))
        self.label.setPixmap(QPixmap(u"../Ventanas/Icons/Avion.png"))
        self.label.setScaledContents(True)
        self.label_cerrarsesion_9 = QLabel(self.pg_bienvenido)
        self.label_cerrarsesion_9.setObjectName(u"label_cerrarsesion_9")
        self.label_cerrarsesion_9.setGeometry(QRect(290, 110, 221, 41))
        font3 = QFont()
        font3.setFamily(u"Franklin Gothic Heavy")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_cerrarsesion_9.setFont(font3)
        self.sk_mainWindow.addWidget(self.pg_bienvenido)
        self.pg_usuarios = QWidget()
        self.pg_usuarios.setObjectName(u"pg_usuarios")
        self.bt_refreshUsuario = QPushButton(self.pg_usuarios)
        self.bt_refreshUsuario.setObjectName(u"bt_refreshUsuario")
        self.bt_refreshUsuario.setGeometry(QRect(600, 520, 131, 41))
        font4 = QFont()
        font4.setFamily(u"Nirmala UI")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.bt_refreshUsuario.setFont(font4)
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
        icon3 = QIcon()
        icon3.addFile(u"../Ventanas/Icons/recarga.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_refreshUsuario.setIcon(icon3)
        self.bt_refreshUsuario.setIconSize(QSize(30, 40))
        self.bt_refreshUsuario.setFlat(True)
        self.bt_buscarUsuario = QPushButton(self.pg_usuarios)
        self.bt_buscarUsuario.setObjectName(u"bt_buscarUsuario")
        self.bt_buscarUsuario.setGeometry(QRect(510, 30, 91, 31))
        self.bt_buscarUsuario.setFont(font4)
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
        icon4 = QIcon()
        icon4.addFile(u"../Ventanas/Icons/buscar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_buscarUsuario.setIcon(icon4)
        self.bt_buscarUsuario.setIconSize(QSize(30, 50))
        self.bt_buscarUsuario.setFlat(True)
        self.groupBox_4 = QGroupBox(self.pg_usuarios)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(40, 100, 701, 401))
        self.groupBox_4.setFont(font4)
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.tb_vistaGeneral_2 = QTableWidget(self.groupBox_4)
        if (self.tb_vistaGeneral_2.columnCount() < 6):
            self.tb_vistaGeneral_2.setColumnCount(6)
        brush = QBrush(QColor(22, 117, 163, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        __qtablewidgetitem.setForeground(brush);
        self.tb_vistaGeneral_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        __qtablewidgetitem1.setForeground(brush);
        self.tb_vistaGeneral_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        __qtablewidgetitem2.setForeground(brush);
        self.tb_vistaGeneral_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        __qtablewidgetitem3.setForeground(brush);
        self.tb_vistaGeneral_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        __qtablewidgetitem4.setForeground(brush);
        self.tb_vistaGeneral_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        __qtablewidgetitem5.setForeground(brush);
        self.tb_vistaGeneral_2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tb_vistaGeneral_2.setObjectName(u"tb_vistaGeneral_2")
        self.tb_vistaGeneral_2.setGeometry(QRect(10, 30, 681, 361))
        font5 = QFont()
        font5.setFamily(u"Open Sans")
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(1)
        self.tb_vistaGeneral_2.setFont(font5)
        self.tb_vistaGeneral_2.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 9 pt \"Open Sans\"")
        self.tb_vistaGeneral_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.bt_eliminarUsuario = QPushButton(self.pg_usuarios)
        self.bt_eliminarUsuario.setObjectName(u"bt_eliminarUsuario")
        self.bt_eliminarUsuario.setGeometry(QRect(220, 520, 171, 41))
        self.bt_eliminarUsuario.setFont(font4)
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
        icon5 = QIcon()
        icon5.addFile(u"../Ventanas/Icons/eliminar_usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_eliminarUsuario.setIcon(icon5)
        self.bt_eliminarUsuario.setIconSize(QSize(30, 50))
        self.bt_eliminarUsuario.setFlat(True)
        self.le_buscarUsuario = QLineEdit(self.pg_usuarios)
        self.le_buscarUsuario.setObjectName(u"le_buscarUsuario")
        self.le_buscarUsuario.setGeometry(QRect(270, 30, 221, 31))
        font6 = QFont()
        font6.setFamily(u"Open Sans")
        font6.setPointSize(9)
        self.le_buscarUsuario.setFont(font6)
        self.bt_editarUsuario = QPushButton(self.pg_usuarios)
        self.bt_editarUsuario.setObjectName(u"bt_editarUsuario")
        self.bt_editarUsuario.setGeometry(QRect(420, 520, 151, 41))
        self.bt_editarUsuario.setFont(font4)
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
        icon6 = QIcon()
        icon6.addFile(u"../Ventanas/Icons/editar_usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_editarUsuario.setIcon(icon6)
        self.bt_editarUsuario.setIconSize(QSize(30, 50))
        self.bt_editarUsuario.setFlat(True)
        self.bt_addUsuario = QPushButton(self.pg_usuarios)
        self.bt_addUsuario.setObjectName(u"bt_addUsuario")
        self.bt_addUsuario.setGeometry(QRect(20, 520, 171, 41))
        self.bt_addUsuario.setFont(font4)
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
        icon7 = QIcon()
        icon7.addFile(u"../Ventanas/Icons/nuevo_usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_addUsuario.setIcon(icon7)
        self.bt_addUsuario.setIconSize(QSize(30, 50))
        self.bt_addUsuario.setFlat(True)
        self.label_cerrarsesion_10 = QLabel(self.pg_usuarios)
        self.label_cerrarsesion_10.setObjectName(u"label_cerrarsesion_10")
        self.label_cerrarsesion_10.setGeometry(QRect(140, 30, 101, 31))
        font7 = QFont()
        font7.setFamily(u"Nirmala UI")
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_cerrarsesion_10.setFont(font7)
        self.sk_mainWindow.addWidget(self.pg_usuarios)
        self.pg_aerolinea = QWidget()
        self.pg_aerolinea.setObjectName(u"pg_aerolinea")
        self.groupBox = QGroupBox(self.pg_aerolinea)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 80, 711, 441))
        self.groupBox.setFont(font4)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.tb_aeroRegistradas = QTableWidget(self.groupBox)
        if (self.tb_aeroRegistradas.columnCount() < 4):
            self.tb_aeroRegistradas.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font4);
        __qtablewidgetitem6.setForeground(brush);
        self.tb_aeroRegistradas.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font4);
        __qtablewidgetitem7.setForeground(brush);
        self.tb_aeroRegistradas.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font4);
        __qtablewidgetitem8.setForeground(brush);
        self.tb_aeroRegistradas.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font4);
        __qtablewidgetitem9.setForeground(brush);
        self.tb_aeroRegistradas.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        self.tb_aeroRegistradas.setObjectName(u"tb_aeroRegistradas")
        self.tb_aeroRegistradas.setGeometry(QRect(20, 40, 671, 381))
        font8 = QFont()
        font8.setFamily(u"Open Sans")
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setWeight(50)
        self.tb_aeroRegistradas.setFont(font8)
        #&&
        self.tb_aeroRegistradas.setSelectionBehavior(QAbstractItemView.SelectRows)
        #&&
        self.le_buscarAero = QLineEdit(self.pg_aerolinea)
        self.le_buscarAero.setObjectName(u"le_buscarAero")
        self.le_buscarAero.setGeometry(QRect(130, 20, 351, 31))
        self.le_buscarAero.setFont(font6)
        self.bt_buscarAerolinea = QPushButton(self.pg_aerolinea)
        self.bt_buscarAerolinea.setObjectName(u"bt_buscarAerolinea")
        self.bt_buscarAerolinea.setGeometry(QRect(500, 20, 91, 31))
        self.bt_buscarAerolinea.setFont(font4)
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
        self.bt_buscarAerolinea.setIcon(icon4)
        self.bt_buscarAerolinea.setIconSize(QSize(30, 50))
        self.bt_buscarAerolinea.setFlat(True)
        self.bt_addAerolinea = QPushButton(self.pg_aerolinea)
        self.bt_addAerolinea.setObjectName(u"bt_addAerolinea")
        self.bt_addAerolinea.setGeometry(QRect(20, 530, 171, 31))
        self.bt_addAerolinea.setFont(font4)
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
        icon8 = QIcon()
        icon8.addFile(u"../Ventanas/Icons/agregar-aero.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_addAerolinea.setIcon(icon8)
        self.bt_addAerolinea.setIconSize(QSize(30, 50))
        self.bt_addAerolinea.setFlat(True)
        self.bt_editarAerolinea = QPushButton(self.pg_aerolinea)
        self.bt_editarAerolinea.setObjectName(u"bt_editarAerolinea")
        self.bt_editarAerolinea.setGeometry(QRect(430, 530, 161, 31))
        self.bt_editarAerolinea.setFont(font4)
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
        icon9 = QIcon()
        icon9.addFile(u"../Ventanas/Icons/editar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_editarAerolinea.setIcon(icon9)
        self.bt_editarAerolinea.setIconSize(QSize(30, 50))
        self.bt_editarAerolinea.setFlat(True)
        self.bt_refreshAerolinea = QPushButton(self.pg_aerolinea)
        self.bt_refreshAerolinea.setObjectName(u"bt_refreshAerolinea")
        self.bt_refreshAerolinea.setGeometry(QRect(620, 530, 131, 31))
        self.bt_refreshAerolinea.setFont(font4)
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
        self.bt_refreshAerolinea.setIcon(icon3)
        self.bt_refreshAerolinea.setIconSize(QSize(30, 40))
        self.bt_refreshAerolinea.setFlat(True)
        self.bt_eliminarAerolinea = QPushButton(self.pg_aerolinea)
        self.bt_eliminarAerolinea.setObjectName(u"bt_eliminarAerolinea")
        self.bt_eliminarAerolinea.setGeometry(QRect(230, 530, 171, 31))
        self.bt_eliminarAerolinea.setFont(font4)
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
        icon10 = QIcon()
        icon10.addFile(u"../Ventanas/Icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_eliminarAerolinea.setIcon(icon10)
        self.bt_eliminarAerolinea.setIconSize(QSize(30, 50))
        self.bt_eliminarAerolinea.setFlat(True)
        self.sk_mainWindow.addWidget(self.pg_aerolinea)
        self.pg_agenda = QWidget()
        self.pg_agenda.setObjectName(u"pg_agenda")
        self.groupBox_2 = QGroupBox(self.pg_agenda)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 80, 721, 391))
        self.groupBox_2.setFont(font4)
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
        __qtablewidgetitem10.setFont(font4);
        __qtablewidgetitem10.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font4);
        __qtablewidgetitem11.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font4);
        __qtablewidgetitem12.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font4);
        __qtablewidgetitem13.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font4);
        __qtablewidgetitem14.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font4);
        __qtablewidgetitem15.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font4);
        __qtablewidgetitem16.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font4);
        __qtablewidgetitem17.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(7, __qtablewidgetitem17)
        self.tb_vistaGeneral.setObjectName(u"tb_vistaGeneral")
        self.tb_vistaGeneral.setGeometry(QRect(0, 0, 681, 341))
        self.tb_vistaGeneral.setFont(font5)
        self.tb_vistaGeneral.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 9 pt \"Open Sans\"")
        self.sk_agendaAero.addWidget(self.sk_vistaGeneral)
        self.sk_salida = QWidget()
        self.sk_salida.setObjectName(u"sk_salida")
        self.tb_vistaSalida = QTableWidget(self.sk_salida)
        if (self.tb_vistaSalida.columnCount() < 6):
            self.tb_vistaSalida.setColumnCount(6)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font4);
        __qtablewidgetitem18.setForeground(brush);
        self.tb_vistaSalida.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font4);
        __qtablewidgetitem19.setForeground(brush);
        self.tb_vistaSalida.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font4);
        __qtablewidgetitem20.setForeground(brush);
        self.tb_vistaSalida.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font4);
        __qtablewidgetitem21.setForeground(brush);
        self.tb_vistaSalida.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font4);
        __qtablewidgetitem22.setForeground(brush);
        self.tb_vistaSalida.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font4);
        __qtablewidgetitem23.setForeground(brush);
        self.tb_vistaSalida.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        self.tb_vistaSalida.setObjectName(u"tb_vistaSalida")
        self.tb_vistaSalida.setGeometry(QRect(0, 0, 681, 341))
        self.tb_vistaSalida.setFont(font5)
        self.tb_vistaSalida.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 9 pt \"Open Sans\"")
        self.sk_agendaAero.addWidget(self.sk_salida)
        self.sk_llegada = QWidget()
        self.sk_llegada.setObjectName(u"sk_llegada")
        self.tb_vistaLlegada = QTableWidget(self.sk_llegada)
        if (self.tb_vistaLlegada.columnCount() < 6):
            self.tb_vistaLlegada.setColumnCount(6)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font4);
        __qtablewidgetitem24.setForeground(brush);
        self.tb_vistaLlegada.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font4);
        __qtablewidgetitem25.setForeground(brush);
        self.tb_vistaLlegada.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font4);
        __qtablewidgetitem26.setForeground(brush);
        self.tb_vistaLlegada.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font4);
        __qtablewidgetitem27.setForeground(brush);
        self.tb_vistaLlegada.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font4);
        __qtablewidgetitem28.setForeground(brush);
        self.tb_vistaLlegada.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font4);
        __qtablewidgetitem29.setForeground(brush);
        self.tb_vistaLlegada.setHorizontalHeaderItem(5, __qtablewidgetitem29)
        self.tb_vistaLlegada.setObjectName(u"tb_vistaLlegada")
        self.tb_vistaLlegada.setGeometry(QRect(0, 0, 681, 341))
        self.tb_vistaLlegada.setFont(font5)
        self.tb_vistaLlegada.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 9 pt \"Open Sans\"")
        self.sk_agendaAero.addWidget(self.sk_llegada)
        self.cb_busca_por = QComboBox(self.pg_agenda)
        self.cb_busca_por.setObjectName(u"cb_busca_por")
        self.cb_busca_por.setGeometry(QRect(130, 30, 121, 31))
        self.cb_busca_por.setFont(font6)
        self.label_cerrarsesion_5 = QLabel(self.pg_agenda)
        self.label_cerrarsesion_5.setObjectName(u"label_cerrarsesion_5")
        self.label_cerrarsesion_5.setGeometry(QRect(40, 30, 81, 31))
        self.label_cerrarsesion_5.setFont(font4)
        self.le_buscarAgenda = QLineEdit(self.pg_agenda)
        self.le_buscarAgenda.setObjectName(u"le_buscarAgenda")
        self.le_buscarAgenda.setGeometry(QRect(270, 30, 201, 31))
        self.le_buscarAgenda.setFont(font6)
        self.bt_buscarAgenda = QPushButton(self.pg_agenda)
        self.bt_buscarAgenda.setObjectName(u"bt_buscarAgenda")
        self.bt_buscarAgenda.setGeometry(QRect(490, 30, 91, 31))
        self.bt_buscarAgenda.setFont(font4)
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
        self.bt_buscarAgenda.setIcon(icon4)
        self.bt_buscarAgenda.setIconSize(QSize(30, 50))
        self.bt_buscarAgenda.setFlat(True)
        self.bt_refreshAgenda = QPushButton(self.pg_agenda)
        self.bt_refreshAgenda.setObjectName(u"bt_refreshAgenda")
        self.bt_refreshAgenda.setGeometry(QRect(590, 30, 111, 31))
        self.bt_refreshAgenda.setFont(font4)
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
        self.bt_refreshAgenda.setIcon(icon3)
        self.bt_refreshAgenda.setIconSize(QSize(30, 40))
        self.bt_refreshAgenda.setFlat(True)
        self.label_cerrarsesion_3 = QLabel(self.pg_agenda)
        self.label_cerrarsesion_3.setObjectName(u"label_cerrarsesion_3")
        self.label_cerrarsesion_3.setGeometry(QRect(330, 540, 121, 21))
        font9 = QFont()
        font9.setFamily(u"Nirmala UI")
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_cerrarsesion_3.setFont(font9)
        self.bt_vuelosSalida = QPushButton(self.pg_agenda)
        self.bt_vuelosSalida.setObjectName(u"bt_vuelosSalida")
        self.bt_vuelosSalida.setGeometry(QRect(220, 490, 51, 51))
        self.bt_vuelosSalida.setFont(font9)
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
        icon11 = QIcon()
        icon11.addFile(u"../Ventanas/Icons/Despegue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_vuelosSalida.setIcon(icon11)
        self.bt_vuelosSalida.setIconSize(QSize(50, 61))
        self.bt_vuelosSalida.setFlat(True)
        self.bt_agendarVuelo = QPushButton(self.pg_agenda)
        self.bt_agendarVuelo.setObjectName(u"bt_agendarVuelo")
        self.bt_agendarVuelo.setGeometry(QRect(630, 490, 61, 51))
        self.bt_agendarVuelo.setFont(font9)
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
        icon12 = QIcon()
        icon12.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/agendar_vuelo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_agendarVuelo.setIcon(icon12)
        self.bt_agendarVuelo.setIconSize(QSize(50, 61))
        self.bt_agendarVuelo.setFlat(True)
        self.bt_vuelosLlegada = QPushButton(self.pg_agenda)
        self.bt_vuelosLlegada.setObjectName(u"bt_vuelosLlegada")
        self.bt_vuelosLlegada.setGeometry(QRect(360, 490, 51, 51))
        self.bt_vuelosLlegada.setFont(font9)
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
        icon13 = QIcon()
        icon13.addFile(u"../Ventanas/Icons/Aterrizaje.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_vuelosLlegada.setIcon(icon13)
        self.bt_vuelosLlegada.setIconSize(QSize(50, 61))
        self.bt_vuelosLlegada.setFlat(True)
        self.label_cerrarsesion_4 = QLabel(self.pg_agenda)
        self.label_cerrarsesion_4.setObjectName(u"label_cerrarsesion_4")
        self.label_cerrarsesion_4.setGeometry(QRect(490, 540, 91, 21))
        self.label_cerrarsesion_4.setFont(font9)
        self.bt_infoVuelo = QPushButton(self.pg_agenda)
        self.bt_infoVuelo.setObjectName(u"bt_infoVuelo")
        self.bt_infoVuelo.setGeometry(QRect(510, 490, 51, 51))
        self.bt_infoVuelo.setFont(font9)
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
        icon14 = QIcon()
        icon14.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/Informaci\u00f3n.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_infoVuelo.setIcon(icon14)
        self.bt_infoVuelo.setIconSize(QSize(50, 61))
        self.bt_infoVuelo.setFlat(True)
        self.label_cerrarsesion_17 = QLabel(self.pg_agenda)
        self.label_cerrarsesion_17.setObjectName(u"label_cerrarsesion_17")
        self.label_cerrarsesion_17.setGeometry(QRect(610, 540, 101, 21))
        self.label_cerrarsesion_17.setFont(font9)
        self.label_cerrarsesion_6 = QLabel(self.pg_agenda)
        self.label_cerrarsesion_6.setObjectName(u"label_cerrarsesion_6")
        self.label_cerrarsesion_6.setGeometry(QRect(50, 540, 91, 21))
        self.label_cerrarsesion_6.setFont(font9)
        self.bt_vistaGeneral = QPushButton(self.pg_agenda)
        self.bt_vistaGeneral.setObjectName(u"bt_vistaGeneral")
        self.bt_vistaGeneral.setGeometry(QRect(70, 490, 51, 51))
        self.bt_vistaGeneral.setFont(font9)
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
        icon15 = QIcon()
        icon15.addFile(u"../Ventanas/Icons/Agenda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_vistaGeneral.setIcon(icon15)
        self.bt_vistaGeneral.setIconSize(QSize(50, 61))
        self.bt_vistaGeneral.setFlat(True)
        self.label_cerrarsesion_2 = QLabel(self.pg_agenda)
        self.label_cerrarsesion_2.setObjectName(u"label_cerrarsesion_2")
        self.label_cerrarsesion_2.setGeometry(QRect(190, 540, 111, 21))
        self.label_cerrarsesion_2.setFont(font9)
        self.sk_mainWindow.addWidget(self.pg_agenda)
        self.pg_vuelos = QWidget()
        self.pg_vuelos.setObjectName(u"pg_vuelos")
        self.bt_aviones = QPushButton(self.pg_vuelos)
        self.bt_aviones.setObjectName(u"bt_aviones")
        self.bt_aviones.setGeometry(QRect(210, 530, 131, 41))
        self.bt_aviones.setFont(font4)
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
        icon16 = QIcon()
        icon16.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/agregar_avion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_aviones.setIcon(icon16)
        self.bt_aviones.setIconSize(QSize(40, 50))
        self.bt_aviones.setFlat(True)
        self.bt_vuelos = QPushButton(self.pg_vuelos)
        self.bt_vuelos.setObjectName(u"bt_vuelos")
        self.bt_vuelos.setGeometry(QRect(80, 530, 121, 41))
        self.bt_vuelos.setFont(font4)
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
        icon17 = QIcon()
        icon17.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/vuelo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_vuelos.setIcon(icon17)
        self.bt_vuelos.setIconSize(QSize(40, 50))
        self.bt_vuelos.setFlat(True)
        self.bt_newTrip = QPushButton(self.pg_vuelos)
        self.bt_newTrip.setObjectName(u"bt_newTrip")
        self.bt_newTrip.setGeometry(QRect(370, 530, 181, 41))
        self.bt_newTrip.setFont(font4)
        self.bt_newTrip.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_newTrip.setStyleSheet(u"QPushButton:hover\n"
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
        icon18 = QIcon()
        icon18.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/piloto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_newTrip.setIcon(icon18)
        self.bt_newTrip.setIconSize(QSize(30, 50))
        self.bt_newTrip.setFlat(True)
        self.sw_vuelos_av_trip = QStackedWidget(self.pg_vuelos)
        self.sw_vuelos_av_trip.setObjectName(u"sw_vuelos_av_trip")
        self.sw_vuelos_av_trip.setGeometry(QRect(30, 20, 731, 511))
        self.pg_agendaAerolin = QWidget()
        self.pg_agendaAerolin.setObjectName(u"pg_agendaAerolin")
        self.groupBox_5 = QGroupBox(self.pg_agendaAerolin)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(0, 90, 731, 411))
        self.groupBox_5.setFont(font4)
        self.groupBox_5.setAlignment(Qt.AlignCenter)
        self.tb_vistaAerolinea = QTableWidget(self.groupBox_5)
        if (self.tb_vistaAerolinea.columnCount() < 8):
            self.tb_vistaAerolinea.setColumnCount(8)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font4);
        __qtablewidgetitem30.setForeground(brush);
        self.tb_vistaAerolinea.setHorizontalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font4);
        __qtablewidgetitem31.setForeground(brush);
        self.tb_vistaAerolinea.setHorizontalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font4);
        __qtablewidgetitem32.setForeground(brush);
        self.tb_vistaAerolinea.setHorizontalHeaderItem(2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font4);
        __qtablewidgetitem33.setForeground(brush);
        self.tb_vistaAerolinea.setHorizontalHeaderItem(3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font4);
        __qtablewidgetitem34.setForeground(brush);
        self.tb_vistaAerolinea.setHorizontalHeaderItem(4, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font4);
        __qtablewidgetitem35.setForeground(brush);
        self.tb_vistaAerolinea.setHorizontalHeaderItem(5, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font4);
        __qtablewidgetitem36.setForeground(brush);
        self.tb_vistaAerolinea.setHorizontalHeaderItem(6, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font4);
        __qtablewidgetitem37.setForeground(brush);
        self.tb_vistaAerolinea.setHorizontalHeaderItem(7, __qtablewidgetitem37)
        self.tb_vistaAerolinea.setObjectName(u"tb_vistaAerolinea")
        self.tb_vistaAerolinea.setGeometry(QRect(20, 40, 691, 351))
        self.tb_vistaAerolinea.setFont(font5)
        self.tb_vistaAerolinea.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 9 pt \"Open Sans\"")
        self.cb_busca_por_2 = QComboBox(self.pg_agendaAerolin)
        self.cb_busca_por_2.setObjectName(u"cb_busca_por_2")
        self.cb_busca_por_2.setGeometry(QRect(120, 20, 121, 31))
        self.cb_busca_por_2.setFont(font6)
        self.label_cerrarsesion_20 = QLabel(self.pg_agendaAerolin)
        self.label_cerrarsesion_20.setObjectName(u"label_cerrarsesion_20")
        self.label_cerrarsesion_20.setGeometry(QRect(30, 20, 81, 31))
        self.label_cerrarsesion_20.setFont(font4)
        self.bt_buscarAgenda_2 = QPushButton(self.pg_agendaAerolin)
        self.bt_buscarAgenda_2.setObjectName(u"bt_buscarAgenda_2")
        self.bt_buscarAgenda_2.setGeometry(QRect(480, 20, 91, 31))
        self.bt_buscarAgenda_2.setFont(font4)
        self.bt_buscarAgenda_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_buscarAgenda_2.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_buscarAgenda_2.setIcon(icon4)
        self.bt_buscarAgenda_2.setIconSize(QSize(30, 50))
        self.bt_buscarAgenda_2.setFlat(True)
        self.le_buscarAgenda_2 = QLineEdit(self.pg_agendaAerolin)
        self.le_buscarAgenda_2.setObjectName(u"le_buscarAgenda_2")
        self.le_buscarAgenda_2.setGeometry(QRect(260, 20, 201, 31))
        self.le_buscarAgenda_2.setFont(font6)
        self.bt_refreshAgenda_2 = QPushButton(self.pg_agendaAerolin)
        self.bt_refreshAgenda_2.setObjectName(u"bt_refreshAgenda_2")
        self.bt_refreshAgenda_2.setGeometry(QRect(580, 20, 111, 31))
        self.bt_refreshAgenda_2.setFont(font4)
        self.bt_refreshAgenda_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_refreshAgenda_2.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_refreshAgenda_2.setIcon(icon3)
        self.bt_refreshAgenda_2.setIconSize(QSize(30, 40))
        self.bt_refreshAgenda_2.setFlat(True)
        self.sw_vuelos_av_trip.addWidget(self.pg_agendaAerolin)
        self.pg_agendaPendiente = QWidget()
        self.pg_agendaPendiente.setObjectName(u"pg_agendaPendiente")
        self.groupBox_13 = QGroupBox(self.pg_agendaPendiente)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setGeometry(QRect(0, 30, 731, 411))
        self.groupBox_13.setFont(font4)
        self.groupBox_13.setAlignment(Qt.AlignCenter)
        self.tb_vistaAerolinea_3 = QTableWidget(self.groupBox_13)
        if (self.tb_vistaAerolinea_3.columnCount() < 8):
            self.tb_vistaAerolinea_3.setColumnCount(8)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font4);
        __qtablewidgetitem38.setForeground(brush);
        self.tb_vistaAerolinea_3.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font4);
        __qtablewidgetitem39.setForeground(brush);
        self.tb_vistaAerolinea_3.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font4);
        __qtablewidgetitem40.setForeground(brush);
        self.tb_vistaAerolinea_3.setHorizontalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFont(font4);
        __qtablewidgetitem41.setForeground(brush);
        self.tb_vistaAerolinea_3.setHorizontalHeaderItem(3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFont(font4);
        __qtablewidgetitem42.setForeground(brush);
        self.tb_vistaAerolinea_3.setHorizontalHeaderItem(4, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setFont(font4);
        __qtablewidgetitem43.setForeground(brush);
        self.tb_vistaAerolinea_3.setHorizontalHeaderItem(5, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setFont(font4);
        __qtablewidgetitem44.setForeground(brush);
        self.tb_vistaAerolinea_3.setHorizontalHeaderItem(6, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setFont(font4);
        __qtablewidgetitem45.setForeground(brush);
        self.tb_vistaAerolinea_3.setHorizontalHeaderItem(7, __qtablewidgetitem45)
        self.tb_vistaAerolinea_3.setObjectName(u"tb_vistaAerolinea_3")
        self.tb_vistaAerolinea_3.setGeometry(QRect(20, 40, 691, 351))
        self.tb_vistaAerolinea_3.setFont(font5)
        self.tb_vistaAerolinea_3.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 9 pt \"Open Sans\"")
        self.bt_agregar_avion_2 = QPushButton(self.pg_agendaPendiente)
        self.bt_agregar_avion_2.setObjectName(u"bt_agregar_avion_2")
        self.bt_agregar_avion_2.setGeometry(QRect(320, 460, 141, 31))
        self.bt_agregar_avion_2.setFont(font4)
        self.bt_agregar_avion_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_agregar_avion_2.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_agregar_avion_2.setIconSize(QSize(40, 50))
        self.bt_agregar_avion_2.setFlat(False)
        self.sw_vuelos_av_trip.addWidget(self.pg_agendaPendiente)
        self.pg_newTrip = QWidget()
        self.pg_newTrip.setObjectName(u"pg_newTrip")
        self.lb_NumeroID_2 = QLabel(self.pg_newTrip)
        self.lb_NumeroID_2.setObjectName(u"lb_NumeroID_2")
        self.lb_NumeroID_2.setGeometry(QRect(370, 290, 91, 31))
        font10 = QFont()
        font10.setFamily(u"Nirmala UI")
        font10.setPointSize(9)
        font10.setBold(True)
        font10.setWeight(75)
        self.lb_NumeroID_2.setFont(font10)
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
        self.lb_tipoID.setFont(font10)
        self.lb_codTripulacion = QLabel(self.pg_newTrip)
        self.lb_codTripulacion.setObjectName(u"lb_codTripulacion")
        self.lb_codTripulacion.setGeometry(QRect(80, 110, 141, 31))
        self.lb_codTripulacion.setFont(font10)
        self.lb_NumeroID = QLabel(self.pg_newTrip)
        self.lb_NumeroID.setObjectName(u"lb_NumeroID")
        self.lb_NumeroID.setGeometry(QRect(360, 230, 91, 31))
        self.lb_NumeroID.setFont(font10)
        self.lb_tipoID_2 = QLabel(self.pg_newTrip)
        self.lb_tipoID_2.setObjectName(u"lb_tipoID_2")
        self.lb_tipoID_2.setGeometry(QRect(90, 290, 121, 31))
        self.lb_tipoID_2.setFont(font10)
        self.lb_Nombre = QLabel(self.pg_newTrip)
        self.lb_Nombre.setObjectName(u"lb_Nombre")
        self.lb_Nombre.setGeometry(QRect(80, 170, 81, 31))
        self.lb_Nombre.setFont(font10)
        self.textedit_codTripulacion = QLineEdit(self.pg_newTrip)
        self.textedit_codTripulacion.setObjectName(u"textedit_codTripulacion")
        self.textedit_codTripulacion.setGeometry(QRect(220, 110, 121, 31))
        self.textedit_codTripulacion.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lb_tipoID_3 = QLabel(self.pg_newTrip)
        self.lb_tipoID_3.setObjectName(u"lb_tipoID_3")
        self.lb_tipoID_3.setGeometry(QRect(160, 360, 211, 31))
        self.lb_tipoID_3.setFont(font10)
        self.bt_GuardarTrip_3 = QPushButton(self.pg_newTrip)
        self.bt_GuardarTrip_3.setObjectName(u"bt_GuardarTrip_3")
        self.bt_GuardarTrip_3.setGeometry(QRect(390, 420, 131, 41))
        font11 = QFont()
        font11.setFamily(u"Nirmala UI")
        font11.setPointSize(10)
        font11.setBold(True)
        font11.setItalic(False)
        font11.setWeight(75)
        self.bt_GuardarTrip_3.setFont(font11)
        self.bt_GuardarTrip_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_GuardarTrip_3.setStyleSheet(u"QPushButton\n"
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
        icon19.addFile(u"../Ventanas/Icons/save-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_GuardarTrip_3.setIcon(icon19)
        self.bt_GuardarTrip_3.setIconSize(QSize(40, 50))
        self.bt_GuardarTrip_3.setFlat(True)
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
        self.lb_apellido.setFont(font10)
        self.textedit_Apellido = QLineEdit(self.pg_newTrip)
        self.textedit_Apellido.setObjectName(u"textedit_Apellido")
        self.textedit_Apellido.setGeometry(QRect(460, 170, 161, 31))
        self.textedit_Apellido.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lb_facturanum_5 = QLabel(self.pg_newTrip)
        self.lb_facturanum_5.setObjectName(u"lb_facturanum_5")
        self.lb_facturanum_5.setGeometry(QRect(180, 40, 391, 41))
        self.lb_facturanum_5.setStyleSheet(u"font: 63 26pt \"Open Sans Semibold\";")
        self.bt_AgregarTrip = QPushButton(self.pg_newTrip)
        self.bt_AgregarTrip.setObjectName(u"bt_AgregarTrip")
        self.bt_AgregarTrip.setGeometry(QRect(190, 420, 161, 41))
        self.bt_AgregarTrip.setFont(font11)
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
        icon20 = QIcon()
        icon20.addFile(u"../Ventanas/Icons/agregar_tripulacion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_AgregarTrip.setIcon(icon20)
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
        self.lb_Modelo_2 = QLabel(self.pg_reg_avion)
        self.lb_Modelo_2.setObjectName(u"lb_Modelo_2")
        self.lb_Modelo_2.setGeometry(QRect(380, 190, 61, 31))
        font12 = QFont()
        font12.setFamily(u"Nirmala UI")
        font12.setPointSize(12)
        font12.setBold(False)
        font12.setItalic(False)
        font12.setWeight(9)
        self.lb_Modelo_2.setFont(font12)
        self.lb_Modelo_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_PesoNominal_2 = QLabel(self.pg_reg_avion)
        self.lb_PesoNominal_2.setObjectName(u"lb_PesoNominal_2")
        self.lb_PesoNominal_2.setGeometry(QRect(400, 260, 111, 31))
        self.lb_PesoNominal_2.setFont(font12)
        self.lb_PesoNominal_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
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
        icon21 = QIcon()
        icon21.addFile(u"../Ventanas/Icons/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_checkIDavion.setIcon(icon21)
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
        self.bt_aceptarAVEA.setGeometry(QRect(270, 390, 171, 41))
        self.bt_aceptarAVEA.setFont(font11)
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
        icon22 = QIcon()
        icon22.addFile(u"../Ventanas/Icons/agregar_avion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_aceptarAVEA.setIcon(icon22)
        self.bt_aceptarAVEA.setIconSize(QSize(40, 50))
        self.bt_aceptarAVEA.setFlat(True)
        self.lb_TipodeAvion_2 = QLabel(self.pg_reg_avion)
        self.lb_TipodeAvion_2.setObjectName(u"lb_TipodeAvion_2")
        self.lb_TipodeAvion_2.setGeometry(QRect(380, 120, 111, 31))
        self.lb_TipodeAvion_2.setFont(font12)
        self.lb_TipodeAvion_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Capacidad_2 = QLabel(self.pg_reg_avion)
        self.lb_Capacidad_2.setObjectName(u"lb_Capacidad_2")
        self.lb_Capacidad_2.setGeometry(QRect(140, 260, 81, 31))
        self.lb_Capacidad_2.setFont(font12)
        self.lb_Capacidad_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Motores_2 = QLabel(self.pg_reg_avion)
        self.lb_Motores_2.setObjectName(u"lb_Motores_2")
        self.lb_Motores_2.setGeometry(QRect(280, 260, 71, 31))
        self.lb_Motores_2.setFont(font12)
        self.lb_Motores_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_facturanum_2 = QLabel(self.pg_reg_avion)
        self.lb_facturanum_2.setObjectName(u"lb_facturanum_2")
        self.lb_facturanum_2.setGeometry(QRect(160, 50, 391, 41))
        self.lb_facturanum_2.setStyleSheet(u"font: 63 26pt \"Open Sans Semibold\";")
        self.lineEdit_identificadorEA = QLineEdit(self.pg_reg_avion)
        self.lineEdit_identificadorEA.setObjectName(u"lineEdit_identificadorEA")
        self.lineEdit_identificadorEA.setGeometry(QRect(160, 120, 101, 31))
        self.lineEdit_identificadorEA.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lb_Propulsion_2 = QLabel(self.pg_reg_avion)
        self.lb_Propulsion_2.setObjectName(u"lb_Propulsion_2")
        self.lb_Propulsion_2.setGeometry(QRect(50, 190, 91, 31))
        self.lb_Propulsion_2.setFont(font12)
        self.lb_Propulsion_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.lb_Identificador_5 = QLabel(self.pg_reg_avion)
        self.lb_Identificador_5.setObjectName(u"lb_Identificador_5")
        self.lb_Identificador_5.setGeometry(QRect(150, 140, 101, 31))
        self.lb_Identificador_5.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.cb_pasajerosEA = QComboBox(self.pg_reg_avion)
        self.cb_pasajerosEA.addItem("")
        self.cb_pasajerosEA.addItem("")
        self.cb_pasajerosEA.setObjectName(u"cb_pasajerosEA")
        self.cb_pasajerosEA.setGeometry(QRect(500, 120, 121, 31))
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
        self.lb_Identificador_3 = QLabel(self.pg_reg_avion)
        self.lb_Identificador_3.setObjectName(u"lb_Identificador_3")
        self.lb_Identificador_3.setGeometry(QRect(50, 120, 101, 31))
        self.lb_Identificador_3.setFont(font12)
        self.lb_Identificador_3.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.cb_ModeloRA = QComboBox(self.pg_reg_avion)
        self.cb_ModeloRA.setObjectName(u"cb_ModeloRA")
        self.cb_ModeloRA.setGeometry(QRect(460, 190, 161, 31))
        self.cb_ModeloRA.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_ModeloRA.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 10pt \"Nirmala UI\"")
        self.cb_ModeloRA.setEditable(False)
        self.cb_ModeloRA.setDuplicatesEnabled(False)
        self.cb_ModeloRA.setFrame(True)
        self.sw_reg_ver_avion.addWidget(self.pg_reg_avion)
        self.pg_vista_aviones = QWidget()
        self.pg_vista_aviones.setObjectName(u"pg_vista_aviones")
        self.label_cerrarsesion_21 = QLabel(self.pg_vista_aviones)
        self.label_cerrarsesion_21.setObjectName(u"label_cerrarsesion_21")
        self.label_cerrarsesion_21.setGeometry(QRect(110, 10, 141, 31))
        self.label_cerrarsesion_21.setFont(font10)
        self.groupBox_6 = QGroupBox(self.pg_vista_aviones)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(0, 60, 671, 411))
        self.groupBox_6.setFont(font4)
        self.groupBox_6.setAlignment(Qt.AlignCenter)
        self.tb_avionesregistradosAV = QTableWidget(self.groupBox_6)
        if (self.tb_avionesregistradosAV.columnCount() < 7):
            self.tb_avionesregistradosAV.setColumnCount(7)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setFont(font4);
        __qtablewidgetitem46.setForeground(brush);
        self.tb_avionesregistradosAV.setHorizontalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setFont(font4);
        __qtablewidgetitem47.setForeground(brush);
        self.tb_avionesregistradosAV.setHorizontalHeaderItem(1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setFont(font4);
        __qtablewidgetitem48.setForeground(brush);
        self.tb_avionesregistradosAV.setHorizontalHeaderItem(2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setFont(font4);
        __qtablewidgetitem49.setForeground(brush);
        self.tb_avionesregistradosAV.setHorizontalHeaderItem(3, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setFont(font4);
        __qtablewidgetitem50.setForeground(brush);
        self.tb_avionesregistradosAV.setHorizontalHeaderItem(4, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setFont(font4);
        __qtablewidgetitem51.setForeground(brush);
        self.tb_avionesregistradosAV.setHorizontalHeaderItem(5, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setFont(font4);
        __qtablewidgetitem52.setForeground(brush);
        self.tb_avionesregistradosAV.setHorizontalHeaderItem(6, __qtablewidgetitem52)
        self.tb_avionesregistradosAV.setObjectName(u"tb_avionesregistradosAV")
        self.tb_avionesregistradosAV.setGeometry(QRect(20, 40, 631, 321))
        self.tb_avionesregistradosAV.setFont(font5)
        self.tb_avionesregistradosAV.setStyleSheet(u"color : rgb(0,0,0);\n"
"font: 9 pt \"Open Sans\"")
        self.bt_eliminar_avion = QPushButton(self.groupBox_6)
        self.bt_eliminar_avion.setObjectName(u"bt_eliminar_avion")
        self.bt_eliminar_avion.setGeometry(QRect(370, 370, 111, 31))
        self.bt_eliminar_avion.setFont(font4)
        self.bt_eliminar_avion.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_eliminar_avion.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_eliminar_avion.setIconSize(QSize(40, 50))
        self.bt_eliminar_avion.setFlat(False)
        self.bt_agregar_avion = QPushButton(self.groupBox_6)
        self.bt_agregar_avion.setObjectName(u"bt_agregar_avion")
        self.bt_agregar_avion.setGeometry(QRect(220, 370, 111, 31))
        self.bt_agregar_avion.setFont(font4)
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
        self.bt_buscarVuelo_2 = QPushButton(self.pg_vista_aviones)
        self.bt_buscarVuelo_2.setObjectName(u"bt_buscarVuelo_2")
        self.bt_buscarVuelo_2.setGeometry(QRect(440, 10, 91, 31))
        self.bt_buscarVuelo_2.setFont(font9)
        self.bt_buscarVuelo_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_buscarVuelo_2.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_buscarVuelo_2.setIcon(icon4)
        self.bt_buscarVuelo_2.setIconSize(QSize(30, 50))
        self.bt_buscarVuelo_2.setFlat(True)
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
        self.bt_newTrip_2 = QPushButton(self.pg_vuelos)
        self.bt_newTrip_2.setObjectName(u"bt_newTrip_2")
        self.bt_newTrip_2.setGeometry(QRect(570, 530, 171, 41))
        self.bt_newTrip_2.setFont(font4)
        self.bt_newTrip_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_newTrip_2.setStyleSheet(u"QPushButton:hover\n"
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
        icon23.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/enviar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_newTrip_2.setIcon(icon23)
        self.bt_newTrip_2.setIconSize(QSize(30, 50))
        self.bt_newTrip_2.setFlat(True)
        self.sk_mainWindow.addWidget(self.pg_vuelos)
        self.pg_hangares = QWidget()
        self.pg_hangares.setObjectName(u"pg_hangares")
        self.groupBox_3 = QGroupBox(self.pg_hangares)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 70, 741, 441))
        self.groupBox_3.setFont(font4)
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.tb_hangares = QTableWidget(self.groupBox_3)
        if (self.tb_hangares.columnCount() < 2):
            self.tb_hangares.setColumnCount(2)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setFont(font4);
        __qtablewidgetitem53.setForeground(brush);
        self.tb_hangares.setHorizontalHeaderItem(0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setFont(font4);
        __qtablewidgetitem54.setForeground(brush);
        self.tb_hangares.setHorizontalHeaderItem(1, __qtablewidgetitem54)
        self.tb_hangares.setObjectName(u"tb_hangares")
        self.tb_hangares.setGeometry(QRect(40, 40, 241, 341))
        font13 = QFont()
        font13.setFamily(u"Open Sans")
        font13.setPointSize(10)
        self.tb_hangares.setFont(font13)
        self.tb_hangares.setGridStyle(Qt.SolidLine)
        #&&
        self.tb_hangares.setSelectionBehavior(QAbstractItemView.SelectRows)
        #&&
        self.sw_funcion_hangares = QStackedWidget(self.groupBox_3)
        self.sw_funcion_hangares.setObjectName(u"sw_funcion_hangares")
        self.sw_funcion_hangares.setGeometry(QRect(300, 30, 421, 401))
        font14 = QFont()
        font14.setBold(False)
        font14.setWeight(50)
        self.sw_funcion_hangares.setFont(font14)
        self.pg_hgprincipal = QWidget()
        self.pg_hgprincipal.setObjectName(u"pg_hgprincipal")
        self.label_2 = QLabel(self.pg_hgprincipal)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 30, 291, 261))
        self.label_2.setPixmap(QPixmap(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/image_hangar.png"))
        self.label_2.setScaledContents(True)
        self.label_cerrarsesion_19 = QLabel(self.pg_hgprincipal)
        self.label_cerrarsesion_19.setObjectName(u"label_cerrarsesion_19")
        self.label_cerrarsesion_19.setGeometry(QRect(40, 270, 361, 51))
        self.label_cerrarsesion_19.setFont(font1)
        self.sw_funcion_hangares.addWidget(self.pg_hgprincipal)
        self.pg_registrar_hg = QWidget()
        self.pg_registrar_hg.setObjectName(u"pg_registrar_hg")
        self.lb_Identificador_4 = QLabel(self.pg_registrar_hg)
        self.lb_Identificador_4.setObjectName(u"lb_Identificador_4")
        self.lb_Identificador_4.setGeometry(QRect(80, 200, 111, 31))
        self.lb_Identificador_4.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.textedit_codigoRH = QLineEdit(self.pg_registrar_hg)
        self.textedit_codigoRH.setObjectName(u"textedit_codigoRH")
        self.textedit_codigoRH.setGeometry(QRect(200, 150, 121, 31))
        self.textedit_codigoRH.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.lb_facturanum = QLabel(self.pg_registrar_hg)
        self.lb_facturanum.setObjectName(u"lb_facturanum")
        self.lb_facturanum.setGeometry(QRect(80, 80, 251, 41))
        self.lb_facturanum.setStyleSheet(u"font: 63 26pt \"Open Sans Semibold\";")
        self.lb_Identificador_2 = QLabel(self.pg_registrar_hg)
        self.lb_Identificador_2.setObjectName(u"lb_Identificador_2")
        self.lb_Identificador_2.setGeometry(QRect(80, 150, 101, 31))
        self.lb_Identificador_2.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.textedit_capacidadRH = QLineEdit(self.pg_registrar_hg)
        self.textedit_capacidadRH.setObjectName(u"textedit_capacidadRH")
        self.textedit_capacidadRH.setGeometry(QRect(200, 200, 121, 31))
        self.textedit_capacidadRH.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.bt_guardarHangar = QPushButton(self.pg_registrar_hg)
        self.bt_guardarHangar.setObjectName(u"bt_guardarHangar")
        self.bt_guardarHangar.setGeometry(QRect(140, 270, 121, 41))
        self.bt_guardarHangar.setFont(font11)
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
        icon24 = QIcon()
        icon24.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/save-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_guardarHangar.setIcon(icon24)
        self.bt_guardarHangar.setIconSize(QSize(40, 50))
        self.bt_guardarHangar.setFlat(True)
        self.sw_funcion_hangares.addWidget(self.pg_registrar_hg)
        self.pg_info_hg = QWidget()
        self.pg_info_hg.setObjectName(u"pg_info_hg")
        self.lb_nomHangar = QLabel(self.pg_info_hg)
        self.lb_nomHangar.setObjectName(u"lb_nomHangar")
        self.lb_nomHangar.setGeometry(QRect(100, 10, 231, 41))
        font15 = QFont()
        font15.setFamily(u"Open Sans")
        font15.setPointSize(12)
        self.lb_nomHangar.setFont(font15)
        self.lb_nomHangar.setTextFormat(Qt.RichText)
        self.label_cerrarsesion_12 = QLabel(self.pg_info_hg)
        self.label_cerrarsesion_12.setObjectName(u"label_cerrarsesion_12")
        self.label_cerrarsesion_12.setGeometry(QRect(90, 60, 71, 31))
        self.label_cerrarsesion_12.setFont(font4)
        self.lb_ModelodeAvion = QLabel(self.pg_info_hg)
        self.lb_ModelodeAvion.setObjectName(u"lb_ModelodeAvion")
        self.lb_ModelodeAvion.setGeometry(QRect(60, 90, 131, 31))
        font16 = QFont()
        font16.setFamily(u"Nirmala UI")
        font16.setPointSize(11)
        self.lb_ModelodeAvion.setFont(font16)
        self.label_cerrarsesion_11 = QLabel(self.pg_info_hg)
        self.label_cerrarsesion_11.setObjectName(u"label_cerrarsesion_11")
        self.label_cerrarsesion_11.setGeometry(QRect(230, 60, 101, 31))
        self.label_cerrarsesion_11.setFont(font9)
        self.lb_NombreAerolinea = QLabel(self.pg_info_hg)
        self.lb_NombreAerolinea.setObjectName(u"lb_NombreAerolinea")
        self.lb_NombreAerolinea.setGeometry(QRect(220, 90, 121, 31))
        font17 = QFont()
        font17.setFamily(u"Nirmala UI")
        font17.setPointSize(12)
        self.lb_NombreAerolinea.setFont(font17)
        self.label_cerrarsesion_13 = QLabel(self.pg_info_hg)
        self.label_cerrarsesion_13.setObjectName(u"label_cerrarsesion_13")
        self.label_cerrarsesion_13.setGeometry(QRect(80, 160, 121, 31))
        self.label_cerrarsesion_13.setFont(font10)
        self.lb_fechaEntrada = QLabel(self.pg_info_hg)
        self.lb_fechaEntrada.setObjectName(u"lb_fechaEntrada")
        self.lb_fechaEntrada.setGeometry(QRect(230, 200, 101, 31))
        font18 = QFont()
        font18.setPointSize(12)
        self.lb_fechaEntrada.setFont(font18)
        self.label_cerrarsesion_14 = QLabel(self.pg_info_hg)
        self.label_cerrarsesion_14.setObjectName(u"label_cerrarsesion_14")
        self.label_cerrarsesion_14.setGeometry(QRect(80, 200, 121, 31))
        self.label_cerrarsesion_14.setFont(font10)
        self.lb_HoraEntrada = QLabel(self.pg_info_hg)
        self.lb_HoraEntrada.setObjectName(u"lb_HoraEntrada")
        self.lb_HoraEntrada.setGeometry(QRect(230, 160, 71, 31))
        font19 = QFont()
        font19.setFamily(u"Nirmala UI")
        self.lb_HoraEntrada.setFont(font19)
        self.lb_TiempoenHoras = QLabel(self.pg_info_hg)
        self.lb_TiempoenHoras.setObjectName(u"lb_TiempoenHoras")
        self.lb_TiempoenHoras.setGeometry(QRect(230, 240, 91, 31))
        self.lb_TiempoenHoras.setFont(font16)
        self.label_cerrarsesion_15 = QLabel(self.pg_info_hg)
        self.label_cerrarsesion_15.setObjectName(u"label_cerrarsesion_15")
        self.label_cerrarsesion_15.setGeometry(QRect(140, 240, 61, 31))
        self.label_cerrarsesion_15.setFont(font9)
        self.lb_ValordelaHora = QLabel(self.pg_info_hg)
        self.lb_ValordelaHora.setObjectName(u"lb_ValordelaHora")
        self.lb_ValordelaHora.setGeometry(QRect(230, 280, 71, 31))
        self.lb_ValordelaHora.setFont(font16)
        self.label_cerrarsesion_16 = QLabel(self.pg_info_hg)
        self.label_cerrarsesion_16.setObjectName(u"label_cerrarsesion_16")
        self.label_cerrarsesion_16.setGeometry(QRect(100, 280, 111, 31))
        self.label_cerrarsesion_16.setFont(font4)
        self.line_2 = QFrame(self.pg_info_hg)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 10, 20, 371))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.pg_info_hg)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(380, 10, 20, 371))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.pg_info_hg)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(30, 0, 361, 20))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(self.pg_info_hg)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(30, 40, 361, 20))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_6 = QFrame(self.pg_info_hg)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(30, 130, 361, 20))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.bt_aceptarinfhg = QPushButton(self.pg_info_hg)
        self.bt_aceptarinfhg.setObjectName(u"bt_aceptarinfhg")
        self.bt_aceptarinfhg.setGeometry(QRect(170, 330, 101, 31))
        font20 = QFont()
        font20.setPointSize(11)
        font20.setBold(True)
        font20.setWeight(75)
        self.bt_aceptarinfhg.setFont(font20)
        self.line_7 = QFrame(self.pg_info_hg)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(30, 370, 361, 20))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.sw_funcion_hangares.addWidget(self.pg_info_hg)
        self.bt_eliminarH = QPushButton(self.groupBox_3)
        self.bt_eliminarH.setObjectName(u"bt_eliminarH")
        self.bt_eliminarH.setGeometry(QRect(40, 390, 111, 31))
        self.bt_eliminarH.setFont(font4)
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
        self.bt_agregarH = QPushButton(self.groupBox_3)
        self.bt_agregarH.setObjectName(u"bt_agregarH")
        self.bt_agregarH.setGeometry(QRect(160, 390, 111, 31))
        self.bt_agregarH.setFont(font4)
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
        self.bt_buscarHangar.setFont(font4)
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
        self.bt_buscarHangar.setIcon(icon4)
        self.bt_buscarHangar.setIconSize(QSize(30, 50))
        self.bt_buscarHangar.setFlat(True)
        self.label_cerrarsesion_7 = QLabel(self.pg_hangares)
        self.label_cerrarsesion_7.setObjectName(u"label_cerrarsesion_7")
        self.label_cerrarsesion_7.setGeometry(QRect(190, 20, 141, 31))
        self.label_cerrarsesion_7.setFont(font9)
        self.cb_codHangar = QComboBox(self.pg_hangares)
        self.cb_codHangar.setObjectName(u"cb_codHangar")
        self.cb_codHangar.setGeometry(QRect(340, 20, 131, 31))
        self.bt_detallesHangar = QPushButton(self.pg_hangares)
        self.bt_detallesHangar.setObjectName(u"bt_detallesHangar")
        self.bt_detallesHangar.setGeometry(QRect(90, 520, 111, 41))
        self.bt_detallesHangar.setFont(font4)
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
        icon25 = QIcon()
        icon25.addFile(u"../Ventanas/Icons/Informaci\u00f3n.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_detallesHangar.setIcon(icon25)
        self.bt_detallesHangar.setIconSize(QSize(40, 50))
        self.bt_detallesHangar.setFlat(True)
        self.bt_ocuparHangar = QPushButton(self.pg_hangares)
        self.bt_ocuparHangar.setObjectName(u"bt_ocuparHangar")
        self.bt_ocuparHangar.setGeometry(QRect(230, 520, 121, 41))
        self.bt_ocuparHangar.setFont(font4)
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
        icon26 = QIcon()
        icon26.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/hangar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_ocuparHangar.setIcon(icon26)
        self.bt_ocuparHangar.setIconSize(QSize(40, 50))
        self.bt_ocuparHangar.setFlat(True)
        self.bt_refreshHangar = QPushButton(self.pg_hangares)
        self.bt_refreshHangar.setObjectName(u"bt_refreshHangar")
        self.bt_refreshHangar.setGeometry(QRect(590, 520, 121, 41))
        self.bt_refreshHangar.setFont(font4)
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
        self.bt_refreshHangar.setIcon(icon3)
        self.bt_refreshHangar.setIconSize(QSize(30, 40))
        self.bt_refreshHangar.setFlat(True)
        self.bt_generarReporte = QPushButton(self.pg_hangares)
        self.bt_generarReporte.setObjectName(u"bt_generarReporte")
        self.bt_generarReporte.setGeometry(QRect(380, 520, 171, 41))
        self.bt_generarReporte.setFont(font4)
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
        icon27 = QIcon()
        icon27.addFile(u"../Ventanas/Icons/Facturaci\u00f3n.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_generarReporte.setIcon(icon27)
        self.bt_generarReporte.setIconSize(QSize(40, 50))
        self.bt_generarReporte.setFlat(True)
        self.label_cerrarsesion_18 = QLabel(self.pg_hangares)
        self.label_cerrarsesion_18.setObjectName(u"label_cerrarsesion_18")
        self.label_cerrarsesion_18.setGeometry(QRect(760, 10, 571, 51))
        self.label_cerrarsesion_18.setFont(font1)
        self.sk_mainWindow.addWidget(self.pg_hangares)

        self.retranslateUi(mainWindow)

        self.bt_usuarios.setDefault(False)
        self.bt_Vuelos.setDefault(False)
        self.bt_Aerolineas.setDefault(False)
        self.bt_Hangares.setDefault(False)
        self.bt_CerrarSesion.setDefault(False)
        self.bt_agendaMain.setDefault(False)
        self.sk_mainWindow.setCurrentIndex(0)
        self.sk_agendaAero.setCurrentIndex(0)
        self.sw_vuelos_av_trip.setCurrentIndex(0)
        self.bt_GuardarTrip_3.setDefault(True)
        self.bt_AgregarTrip.setDefault(True)
        self.sw_reg_ver_avion.setCurrentIndex(1)
        self.bt_aceptarAVEA.setDefault(True)
        self.bt_eliminar_avion.setDefault(False)
        self.sw_funcion_hangares.setCurrentIndex(0)
        self.bt_guardarHangar.setDefault(True)
        self.bt_eliminarH.setDefault(False)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Bienvenido - Aeropuerto el Campanero", None))
        self.label_tipousuario.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#1675a3;\">Administrador</span></p></body></html>", None))
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
        self.label_cerrarsesion_8.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#000000;\">Sistema de Gesti\u00f3n Aeropuerto el Campanero</span></p></body></html>", None))
        self.label.setText("")
        self.label_cerrarsesion_9.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#000000;\">BIENVENIDO</span></p></body></html>", None))
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
        self.label_cerrarsesion_10.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Id de Usuario</span></p></body></html>", None))
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
        self.label_cerrarsesion_5.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Buscar por</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.le_buscarAgenda.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.le_buscarAgenda.setInputMask("")
        self.le_buscarAgenda.setText("")
        self.le_buscarAgenda.setPlaceholderText("")
        self.bt_buscarAgenda.setText(QCoreApplication.translate("mainWindow", u"Buscar", None))
        self.bt_refreshAgenda.setText(QCoreApplication.translate("mainWindow", u"Actualizar", None))
        self.label_cerrarsesion_3.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Vuelos de Llegada</span></p></body></html>", None))
        self.bt_vuelosSalida.setText("")
        self.bt_agendarVuelo.setText("")
        self.bt_vuelosLlegada.setText("")
        self.label_cerrarsesion_4.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Info. Vuelo</span></p></body></html>", None))
        self.bt_infoVuelo.setText("")
        self.label_cerrarsesion_17.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Agendar Vuelo</span></p></body></html>", None))
        self.label_cerrarsesion_6.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\">Vista General</p></body></html>", None))
        self.bt_vistaGeneral.setText("")
        self.label_cerrarsesion_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Vuelos de Salida</span></p></body></html>", None))
        self.bt_aviones.setText(QCoreApplication.translate("mainWindow", u"Aviones", None))
        self.bt_vuelos.setText(QCoreApplication.translate("mainWindow", u"Vuelos", None))
        self.bt_newTrip.setText(QCoreApplication.translate("mainWindow", u"Nueva Tripulaci\u00f3n", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("mainWindow", u"Agenda de Aerolinea", None))
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
        self.label_cerrarsesion_20.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Buscar por</span></p></body></html>", None))
        self.bt_buscarAgenda_2.setText(QCoreApplication.translate("mainWindow", u"Buscar", None))
#if QT_CONFIG(tooltip)
        self.le_buscarAgenda_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.le_buscarAgenda_2.setInputMask("")
        self.le_buscarAgenda_2.setText("")
        self.le_buscarAgenda_2.setPlaceholderText("")
        self.bt_refreshAgenda_2.setText(QCoreApplication.translate("mainWindow", u"Actualizar", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("mainWindow", u"Agenda Pendiente por enviar", None))
        ___qtablewidgetitem38 = self.tb_vistaAerolinea_3.horizontalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("mainWindow", u"Fecha", None));
        ___qtablewidgetitem39 = self.tb_vistaAerolinea_3.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("mainWindow", u"Hora", None));
        ___qtablewidgetitem40 = self.tb_vistaAerolinea_3.horizontalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("mainWindow", u"Codigo", None));
        ___qtablewidgetitem41 = self.tb_vistaAerolinea_3.horizontalHeaderItem(3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("mainWindow", u"Tipo", None));
        ___qtablewidgetitem42 = self.tb_vistaAerolinea_3.horizontalHeaderItem(4)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("mainWindow", u"Vuelo", None));
        ___qtablewidgetitem43 = self.tb_vistaAerolinea_3.horizontalHeaderItem(5)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("mainWindow", u"Destino", None));
        ___qtablewidgetitem44 = self.tb_vistaAerolinea_3.horizontalHeaderItem(6)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("mainWindow", u"Origen", None));
        ___qtablewidgetitem45 = self.tb_vistaAerolinea_3.horizontalHeaderItem(7)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("mainWindow", u"Estado", None));
        self.bt_agregar_avion_2.setText(QCoreApplication.translate("mainWindow", u"Enviar agenda", None))
        self.lb_NumeroID_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Licencia</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.lb_tipoID.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Tipo ID</span></p></body></html>", None))
        self.lb_codTripulacion.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Cod Tripulaci\u00f3n</span></p></body></html>", None))
        self.lb_NumeroID.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Numero ID</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.lb_tipoID_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Horas de vuelo</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.lb_Nombre.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Nombre</span></p></body></html>", None))
        self.lb_tipoID_3.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Fecha \u00faltima rev. m\u00e9dica</span></p></body></html>", None))
        self.bt_GuardarTrip_3.setText(QCoreApplication.translate("mainWindow", u"GUARDAR", None))
        self.cb_tipoID.setItemText(0, QCoreApplication.translate("mainWindow", u"C\u00e9dula", None))
        self.cb_tipoID.setItemText(1, QCoreApplication.translate("mainWindow", u"C\u00e9dula Extranjer\u00eda ", None))
        self.cb_tipoID.setItemText(2, QCoreApplication.translate("mainWindow", u"NIT", None))

        self.lb_apellido.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Apellido</span></p></body></html>", None))
        self.lb_facturanum_5.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:400; color:#1675a3;\">Registrar Tripulaci\u00f3n</span></p></body></html>", None))
        self.bt_AgregarTrip.setText(QCoreApplication.translate("mainWindow", u"AGREGAR TRIP.", None))
        self.lb_Modelo_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Modelo</span></p></body></html>", None))
        self.lb_PesoNominal_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Peso Nominal</span></p></body></html>", None))
        self.bt_checkIDavion.setText("")
        self.cb_PropulsionEA.setItemText(0, QCoreApplication.translate("mainWindow", u"Reacci\u00f3n", None))
        self.cb_PropulsionEA.setItemText(1, QCoreApplication.translate("mainWindow", u"Turbo H\u00e9lice", None))
        self.cb_PropulsionEA.setItemText(2, QCoreApplication.translate("mainWindow", u"H\u00e9lice", None))

        self.bt_aceptarAVEA.setText(QCoreApplication.translate("mainWindow", u"GUARDAR AVION", None))
        self.lb_TipodeAvion_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Tipo de Avi\u00f3n</span></p></body></html>", None))
        self.lb_Capacidad_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Capacidad</span></p></body></html>", None))
        self.lb_Motores_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Motores</span></p></body></html>", None))
        self.lb_facturanum_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:400; color:#1675a3;\">Registrar avion</span></p></body></html>", None))
        self.lb_Propulsion_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Propulsi\u00f3n</span></p></body></html>", None))
        self.lb_Identificador_5.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:400; color:#00aa00;\"> </span></p></body></html>", None))
        self.cb_pasajerosEA.setItemText(0, QCoreApplication.translate("mainWindow", u"Pasajeros", None))
        self.cb_pasajerosEA.setItemText(1, QCoreApplication.translate("mainWindow", u"Carga", None))

        self.lb_Identificador_3.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Identificador</span></p></body></html>", None))
        self.label_cerrarsesion_21.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">C\u00f3digo de Avi\u00f3n</span></p></body></html>", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("mainWindow", u"Aviones registrados", None))
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
        self.bt_eliminar_avion.setText(QCoreApplication.translate("mainWindow", u"Eliminar ", None))
        self.bt_agregar_avion.setText(QCoreApplication.translate("mainWindow", u"Agregar", None))
        self.bt_buscarVuelo_2.setText(QCoreApplication.translate("mainWindow", u"Buscar", None))
        self.bt_newTrip_2.setText(QCoreApplication.translate("mainWindow", u"Agenda Pendiente", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("mainWindow", u"Hangares ", None))
        ___qtablewidgetitem53 = self.tb_hangares.horizontalHeaderItem(0)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("mainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem54 = self.tb_hangares.horizontalHeaderItem(1)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("mainWindow", u"Estado", None));
        self.label_2.setText("")
        self.label_cerrarsesion_19.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Sistema de Gesti\u00f3n Aeropuerto el Campanero</span></p></body></html>", None))
        self.lb_Identificador_4.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Capacidad m</span><span style=\" font-weight:600; color:#000000; vertical-align:super;\">2</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.lb_facturanum.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:400; color:#1675a3;\">Registrar de hangares</span></p></body></html>", None))
        self.lb_Identificador_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">C\u00f3digo</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.bt_guardarHangar.setText(QCoreApplication.translate("mainWindow", u"GUARDAR", None))
        self.lb_nomHangar.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#1675a3;\">Hangar</span></p></body></html>", None))
        self.label_cerrarsesion_12.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\">Avi\u00f3n</p></body></html>", None))
        self.lb_ModelodeAvion.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Boeing 747</span></p></body></html>", None))
        self.label_cerrarsesion_11.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Aerol\u00ednea</span></p></body></html>", None))
        self.lb_NombreAerolinea.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#000000;\">Avianca</span></p></body></html>", None))
        self.label_cerrarsesion_13.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Hora de Entrada</span></p></body></html>", None))
        self.lb_fechaEntrada.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">01/01/2021</span></p></body></html>", None))
        self.label_cerrarsesion_14.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Fecha de Entrada</span></p></body></html>", None))
        self.lb_HoraEntrada.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">7:00 PM</span></p></body></html>", None))
        self.lb_TiempoenHoras.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">7 horas</span></p></body></html>", None))
        self.label_cerrarsesion_15.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Tiempo</span></p></body></html>", None))
        self.lb_ValordelaHora.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">$ 30.000</span></p></body></html>", None))
        self.label_cerrarsesion_16.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\">Valor por Hora</p></body></html>", None))
        self.bt_aceptarinfhg.setText(QCoreApplication.translate("mainWindow", u"Aceptar", None))
        self.bt_eliminarH.setText(QCoreApplication.translate("mainWindow", u"Eliminar ", None))
        self.bt_agregarH.setText(QCoreApplication.translate("mainWindow", u"Agregar", None))
        self.bt_buscarHangar.setText(QCoreApplication.translate("mainWindow", u"Buscar", None))
        self.label_cerrarsesion_7.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">C\u00f3digo de Hangar</span></p></body></html>", None))
        self.bt_detallesHangar.setText(QCoreApplication.translate("mainWindow", u"Detalles", None))
        self.bt_ocuparHangar.setText(QCoreApplication.translate("mainWindow", u"Ocupar", None))
        self.bt_refreshHangar.setText(QCoreApplication.translate("mainWindow", u"Actualizar", None))
        self.bt_generarReporte.setText(QCoreApplication.translate("mainWindow", u"Generar Reporte", None))
        self.label_cerrarsesion_18.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#000000;\">Sistema de Gesti\u00f3n Aeropuerto el Campanero</span></p></body></html>", None))
    # retranslateUi

