# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Uniq.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1086, 720)
        MainWindow.setMinimumSize(QSize(1086, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QSize(16777215, 100))
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 0);\n"
"    border-bottom: 1px solid red;\n"
"    \n"
"    /* Gradiente para profundidade */\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, \n"
"        stop: 0.5 #000000,\n"
"        stop: 1 #000000);\n"
"    \n"
"    /* Sombra externa para efeito 3D */\n"
"    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.2),\n"
"                -1px -1px 2px rgba(255, 255, 255, 0.3);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.btn_caixa = QPushButton(self.widget)
        self.btn_caixa.setObjectName(u"btn_caixa")
        self.btn_caixa.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 12px 24px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        self.btn_caixa.setIcon(icon)
        self.btn_caixa.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.btn_caixa)

        self.btn_clientes = QPushButton(self.widget)
        self.btn_clientes.setObjectName(u"btn_clientes")
        self.btn_clientes.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 12px 24px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ContactNew))
        self.btn_clientes.setIcon(icon1)
        self.btn_clientes.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.btn_clientes)

        self.btn_delivery = QPushButton(self.widget)
        self.btn_delivery.setObjectName(u"btn_delivery")
        self.btn_delivery.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 12px 24px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.CallStart))
        self.btn_delivery.setIcon(icon2)
        self.btn_delivery.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.btn_delivery)

        self.btn_mesas = QPushButton(self.widget)
        self.btn_mesas.setObjectName(u"btn_mesas")
        self.btn_mesas.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 12px 24px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderNew))
        self.btn_mesas.setIcon(icon3)
        self.btn_mesas.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.btn_mesas)

        self.btn_produtos = QPushButton(self.widget)
        self.btn_produtos.setObjectName(u"btn_produtos")
        self.btn_produtos.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 12px 24px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.Computer))
        self.btn_produtos.setIcon(icon4)
        self.btn_produtos.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.btn_produtos)

        self.btn_loggout = QPushButton(self.widget)
        self.btn_loggout.setObjectName(u"btn_loggout")
        self.btn_loggout.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 12px 24px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.btn_loggout.setIcon(icon5)
        self.btn_loggout.setIconSize(QSize(35, 35))
        self.btn_loggout.setFlat(False)

        self.horizontalLayout_2.addWidget(self.btn_loggout)


        self.verticalLayout.addWidget(self.widget)

        self.stackedWidget_container = QStackedWidget(self.centralwidget)
        self.stackedWidget_container.setObjectName(u"stackedWidget_container")
        self.Produtos_atuais = QWidget()
        self.Produtos_atuais.setObjectName(u"Produtos_atuais")
        self.horizontalLayout_3 = QHBoxLayout(self.Produtos_atuais)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget = QTableWidget(self.Produtos_atuais)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_3.addWidget(self.tableWidget)

        self.stackedWidget_container.addWidget(self.Produtos_atuais)

        self.verticalLayout.addWidget(self.stackedWidget_container)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMaximumSize(QSize(16777215, 30))
        self.widget_3.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 0);\n"
"    border-top: 1px solid red;\n"
"    \n"
"    /* Gradiente para profundidade */\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, \n"
"        stop: 0.5 #000000,\n"
"        stop: 1 #000000);\n"
"    \n"
"    /* Sombra externa para efeito 3D */\n"
"    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.2),\n"
"                -1px -1px 2px rgba(255, 255, 255, 0.3);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: white;")

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"color: white;")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1086, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_caixa.setText(QCoreApplication.translate("MainWindow", u"Caixa", None))
        self.btn_clientes.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.btn_delivery.setText(QCoreApplication.translate("MainWindow", u"Delivery", None))
        self.btn_mesas.setText(QCoreApplication.translate("MainWindow", u"Mesas", None))
        self.btn_produtos.setText(QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.btn_loggout.setText(QCoreApplication.translate("MainWindow", u"Loggout", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Teste1", None))
    # retranslateUi

