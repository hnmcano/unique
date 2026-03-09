# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'unique.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
from pictures import imagens_rc

class Ui_Unique(object):
    def setupUi(self, Unique):
        if not Unique.objectName():
            Unique.setObjectName(u"Unique")
        Unique.setWindowModality(Qt.WindowModality.WindowModal)
        Unique.resize(1087, 720)
        Unique.setMinimumSize(QSize(1086, 720))
        icon = QIcon()
        icon.addFile(u":/unique/icone.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Unique.setWindowIcon(icon)
        Unique.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Unique.setStyleSheet(u"")
        Unique.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        Unique.setIconSize(QSize(40, 40))
        self.estabelecimento = QAction(Unique)
        self.estabelecimento.setObjectName(u"estabelecimento")
        self.configuracoes = QAction(Unique)
        self.configuracoes.setObjectName(u"configuracoes")
        self.catalago = QAction(Unique)
        self.catalago.setObjectName(u"catalago")
        self.centralwidget = QWidget(Unique)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QSize(210, 16777215))
        self.widget.setStyleSheet(u"QWidget{\n"
"	background-color: #131314;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"    border: 1px solid rgb(75,75,65);\n"
"    padding-left: 22px;\n"
"    text-align: left;\n"
"    background-color: transparent;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(60,60,60);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(90,90,90);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border-left: 4px solid #ff2b2b;\n"
"    background-color: #1c1c1c;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 60))
        self.label_3.setPixmap(QPixmap(u":/unique/unique.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.btn_venda = QPushButton(self.widget)
        self.btn_venda.setObjectName(u"btn_venda")
        self.btn_venda.setMinimumSize(QSize(0, 45))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.btn_venda.setFont(font)
        self.btn_venda.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/unique/icons8-loja-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_venda.setIcon(icon1)
        self.btn_venda.setIconSize(QSize(30, 30))
        self.btn_venda.setCheckable(False)
        self.btn_venda.setChecked(False)
        self.btn_venda.setAutoDefault(False)
        self.btn_venda.setFlat(False)

        self.verticalLayout.addWidget(self.btn_venda)

        self.btn_relatorios = QPushButton(self.widget)
        self.btn_relatorios.setObjectName(u"btn_relatorios")
        self.btn_relatorios.setMinimumSize(QSize(0, 45))
        self.btn_relatorios.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/unique/icons8-relat\u00f3rio-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_relatorios.setIcon(icon2)
        self.btn_relatorios.setIconSize(QSize(30, 30))
        self.btn_relatorios.setAutoDefault(False)
        self.btn_relatorios.setFlat(False)

        self.verticalLayout.addWidget(self.btn_relatorios)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")

        self.verticalLayout.addWidget(self.widget_6)

        self.btn_loggout = QPushButton(self.widget)
        self.btn_loggout.setObjectName(u"btn_loggout")
        self.btn_loggout.setMinimumSize(QSize(0, 45))
        self.btn_loggout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_loggout.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/unique/sair.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_loggout.setIcon(icon3)
        self.btn_loggout.setIconSize(QSize(30, 30))
        self.btn_loggout.setAutoDefault(False)
        self.btn_loggout.setFlat(False)

        self.verticalLayout.addWidget(self.btn_loggout)


        self.horizontalLayout_2.addWidget(self.widget)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMaximumSize(QSize(16777215, 16777215))
        self.widget_3.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 6)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 40))
        self.widget_5.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")

        self.horizontalLayout_7.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_5)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget_9)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 5, 5, 5)

        self.horizontalLayout_12.addWidget(self.widget_2)

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.BemVindo = QLabel(self.widget_11)
        self.BemVindo.setObjectName(u"BemVindo")
        font1 = QFont()
        font1.setPointSize(14)
        self.BemVindo.setFont(font1)
        self.BemVindo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.BemVindo.setWordWrap(False)

        self.horizontalLayout_13.addWidget(self.BemVindo)

        self.label_2 = QLabel(self.widget_11)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(45, 45))
        self.label_2.setBaseSize(QSize(0, 0))
        self.label_2.setPixmap(QPixmap(u":/unique/user.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_2)


        self.horizontalLayout_12.addWidget(self.widget_11)


        self.horizontalLayout_7.addWidget(self.widget_9)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.StackedWidgetVendas = QStackedWidget(self.widget_3)
        self.StackedWidgetVendas.setObjectName(u"StackedWidgetVendas")
        self.StackedWidgetVendas.setEnabled(True)
        self.StackedWidgetVendas.setStyleSheet(u"QFrame {\n"
"	background-color: #131314;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	background-color: rgb(60,60,60);\n"
"}")
        self.WidgetRelatorios = QWidget()
        self.WidgetRelatorios.setObjectName(u"WidgetRelatorios")
        self.StackedWidgetVendas.addWidget(self.WidgetRelatorios)
        self.WidgetVendas = QWidget()
        self.WidgetVendas.setObjectName(u"WidgetVendas")
        self.gridLayout = QGridLayout(self.WidgetVendas)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.frame_8 = QFrame(self.WidgetVendas)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"#frame_8 {\n"
"    background-color: #131314;\n"
"    border-radius: 8px;\n"
"	padding: 8px;\n"
"}\n"
"\n"
"#frame_8:hover {\n"
"		background-color: rgb(60,60,60);\n"
"}\n"
"\n"
"#frame_8 QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frame_8 QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frame_8 QPushButton {\n"
"    background-color: red;\n"
"}\n"
"\n"
"#frame_8 QPushButton:hover {\n"
"    background-color: green;\n"
"}")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_12 = QWidget(self.frame_8)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_estabelecimento = QPushButton(self.widget_12)
        self.btn_estabelecimento.setObjectName(u"btn_estabelecimento")
        self.btn_estabelecimento.setMinimumSize(QSize(27, 27))
        self.btn_estabelecimento.setMaximumSize(QSize(45, 45))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setKerning(True)
        self.btn_estabelecimento.setFont(font2)
        self.btn_estabelecimento.setStyleSheet(u"")
        self.btn_estabelecimento.setIconSize(QSize(20, 16))

        self.horizontalLayout_5.addWidget(self.btn_estabelecimento)

        self.label_6 = QLabel(self.widget_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_6)


        self.verticalLayout_9.addWidget(self.widget_12)

        self.widget_36 = QWidget(self.frame_8)
        self.widget_36.setObjectName(u"widget_36")
        self.verticalLayout_26 = QVBoxLayout(self.widget_36)
        self.verticalLayout_26.setSpacing(20)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.widget_36)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(182, 100))
        self.label_40.setPixmap(QPixmap(u":/unique/loja.png"))
        self.label_40.setScaledContents(False)
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_40)

        self.widget_37 = QWidget(self.widget_36)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setStyleSheet(u"")
        self.verticalLayout_27 = QVBoxLayout(self.widget_37)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.widget_37)
        self.label_41.setObjectName(u"label_41")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_41.setFont(font3)

        self.verticalLayout_27.addWidget(self.label_41)

        self.label_42 = QLabel(self.widget_37)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(16777215, 20))
        self.label_42.setBaseSize(QSize(0, 0))
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        self.label_42.setFont(font4)
        self.label_42.setStyleSheet(u"color: rgb(126, 126, 126);")

        self.verticalLayout_27.addWidget(self.label_42)

        self.label_43 = QLabel(self.widget_37)
        self.label_43.setObjectName(u"label_43")

        self.verticalLayout_27.addWidget(self.label_43)


        self.verticalLayout_26.addWidget(self.widget_37)


        self.verticalLayout_9.addWidget(self.widget_36)


        self.gridLayout.addWidget(self.frame_8, 1, 3, 1, 1)

        self.frame_7 = QFrame(self.WidgetVendas)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"#frame_7 {\n"
"    background-color: #131314;\n"
"    border-radius: 8px;\n"
"	padding: 8px;\n"
"}\n"
"\n"
"#frame_7:hover {\n"
"		background-color: rgb(60,60,60);\n"
"}\n"
"\n"
"#frame_7 QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frame_7 QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frame_7 QPushButton {\n"
"    background-color: red;\n"
"}\n"
"\n"
"#frame_7 QPushButton:hover {\n"
"    background-color: green;\n"
"}")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_10 = QWidget(self.frame_7)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_funcionarios = QPushButton(self.widget_10)
        self.btn_funcionarios.setObjectName(u"btn_funcionarios")
        self.btn_funcionarios.setMinimumSize(QSize(27, 27))
        self.btn_funcionarios.setMaximumSize(QSize(45, 45))
        self.btn_funcionarios.setFont(font2)
        self.btn_funcionarios.setStyleSheet(u"")
        self.btn_funcionarios.setIconSize(QSize(20, 16))

        self.horizontalLayout_4.addWidget(self.btn_funcionarios)

        self.label_5 = QLabel(self.widget_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_5)


        self.verticalLayout_10.addWidget(self.widget_10)

        self.widget_34 = QWidget(self.frame_7)
        self.widget_34.setObjectName(u"widget_34")
        self.verticalLayout_24 = QVBoxLayout(self.widget_34)
        self.verticalLayout_24.setSpacing(20)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.widget_34)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(182, 100))
        self.label_39.setPixmap(QPixmap(u":/unique/funcionarios.png"))
        self.label_39.setScaledContents(False)
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_39)

        self.widget_35 = QWidget(self.widget_34)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setStyleSheet(u"")
        self.verticalLayout_25 = QVBoxLayout(self.widget_35)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.widget_35)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)

        self.verticalLayout_25.addWidget(self.label_27)

        self.label_28 = QLabel(self.widget_35)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(16777215, 20))
        self.label_28.setBaseSize(QSize(0, 0))
        self.label_28.setFont(font4)
        self.label_28.setStyleSheet(u"color: rgb(126, 126, 126);")

        self.verticalLayout_25.addWidget(self.label_28)

        self.label_29 = QLabel(self.widget_35)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_25.addWidget(self.label_29)


        self.verticalLayout_24.addWidget(self.widget_35)


        self.verticalLayout_10.addWidget(self.widget_34)


        self.gridLayout.addWidget(self.frame_7, 1, 2, 1, 1)

        self.frame_9 = QFrame(self.WidgetVendas)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setMaximumSize(QSize(16777215, 16777215))
        self.frame_9.setStyleSheet(u"#frame_9 {\n"
"    background-color: #131314;\n"
"    border-radius: 8px;\n"
"	padding: 8px;\n"
"}\n"
"\n"
"#frame_9:hover {\n"
"		background-color: rgb(60,60,60);\n"
"}\n"
"\n"
"#frame_9 QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frame_9 QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frame_9 QPushButton {\n"
"    background-color: red;\n"
"}\n"
"\n"
"#frame_9 QPushButton:hover {\n"
"    background-color: green;\n"
"}")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_14 = QWidget(self.frame_9)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, 0, 0)
        self.btn_config = QPushButton(self.widget_14)
        self.btn_config.setObjectName(u"btn_config")
        self.btn_config.setMinimumSize(QSize(27, 27))
        self.btn_config.setMaximumSize(QSize(45, 45))
        self.btn_config.setFont(font2)
        self.btn_config.setStyleSheet(u"")
        self.btn_config.setIconSize(QSize(20, 16))

        self.horizontalLayout_6.addWidget(self.btn_config)

        self.label_7 = QLabel(self.widget_14)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_7)


        self.verticalLayout_7.addWidget(self.widget_14)

        self.widget_32 = QWidget(self.frame_9)
        self.widget_32.setObjectName(u"widget_32")
        self.verticalLayout_22 = QVBoxLayout(self.widget_32)
        self.verticalLayout_22.setSpacing(20)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.widget_32)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(182, 100))
        self.label_36.setPixmap(QPixmap(u":/unique/configuracoes.png"))
        self.label_36.setScaledContents(False)
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_36)

        self.widget_33 = QWidget(self.widget_32)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setStyleSheet(u"")
        self.verticalLayout_23 = QVBoxLayout(self.widget_33)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.widget_33)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)

        self.verticalLayout_23.addWidget(self.label_30)

        self.label_37 = QLabel(self.widget_33)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(16777215, 20))
        self.label_37.setBaseSize(QSize(0, 0))
        self.label_37.setFont(font4)
        self.label_37.setStyleSheet(u"color: rgb(126, 126, 126);")

        self.verticalLayout_23.addWidget(self.label_37)

        self.label_38 = QLabel(self.widget_33)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_23.addWidget(self.label_38)


        self.verticalLayout_22.addWidget(self.widget_33)


        self.verticalLayout_7.addWidget(self.widget_32)


        self.gridLayout.addWidget(self.frame_9, 1, 4, 1, 1)

        self.frame_6 = QFrame(self.WidgetVendas)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"#frame_6 {\n"
"    background-color: #131314;\n"
"    border-radius: 8px;\n"
"	padding: 8px;\n"
"}\n"
"\n"
"#frame_6:hover {\n"
"		background-color: rgb(60,60,60);\n"
"}\n"
"\n"
"#frame_6 QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frame_6 QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frame_6 QPushButton {\n"
"    background-color: red;\n"
"}\n"
"\n"
"#frame_6 QPushButton:hover {\n"
"    background-color: green;\n"
"}")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_7 = QWidget(self.frame_6)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_caixa = QPushButton(self.widget_7)
        self.btn_caixa.setObjectName(u"btn_caixa")
        self.btn_caixa.setMinimumSize(QSize(27, 27))
        self.btn_caixa.setMaximumSize(QSize(45, 45))
        self.btn_caixa.setFont(font2)
        self.btn_caixa.setStyleSheet(u"")
        self.btn_caixa.setIconSize(QSize(20, 16))

        self.horizontalLayout_3.addWidget(self.btn_caixa)

        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout_8.addWidget(self.widget_7)

        self.widget_30 = QWidget(self.frame_6)
        self.widget_30.setObjectName(u"widget_30")
        self.verticalLayout_16 = QVBoxLayout(self.widget_30)
        self.verticalLayout_16.setSpacing(20)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.widget_30)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(182, 100))
        self.label_35.setPixmap(QPixmap(u":/unique/caixa-registradora.png"))
        self.label_35.setScaledContents(False)
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_35)

        self.widget_31 = QWidget(self.widget_30)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setStyleSheet(u"")
        self.verticalLayout_21 = QVBoxLayout(self.widget_31)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.widget_31)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font3)

        self.verticalLayout_21.addWidget(self.label_24)

        self.label_25 = QLabel(self.widget_31)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 20))
        self.label_25.setBaseSize(QSize(0, 0))
        self.label_25.setFont(font4)
        self.label_25.setStyleSheet(u"color: rgb(126, 126, 126);")

        self.verticalLayout_21.addWidget(self.label_25)

        self.label_26 = QLabel(self.widget_31)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_21.addWidget(self.label_26)


        self.verticalLayout_16.addWidget(self.widget_31)


        self.verticalLayout_8.addWidget(self.widget_30)


        self.gridLayout.addWidget(self.frame_6, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.WidgetVendas)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"#frame_5 {\n"
"    background-color: #131314;\n"
"    border-radius: 8px;\n"
"	padding: 8px;\n"
"}\n"
"\n"
"#frame_5:hover {\n"
"		background-color: rgb(60,60,60);\n"
"}\n"
"\n"
"#frame_5 QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frame_5 QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frame_5 QPushButton {\n"
"    background-color: red;\n"
"}\n"
"\n"
"#frame_5 QPushButton:hover {\n"
"    background-color: green;\n"
"}")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_16 = QWidget(self.frame_5)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_clientes = QPushButton(self.widget_16)
        self.btn_clientes.setObjectName(u"btn_clientes")
        self.btn_clientes.setMinimumSize(QSize(27, 27))
        self.btn_clientes.setMaximumSize(QSize(45, 45))
        self.btn_clientes.setFont(font2)
        self.btn_clientes.setStyleSheet(u"")
        self.btn_clientes.setIconSize(QSize(30, 30))

        self.horizontalLayout_11.addWidget(self.btn_clientes)

        self.label_11 = QLabel(self.widget_16)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_11)


        self.verticalLayout_6.addWidget(self.widget_16)

        self.widget_28 = QWidget(self.frame_5)
        self.widget_28.setObjectName(u"widget_28")
        self.verticalLayout_14 = QVBoxLayout(self.widget_28)
        self.verticalLayout_14.setSpacing(20)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.widget_28)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(182, 100))
        self.label_34.setPixmap(QPixmap(u":/unique/clientes.png"))
        self.label_34.setScaledContents(False)
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_34)

        self.widget_29 = QWidget(self.widget_28)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setStyleSheet(u"")
        self.verticalLayout_20 = QVBoxLayout(self.widget_29)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.widget_29)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)

        self.verticalLayout_20.addWidget(self.label_21)

        self.label_22 = QLabel(self.widget_29)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 20))
        self.label_22.setBaseSize(QSize(0, 0))
        self.label_22.setFont(font4)
        self.label_22.setStyleSheet(u"color: rgb(126, 126, 126);")

        self.verticalLayout_20.addWidget(self.label_22)

        self.label_23 = QLabel(self.widget_29)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_20.addWidget(self.label_23)


        self.verticalLayout_14.addWidget(self.widget_29)


        self.verticalLayout_6.addWidget(self.widget_28)


        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.WidgetVendas)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"#frame_4 {\n"
"    background-color: #131314;\n"
"    border-radius: 8px;\n"
"	padding: 8px;\n"
"}\n"
"\n"
"#frame_4:hover {\n"
"		background-color: rgb(60,60,60);\n"
"}\n"
"\n"
"#frame_4 QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frame_4 QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frame_4 QPushButton {\n"
"    background-color: red;\n"
"}\n"
"\n"
"#frame_4 QPushButton:hover {\n"
"    background-color: green;\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_18 = QWidget(self.frame_4)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMaximumSize(QSize(16777215, 35))
        self.widget_18.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_produtos = QPushButton(self.widget_18)
        self.btn_produtos.setObjectName(u"btn_produtos")
        self.btn_produtos.setMinimumSize(QSize(27, 27))
        self.btn_produtos.setMaximumSize(QSize(45, 45))
        self.btn_produtos.setFont(font2)
        self.btn_produtos.setStyleSheet(u"")
        self.btn_produtos.setIconSize(QSize(20, 16))

        self.horizontalLayout_10.addWidget(self.btn_produtos)

        self.label_10 = QLabel(self.widget_18)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_10)


        self.verticalLayout_5.addWidget(self.widget_18)

        self.widget_26 = QWidget(self.frame_4)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.widget_26)
        self.verticalLayout_13.setSpacing(20)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.widget_26)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(182, 100))
        self.label_33.setStyleSheet(u"")
        self.label_33.setPixmap(QPixmap(u":/unique/produtos.png"))
        self.label_33.setScaledContents(False)
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_33)

        self.widget_27 = QWidget(self.widget_26)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setStyleSheet(u"")
        self.verticalLayout_19 = QVBoxLayout(self.widget_27)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.widget_27)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"")

        self.verticalLayout_19.addWidget(self.label_18)

        self.label_19 = QLabel(self.widget_27)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 20))
        self.label_19.setBaseSize(QSize(0, 0))
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"color: rgb(126, 126, 126);")

        self.verticalLayout_19.addWidget(self.label_19)

        self.label_20 = QLabel(self.widget_27)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_19.addWidget(self.label_20)


        self.verticalLayout_13.addWidget(self.widget_27)


        self.verticalLayout_5.addWidget(self.widget_26)


        self.gridLayout.addWidget(self.frame_4, 0, 4, 1, 1)

        self.frame_3 = QFrame(self.WidgetVendas)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"#frame_3 {\n"
"    background-color: #131314;\n"
"    border-radius: 8px;\n"
"	padding: 8px;\n"
"}\n"
"\n"
"#frame_3:hover {\n"
"		background-color: rgb(60,60,60);\n"
"}\n"
"\n"
"#frame_3 QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frame_3 QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frame_3 QPushButton {\n"
"    background-color: red;\n"
"}\n"
"\n"
"#frame_3 QPushButton:hover {\n"
"    background-color: green;\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_20 = QWidget(self.frame_3)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMaximumSize(QSize(16777215, 35))
        self.widget_20.setStyleSheet(u"")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_delivery = QPushButton(self.widget_20)
        self.btn_delivery.setObjectName(u"btn_delivery")
        self.btn_delivery.setMinimumSize(QSize(27, 27))
        self.btn_delivery.setMaximumSize(QSize(45, 45))
        self.btn_delivery.setFont(font2)
        self.btn_delivery.setStyleSheet(u"")
        self.btn_delivery.setIconSize(QSize(20, 16))
        self.btn_delivery.setAutoDefault(True)

        self.horizontalLayout_9.addWidget(self.btn_delivery)

        self.label_9 = QLabel(self.widget_20)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_9)


        self.verticalLayout_4.addWidget(self.widget_20)

        self.widget_24 = QWidget(self.frame_3)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.widget_24)
        self.verticalLayout_12.setSpacing(20)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.widget_24)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(182, 100))
        self.label_32.setStyleSheet(u"")
        self.label_32.setPixmap(QPixmap(u":/unique/Entrega.png"))
        self.label_32.setScaledContents(False)
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_32)

        self.widget_25 = QWidget(self.widget_24)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.widget_25)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.widget_25)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.verticalLayout_18.addWidget(self.label_15)

        self.label_16 = QLabel(self.widget_25)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 20))
        self.label_16.setBaseSize(QSize(0, 0))
        self.label_16.setFont(font4)
        self.label_16.setStyleSheet(u"color: rgb(126, 126, 126);")

        self.verticalLayout_18.addWidget(self.label_16)

        self.label_17 = QLabel(self.widget_25)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.label_17)


        self.verticalLayout_12.addWidget(self.widget_25)


        self.verticalLayout_4.addWidget(self.widget_24)


        self.gridLayout.addWidget(self.frame_3, 0, 3, 1, 1)

        self.frame = QFrame(self.WidgetVendas)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame {\n"
"    background-color: #131314;\n"
"    border-radius: 8px;\n"
"	padding: 8px;\n"
"}\n"
"\n"
"#frame:hover {\n"
"		background-color: rgb(60,60,60);\n"
"}\n"
"\n"
"#frame QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frame QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frame QPushButton {\n"
"    background-color: red;\n"
"}\n"
"\n"
"#frame QPushButton:hover {\n"
"    background-color: green;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_22 = QWidget(self.frame)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMaximumSize(QSize(16777215, 35))
        self.widget_22.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_mesas = QPushButton(self.widget_22)
        self.btn_mesas.setObjectName(u"btn_mesas")
        self.btn_mesas.setMinimumSize(QSize(27, 27))
        self.btn_mesas.setMaximumSize(QSize(45, 45))
        self.btn_mesas.setFont(font2)
        self.btn_mesas.setStyleSheet(u"")
        self.btn_mesas.setIconSize(QSize(20, 16))

        self.horizontalLayout_8.addWidget(self.btn_mesas)

        self.label_8 = QLabel(self.widget_22)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_8)


        self.verticalLayout_3.addWidget(self.widget_22)

        self.widget_21 = QWidget(self.frame)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.widget_21)
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.widget_21)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(182, 100))
        self.label_31.setStyleSheet(u"")
        self.label_31.setPixmap(QPixmap(u":/unique/mesas.png"))
        self.label_31.setScaledContents(False)
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_31)

        self.widget_23 = QWidget(self.widget_21)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setStyleSheet(u"")
        self.verticalLayout_17 = QVBoxLayout(self.widget_23)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget_23)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.verticalLayout_17.addWidget(self.label_12)

        self.label_13 = QLabel(self.widget_23)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 20))
        self.label_13.setBaseSize(QSize(0, 0))
        self.label_13.setFont(font4)
        self.label_13.setStyleSheet(u"color: rgb(126, 126, 126);")

        self.verticalLayout_17.addWidget(self.label_13)

        self.label_14 = QLabel(self.widget_23)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_17.addWidget(self.label_14)


        self.verticalLayout_11.addWidget(self.widget_23)


        self.verticalLayout_3.addWidget(self.widget_21)


        self.gridLayout.addWidget(self.frame, 0, 2, 1, 1)

        self.StackedWidgetVendas.addWidget(self.WidgetVendas)

        self.verticalLayout_2.addWidget(self.StackedWidgetVendas)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 30))
        self.widget_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.IdUsuario = QLabel(self.widget_4)
        self.IdUsuario.setObjectName(u"IdUsuario")
        self.IdUsuario.setMinimumSize(QSize(0, 20))
        font5 = QFont()
        font5.setPointSize(12)
        self.IdUsuario.setFont(font5)
        self.IdUsuario.setStyleSheet(u"color: white;")

        self.horizontalLayout.addWidget(self.IdUsuario)

        self.labelStatus = QLabel(self.widget_4)
        self.labelStatus.setObjectName(u"labelStatus")
        self.labelStatus.setMaximumSize(QSize(1677777, 16777215))
        self.labelStatus.setFont(font5)
        self.labelStatus.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.labelStatus.setStyleSheet(u"")
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.labelStatus)


        self.verticalLayout_2.addWidget(self.widget_4)


        self.horizontalLayout_2.addWidget(self.widget_3)

        Unique.setCentralWidget(self.centralwidget)

        self.retranslateUi(Unique)

        self.btn_venda.setDefault(False)
        self.btn_relatorios.setDefault(False)
        self.btn_loggout.setDefault(False)
        self.StackedWidgetVendas.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Unique)
    # setupUi

    def retranslateUi(self, Unique):
        Unique.setWindowTitle(QCoreApplication.translate("Unique", u"UNIQUE", None))
        self.estabelecimento.setText(QCoreApplication.translate("Unique", u"ESTABELECIMENTO", None))
        self.configuracoes.setText(QCoreApplication.translate("Unique", u"CONFIGURA\u00c7\u00d5ES", None))
        self.catalago.setText(QCoreApplication.translate("Unique", u"CATALAGO", None))
        self.label_3.setText("")
        self.btn_venda.setText(QCoreApplication.translate("Unique", u"Vendas ", None))
        self.btn_relatorios.setText(QCoreApplication.translate("Unique", u"Relatorios", None))
        self.btn_loggout.setText(QCoreApplication.translate("Unique", u"Sair", None))
        self.BemVindo.setText("")
        self.label_2.setText("")
        self.btn_estabelecimento.setText(QCoreApplication.translate("Unique", u"+", None))
        self.label_6.setText("")
        self.label_40.setText("")
        self.label_41.setText(QCoreApplication.translate("Unique", u"Loja", None))
        self.label_42.setText(QCoreApplication.translate("Unique", u"Store", None))
        self.label_43.setText("")
        self.btn_funcionarios.setText(QCoreApplication.translate("Unique", u"+", None))
        self.label_5.setText("")
        self.label_39.setText("")
        self.label_27.setText(QCoreApplication.translate("Unique", u"Funcionarios", None))
        self.label_28.setText(QCoreApplication.translate("Unique", u"Employees", None))
        self.label_29.setText("")
        self.btn_config.setText(QCoreApplication.translate("Unique", u"+", None))
        self.label_7.setText("")
        self.label_36.setText("")
        self.label_30.setText(QCoreApplication.translate("Unique", u"Configura\u00e7\u00f5es", None))
        self.label_37.setText(QCoreApplication.translate("Unique", u"Settings", None))
        self.label_38.setText("")
        self.btn_caixa.setText(QCoreApplication.translate("Unique", u"+", None))
        self.label_4.setText("")
        self.label_35.setText("")
        self.label_24.setText(QCoreApplication.translate("Unique", u"Caixa Registradora", None))
        self.label_25.setText(QCoreApplication.translate("Unique", u"Cash register", None))
        self.label_26.setText("")
        self.btn_clientes.setText(QCoreApplication.translate("Unique", u"+", None))
        self.label_11.setText("")
        self.label_34.setText("")
        self.label_21.setText(QCoreApplication.translate("Unique", u"Clientes", None))
        self.label_22.setText(QCoreApplication.translate("Unique", u"Customers", None))
        self.label_23.setText("")
        self.btn_produtos.setText(QCoreApplication.translate("Unique", u"+", None))
        self.label_10.setText("")
        self.label_33.setText("")
        self.label_18.setText(QCoreApplication.translate("Unique", u"Produtos", None))
        self.label_19.setText(QCoreApplication.translate("Unique", u"Products", None))
        self.label_20.setText("")
        self.btn_delivery.setText(QCoreApplication.translate("Unique", u"+", None))
        self.label_9.setText("")
        self.label_32.setText("")
        self.label_15.setText(QCoreApplication.translate("Unique", u"Entregas", None))
        self.label_16.setText(QCoreApplication.translate("Unique", u"Delivery", None))
        self.label_17.setText("")
        self.btn_mesas.setText(QCoreApplication.translate("Unique", u"+", None))
        self.label_8.setText("")
        self.label_31.setText("")
        self.label_12.setText(QCoreApplication.translate("Unique", u"Mesas", None))
        self.label_13.setText(QCoreApplication.translate("Unique", u"Tables", None))
        self.label_14.setText("")
        self.IdUsuario.setText("")
        self.labelStatus.setText("")
    # retranslateUi

