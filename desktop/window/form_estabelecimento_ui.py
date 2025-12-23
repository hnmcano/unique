# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_estabelecimento.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(644, 502)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 140))
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.estabelecimento_logo = QLabel(self.widget_2)
        self.estabelecimento_logo.setObjectName(u"estabelecimento_logo")
        self.estabelecimento_logo.setMaximumSize(QSize(16777215, 300))
        self.estabelecimento_logo.setStyleSheet(u"QLabel {\n"
"		\n"
"	background-color: rgb(98, 98, 98);\n"
"	\n"
"}\n"
"")
        self.estabelecimento_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.estabelecimento_logo)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.NomeEstabelecimento = QLineEdit(self.widget_3)
        self.NomeEstabelecimento.setObjectName(u"NomeEstabelecimento")

        self.gridLayout.addWidget(self.NomeEstabelecimento, 2, 1, 1, 1)

        self.EnderecoEstabelecimento = QLineEdit(self.widget_3)
        self.EnderecoEstabelecimento.setObjectName(u"EnderecoEstabelecimento")

        self.gridLayout.addWidget(self.EnderecoEstabelecimento, 3, 1, 1, 1)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.EstabelecimentoInstagram = QLineEdit(self.widget_3)
        self.EstabelecimentoInstagram.setObjectName(u"EstabelecimentoInstagram")

        self.gridLayout.addWidget(self.EstabelecimentoInstagram, 4, 1, 1, 1)

        self.TelefoneEstabelecimento = QLineEdit(self.widget_3)
        self.TelefoneEstabelecimento.setObjectName(u"TelefoneEstabelecimento")

        self.gridLayout.addWidget(self.TelefoneEstabelecimento, 5, 1, 1, 1)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 55))
        self.widget_4.setStyleSheet(u"QPushButton {\n"
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
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.EnviaDados = QPushButton(self.widget_4)
        self.EnviaDados.setObjectName(u"EnviaDados")

        self.horizontalLayout.addWidget(self.EnviaDados)

        self.CancelaEnvio = QPushButton(self.widget_4)
        self.CancelaEnvio.setObjectName(u"CancelaEnvio")

        self.horizontalLayout.addWidget(self.CancelaEnvio)


        self.verticalLayout_2.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.NomeEstabelecimento, self.EnderecoEstabelecimento)
        QWidget.setTabOrder(self.EnderecoEstabelecimento, self.EstabelecimentoInstagram)
        QWidget.setTabOrder(self.EstabelecimentoInstagram, self.TelefoneEstabelecimento)
        QWidget.setTabOrder(self.TelefoneEstabelecimento, self.EnviaDados)
        QWidget.setTabOrder(self.EnviaDados, self.CancelaEnvio)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.estabelecimento_logo.setText(QCoreApplication.translate("MainWindow", u"CLIQUE DUAS VEZES PARA SELECIONAR O LOGO!!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"NOME ESTABELECIMENTO", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O C/ NUMERO", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"REDE SOCIAL INSTAGRAM", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TELEFONE P/ CONTATO", None))
        self.EnviaDados.setText(QCoreApplication.translate("MainWindow", u"ENVIAR", None))
        self.CancelaEnvio.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
    # retranslateUi

