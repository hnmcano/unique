# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_estabelecimento.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(840, 640)
        MainWindow.setMinimumSize(QSize(840, 640))
        MainWindow.setMaximumSize(QSize(840, 640))
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.estabelecimento_logo.sizePolicy().hasHeightForWidth())
        self.estabelecimento_logo.setSizePolicy(sizePolicy)
        self.estabelecimento_logo.setMinimumSize(QSize(819, 120))
        self.estabelecimento_logo.setMaximumSize(QSize(16777215, 120))
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
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.widget_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.frame)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.IdLine = QLineEdit(self.widget_5)
        self.IdLine.setObjectName(u"IdLine")
        self.IdLine.setEnabled(False)
        self.IdLine.setMaximumSize(QSize(170, 16777215))

        self.horizontalLayout_3.addWidget(self.IdLine)

        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.NomeLine = QLineEdit(self.widget_5)
        self.NomeLine.setObjectName(u"NomeLine")
        self.NomeLine.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.NomeLine)

        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.DocumentoLine = QLineEdit(self.widget_5)
        self.DocumentoLine.setObjectName(u"DocumentoLine")
        self.DocumentoLine.setEnabled(False)
        font = QFont()
        font.setStrikeOut(False)
        self.DocumentoLine.setFont(font)

        self.horizontalLayout_3.addWidget(self.DocumentoLine)


        self.verticalLayout_4.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.frame)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 175))
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(16777215, 95))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.widget_8)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.NomeFanLine = QLineEdit(self.widget_8)
        self.NomeFanLine.setObjectName(u"NomeFanLine")

        self.horizontalLayout_4.addWidget(self.NomeFanLine)

        self.label_6 = QLabel(self.widget_8)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.EmailLine = QLineEdit(self.widget_8)
        self.EmailLine.setObjectName(u"EmailLine")

        self.horizontalLayout_4.addWidget(self.EmailLine)


        self.verticalLayout_5.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMaximumSize(QSize(16777215, 95))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.widget_9)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.TelefoneLine = QLineEdit(self.widget_9)
        self.TelefoneLine.setObjectName(u"TelefoneLine")

        self.horizontalLayout_5.addWidget(self.TelefoneLine)

        self.label_7 = QLabel(self.widget_9)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.EnderecoLine = QLineEdit(self.widget_9)
        self.EnderecoLine.setObjectName(u"EnderecoLine")

        self.horizontalLayout_5.addWidget(self.EnderecoLine)

        self.label_8 = QLabel(self.widget_9)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.RedeSocialLine = QLineEdit(self.widget_9)
        self.RedeSocialLine.setObjectName(u"RedeSocialLine")

        self.horizontalLayout_5.addWidget(self.RedeSocialLine)


        self.verticalLayout_5.addWidget(self.widget_9)


        self.verticalLayout_4.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.frame)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_6 = QVBoxLayout(self.widget_7)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_7)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.widget_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.PlanoLine = QLineEdit(self.widget_10)
        self.PlanoLine.setObjectName(u"PlanoLine")
        self.PlanoLine.setEnabled(False)
        self.PlanoLine.setMaximumSize(QSize(170, 16777215))

        self.horizontalLayout_6.addWidget(self.PlanoLine)

        self.label_12 = QLabel(self.widget_10)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.LimiteUsuarioLine = QLineEdit(self.widget_10)
        self.LimiteUsuarioLine.setObjectName(u"LimiteUsuarioLine")
        self.LimiteUsuarioLine.setEnabled(False)
        self.LimiteUsuarioLine.setMaximumSize(QSize(170, 16777215))

        self.horizontalLayout_6.addWidget(self.LimiteUsuarioLine)

        self.label_13 = QLabel(self.widget_10)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_13)

        self.AtivoLine = QLineEdit(self.widget_10)
        self.AtivoLine.setObjectName(u"AtivoLine")
        self.AtivoLine.setEnabled(False)
        self.AtivoLine.setMaximumSize(QSize(170, 16777215))

        self.horizontalLayout_6.addWidget(self.AtivoLine)


        self.verticalLayout_6.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_7)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_16 = QLabel(self.widget_11)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 0))
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_16)

        self.DataCriacaoLine = QLineEdit(self.widget_11)
        self.DataCriacaoLine.setObjectName(u"DataCriacaoLine")
        self.DataCriacaoLine.setEnabled(False)
        self.DataCriacaoLine.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_7.addWidget(self.DataCriacaoLine)

        self.label_17 = QLabel(self.widget_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 0))
        self.label_17.setMaximumSize(QSize(130, 16777215))
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_17)

        self.DataAtualizacaoLine = QLineEdit(self.widget_11)
        self.DataAtualizacaoLine.setObjectName(u"DataAtualizacaoLine")
        self.DataAtualizacaoLine.setEnabled(False)
        self.DataAtualizacaoLine.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_7.addWidget(self.DataAtualizacaoLine)

        self.label_14 = QLabel(self.widget_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_14)

        self.DataExpiracaoLine = QLineEdit(self.widget_11)
        self.DataExpiracaoLine.setObjectName(u"DataExpiracaoLine")
        self.DataExpiracaoLine.setEnabled(False)
        self.DataExpiracaoLine.setMaximumSize(QSize(170, 16777215))

        self.horizontalLayout_7.addWidget(self.DataExpiracaoLine)


        self.verticalLayout_6.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_7)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_15 = QLabel(self.widget_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(130, 16777215))
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_15)

        self.SubDominioLine = QLineEdit(self.widget_12)
        self.SubDominioLine.setObjectName(u"SubDominioLine")
        self.SubDominioLine.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.SubDominioLine)


        self.verticalLayout_6.addWidget(self.widget_12)


        self.verticalLayout_4.addWidget(self.widget_7)


        self.horizontalLayout_2.addWidget(self.frame)


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
        QWidget.setTabOrder(self.EnviaDados, self.CancelaEnvio)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.estabelecimento_logo.setText(QCoreApplication.translate("MainWindow", u"CLIQUE DUAS VEZES PARA SELECIONAR O LOGO!!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.NomeLine.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DOCUMENTO", None))
        self.DocumentoLine.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"NOME FANTASIA", None))
        self.NomeFanLine.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"E-MAIL", None))
        self.EmailLine.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.TelefoneLine.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ENDERECO", None))
        self.EnderecoLine.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"REDE SOCIAL", None))
        self.RedeSocialLine.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"PLANO", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"LIMITE USUARIOS", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ATIVO", None))
        self.AtivoLine.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"DATA CRIA\u00c7\u00c3O", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"DATA ATUALIZA\u00c7\u00c3O", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"DATA EXPIRA\u00c7\u00c3O", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"SUBDOMINIO", None))
        self.EnviaDados.setText(QCoreApplication.translate("MainWindow", u"ENVIAR", None))
        self.CancelaEnvio.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
    # retranslateUi

