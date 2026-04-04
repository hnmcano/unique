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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(840, 640)
        MainWindow.setMinimumSize(QSize(840, 640))
        MainWindow.setMaximumSize(QSize(840, 640))
        MainWindow.setStyleSheet(u"#centralwidget{\n"
"	background-color: black;\n"
"}\n"
"\n"
"#centralwidget #page{\n"
"	background-color: black;\n"
"}\n"
"\n"
"#centralwidget #page_3{\n"
"	background-color: black;\n"
"}\n"
"\n"
"#centralwidget #page_2{\n"
"	background-color: black;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.centralwidget)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy)
        self.widget_13.setMinimumSize(QSize(0, 50))
        self.widget_13.setMaximumSize(QSize(16777215, 50))
        self.widget_13.setStyleSheet(u"QPushButton{\n"
"	\n"
"	border-top: 5px solid white;\n"
"\n"
"}")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_informacoes = QPushButton(self.widget_13)
        self.btn_informacoes.setObjectName(u"btn_informacoes")
        sizePolicy.setHeightForWidth(self.btn_informacoes.sizePolicy().hasHeightForWidth())
        self.btn_informacoes.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.btn_informacoes)

        self.btn_layout = QPushButton(self.widget_13)
        self.btn_layout.setObjectName(u"btn_layout")
        sizePolicy.setHeightForWidth(self.btn_layout.sizePolicy().hasHeightForWidth())
        self.btn_layout.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.btn_layout)

        self.btn_horarios_config = QPushButton(self.widget_13)
        self.btn_horarios_config.setObjectName(u"btn_horarios_config")
        sizePolicy.setHeightForWidth(self.btn_horarios_config.sizePolicy().hasHeightForWidth())
        self.btn_horarios_config.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.btn_horarios_config)


        self.verticalLayout.addWidget(self.widget_13)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.widget_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
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
        self.IdLine.setEchoMode(QLineEdit.EchoMode.Password)

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
        self.DocumentoLine.setEchoMode(QLineEdit.EchoMode.Password)

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
        self.horizontalLayout_5.setContentsMargins(9, -1, -1, -1)
        self.widget_17 = QWidget(self.widget_9)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy1)
        self.verticalLayout_11 = QVBoxLayout(self.widget_17)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_23 = QWidget(self.widget_17)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, -1)
        self.label_5 = QLabel(self.widget_23)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_14.addWidget(self.label_5)

        self.TelefoneLine = QLineEdit(self.widget_23)
        self.TelefoneLine.setObjectName(u"TelefoneLine")

        self.horizontalLayout_14.addWidget(self.TelefoneLine)


        self.verticalLayout_11.addWidget(self.widget_23)

        self.widget_24 = QWidget(self.widget_17)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget_24)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_13.addWidget(self.label_7)

        self.EnderecoLine = QLineEdit(self.widget_24)
        self.EnderecoLine.setObjectName(u"EnderecoLine")

        self.horizontalLayout_13.addWidget(self.EnderecoLine)


        self.verticalLayout_11.addWidget(self.widget_24)


        self.horizontalLayout_5.addWidget(self.widget_17)

        self.widget_20 = QWidget(self.widget_9)
        self.widget_20.setObjectName(u"widget_20")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy2)
        self.verticalLayout_12 = QVBoxLayout(self.widget_20)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_22 = QWidget(self.widget_20)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_22)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_12.addWidget(self.label_8)

        self.RedeSocialLine = QLineEdit(self.widget_22)
        self.RedeSocialLine.setObjectName(u"RedeSocialLine")

        self.horizontalLayout_12.addWidget(self.RedeSocialLine)


        self.verticalLayout_12.addWidget(self.widget_22)

        self.widget_21 = QWidget(self.widget_20)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_21)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.DescricaoLine = QLineEdit(self.widget_21)
        self.DescricaoLine.setObjectName(u"DescricaoLine")

        self.horizontalLayout_11.addWidget(self.DescricaoLine)


        self.verticalLayout_12.addWidget(self.widget_21)


        self.horizontalLayout_5.addWidget(self.widget_20)


        self.verticalLayout_5.addWidget(self.widget_9)


        self.verticalLayout_4.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.frame)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_6 = QVBoxLayout(self.widget_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
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

        self.widget_12 = QWidget(self.widget_7)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_15 = QLabel(self.widget_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(130, 16777215))
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_15)

        self.SubDominioLine = QLineEdit(self.widget_12)
        self.SubDominioLine.setObjectName(u"SubDominioLine")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.SubDominioLine.sizePolicy().hasHeightForWidth())
        self.SubDominioLine.setSizePolicy(sizePolicy3)
        self.SubDominioLine.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_8.addWidget(self.SubDominioLine)

        self.SubDominioLine_2 = QLineEdit(self.widget_12)
        self.SubDominioLine_2.setObjectName(u"SubDominioLine_2")
        self.SubDominioLine_2.setEnabled(False)
        self.SubDominioLine_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.SubDominioLine_2)


        self.verticalLayout_6.addWidget(self.widget_12)


        self.verticalLayout_4.addWidget(self.widget_7)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 55))
        self.widget_4.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.EnviaDados = QPushButton(self.widget_4)
        self.EnviaDados.setObjectName(u"EnviaDados")

        self.horizontalLayout.addWidget(self.EnviaDados)

        self.CancelaEnvio = QPushButton(self.widget_4)
        self.CancelaEnvio.setObjectName(u"CancelaEnvio")

        self.horizontalLayout.addWidget(self.CancelaEnvio)


        self.verticalLayout_2.addWidget(self.widget_4)


        self.verticalLayout_7.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_16 = QWidget(self.page_2)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_9 = QVBoxLayout(self.widget_16)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget_16)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 140))
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.estabelecimento_logo = QLabel(self.widget_2)
        self.estabelecimento_logo.setObjectName(u"estabelecimento_logo")
        sizePolicy.setHeightForWidth(self.estabelecimento_logo.sizePolicy().hasHeightForWidth())
        self.estabelecimento_logo.setSizePolicy(sizePolicy)
        self.estabelecimento_logo.setMinimumSize(QSize(819, 120))
        self.estabelecimento_logo.setMaximumSize(QSize(16777215, 120))
        self.estabelecimento_logo.setStyleSheet(u"")
        self.estabelecimento_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.estabelecimento_logo)


        self.verticalLayout_9.addWidget(self.widget_2)

        self.widget_14 = QWidget(self.widget_16)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_orange = QPushButton(self.widget_14)
        self.btn_orange.setObjectName(u"btn_orange")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_orange.sizePolicy().hasHeightForWidth())
        self.btn_orange.setSizePolicy(sizePolicy4)
        self.btn_orange.setStyleSheet(u"background-color: #ffb14c;")

        self.horizontalLayout_10.addWidget(self.btn_orange)

        self.btn_green = QPushButton(self.widget_14)
        self.btn_green.setObjectName(u"btn_green")
        sizePolicy4.setHeightForWidth(self.btn_green.sizePolicy().hasHeightForWidth())
        self.btn_green.setSizePolicy(sizePolicy4)
        self.btn_green.setStyleSheet(u"background-color: #2ecc71;")

        self.horizontalLayout_10.addWidget(self.btn_green)

        self.btn_purple = QPushButton(self.widget_14)
        self.btn_purple.setObjectName(u"btn_purple")
        sizePolicy4.setHeightForWidth(self.btn_purple.sizePolicy().hasHeightForWidth())
        self.btn_purple.setSizePolicy(sizePolicy4)
        self.btn_purple.setStyleSheet(u"background-color: #a94dc1;")

        self.horizontalLayout_10.addWidget(self.btn_purple)

        self.btn_red = QPushButton(self.widget_14)
        self.btn_red.setObjectName(u"btn_red")
        sizePolicy4.setHeightForWidth(self.btn_red.sizePolicy().hasHeightForWidth())
        self.btn_red.setSizePolicy(sizePolicy4)
        self.btn_red.setStyleSheet(u"background-color: #e52c29;")

        self.horizontalLayout_10.addWidget(self.btn_red)


        self.verticalLayout_9.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.widget_16)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_10 = QVBoxLayout(self.widget_15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.cor_definida = QWidget(self.widget_15)
        self.cor_definida.setObjectName(u"cor_definida")
        self.cor_definida.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_10.addWidget(self.cor_definida)

        self.widget_18 = QWidget(self.widget_15)
        self.widget_18.setObjectName(u"widget_18")

        self.verticalLayout_10.addWidget(self.widget_18)

        self.widget_19 = QWidget(self.widget_15)
        self.widget_19.setObjectName(u"widget_19")

        self.verticalLayout_10.addWidget(self.widget_19)


        self.verticalLayout_9.addWidget(self.widget_15)


        self.verticalLayout_8.addWidget(self.widget_16)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_15 = QHBoxLayout(self.page_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.widget_25 = QWidget(self.page_3)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMaximumSize(QSize(410, 575))
        self.horizontalLayout_16 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_2 = QFrame(self.widget_25)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_34 = QWidget(self.frame_2)
        self.widget_34.setObjectName(u"widget_34")

        self.verticalLayout_15.addWidget(self.widget_34)

        self.widget_33 = QWidget(self.frame_2)
        self.widget_33.setObjectName(u"widget_33")

        self.verticalLayout_15.addWidget(self.widget_33)

        self.widget_32 = QWidget(self.frame_2)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setMinimumSize(QSize(0, 210))
        self.widget_32.setMaximumSize(QSize(16777215, 210))
        self.verticalLayout_16 = QVBoxLayout(self.widget_32)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.widget_35 = QWidget(self.widget_32)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setMaximumSize(QSize(16777215, 35))
        self.widget_35.setStyleSheet(u"")
        self.verticalLayout_17 = QVBoxLayout(self.widget_35)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_35)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_17.addWidget(self.label_10)


        self.verticalLayout_16.addWidget(self.widget_35)

        self.frame_3 = QFrame(self.widget_32)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setMinimumSize(QSize(0, 90))
        self.frame_3.setMaximumSize(QSize(16777215, 90))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.unique = QCheckBox(self.frame_3)
        self.unique.setObjectName(u"unique")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.unique.sizePolicy().hasHeightForWidth())
        self.unique.setSizePolicy(sizePolicy5)
        self.unique.setChecked(True)
        self.unique.setTristate(False)

        self.horizontalLayout_19.addWidget(self.unique)

        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setScaledContents(False)
        self.label_18.setWordWrap(True)

        self.horizontalLayout_19.addWidget(self.label_18)


        self.verticalLayout_16.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.widget_32)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setMinimumSize(QSize(0, 90))
        self.frame_4.setMaximumSize(QSize(16777215, 90))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.whatsapp = QCheckBox(self.frame_4)
        self.whatsapp.setObjectName(u"whatsapp")
        sizePolicy5.setHeightForWidth(self.whatsapp.sizePolicy().hasHeightForWidth())
        self.whatsapp.setSizePolicy(sizePolicy5)
        self.whatsapp.setTristate(False)

        self.horizontalLayout_20.addWidget(self.whatsapp)

        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setWordWrap(True)

        self.horizontalLayout_20.addWidget(self.label_19)


        self.verticalLayout_16.addWidget(self.frame_4)


        self.verticalLayout_15.addWidget(self.widget_32)


        self.horizontalLayout_16.addWidget(self.frame_2)


        self.horizontalLayout_15.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.page_3)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMaximumSize(QSize(410, 575))
        self.verticalLayout_13 = QVBoxLayout(self.widget_26)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_27 = QWidget(self.widget_26)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMinimumSize(QSize(0, 0))
        self.widget_27.setMaximumSize(QSize(16777215, 90))
        self.verticalLayout_14 = QVBoxLayout(self.widget_27)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_30 = QWidget(self.widget_27)
        self.widget_30.setObjectName(u"widget_30")

        self.verticalLayout_14.addWidget(self.widget_30)

        self.widget_31 = QWidget(self.widget_27)
        self.widget_31.setObjectName(u"widget_31")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn_adicionar = QPushButton(self.widget_31)
        self.btn_adicionar.setObjectName(u"btn_adicionar")

        self.horizontalLayout_18.addWidget(self.btn_adicionar)

        self.btn_editar = QPushButton(self.widget_31)
        self.btn_editar.setObjectName(u"btn_editar")

        self.horizontalLayout_18.addWidget(self.btn_editar)


        self.verticalLayout_14.addWidget(self.widget_31)


        self.verticalLayout_13.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_26)
        self.widget_28.setObjectName(u"widget_28")
        sizePolicy2.setHeightForWidth(self.widget_28.sizePolicy().hasHeightForWidth())
        self.widget_28.setSizePolicy(sizePolicy2)
        self.widget_28.setMaximumSize(QSize(410, 440))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.tableWidget = QTableWidget(self.widget_28)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy6)

        self.horizontalLayout_17.addWidget(self.tableWidget)


        self.verticalLayout_13.addWidget(self.widget_28)

        self.widget_29 = QWidget(self.widget_26)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMaximumSize(QSize(16777215, 45))

        self.verticalLayout_13.addWidget(self.widget_29)


        self.horizontalLayout_15.addWidget(self.widget_26)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.EnviaDados, self.CancelaEnvio)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_informacoes.setText(QCoreApplication.translate("MainWindow", u"INFORMA\u00c7\u00d5ES", None))
        self.btn_layout.setText(QCoreApplication.translate("MainWindow", u"LAYOUT E CORES", None))
        self.btn_horarios_config.setText(QCoreApplication.translate("MainWindow", u"HORARIOS E CONFIGURA\u00c7\u00d5ES", None))
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
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O", None))
        self.DescricaoLine.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"DATA CRIA\u00c7\u00c3O", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"DATA ATUALIZA\u00c7\u00c3O", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"DATA EXPIRA\u00c7\u00c3O", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"PLANO", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"LIMITE USUARIOS", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ATIVO", None))
        self.AtivoLine.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"SUBDOMINIO", None))
        self.SubDominioLine_2.setText(QCoreApplication.translate("MainWindow", u".uniqsystems.com.br", None))
        self.EnviaDados.setText(QCoreApplication.translate("MainWindow", u"ENVIAR", None))
        self.CancelaEnvio.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.estabelecimento_logo.setText(QCoreApplication.translate("MainWindow", u"CLIQUE DUAS VEZES PARA SELECIONAR O LOGO!!", None))
        self.btn_orange.setText("")
        self.btn_green.setText("")
        self.btn_purple.setText("")
        self.btn_red.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es de Canal - Pedidos", None))
        self.unique.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Ao selecionar est\u00e1 op\u00e7\u00e3o os atendimento realizados pelo catalago a online, passam a ser redirecionados para o sistema UNIQUE", None))
        self.whatsapp.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Ao selecionar est\u00e1 op\u00e7\u00e3o os atendimento realizados pelo catalago a online, passam a ser redirecionados para o WhatsApp", None))
        self.btn_adicionar.setText(QCoreApplication.translate("MainWindow", u"ADICIONAR", None))
        self.btn_editar.setText(QCoreApplication.translate("MainWindow", u"EDITAR", None))
    # retranslateUi

