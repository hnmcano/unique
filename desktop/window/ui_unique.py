# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'unique.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
from pictures import imagens_rc

class Ui_Unique(object):
    def setupUi(self, Unique):
        if not Unique.objectName():
            Unique.setObjectName(u"Unique")
        Unique.setWindowModality(Qt.WindowModality.ApplicationModal)
        Unique.resize(1086, 720)
        Unique.setMinimumSize(QSize(1086, 720))
        Unique.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Unique.setStyleSheet(u"")
        Unique.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.centralwidget = QWidget(Unique)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(162, 165, 171);")
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
"	\n"
"	background-color: rgb(181, 184, 190);\n"
"    \n"
"    box-shadow: 0px 64px 64px rgba(0, 0, 0, 0);\n"
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

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"image: url(:/unique/boas_vindas.png);")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.widget_2)

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

        Unique.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Unique)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1086, 33))
        Unique.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Unique)
        self.statusbar.setObjectName(u"statusbar")
        Unique.setStatusBar(self.statusbar)

        self.retranslateUi(Unique)

        QMetaObject.connectSlotsByName(Unique)
    # setupUi

    def retranslateUi(self, Unique):
        Unique.setWindowTitle(QCoreApplication.translate("Unique", u"unique", None))
        self.btn_caixa.setText(QCoreApplication.translate("Unique", u"Caixa", None))
        self.btn_clientes.setText(QCoreApplication.translate("Unique", u"Cliente", None))
        self.btn_delivery.setText(QCoreApplication.translate("Unique", u"Delivery", None))
        self.btn_mesas.setText(QCoreApplication.translate("Unique", u"Mesas", None))
        self.btn_produtos.setText(QCoreApplication.translate("Unique", u"Produtos", None))
        self.btn_loggout.setText(QCoreApplication.translate("Unique", u"Loggout", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("Unique", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Unique", u"Teste1", None))
    # retranslateUi

