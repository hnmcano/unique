# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'produtos.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1217, 669)
        MainWindow.setMaximumSize(QSize(1217, 669))
        MainWindow.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0,0,0);\n"
"	border: 1px solid red;\n"
"}\n"
"\n"
"QLineEdit, QComboBox{\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 4px 2px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 5px 17px;\n"
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
"}\n"
"\n"
"QTextEdit{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
""
                        "    border: 1px solid red;\n"
"    padding: 4px 2px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 10px;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QTextEdit:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 70))
        self.widget.setMaximumSize(QSize(16777215, 70))
        self.widget.setStyleSheet(u"QWidget  {\n"
"		border-left: transparent;\n"
"		border-right: transparent;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(120, 0))
        self.widget_3.setMaximumSize(QSize(120, 120))
        self.widget_3.setStyleSheet(u"border-right: transparent;\n"
"border-left: 1px solid red;")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(120, 16777215))
        self.label.setStyleSheet(u"border: transparent;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)


        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(700, 0))
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.widget_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(550, 16777215))
        self.lineEdit.setStyleSheet(u"border-left: 1px solid red;\n"
"border-right: 1px solid red;")

        self.verticalLayout_3.addWidget(self.lineEdit)


        self.horizontalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(300, 0))
        self.widget_5.setStyleSheet(u"QPushButton {\n"
"				border: 1px solid red;\n"
"				min-right: 35px;\n"
"}\n"
"QWidget {\n"
"	border-right: 1px solid red;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.add_products = QPushButton(self.widget_5)
        self.add_products.setObjectName(u"add_products")
        self.add_products.setMinimumSize(QSize(50, 45))
        self.add_products.setMaximumSize(QSize(16777215, 45))

        self.horizontalLayout_2.addWidget(self.add_products)

        self.atualizar_estoque = QPushButton(self.widget_5)
        self.atualizar_estoque.setObjectName(u"atualizar_estoque")
        self.atualizar_estoque.setMinimumSize(QSize(50, 45))
        self.atualizar_estoque.setMaximumSize(QSize(16777215, 45))

        self.horizontalLayout_2.addWidget(self.atualizar_estoque)


        self.horizontalLayout.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.table_products = QTableWidget(self.widget_2)
        self.table_products.setObjectName(u"table_products")
        self.table_products.setStyleSheet(u"background- color: white;\n"
"border: 1px solid blue;\n"
"boder-radius: 5px;")

        self.verticalLayout_2.addWidget(self.table_products)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PRODUTO", None))
        self.add_products.setText(QCoreApplication.translate("MainWindow", u"ADD PRODUTO", None))
        self.atualizar_estoque.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
    # retranslateUi

