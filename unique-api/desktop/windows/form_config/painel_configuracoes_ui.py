# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'painel_configuracoes.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from pictures import imagens_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(390, 170)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(390, 170))
        self.centralwidget.setMaximumSize(QSize(390, 170))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(390, 170))
        self.widget.setMaximumSize(QSize(390, 170))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(195, 170))
        self.widget_2.setMaximumSize(QSize(195, 170))
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.btn_estabelecimento = QPushButton(self.widget_2)
        self.btn_estabelecimento.setObjectName(u"btn_estabelecimento")
        self.btn_estabelecimento.setMinimumSize(QSize(160, 120))
        self.btn_estabelecimento.setMaximumSize(QSize(160, 120))
        font = QFont()
        font.setUnderline(False)
        self.btn_estabelecimento.setFont(font)
        self.btn_estabelecimento.setStyleSheet(u"background-color: rgb(57, 57, 57);")
        icon = QIcon()
        icon.addFile(u":/unique/estabelecimento.png", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.btn_estabelecimento.setIcon(icon)
        self.btn_estabelecimento.setIconSize(QSize(54, 54))
        self.btn_estabelecimento.setAutoDefault(True)
        self.btn_estabelecimento.setFlat(True)

        self.verticalLayout_3.addWidget(self.btn_estabelecimento)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(160, 0))
        self.label.setMaximumSize(QSize(160, 16777215))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(195, 170))
        self.widget_3.setMaximumSize(QSize(195, 170))
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.btn_loggout = QPushButton(self.widget_3)
        self.btn_loggout.setObjectName(u"btn_loggout")
        self.btn_loggout.setMinimumSize(QSize(160, 120))
        self.btn_loggout.setMaximumSize(QSize(160, 120))
        self.btn_loggout.setStyleSheet(u"background-color: rgb(57, 57, 57);")
        icon1 = QIcon()
        icon1.addFile(u":/unique/sair.png", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.btn_loggout.setIcon(icon1)
        self.btn_loggout.setIconSize(QSize(54, 54))
        self.btn_loggout.setAutoDefault(True)
        self.btn_loggout.setFlat(True)

        self.verticalLayout_2.addWidget(self.btn_loggout)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(160, 0))
        self.label_2.setMaximumSize(QSize(160, 16777215))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_estabelecimento.setDefault(True)
        self.btn_loggout.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_estabelecimento.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"ESTABELECIMENTO", None))
        self.btn_loggout.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LOGGOUT", None))
    # retranslateUi

