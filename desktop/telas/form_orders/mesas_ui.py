# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mesas.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(994, 618)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 45))
        self.widget.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.widget)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Mesa_01 = QPushButton(self.widget_3)
        self.Mesa_01.setObjectName(u"Mesa_01")
        self.Mesa_01.setMinimumSize(QSize(120, 120))
        self.Mesa_01.setMaximumSize(QSize(120, 120))
        self.Mesa_01.setStyleSheet(u"")

        self.gridLayout.addWidget(self.Mesa_01, 0, 2, 1, 1)

        self.Mesa_02 = QPushButton(self.widget_3)
        self.Mesa_02.setObjectName(u"Mesa_02")
        self.Mesa_02.setMinimumSize(QSize(120, 120))
        self.Mesa_02.setMaximumSize(QSize(120, 120))
        self.Mesa_02.setStyleSheet(u"")

        self.gridLayout.addWidget(self.Mesa_02, 0, 3, 1, 1)

        self.Mesa_03 = QPushButton(self.widget_3)
        self.Mesa_03.setObjectName(u"Mesa_03")
        self.Mesa_03.setMinimumSize(QSize(120, 120))
        self.Mesa_03.setMaximumSize(QSize(120, 120))
        self.Mesa_03.setStyleSheet(u"")

        self.gridLayout.addWidget(self.Mesa_03, 0, 4, 1, 1)

        self.Mesa_04 = QPushButton(self.widget_3)
        self.Mesa_04.setObjectName(u"Mesa_04")
        self.Mesa_04.setMinimumSize(QSize(120, 120))
        self.Mesa_04.setMaximumSize(QSize(120, 120))
        self.Mesa_04.setStyleSheet(u"")

        self.gridLayout.addWidget(self.Mesa_04, 0, 5, 1, 1)

        self.Mesa_07 = QPushButton(self.widget_3)
        self.Mesa_07.setObjectName(u"Mesa_07")
        self.Mesa_07.setMinimumSize(QSize(120, 120))
        self.Mesa_07.setMaximumSize(QSize(120, 120))
        self.Mesa_07.setStyleSheet(u"")

        self.gridLayout.addWidget(self.Mesa_07, 1, 4, 1, 1)

        self.Mesa_06 = QPushButton(self.widget_3)
        self.Mesa_06.setObjectName(u"Mesa_06")
        self.Mesa_06.setMinimumSize(QSize(120, 120))
        self.Mesa_06.setMaximumSize(QSize(120, 120))
        self.Mesa_06.setStyleSheet(u"")

        self.gridLayout.addWidget(self.Mesa_06, 1, 3, 1, 1)

        self.Mesa_05 = QPushButton(self.widget_3)
        self.Mesa_05.setObjectName(u"Mesa_05")
        self.Mesa_05.setMinimumSize(QSize(120, 120))
        self.Mesa_05.setMaximumSize(QSize(120, 120))
        self.Mesa_05.setStyleSheet(u"")

        self.gridLayout.addWidget(self.Mesa_05, 1, 2, 1, 1)

        self.Mesa_08 = QPushButton(self.widget_3)
        self.Mesa_08.setObjectName(u"Mesa_08")
        self.Mesa_08.setMinimumSize(QSize(120, 120))
        self.Mesa_08.setMaximumSize(QSize(120, 120))
        self.Mesa_08.setStyleSheet(u"")

        self.gridLayout.addWidget(self.Mesa_08, 1, 5, 1, 1)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 30))
        self.widget_2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.widget_3.raise_()
        self.widget.raise_()
        self.widget_2.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MESAS", None))
        self.Mesa_01.setText(QCoreApplication.translate("MainWindow", u"Mesa 01", None))
        self.Mesa_02.setText(QCoreApplication.translate("MainWindow", u"Mesa 02", None))
        self.Mesa_03.setText(QCoreApplication.translate("MainWindow", u"Mesa 03", None))
        self.Mesa_04.setText(QCoreApplication.translate("MainWindow", u"Mesa 04", None))
        self.Mesa_07.setText(QCoreApplication.translate("MainWindow", u"Mesa 07", None))
        self.Mesa_06.setText(QCoreApplication.translate("MainWindow", u"Mesa 06", None))
        self.Mesa_05.setText(QCoreApplication.translate("MainWindow", u"Mesa 05", None))
        self.Mesa_08.setText(QCoreApplication.translate("MainWindow", u"Mesa 08", None))
    # retranslateUi

