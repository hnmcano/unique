# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pedido_mesa.ui'
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
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(540, 590)
        MainWindow.setMinimumSize(QSize(540, 590))
        MainWindow.setMaximumSize(QSize(540, 590))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(540, 590))
        self.centralwidget.setMaximumSize(QSize(540, 590))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(540, 90))
        self.widget.setMaximumSize(QSize(540, 90))
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(380, 0))
        self.widget_7.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.mesa = QLabel(self.widget_7)
        self.mesa.setObjectName(u"mesa")
        self.mesa.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_7.addWidget(self.mesa)


        self.horizontalLayout_3.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.adicionar_produto = QPushButton(self.widget_8)
        self.adicionar_produto.setObjectName(u"adicionar_produto")

        self.verticalLayout_4.addWidget(self.adicionar_produto)


        self.horizontalLayout_3.addWidget(self.widget_8)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(170, 501))
        self.widget_3.setMaximumSize(QSize(170, 501))
        self.widget_3.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.status = QLabel(self.widget_6)
        self.status.setObjectName(u"status")
        self.status.setMaximumSize(QSize(16777215, 45))
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.status)

        self.data_criacao = QLineEdit(self.widget_6)
        self.data_criacao.setObjectName(u"data_criacao")

        self.verticalLayout_6.addWidget(self.data_criacao)

        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 80))
        self.widget_5.setMaximumSize(QSize(16777215, 80))
        self.widget_5.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_excluir = QPushButton(self.widget_5)
        self.btn_excluir.setObjectName(u"btn_excluir")

        self.verticalLayout_3.addWidget(self.btn_excluir)


        self.verticalLayout_2.addWidget(self.widget_5)


        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(370, 501))
        self.widget_4.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.widget_4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(16777215, 415))
        self.tableWidget.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.tableWidget)

        self.widget_9 = QWidget(self.widget_4)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 80))
        self.widget_9.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(self.widget_9)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_9)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout_5.addWidget(self.widget_9)


        self.horizontalLayout.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PEDIDOS EM MESA", None))
        self.mesa.setText("")
        self.adicionar_produto.setText(QCoreApplication.translate("MainWindow", u"ADD PRODUTO", None))
        self.status.setText("")
        self.label_2.setText("")
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"FINALIZAR", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"IMPRIMIR", None))
    # retranslateUi

