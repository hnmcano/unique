# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delivery.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(1120, 523)
        MainWindow.setMaximumSize(QSize(1217, 669))
        MainWindow.setStyleSheet(u"")
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
        self.widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(120, 0))
        self.widget_3.setMaximumSize(QSize(120, 120))
        self.widget_3.setStyleSheet(u"")
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
        self.FilterPedidos = QLineEdit(self.widget_4)
        self.FilterPedidos.setObjectName(u"FilterPedidos")
        self.FilterPedidos.setMaximumSize(QSize(550, 16777215))
        self.FilterPedidos.setStyleSheet(u"border-left: 1px solid red;\n"
"border-right: 1px solid red;")

        self.verticalLayout_3.addWidget(self.FilterPedidos)


        self.horizontalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(200, 0))
        self.widget_5.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.widget_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 55))
        self.pushButton.setMaximumSize(QSize(120, 55))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.pushButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.widget)

        self.delivery = QFrame(self.centralwidget)
        self.delivery.setObjectName(u"delivery")
        self.verticalLayout_5 = QVBoxLayout(self.delivery)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableWidget = QTableWidget(self.delivery)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_5.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.delivery)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PEDIDOS DELIVERY", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PEDIDO", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"NovoPedido", None))
    # retranslateUi

