# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'atualizacao_localizacao.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(629, 66)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.LatitudeLine = QLineEdit(self.widget)
        self.LatitudeLine.setObjectName(u"LatitudeLine")

        self.horizontalLayout.addWidget(self.LatitudeLine)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.LongitudeLine = QLineEdit(self.widget)
        self.LongitudeLine.setObjectName(u"LongitudeLine")

        self.horizontalLayout.addWidget(self.LongitudeLine)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.NomeLine = QLineEdit(self.widget)
        self.NomeLine.setObjectName(u"NomeLine")

        self.horizontalLayout.addWidget(self.NomeLine)

        self.btn_atualizar = QPushButton(self.widget)
        self.btn_atualizar.setObjectName(u"btn_atualizar")

        self.horizontalLayout.addWidget(self.btn_atualizar)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Longetude", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.btn_atualizar.setText(QCoreApplication.translate("MainWindow", u"ATUALIZAR", None))
    # retranslateUi

