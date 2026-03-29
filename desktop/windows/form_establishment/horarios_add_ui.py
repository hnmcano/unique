# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'horarios_add.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTimeEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(473, 85)
        MainWindow.setStyleSheet(u"background-color: black;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(75, 16777215))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(75, 16777215))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_2.addWidget(self.label_4)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.dia_semana = QComboBox(self.widget_2)
        self.dia_semana.setObjectName(u"dia_semana")

        self.horizontalLayout.addWidget(self.dia_semana)

        self.hora_inicial = QTimeEdit(self.widget_2)
        self.hora_inicial.setObjectName(u"hora_inicial")
        self.hora_inicial.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.hora_inicial)

        self.hora_final = QTimeEdit(self.widget_2)
        self.hora_final.setObjectName(u"hora_final")
        self.hora_final.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.hora_final)

        self.btn_aplicar = QPushButton(self.widget_2)
        self.btn_aplicar.setObjectName(u"btn_aplicar")
        self.btn_aplicar.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.btn_aplicar)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dia da Semana", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Hora Inicial", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Hora Final", None))
        self.label_4.setText("")
        self.btn_aplicar.setText(QCoreApplication.translate("MainWindow", u"APLICAR", None))
    # retranslateUi

