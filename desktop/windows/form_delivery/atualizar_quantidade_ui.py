# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'atualizar_quantidade.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        MainWindow.resize(365, 75)
        MainWindow.setMinimumSize(QSize(365, 75))
        MainWindow.setMaximumSize(QSize(365, 75))
        MainWindow.setStyleSheet(u"#centralwidget{\n"
"	background-color: black;\n"
"}\n"
"\n"
"#centralwidget #btn_aumentar {\n"
"	background-color: green;\n"
"	font-size: 14px;\n"
" 	border-radius: 10px;\n"
"}\n"
"\n"
"#centralwidget #btn_diminuir {\n"
"	background-color: red;\n"
"	font-size: 14px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#centralwidget #quantidade {\n"
"	background-color: grey;\n"
"	border-radius: 5px;\n"
"	color: black;\n"
"}\n"
"\n"
"#centralwidget #widget QPushButton:hover{\n"
"	background-color: #3c3c3c;\n"
"}\n"
"\n"
"#centralwidget #widget_2 QPushButton {\n"
"	background-color: #131314;\n"
"}\n"
"\n"
"#centralwidget #widget_2 QPushButton:hover {\n"
"	background-color: #3c3c3c;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(150, 16777215))
        self.quantidade = QLabel(self.widget)
        self.quantidade.setObjectName(u"quantidade")
        self.quantidade.setGeometry(QRect(36, 17, 61, 21))
        self.quantidade.setMaximumSize(QSize(16777215, 30))
        self.quantidade.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_diminuir = QPushButton(self.widget)
        self.btn_diminuir.setObjectName(u"btn_diminuir")
        self.btn_diminuir.setGeometry(QRect(90, 10, 35, 35))
        self.btn_diminuir.setMinimumSize(QSize(35, 35))
        self.btn_diminuir.setMaximumSize(QSize(35, 35))
        self.btn_diminuir.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.btn_diminuir.setAcceptDrops(False)
        self.btn_diminuir.setToolTipDuration(-1)
        self.btn_diminuir.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_diminuir.setAutoFillBackground(False)
        self.btn_diminuir.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.btn_aumentar = QPushButton(self.widget)
        self.btn_aumentar.setObjectName(u"btn_aumentar")
        self.btn_aumentar.setGeometry(QRect(10, 10, 35, 35))
        self.btn_aumentar.setMaximumSize(QSize(35, 35))
        self.btn_aumentar.setBaseSize(QSize(0, 0))
        self.btn_aumentar.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)

        self.horizontalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_atualizar = QPushButton(self.widget_2)
        self.btn_atualizar.setObjectName(u"btn_atualizar")

        self.horizontalLayout.addWidget(self.btn_atualizar)

        self.btn_cancelar = QPushButton(self.widget_2)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.horizontalLayout.addWidget(self.btn_cancelar)


        self.horizontalLayout_2.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QUANTIDADE", None))
        self.quantidade.setText("")
        self.btn_diminuir.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_aumentar.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_atualizar.setText(QCoreApplication.translate("MainWindow", u"ATUALIZAR", None))
        self.btn_cancelar.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
    # retranslateUi

