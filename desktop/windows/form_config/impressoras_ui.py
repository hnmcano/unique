# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'impressoras.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(301, 398)
        MainWindow.setStyleSheet(u"#centralwidget {\n"
"	background-color: black;\n"
"}\n"
"\n"
"#centralwidget #comboBox{\n"
"	background-color: #131314;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 100))
        self.widget_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widget_2.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ListImpressoras = QComboBox(self.widget_2)
        self.ListImpressoras.setObjectName(u"ListImpressoras")
        self.ListImpressoras.setMaximumSize(QSize(220, 16777215))
        self.ListImpressoras.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.ListImpressoras, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_6 = QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_3 = QWidget(self.widget_6)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 60))
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tamanho = QComboBox(self.widget_3)
        self.tamanho.setObjectName(u"tamanho")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tamanho.sizePolicy().hasHeightForWidth())
        self.tamanho.setSizePolicy(sizePolicy)
        self.tamanho.setMaximumSize(QSize(90, 16777215))

        self.gridLayout.addWidget(self.tamanho, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.widget_3)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.widget_8)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_4.addWidget(self.checkBox)

        self.TestarImp = QPushButton(self.widget_8)
        self.TestarImp.setObjectName(u"TestarImp")
        sizePolicy.setHeightForWidth(self.TestarImp.sizePolicy().hasHeightForWidth())
        self.TestarImp.setSizePolicy(sizePolicy)
        self.TestarImp.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.TestarImp)


        self.verticalLayout_6.addWidget(self.widget_8)

        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout = QHBoxLayout(self.widget_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.AplicarAlteracoes = QPushButton(self.widget_7)
        self.AplicarAlteracoes.setObjectName(u"AplicarAlteracoes")

        self.horizontalLayout.addWidget(self.AplicarAlteracoes)

        self.Cancelar = QPushButton(self.widget_7)
        self.Cancelar.setObjectName(u"Cancelar")

        self.horizontalLayout.addWidget(self.Cancelar)


        self.verticalLayout_6.addWidget(self.widget_7)


        self.verticalLayout_4.addWidget(self.widget_6)


        self.verticalLayout_2.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Definir impressora como padr\u00e3o!?", None))
        self.TestarImp.setText(QCoreApplication.translate("MainWindow", u"TESTAR IMP.", None))
        self.AplicarAlteracoes.setText(QCoreApplication.translate("MainWindow", u"APLICAR", None))
        self.Cancelar.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
    # retranslateUi

