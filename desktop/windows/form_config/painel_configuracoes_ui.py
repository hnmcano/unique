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
        MainWindow.resize(300, 135)
        MainWindow.setMinimumSize(QSize(300, 135))
        MainWindow.setMaximumSize(QSize(300, 135))
        MainWindow.setStyleSheet(u"#centralwidget{\n"
"	background-color: black;\n"
"}\n"
"\n"
"#centralwidget #widget_2{\n"
"	background-color: #131314;\n"
"}\n"
"\n"
"#centralwidget #widget_3{\n"
"	background-color: #131314;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.widget_2.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.btn_impressoras = QPushButton(self.widget_2)
        self.btn_impressoras.setObjectName(u"btn_impressoras")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_impressoras.sizePolicy().hasHeightForWidth())
        self.btn_impressoras.setSizePolicy(sizePolicy)
        self.btn_impressoras.setMinimumSize(QSize(0, 0))
        self.btn_impressoras.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setUnderline(False)
        self.btn_impressoras.setFont(font)
        self.btn_impressoras.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/unique/impressora.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_impressoras.setIcon(icon)
        self.btn_impressoras.setIconSize(QSize(54, 54))
        self.btn_impressoras.setAutoDefault(True)
        self.btn_impressoras.setFlat(True)

        self.verticalLayout_3.addWidget(self.btn_impressoras)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.widget_3.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)

        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_impressoras.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_impressoras.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"IMPRESSORAS", None))
    # retranslateUi

