# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'finalizar_pedido.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 485)
        MainWindow.setMinimumSize(QSize(640, 485))
        MainWindow.setMaximumSize(QSize(640, 485))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(250, 465))
        self.widget_2.setMaximumSize(QSize(250, 465))
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 80))
        self.widget_7.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_7 = QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setBold(True)
        self.label_3.setFont(font)

        self.verticalLayout_7.addWidget(self.label_3)

        self.cliente_label = QLabel(self.widget_7)
        self.cliente_label.setObjectName(u"cliente_label")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.cliente_label.setFont(font1)
        self.cliente_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.cliente_label)


        self.verticalLayout_4.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_2)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_6 = QVBoxLayout(self.widget_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")

        self.verticalLayout_6.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_8)
        self.widget_11.setObjectName(u"widget_11")

        self.verticalLayout_6.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_8)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.label = QLabel(self.widget_12)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_3.addWidget(self.label)

        self.total_label = QLabel(self.widget_12)
        self.total_label.setObjectName(u"total_label")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.total_label.setFont(font3)
        self.total_label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.horizontalLayout_3.addWidget(self.total_label)


        self.verticalLayout_6.addWidget(self.widget_12)


        self.verticalLayout_4.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 60))
        self.widget_9.setMaximumSize(QSize(16777215, 60))
        self.verticalLayout_5 = QVBoxLayout(self.widget_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_5 = QPushButton(self.widget_9)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.pushButton_5)


        self.verticalLayout_4.addWidget(self.widget_9)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(370, 465))
        self.widget_3.setMaximumSize(QSize(370, 465))
        self.widget_3.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QSize(370, 130))
        self.widget_4.setMaximumSize(QSize(370, 130))
        self.widget_4.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnpix = QPushButton(self.widget_4)
        self.btnpix.setObjectName(u"btnpix")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnpix.sizePolicy().hasHeightForWidth())
        self.btnpix.setSizePolicy(sizePolicy1)
        self.btnpix.setMinimumSize(QSize(30, 30))
        self.btnpix.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.btnpix, 3, 0, 1, 1)

        self.btncredito = QPushButton(self.widget_4)
        self.btncredito.setObjectName(u"btncredito")
        sizePolicy1.setHeightForWidth(self.btncredito.sizePolicy().hasHeightForWidth())
        self.btncredito.setSizePolicy(sizePolicy1)
        self.btncredito.setMinimumSize(QSize(30, 30))
        self.btncredito.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.btncredito, 3, 1, 1, 1)

        self.btndebito = QPushButton(self.widget_4)
        self.btndebito.setObjectName(u"btndebito")
        sizePolicy1.setHeightForWidth(self.btndebito.sizePolicy().hasHeightForWidth())
        self.btndebito.setSizePolicy(sizePolicy1)
        self.btndebito.setMinimumSize(QSize(30, 30))
        self.btndebito.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.btndebito, 4, 1, 1, 1)

        self.btndinheiro = QPushButton(self.widget_4)
        self.btndinheiro.setObjectName(u"btndinheiro")
        sizePolicy1.setHeightForWidth(self.btndinheiro.sizePolicy().hasHeightForWidth())
        self.btndinheiro.setSizePolicy(sizePolicy1)
        self.btndinheiro.setMinimumSize(QSize(30, 30))
        self.btndinheiro.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.btndinheiro, 4, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(370, 290))
        self.widget_5.setMaximumSize(QSize(370, 290))
        self.widget_5.setStyleSheet(u"background-color: rgb(45, 45, 45);")

        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(370, 45))
        self.widget_6.setMaximumSize(QSize(370, 45))
        self.widget_6.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.finaliza_pedido = QPushButton(self.widget_6)
        self.finaliza_pedido.setObjectName(u"finaliza_pedido")

        self.horizontalLayout_2.addWidget(self.finaliza_pedido)

        self.pushButton_4 = QPushButton(self.widget_6)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout_2.addWidget(self.widget_6)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.label_3)
        self.cliente_label.setBuddy(self.cliente_label)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.pushButton_5, self.finaliza_pedido)
        QWidget.setTabOrder(self.finaliza_pedido, self.pushButton_4)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.cliente_label.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.total_label.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"APLICAR DESCONTOS", None))
        self.btnpix.setText(QCoreApplication.translate("MainWindow", u"PIX", None))
        self.btncredito.setText(QCoreApplication.translate("MainWindow", u"CREDITO", None))
        self.btndebito.setText(QCoreApplication.translate("MainWindow", u"DEBITO", None))
        self.btndinheiro.setText(QCoreApplication.translate("MainWindow", u"DINHEIRO", None))
        self.finaliza_pedido.setText(QCoreApplication.translate("MainWindow", u"CONFIRMAR", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"IMPRIMIR", None))
    # retranslateUi

