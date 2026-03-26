# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Caixa.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_CAIXA(object):
    def setupUi(self, CAIXA):
        if not CAIXA.objectName():
            CAIXA.setObjectName(u"CAIXA")
        CAIXA.setWindowModality(Qt.WindowModality.NonModal)
        CAIXA.resize(777, 477)
        CAIXA.setMinimumSize(QSize(0, 0))
        CAIXA.setMaximumSize(QSize(16777215, 16777215))
        CAIXA.setStyleSheet(u"#centralwidget #widget_2 {\n"
"	background-color: black;\n"
"}\n"
"\n"
"#centralwidget #widget_3 {\n"
"	background-color: black;\n"
"}\n"
"")
        self.centralwidget = QWidget(CAIXA)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(220, 16777215))
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 60))
        self.verticalLayout_7 = QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.StatusCaixa = QLabel(self.widget_6)
        self.StatusCaixa.setObjectName(u"StatusCaixa")
        self.StatusCaixa.setMinimumSize(QSize(0, 60))
        self.StatusCaixa.setMaximumSize(QSize(16777215, 60))
        self.StatusCaixa.setStyleSheet(u"")
        self.StatusCaixa.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.StatusCaixa)


        self.verticalLayout_3.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout = QVBoxLayout(self.widget_7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.widget_7)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 9, -1)
        self.ValorCaixa = QLineEdit(self.frame)
        self.ValorCaixa.setObjectName(u"ValorCaixa")
        self.ValorCaixa.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.ValorCaixa, 0, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_5 = QVBoxLayout(self.widget_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.widget_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.DataAbertura = QLineEdit(self.widget_9)
        self.DataAbertura.setObjectName(u"DataAbertura")
        self.DataAbertura.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.DataAbertura)


        self.verticalLayout_4.addWidget(self.widget_9)

        self.widget_12 = QWidget(self.widget_8)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.label_3 = QLabel(self.widget_12)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.LabelTotal = QLabel(self.widget_12)
        self.LabelTotal.setObjectName(u"LabelTotal")
        self.LabelTotal.setFont(font)
        self.LabelTotal.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.horizontalLayout_3.addWidget(self.LabelTotal)


        self.verticalLayout_4.addWidget(self.widget_12)


        self.verticalLayout.addWidget(self.widget_8)


        self.verticalLayout_3.addWidget(self.widget_7)

        self.widget_11 = QWidget(self.widget_2)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(215, 0))
        self.widget_11.setMaximumSize(QSize(215, 80))
        self.verticalLayout_8 = QVBoxLayout(self.widget_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.AbrirCaixa = QPushButton(self.widget_11)
        self.AbrirCaixa.setObjectName(u"AbrirCaixa")

        self.verticalLayout_8.addWidget(self.AbrirCaixa)


        self.verticalLayout_3.addWidget(self.widget_11)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 60))
        self.widget_4.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tableCaixa = QTableWidget(self.widget_5)
        self.tableCaixa.setObjectName(u"tableCaixa")

        self.verticalLayout_6.addWidget(self.tableCaixa)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_10 = QWidget(self.widget_3)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_10.setMinimumSize(QSize(0, 80))
        self.widget_10.setMaximumSize(QSize(16777215, 80))
        self.gridLayout_2 = QGridLayout(self.widget_10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.FecharCaixa = QPushButton(self.widget_10)
        self.FecharCaixa.setObjectName(u"FecharCaixa")

        self.gridLayout_2.addWidget(self.FecharCaixa, 0, 0, 1, 1)

        self.ImprimirCaixa = QPushButton(self.widget_10)
        self.ImprimirCaixa.setObjectName(u"ImprimirCaixa")

        self.gridLayout_2.addWidget(self.ImprimirCaixa, 0, 1, 1, 1)

        self.FecharAndImprimir = QPushButton(self.widget_10)
        self.FecharAndImprimir.setObjectName(u"FecharAndImprimir")

        self.gridLayout_2.addWidget(self.FecharAndImprimir, 0, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_10)


        self.horizontalLayout.addWidget(self.widget_3)


        self.horizontalLayout_2.addWidget(self.widget)

        CAIXA.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(CAIXA)
        self.statusbar.setObjectName(u"statusbar")
        CAIXA.setStatusBar(self.statusbar)

        self.retranslateUi(CAIXA)

        QMetaObject.connectSlotsByName(CAIXA)
    # setupUi

    def retranslateUi(self, CAIXA):
        CAIXA.setWindowTitle(QCoreApplication.translate("CAIXA", u"CAIXA", None))
        self.StatusCaixa.setText("")
        self.label.setText(QCoreApplication.translate("CAIXA", u"Valor Abertura", None))
        self.label_2.setText(QCoreApplication.translate("CAIXA", u"Data Abertura", None))
        self.label_3.setText(QCoreApplication.translate("CAIXA", u"Total", None))
        self.LabelTotal.setText("")
        self.AbrirCaixa.setText(QCoreApplication.translate("CAIXA", u"ABRIR", None))
        self.FecharCaixa.setText(QCoreApplication.translate("CAIXA", u"FECHAR", None))
        self.ImprimirCaixa.setText(QCoreApplication.translate("CAIXA", u"IMPRIMIR", None))
        self.FecharAndImprimir.setText(QCoreApplication.translate("CAIXA", u"FECHAR E IMPRIMIR", None))
    # retranslateUi

