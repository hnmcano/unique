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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_CAIXA(object):
    def setupUi(self, CAIXA):
        if not CAIXA.objectName():
            CAIXA.setObjectName(u"CAIXA")
        CAIXA.setWindowModality(Qt.WindowModality.ApplicationModal)
        CAIXA.resize(536, 498)
        CAIXA.setMinimumSize(QSize(536, 498))
        CAIXA.setMaximumSize(QSize(536, 498))
        self.centralwidget = QWidget(CAIXA)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.widget_2.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(90, 0))
        self.widget_8.setMaximumSize(QSize(90, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.widget_8)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_8)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(90, 0))
        self.label.setMaximumSize(QSize(90, 16777215))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_7)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(125, 0))
        self.widget_9.setMaximumSize(QSize(100, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.widget_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ValorCaixa = QLineEdit(self.widget_9)
        self.ValorCaixa.setObjectName(u"ValorCaixa")
        self.ValorCaixa.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.ValorCaixa)


        self.horizontalLayout_3.addWidget(self.widget_9)


        self.verticalLayout_3.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 75))
        self.widget_6.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0,\n"
"        x2:1, y2:0,\n"
"        stop:0 #393939,\n"
"        stop:1 #7d7d7d\n"
"    );\n"
"    color: white;\n"
"    border: 2px solid #282828;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0,\n"
"        x2:1, y2:0,\n"
"        stop:0 #7d7d7d,\n"
"        stop:1 #393939\n"
"    );\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.open_caixa = QPushButton(self.widget_6)
        self.open_caixa.setObjectName(u"open_caixa")
        self.open_caixa.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.open_caixa)


        self.verticalLayout_3.addWidget(self.widget_6)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0,\n"
"        x2:1, y2:0,\n"
"        stop:0 #ff7e5f,\n"
"        stop:1 #feb47b\n"
"    );\n"
"    color: white;\n"
"    border: 2px solid #d35400;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 400))
        self.widget_4.setMaximumSize(QSize(16777215, 720))
        self.widget_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widget_4.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.StatusCaixa = QLabel(self.widget_4)
        self.StatusCaixa.setObjectName(u"StatusCaixa")
        self.StatusCaixa.setMaximumSize(QSize(16777215, 75))
        self.StatusCaixa.setStyleSheet(u"")
        self.StatusCaixa.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.StatusCaixa)

        self.widget_10 = QWidget(self.widget_4)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.widget_10)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0,\n"
"        x2:1, y2:0,\n"
"        stop:0 #393939,\n"
"        stop:1 #7d7d7d\n"
"    );\n"
"    color: white;\n"
"    border: 2px solid #282828;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0,\n"
"        x2:1, y2:0,\n"
"        stop:0 #7d7d7d,\n"
"        stop:1 #393939\n"
"    );\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_2 = QPushButton(self.widget_5)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.CloseCaixa = QPushButton(self.widget_5)
        self.CloseCaixa.setObjectName(u"CloseCaixa")

        self.horizontalLayout_4.addWidget(self.CloseCaixa)


        self.verticalLayout_2.addWidget(self.widget_5)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget)

        CAIXA.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(CAIXA)
        self.statusbar.setObjectName(u"statusbar")
        CAIXA.setStatusBar(self.statusbar)

        self.retranslateUi(CAIXA)

        QMetaObject.connectSlotsByName(CAIXA)
    # setupUi

    def retranslateUi(self, CAIXA):
        CAIXA.setWindowTitle(QCoreApplication.translate("CAIXA", u"CAIXA", None))
        self.label.setText(QCoreApplication.translate("CAIXA", u"VALOR CAIXA", None))
        self.open_caixa.setText(QCoreApplication.translate("CAIXA", u"ABRIR CAIXA", None))
        self.StatusCaixa.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("CAIXA", u"IMPRIMIR CAIXA", None))
        self.CloseCaixa.setText(QCoreApplication.translate("CAIXA", u"FECHAR CAIXA", None))
    # retranslateUi

