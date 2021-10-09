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
        mainWindow.resize(805, 482)
        icon = QIcon()
        icon.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/Paper-Plane-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.Frameizq_menu = QFrame(mainWindow)
        self.Frameizq_menu.setObjectName(u"Frameizq_menu")
        self.Frameizq_menu.setGeometry(QRect(0, 10, 221, 471))
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
        self.bt_usuarios.setGeometry(QRect(40, 200, 141, 31))
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
        self.bt_Vuelos.setGeometry(QRect(40, 280, 141, 31))
        self.bt_Vuelos.setFont(font1)
        self.bt_Vuelos.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_Vuelos.setStyleSheet(u"color:rgb(22, 117, 163)")
        self.bt_Vuelos.setAutoRepeatDelay(309)
        self.bt_Vuelos.setAutoDefault(False)
        self.bt_Vuelos.setFlat(False)
        self.bt_Aerolineas = QPushButton(self.Frameizq_menu)
        self.bt_Aerolineas.setObjectName(u"bt_Aerolineas")
        self.bt_Aerolineas.setGeometry(QRect(40, 240, 141, 31))
        self.bt_Aerolineas.setFont(font1)
        self.bt_Aerolineas.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_Aerolineas.setStyleSheet(u"color: rgb(22, 117, 163);")
        self.bt_Aerolineas.setAutoRepeatDelay(309)
        self.bt_Aerolineas.setAutoDefault(False)
        self.bt_Aerolineas.setFlat(False)
        self.bt_Hangares = QPushButton(self.Frameizq_menu)
        self.bt_Hangares.setObjectName(u"bt_Hangares")
        self.bt_Hangares.setGeometry(QRect(40, 320, 141, 31))
        self.bt_Hangares.setFont(font1)
        self.bt_Hangares.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_Hangares.setStyleSheet(u"color:rgb(22, 117, 163)\n"
"")
        self.bt_Hangares.setAutoRepeatDelay(309)
        self.bt_Hangares.setAutoDefault(False)
        self.bt_Hangares.setFlat(False)
        self.bt_CerrarSesion = QPushButton(self.Frameizq_menu)
        self.bt_CerrarSesion.setObjectName(u"bt_CerrarSesion")
        self.bt_CerrarSesion.setGeometry(QRect(70, 380, 71, 61))
        font2 = QFont()
        font2.setFamily(u"HoloLens MDL2 Assets")
        font2.setPointSize(16)
        self.bt_CerrarSesion.setFont(font2)
        self.bt_CerrarSesion.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_CerrarSesion.setAcceptDrops(False)
        self.bt_CerrarSesion.setStyleSheet(u"\n"
"border-image: url(:/cct/icono_cerrarsesion.jpg);\n"
"border-image: url(:/cct/BT_cerrarSesion.png);")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/door_outside.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_CerrarSesion.setIcon(icon1)
        self.bt_CerrarSesion.setIconSize(QSize(61, 61))
        self.bt_CerrarSesion.setCheckable(False)
        self.bt_CerrarSesion.setAutoRepeat(False)
        self.bt_CerrarSesion.setAutoExclusive(False)
        self.bt_CerrarSesion.setAutoRepeatDelay(309)
        self.bt_CerrarSesion.setAutoDefault(False)
        self.bt_CerrarSesion.setFlat(True)
        self.label_cerrarsesion = QLabel(self.Frameizq_menu)
        self.label_cerrarsesion.setObjectName(u"label_cerrarsesion")
        self.label_cerrarsesion.setGeometry(QRect(50, 440, 111, 16))
        self.label_cerrarsesion.setFont(font1)
        self.bt_user = QPushButton(self.Frameizq_menu)
        self.bt_user.setObjectName(u"bt_user")
        self.bt_user.setGeometry(QRect(40, 20, 141, 121))
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/persona_.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_user.setIcon(icon2)
        self.bt_user.setIconSize(QSize(131, 121))
        self.bt_user.setFlat(True)
        self.line = QFrame(mainWindow)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(213, 0, 21, 481))
        self.line.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.sk_mainWindow = QStackedWidget(mainWindow)
        self.sk_mainWindow.setObjectName(u"sk_mainWindow")
        self.sk_mainWindow.setGeometry(QRect(240, 10, 551, 461))
        self.pg_bienvenido = QWidget()
        self.pg_bienvenido.setObjectName(u"pg_bienvenido")
        self.label_cerrarsesion_8 = QLabel(self.pg_bienvenido)
        self.label_cerrarsesion_8.setObjectName(u"label_cerrarsesion_8")
        self.label_cerrarsesion_8.setGeometry(QRect(70, 310, 431, 51))
        self.label_cerrarsesion_8.setFont(font1)
        self.label = QLabel(self.pg_bienvenido)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 120, 241, 211))
        self.label.setPixmap(QPixmap(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/Avion.png"))
        self.label.setScaledContents(True)
        self.label_cerrarsesion_9 = QLabel(self.pg_bienvenido)
        self.label_cerrarsesion_9.setObjectName(u"label_cerrarsesion_9")
        self.label_cerrarsesion_9.setGeometry(QRect(180, 100, 181, 31))
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
        self.bt_refreshUsuario.setGeometry(QRect(500, 410, 41, 31))
        font4 = QFont()
        font4.setFamily(u"Nirmala UI")
        font4.setPointSize(9)
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
        icon3.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/recarga.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_refreshUsuario.setIcon(icon3)
        self.bt_refreshUsuario.setIconSize(QSize(30, 40))
        self.bt_refreshUsuario.setFlat(True)
        self.bt_buscarUsuario = QPushButton(self.pg_usuarios)
        self.bt_buscarUsuario.setObjectName(u"bt_buscarUsuario")
        self.bt_buscarUsuario.setGeometry(QRect(390, 20, 91, 31))
        font5 = QFont()
        font5.setFamily(u"Nirmala UI")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.bt_buscarUsuario.setFont(font5)
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
        icon4.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/buscar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_buscarUsuario.setIcon(icon4)
        self.bt_buscarUsuario.setIconSize(QSize(30, 50))
        self.bt_buscarUsuario.setFlat(True)
        self.groupBox_4 = QGroupBox(self.pg_usuarios)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 80, 541, 311))
        font6 = QFont()
        font6.setFamily(u"Nirmala UI")
        font6.setPointSize(11)
        font6.setBold(True)
        font6.setWeight(75)
        self.groupBox_4.setFont(font6)
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.tb_usuarios = QTableWidget(self.groupBox_4)
        self.tb_usuarios.setObjectName(u"tb_usuarios")
        self.tb_usuarios.setGeometry(QRect(20, 40, 501, 251))
        self.tb_usuarios.setFont(font)
        self.tb_usuarios.setGridStyle(Qt.SolidLine)
        self.bt_eliminarUsuario = QPushButton(self.pg_usuarios)
        self.bt_eliminarUsuario.setObjectName(u"bt_eliminarUsuario")
        self.bt_eliminarUsuario.setGeometry(QRect(180, 410, 161, 31))
        self.bt_eliminarUsuario.setFont(font5)
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
        icon5.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/eliminar_usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_eliminarUsuario.setIcon(icon5)
        self.bt_eliminarUsuario.setIconSize(QSize(30, 50))
        self.bt_eliminarUsuario.setFlat(True)
        self.le_buscarUsuario = QLineEdit(self.pg_usuarios)
        self.le_buscarUsuario.setObjectName(u"le_buscarUsuario")
        self.le_buscarUsuario.setGeometry(QRect(160, 20, 211, 31))
        font7 = QFont()
        font7.setFamily(u"Open Sans")
        font7.setPointSize(9)
        self.le_buscarUsuario.setFont(font7)
        self.bt_editarUsuario = QPushButton(self.pg_usuarios)
        self.bt_editarUsuario.setObjectName(u"bt_editarUsuario")
        self.bt_editarUsuario.setGeometry(QRect(350, 410, 141, 31))
        self.bt_editarUsuario.setFont(font5)
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
        icon6.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/editar_usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_editarUsuario.setIcon(icon6)
        self.bt_editarUsuario.setIconSize(QSize(30, 50))
        self.bt_editarUsuario.setFlat(True)
        self.bt_addUsuario = QPushButton(self.pg_usuarios)
        self.bt_addUsuario.setObjectName(u"bt_addUsuario")
        self.bt_addUsuario.setGeometry(QRect(20, 410, 161, 31))
        self.bt_addUsuario.setFont(font5)
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
        icon7.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/nuevo_usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_addUsuario.setIcon(icon7)
        self.bt_addUsuario.setIconSize(QSize(30, 50))
        self.bt_addUsuario.setFlat(True)
        self.label_cerrarsesion_10 = QLabel(self.pg_usuarios)
        self.label_cerrarsesion_10.setObjectName(u"label_cerrarsesion_10")
        self.label_cerrarsesion_10.setGeometry(QRect(40, 20, 101, 31))
        font8 = QFont()
        font8.setFamily(u"Nirmala UI")
        font8.setPointSize(12)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_cerrarsesion_10.setFont(font8)
        self.sk_mainWindow.addWidget(self.pg_usuarios)
        self.pg_aerolinea = QWidget()
        self.pg_aerolinea.setObjectName(u"pg_aerolinea")
        self.groupBox = QGroupBox(self.pg_aerolinea)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 80, 541, 311))
        self.groupBox.setFont(font6)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.tb_aeroRegistradas = QTableWidget(self.groupBox)
        if (self.tb_aeroRegistradas.columnCount() < 4):
            self.tb_aeroRegistradas.setColumnCount(4)
        brush = QBrush(QColor(22, 117, 163, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font6);
        __qtablewidgetitem.setForeground(brush);
        self.tb_aeroRegistradas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font6);
        __qtablewidgetitem1.setForeground(brush);
        self.tb_aeroRegistradas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font6);
        __qtablewidgetitem2.setForeground(brush);
        self.tb_aeroRegistradas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font6);
        __qtablewidgetitem3.setForeground(brush);
        self.tb_aeroRegistradas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tb_aeroRegistradas.setObjectName(u"tb_aeroRegistradas")
        self.tb_aeroRegistradas.setGeometry(QRect(10, 30, 521, 271))
        font9 = QFont()
        font9.setFamily(u"Open Sans")
        font9.setPointSize(10)
        font9.setBold(False)
        font9.setWeight(50)
        self.tb_aeroRegistradas.setFont(font9)
        self.tb_aeroRegistradas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.le_buscarAero = QLineEdit(self.pg_aerolinea)
        self.le_buscarAero.setObjectName(u"le_buscarAero")
        self.le_buscarAero.setGeometry(QRect(50, 20, 351, 31))
        self.le_buscarAero.setFont(font7)
        self.bt_buscarAerolinea = QPushButton(self.pg_aerolinea)
        self.bt_buscarAerolinea.setObjectName(u"bt_buscarAerolinea")
        self.bt_buscarAerolinea.setGeometry(QRect(400, 20, 91, 31))
        self.bt_buscarAerolinea.setFont(font5)
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
        self.bt_addAerolinea.setGeometry(QRect(20, 410, 161, 31))
        self.bt_addAerolinea.setFont(font5)
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
        icon8.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/agregar-aero.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_addAerolinea.setIcon(icon8)
        self.bt_addAerolinea.setIconSize(QSize(30, 50))
        self.bt_addAerolinea.setFlat(True)
        self.bt_editarAerolinea = QPushButton(self.pg_aerolinea)
        self.bt_editarAerolinea.setObjectName(u"bt_editarAerolinea")
        self.bt_editarAerolinea.setGeometry(QRect(350, 410, 141, 31))
        self.bt_editarAerolinea.setFont(font5)
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
        icon9.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/editar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_editarAerolinea.setIcon(icon9)
        self.bt_editarAerolinea.setIconSize(QSize(30, 50))
        self.bt_editarAerolinea.setFlat(True)
        self.bt_refreshAerolinea = QPushButton(self.pg_aerolinea)
        self.bt_refreshAerolinea.setObjectName(u"bt_refreshAerolinea")
        self.bt_refreshAerolinea.setGeometry(QRect(500, 410, 41, 31))
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
        self.bt_eliminarAerolinea.setGeometry(QRect(180, 410, 161, 31))
        self.bt_eliminarAerolinea.setFont(font5)
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
        icon10.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_eliminarAerolinea.setIcon(icon10)
        self.bt_eliminarAerolinea.setIconSize(QSize(30, 50))
        self.bt_eliminarAerolinea.setFlat(True)
        self.sk_mainWindow.addWidget(self.pg_aerolinea)
        self.pg_vuelos = QWidget()
        self.pg_vuelos.setObjectName(u"pg_vuelos")
        self.groupBox_2 = QGroupBox(self.pg_vuelos)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 80, 541, 291))
        self.groupBox_2.setFont(font6)
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.sk_agendaAero = QStackedWidget(self.groupBox_2)
        self.sk_agendaAero.setObjectName(u"sk_agendaAero")
        self.sk_agendaAero.setGeometry(QRect(20, 30, 501, 241))
        self.sk_vistaGeneral = QWidget()
        self.sk_vistaGeneral.setObjectName(u"sk_vistaGeneral")
        self.tb_vistaGeneral = QTableWidget(self.sk_vistaGeneral)
        if (self.tb_vistaGeneral.columnCount() < 11):
            self.tb_vistaGeneral.setColumnCount(11)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font6);
        __qtablewidgetitem4.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font6);
        __qtablewidgetitem5.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font6);
        __qtablewidgetitem6.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font6);
        __qtablewidgetitem7.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font6);
        __qtablewidgetitem8.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font6);
        __qtablewidgetitem9.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font6);
        __qtablewidgetitem10.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font6);
        __qtablewidgetitem11.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font6);
        __qtablewidgetitem12.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font6);
        __qtablewidgetitem13.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font6);
        __qtablewidgetitem14.setForeground(brush);
        self.tb_vistaGeneral.setHorizontalHeaderItem(10, __qtablewidgetitem14)
        self.tb_vistaGeneral.setObjectName(u"tb_vistaGeneral")
        self.tb_vistaGeneral.setGeometry(QRect(10, 0, 491, 241))
        font10 = QFont()
        font10.setFamily(u"Open Sans")
        font10.setPointSize(10)
        font10.setBold(False)
        font10.setItalic(False)
        font10.setWeight(50)
        self.tb_vistaGeneral.setFont(font10)
        self.tb_vistaGeneral.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.sk_agendaAero.addWidget(self.sk_vistaGeneral)
        self.sk_salida = QWidget()
        self.sk_salida.setObjectName(u"sk_salida")
        self.tb_vuelosSalida = QTableWidget(self.sk_salida)
        self.tb_vuelosSalida.setObjectName(u"tb_vuelosSalida")
        self.tb_vuelosSalida.setGeometry(QRect(0, 0, 501, 241))
        self.sk_agendaAero.addWidget(self.sk_salida)
        self.sk_llegada = QWidget()
        self.sk_llegada.setObjectName(u"sk_llegada")
        self.tb_vuelosLlegada = QTableWidget(self.sk_llegada)
        self.tb_vuelosLlegada.setObjectName(u"tb_vuelosLlegada")
        self.tb_vuelosLlegada.setGeometry(QRect(0, 0, 501, 241))
        self.sk_agendaAero.addWidget(self.sk_llegada)
        self.label_cerrarsesion_4 = QLabel(self.pg_vuelos)
        self.label_cerrarsesion_4.setObjectName(u"label_cerrarsesion_4")
        self.label_cerrarsesion_4.setGeometry(QRect(400, 430, 121, 21))
        self.label_cerrarsesion_4.setFont(font4)
        self.bt_editarAgenda = QPushButton(self.pg_vuelos)
        self.bt_editarAgenda.setObjectName(u"bt_editarAgenda")
        self.bt_editarAgenda.setGeometry(QRect(430, 380, 51, 51))
        self.bt_editarAgenda.setFont(font5)
        self.bt_editarAgenda.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_editarAgenda.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_editarAgenda.setIcon(icon9)
        self.bt_editarAgenda.setIconSize(QSize(50, 61))
        self.bt_editarAgenda.setFlat(True)
        self.bt_vuelosSalida = QPushButton(self.pg_vuelos)
        self.bt_vuelosSalida.setObjectName(u"bt_vuelosSalida")
        self.bt_vuelosSalida.setGeometry(QRect(170, 380, 51, 51))
        self.bt_vuelosSalida.setFont(font5)
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
        icon11.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/Despegue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_vuelosSalida.setIcon(icon11)
        self.bt_vuelosSalida.setIconSize(QSize(50, 61))
        self.bt_vuelosSalida.setFlat(True)
        self.bt_vuelosLlegada = QPushButton(self.pg_vuelos)
        self.bt_vuelosLlegada.setObjectName(u"bt_vuelosLlegada")
        self.bt_vuelosLlegada.setGeometry(QRect(300, 380, 51, 51))
        self.bt_vuelosLlegada.setFont(font5)
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
        icon12 = QIcon()
        icon12.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/Aterrizaje.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_vuelosLlegada.setIcon(icon12)
        self.bt_vuelosLlegada.setIconSize(QSize(50, 61))
        self.bt_vuelosLlegada.setFlat(True)
        self.label_cerrarsesion_3 = QLabel(self.pg_vuelos)
        self.label_cerrarsesion_3.setObjectName(u"label_cerrarsesion_3")
        self.label_cerrarsesion_3.setGeometry(QRect(270, 430, 121, 21))
        self.label_cerrarsesion_3.setFont(font4)
        self.label_cerrarsesion_2 = QLabel(self.pg_vuelos)
        self.label_cerrarsesion_2.setObjectName(u"label_cerrarsesion_2")
        self.label_cerrarsesion_2.setGeometry(QRect(140, 430, 111, 21))
        self.label_cerrarsesion_2.setFont(font4)
        self.cb_busca_por = QComboBox(self.pg_vuelos)
        self.cb_busca_por.setObjectName(u"cb_busca_por")
        self.cb_busca_por.setGeometry(QRect(10, 30, 121, 31))
        self.cb_busca_por.setFont(font7)
        self.label_cerrarsesion_5 = QLabel(self.pg_vuelos)
        self.label_cerrarsesion_5.setObjectName(u"label_cerrarsesion_5")
        self.label_cerrarsesion_5.setGeometry(QRect(0, 10, 81, 21))
        self.label_cerrarsesion_5.setFont(font5)
        self.le_buscarAgenda = QLineEdit(self.pg_vuelos)
        self.le_buscarAgenda.setObjectName(u"le_buscarAgenda")
        self.le_buscarAgenda.setGeometry(QRect(140, 30, 181, 31))
        self.le_buscarAgenda.setFont(font7)
        self.bt_buscarAgenda = QPushButton(self.pg_vuelos)
        self.bt_buscarAgenda.setObjectName(u"bt_buscarAgenda")
        self.bt_buscarAgenda.setGeometry(QRect(320, 30, 91, 31))
        self.bt_buscarAgenda.setFont(font5)
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
        self.bt_refreshAgenda = QPushButton(self.pg_vuelos)
        self.bt_refreshAgenda.setObjectName(u"bt_refreshAgenda")
        self.bt_refreshAgenda.setGeometry(QRect(420, 30, 111, 31))
        self.bt_refreshAgenda.setFont(font5)
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
        self.label_cerrarsesion_6 = QLabel(self.pg_vuelos)
        self.label_cerrarsesion_6.setObjectName(u"label_cerrarsesion_6")
        self.label_cerrarsesion_6.setGeometry(QRect(30, 430, 91, 21))
        self.label_cerrarsesion_6.setFont(font4)
        self.bt_vistaGeneral = QPushButton(self.pg_vuelos)
        self.bt_vistaGeneral.setObjectName(u"bt_vistaGeneral")
        self.bt_vistaGeneral.setGeometry(QRect(50, 380, 51, 51))
        self.bt_vistaGeneral.setFont(font5)
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
        icon13.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/Agenda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_vistaGeneral.setIcon(icon13)
        self.bt_vistaGeneral.setIconSize(QSize(50, 61))
        self.bt_vistaGeneral.setFlat(True)
        self.sk_mainWindow.addWidget(self.pg_vuelos)
        self.pg_hangares = QWidget()
        self.pg_hangares.setObjectName(u"pg_hangares")
        self.groupBox_3 = QGroupBox(self.pg_hangares)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 70, 541, 321))
        self.groupBox_3.setFont(font6)
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.tb_hangares = QTableWidget(self.groupBox_3)
        if (self.tb_hangares.columnCount() < 2):
            self.tb_hangares.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font6);
        __qtablewidgetitem4.setForeground(brush);
        self.tb_hangares.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font6);
        __qtablewidgetitem5.setForeground(brush);
        self.tb_hangares.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.tb_hangares.setObjectName(u"tb_hangares")
        self.tb_hangares.setGeometry(QRect(20, 30, 231, 271))
        font10 = QFont()
        font10.setFamily(u"Open Sans")
        font10.setPointSize(10)
        self.tb_hangares.setFont(font10)
        self.tb_hangares.setGridStyle(Qt.SolidLine)
        self.tb_hangares.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.stackedWidget = QStackedWidget(self.groupBox_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(260, 20, 271, 291))
        font11 = QFont()
        font11.setBold(False)
        font11.setWeight(50)
        self.stackedWidget.setFont(font11)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.lb_nomHangar = QLabel(self.page_2)
        self.lb_nomHangar.setObjectName(u"lb_nomHangar")
        self.lb_nomHangar.setGeometry(QRect(20, 10, 231, 31))
        font12 = QFont()
        font12.setFamily(u"Open Sans")
        font12.setPointSize(12)
        self.lb_nomHangar.setFont(font12)
        self.lb_nomHangar.setTextFormat(Qt.RichText)
        self.label_cerrarsesion_12 = QLabel(self.page_2)
        self.label_cerrarsesion_12.setObjectName(u"label_cerrarsesion_12")
        self.label_cerrarsesion_12.setGeometry(QRect(50, 50, 61, 31))
        self.label_cerrarsesion_12.setFont(font5)
        self.lb_ModelodeAvion = QLabel(self.page_2)
        self.lb_ModelodeAvion.setObjectName(u"lb_ModelodeAvion")
        self.lb_ModelodeAvion.setGeometry(QRect(10, 70, 131, 31))
        font13 = QFont()
        font13.setFamily(u"Nirmala UI")
        font13.setPointSize(10)
        self.lb_ModelodeAvion.setFont(font13)
        self.label_cerrarsesion_11 = QLabel(self.page_2)
        self.label_cerrarsesion_11.setObjectName(u"label_cerrarsesion_11")
        self.label_cerrarsesion_11.setGeometry(QRect(160, 50, 61, 31))
        self.label_cerrarsesion_11.setFont(font4)
        self.lb_NombreAerolinea = QLabel(self.page_2)
        self.lb_NombreAerolinea.setObjectName(u"lb_NombreAerolinea")
        self.lb_NombreAerolinea.setGeometry(QRect(130, 70, 121, 31))
        font14 = QFont()
        font14.setFamily(u"Nirmala UI")
        font14.setPointSize(11)
        self.lb_NombreAerolinea.setFont(font14)
        self.label_cerrarsesion_13 = QLabel(self.page_2)
        self.label_cerrarsesion_13.setObjectName(u"label_cerrarsesion_13")
        self.label_cerrarsesion_13.setGeometry(QRect(20, 110, 111, 31))
        self.label_cerrarsesion_13.setFont(font4)
        self.lb_fechaEntrada = QLabel(self.page_2)
        self.lb_fechaEntrada.setObjectName(u"lb_fechaEntrada")
        self.lb_fechaEntrada.setGeometry(QRect(150, 140, 101, 31))
        self.label_cerrarsesion_14 = QLabel(self.page_2)
        self.label_cerrarsesion_14.setObjectName(u"label_cerrarsesion_14")
        self.label_cerrarsesion_14.setGeometry(QRect(20, 140, 111, 31))
        self.label_cerrarsesion_14.setFont(font4)
        self.lb_HoraEntrada = QLabel(self.page_2)
        self.lb_HoraEntrada.setObjectName(u"lb_HoraEntrada")
        self.lb_HoraEntrada.setGeometry(QRect(150, 110, 71, 31))
        font15 = QFont()
        font15.setFamily(u"Nirmala UI")
        self.lb_HoraEntrada.setFont(font15)
        self.lb_TiempoenHoras = QLabel(self.page_2)
        self.lb_TiempoenHoras.setObjectName(u"lb_TiempoenHoras")
        self.lb_TiempoenHoras.setGeometry(QRect(150, 170, 91, 31))
        self.lb_TiempoenHoras.setFont(font13)
        self.label_cerrarsesion_15 = QLabel(self.page_2)
        self.label_cerrarsesion_15.setObjectName(u"label_cerrarsesion_15")
        self.label_cerrarsesion_15.setGeometry(QRect(80, 170, 51, 31))
        self.label_cerrarsesion_15.setFont(font4)
        self.lb_ValordelaHora = QLabel(self.page_2)
        self.lb_ValordelaHora.setObjectName(u"lb_ValordelaHora")
        self.lb_ValordelaHora.setGeometry(QRect(150, 200, 71, 31))
        self.lb_ValordelaHora.setFont(font13)
        self.label_cerrarsesion_16 = QLabel(self.page_2)
        self.label_cerrarsesion_16.setObjectName(u"label_cerrarsesion_16")
        self.label_cerrarsesion_16.setGeometry(QRect(40, 200, 91, 31))
        self.label_cerrarsesion_16.setFont(font4)
        self.line_2 = QFrame(self.page_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(-7, 10, 20, 271))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.page_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(250, 10, 20, 271))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.page_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(0, 0, 261, 16))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(self.page_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(0, 40, 261, 16))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_6 = QFrame(self.page_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(0, 100, 261, 16))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.bt_aceptarinfhg = QPushButton(self.page_2)
        self.bt_aceptarinfhg.setObjectName(u"bt_aceptarinfhg")
        self.bt_aceptarinfhg.setGeometry(QRect(100, 240, 81, 21))
        font16 = QFont()
        font16.setPointSize(10)
        font16.setBold(True)
        font16.setWeight(75)
        self.bt_aceptarinfhg.setFont(font16)
        self.line_7 = QFrame(self.page_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(0, 270, 261, 16))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.stackedWidget.addWidget(self.page_2)
        self.bt_buscarHangar = QPushButton(self.pg_hangares)
        self.bt_buscarHangar.setObjectName(u"bt_buscarHangar")
        self.bt_buscarHangar.setGeometry(QRect(330, 20, 91, 31))
        self.bt_buscarHangar.setFont(font5)
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
        self.label_cerrarsesion_7.setGeometry(QRect(40, 20, 141, 31))
        self.label_cerrarsesion_7.setFont(font4)
        self.cb_codHangar = QComboBox(self.pg_hangares)
        self.cb_codHangar.setObjectName(u"cb_codHangar")
        self.cb_codHangar.setGeometry(QRect(190, 20, 131, 31))
        self.bt_detallesHangar = QPushButton(self.pg_hangares)
        self.bt_detallesHangar.setObjectName(u"bt_detallesHangar")
        self.bt_detallesHangar.setGeometry(QRect(20, 400, 111, 41))
        self.bt_detallesHangar.setFont(font5)
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
        icon14 = QIcon()
        icon14.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/Información.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_detallesHangar.setIcon(icon14)
        self.bt_detallesHangar.setIconSize(QSize(40, 50))
        self.bt_detallesHangar.setFlat(True)
        self.bt_editaInforHangar = QPushButton(self.pg_hangares)
        self.bt_editaInforHangar.setObjectName(u"bt_editaInforHangar")
        self.bt_editaInforHangar.setGeometry(QRect(420, 400, 121, 41))
        self.bt_editaInforHangar.setFont(font5)
        self.bt_editaInforHangar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_editaInforHangar.setStyleSheet(u"QPushButton:hover\n"
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
        self.bt_editaInforHangar.setIcon(icon9)
        self.bt_editaInforHangar.setIconSize(QSize(40, 50))
        self.bt_editaInforHangar.setFlat(True)
        self.bt_ocuparHangar = QPushButton(self.pg_hangares)
        self.bt_ocuparHangar.setObjectName(u"bt_ocuparHangar")
        self.bt_ocuparHangar.setGeometry(QRect(130, 400, 121, 41))
        self.bt_ocuparHangar.setFont(font5)
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
        icon15 = QIcon()
        icon15.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/Ocupar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_ocuparHangar.setIcon(icon15)
        self.bt_ocuparHangar.setIconSize(QSize(40, 50))
        self.bt_ocuparHangar.setFlat(True)
        self.bt_refreshHangar = QPushButton(self.pg_hangares)
        self.bt_refreshHangar.setObjectName(u"bt_refreshHangar")
        self.bt_refreshHangar.setGeometry(QRect(420, 20, 111, 31))
        self.bt_refreshHangar.setFont(font5)
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
        self.bt_generarReporte.setGeometry(QRect(250, 400, 161, 41))
        self.bt_generarReporte.setFont(font5)
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
        icon16 = QIcon()
        icon16.addFile(u"C:/Users/Sofia/OneDrive/Proyecto-El Campanero/Backend/Ventanas/Icons/Facturación.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_generarReporte.setIcon(icon16)
        self.bt_generarReporte.setIconSize(QSize(40, 50))
        self.bt_generarReporte.setFlat(True)
        self.sk_mainWindow.addWidget(self.pg_hangares)

        self.retranslateUi(mainWindow)

        self.bt_usuarios.setDefault(False)
        self.bt_Vuelos.setDefault(False)
        self.bt_Aerolineas.setDefault(False)
        self.bt_Hangares.setDefault(False)
        self.bt_CerrarSesion.setDefault(False)
        self.sk_mainWindow.setCurrentIndex(0)
        self.sk_agendaAero.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


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
        self.label_cerrarsesion_8.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#000000;\">Sistema de Gesti\u00f3n Aeropuerto el Campanero</span></p></body></html>", None))
        self.label.setText("")
        self.label_cerrarsesion_9.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#000000;\">BIENVENIDO</span></p></body></html>", None))
        self.bt_refreshUsuario.setText("")
        self.bt_buscarUsuario.setText(QCoreApplication.translate("mainWindow", u"Buscar", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("mainWindow", u"Usuarios Registradas", None))
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
        ___qtablewidgetitem = self.tb_aeroRegistradas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mainWindow", u"NIT", None));
        ___qtablewidgetitem1 = self.tb_aeroRegistradas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mainWindow", u"Nombre Aerol\u00ednea", None));
        ___qtablewidgetitem2 = self.tb_aeroRegistradas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("mainWindow", u"Correo ", None));
        ___qtablewidgetitem3 = self.tb_aeroRegistradas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("mainWindow", u"Tel\u00e9fono", None));
#if QT_CONFIG(tooltip)
        self.le_buscarAero.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.le_buscarAero.setInputMask("")
        self.le_buscarAero.setText("")
        self.le_buscarAero.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Ingrese el nombre de su aerolinea", None))
        self.bt_buscarAerolinea.setText(QCoreApplication.translate("mainWindow", u"Buscar", None))
        self.bt_addAerolinea.setText(QCoreApplication.translate("mainWindow", u"Agregar Aerol\u00ednea ", None))
        self.bt_editarAerolinea.setText(QCoreApplication.translate("mainWindow", u"Editar Aerol\u00ednea", None))
        self.bt_refreshAerolinea.setText("")
        self.bt_eliminarAerolinea.setText(QCoreApplication.translate("mainWindow", u"Eliminar Aerol\u00ednea", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("mainWindow", u"Agenda del D\u00eda", None))
        ___qtablewidgetitem4 = self.tb_vistaGeneral.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("mainWindow", u"Codigo", None));
        ___qtablewidgetitem5 = self.tb_vistaGeneral.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("mainWindow", u"Tipo", None));
        ___qtablewidgetitem6 = self.tb_vistaGeneral.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("mainWindow", u"Vuelo", None));
        ___qtablewidgetitem7 = self.tb_vistaGeneral.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("mainWindow", u"Destino", None));
        ___qtablewidgetitem8 = self.tb_vistaGeneral.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("mainWindow", u"Origen", None));
        ___qtablewidgetitem9 = self.tb_vistaGeneral.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("mainWindow", u"Fecha", None));
        ___qtablewidgetitem10 = self.tb_vistaGeneral.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("mainWindow", u"Hora", None));
        ___qtablewidgetitem11 = self.tb_vistaGeneral.horizontalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("mainWindow", u"Avi\u00f3n", None));
        ___qtablewidgetitem12 = self.tb_vistaGeneral.horizontalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("mainWindow", u"Aerolinea", None));
        ___qtablewidgetitem13 = self.tb_vistaGeneral.horizontalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("mainWindow", u"Piloto", None));
        ___qtablewidgetitem14 = self.tb_vistaGeneral.horizontalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("mainWindow", u"Copiloto", None));
        self.label_cerrarsesion_4.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Editar Agenda</span></p></body></html>", None))
        self.bt_editarAgenda.setText("")
        self.bt_vuelosSalida.setText("")
        self.bt_vuelosLlegada.setText("")
        self.label_cerrarsesion_3.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Vuelos de Llegada</span></p></body></html>", None))
        self.label_cerrarsesion_2.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Vuelos de Salida</span></p></body></html>", None))
        self.label_cerrarsesion_5.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Buscar por</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.le_buscarAgenda.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.le_buscarAgenda.setInputMask("")
        self.le_buscarAgenda.setText("")
        self.le_buscarAgenda.setPlaceholderText("")
        self.bt_buscarAgenda.setText(QCoreApplication.translate("mainWindow", u"Buscar", None))
        self.bt_refreshAgenda.setText(QCoreApplication.translate("mainWindow", u"Actualizar", None))
        self.label_cerrarsesion_6.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\">Vista General</p></body></html>", None))
        self.bt_vistaGeneral.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("mainWindow", u"Hangares ", None))
        ___qtablewidgetitem4 = self.tb_hangares.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("mainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem5 = self.tb_hangares.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("mainWindow", u"Estado", None));
        self.lb_nomHangar.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#1675a3;\">Hangar</span></p></body></html>", None))
        self.label_cerrarsesion_12.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\">Avi\u00f3n</p></body></html>", None))
        self.lb_ModelodeAvion.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Boeing 747</span></p></body></html>", None))
        self.label_cerrarsesion_11.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Aerol\u00ednea</span></p></body></html>", None))
        self.lb_NombreAerolinea.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#000000;\">Avianca</span></p></body></html>", None))
        self.label_cerrarsesion_13.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Hora de Entrada</span></p></body></html>", None))
        self.lb_fechaEntrada.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">01/01/2021</span></p></body></html>", None))
        self.label_cerrarsesion_14.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Fecha de Entrada</span></p></body></html>", None))
        self.lb_HoraEntrada.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">7:00 PM</span></p></body></html>", None))
        self.lb_TiempoenHoras.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">7 horas</span></p></body></html>", None))
        self.label_cerrarsesion_15.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Tiempo</span></p></body></html>", None))
        self.lb_ValordelaHora.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">$ 30.000</span></p></body></html>", None))
        self.label_cerrarsesion_16.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Valor por Hora</span></p></body></html>", None))
        self.bt_aceptarinfhg.setText(QCoreApplication.translate("mainWindow", u"Aceptar", None))
        self.bt_buscarHangar.setText(QCoreApplication.translate("mainWindow", u"Buscar", None))
        self.label_cerrarsesion_7.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">C\u00f3digo de Hangar</span></p></body></html>", None))
        self.bt_detallesHangar.setText(QCoreApplication.translate("mainWindow", u"Detalles", None))
        self.bt_editaInforHangar.setText(QCoreApplication.translate("mainWindow", u"Editar Inf", None))
        self.bt_ocuparHangar.setText(QCoreApplication.translate("mainWindow", u"Ocupar", None))
        self.bt_refreshHangar.setText(QCoreApplication.translate("mainWindow", u"Actualizar", None))
        self.bt_generarReporte.setText(QCoreApplication.translate("mainWindow", u"Generar Reporte", None))
    # retranslateUi

