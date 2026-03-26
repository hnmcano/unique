# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pedido_delivery.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1056, 590)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 590))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(980, 591))
        self.centralwidget.setMaximumSize(QSize(16777215, 590))
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_18 = QWidget(self.centralwidget)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(670, 0))
        self.widget_18.setMaximumSize(QSize(670, 580))
        self.verticalLayout_15 = QVBoxLayout(self.widget_18)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_18)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(540, 90))
        self.widget.setMaximumSize(QSize(16777215, 90))
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(380, 0))
        self.widget_7.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.mesa = QLabel(self.widget_7)
        self.mesa.setObjectName(u"mesa")
        self.mesa.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_7.addWidget(self.mesa)


        self.horizontalLayout_3.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(170, 16777215))
        self.widget_8.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_adicionar = QPushButton(self.widget_8)
        self.btn_adicionar.setObjectName(u"btn_adicionar")

        self.verticalLayout_4.addWidget(self.btn_adicionar)


        self.horizontalLayout_3.addWidget(self.widget_8)


        self.verticalLayout_15.addWidget(self.widget)

        self.widget_2 = QWidget(self.widget_18)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(170, 490))
        self.widget_3.setMaximumSize(QSize(170, 501))
        self.widget_3.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.status = QLabel(self.widget_6)
        self.status.setObjectName(u"status")
        self.status.setMaximumSize(QSize(16777215, 45))
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.status)

        self.data_criacao = QLineEdit(self.widget_6)
        self.data_criacao.setObjectName(u"data_criacao")

        self.verticalLayout_6.addWidget(self.data_criacao)

        self.widget_11 = QWidget(self.widget_6)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_13 = QVBoxLayout(self.widget_11)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.widget_11)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.widget_17)

        self.widget_16 = QWidget(self.widget_11)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.widget_16)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_16)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 25))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_3)

        self.taxa_entrega = QLabel(self.widget_16)
        self.taxa_entrega.setObjectName(u"taxa_entrega")
        self.taxa_entrega.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.taxa_entrega)


        self.verticalLayout_13.addWidget(self.widget_16)


        self.verticalLayout_6.addWidget(self.widget_11)

        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.widget_10)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.widget_10)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_9 = QVBoxLayout(self.widget_12)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_12)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label)

        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_11 = QVBoxLayout(self.widget_14)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.quantidade_itens_mesa = QLabel(self.widget_14)
        self.quantidade_itens_mesa.setObjectName(u"quantidade_itens_mesa")
        self.quantidade_itens_mesa.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.quantidade_itens_mesa)


        self.verticalLayout_9.addWidget(self.widget_14)


        self.verticalLayout_8.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.widget_10)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_10 = QVBoxLayout(self.widget_13)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_13)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 25))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_2)

        self.widget_15 = QWidget(self.widget_13)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_12 = QVBoxLayout(self.widget_15)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.valor_total_mesa = QLabel(self.widget_15)
        self.valor_total_mesa.setObjectName(u"valor_total_mesa")
        self.valor_total_mesa.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.valor_total_mesa)


        self.verticalLayout_10.addWidget(self.widget_15)


        self.verticalLayout_8.addWidget(self.widget_13)


        self.verticalLayout_6.addWidget(self.widget_10)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 80))
        self.widget_5.setMaximumSize(QSize(16777215, 80))
        self.widget_5.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_excluir = QPushButton(self.widget_5)
        self.btn_excluir.setObjectName(u"btn_excluir")

        self.verticalLayout_3.addWidget(self.btn_excluir)


        self.verticalLayout_2.addWidget(self.widget_5)


        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 501))
        self.widget_4.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.widget_4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(16777215, 415))
        self.tableWidget.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.tableWidget)

        self.widget_9 = QWidget(self.widget_4)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 80))
        self.widget_9.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_finalizar = QPushButton(self.widget_9)
        self.btn_finalizar.setObjectName(u"btn_finalizar")

        self.horizontalLayout_2.addWidget(self.btn_finalizar)

        self.btn_imprimir = QPushButton(self.widget_9)
        self.btn_imprimir.setObjectName(u"btn_imprimir")

        self.horizontalLayout_2.addWidget(self.btn_imprimir)


        self.verticalLayout_5.addWidget(self.widget_9)


        self.horizontalLayout.addWidget(self.widget_4)


        self.verticalLayout_15.addWidget(self.widget_2)


        self.horizontalLayout_4.addWidget(self.widget_18)

        self.widget_19 = QWidget(self.centralwidget)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget_19)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, -1, -1)
        self.widget_20 = QWidget(self.widget_19)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMaximumSize(QSize(16777215, 120))
        self.widget_20.setStyleSheet(u"#widget_20 {\n"
"	background-color: #2d2d2d;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"#widget_23 {\n"
"	border-bottom: 1px solid grey;\n"
"}\n"
"\n"
"#widget_24 {\n"
"	border-bottom: 1px solid grey;\n"
"}\n"
"\n"
"#widget_25 {\n"
"	border-bottom: 1px solid grey;\n"
"}")
        self.verticalLayout_16 = QVBoxLayout(self.widget_20)
        self.verticalLayout_16.setSpacing(2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(9, -1, 9, -1)
        self.widget_23 = QWidget(self.widget_20)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_23)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_4.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.label_cliente = QLabel(self.widget_23)
        self.label_cliente.setObjectName(u"label_cliente")
        self.label_cliente.setStyleSheet(u"")
        self.label_cliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_cliente)


        self.verticalLayout_16.addWidget(self.widget_23)

        self.widget_24 = QWidget(self.widget_20)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_24)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.label_telefone = QLabel(self.widget_24)
        self.label_telefone.setObjectName(u"label_telefone")
        self.label_telefone.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_telefone)


        self.verticalLayout_16.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.widget_20)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_25)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.label_email = QLabel(self.widget_25)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_email)


        self.verticalLayout_16.addWidget(self.widget_25)


        self.verticalLayout.addWidget(self.widget_20)

        self.widget_21 = QWidget(self.widget_19)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMaximumSize(QSize(16777215, 220))
        font1 = QFont()
        font1.setWeight(QFont.Thin)
        self.widget_21.setFont(font1)
        self.widget_21.setStyleSheet(u"#widget_21 {\n"
"	background-color: #2d2d2d;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"#widget_26 {\n"
"	border-bottom: 1px solid grey;\n"
"}\n"
"\n"
"#widget_27 {\n"
"	border-bottom: 1px solid grey;\n"
"}\n"
"\n"
"#widget_28 {\n"
"	border-bottom: 1px solid grey;\n"
"}\n"
"\n"
"#widget_29 {\n"
"	border-bottom: 1px solid grey;\n"
"}\n"
"\n"
"#widget_30 {\n"
"	border-bottom: 1px solid grey;\n"
"}")
        self.verticalLayout_17 = QVBoxLayout(self.widget_21)
        self.verticalLayout_17.setSpacing(2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_26 = QWidget(self.widget_21)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_8.setSpacing(9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget_26)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.label_cep = QLabel(self.widget_26)
        self.label_cep.setObjectName(u"label_cep")
        self.label_cep.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_cep)


        self.verticalLayout_17.addWidget(self.widget_26)

        self.widget_27 = QWidget(self.widget_21)
        self.widget_27.setObjectName(u"widget_27")
        font2 = QFont()
        font2.setBold(False)
        self.widget_27.setFont(font2)
        self.widget_27.setStyleSheet(u"")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_9.setSpacing(9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_27)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.label_rua = QLabel(self.widget_27)
        self.label_rua.setObjectName(u"label_rua")
        self.label_rua.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_rua)

        self.label_12 = QLabel(self.widget_27)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_12)

        self.label_numero = QLabel(self.widget_27)
        self.label_numero.setObjectName(u"label_numero")
        self.label_numero.setMaximumSize(QSize(70, 16777215))
        self.label_numero.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_numero)


        self.verticalLayout_17.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_21)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_10.setSpacing(9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_28)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.label_complemento = QLabel(self.widget_28)
        self.label_complemento.setObjectName(u"label_complemento")
        self.label_complemento.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_complemento)


        self.verticalLayout_17.addWidget(self.widget_28)

        self.widget_29 = QWidget(self.widget_21)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setStyleSheet(u"")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_11.setSpacing(9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_29)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setFont(font)
        self.label_10.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.label_bairro = QLabel(self.widget_29)
        self.label_bairro.setObjectName(u"label_bairro")
        self.label_bairro.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_bairro)


        self.verticalLayout_17.addWidget(self.widget_29)

        self.widget_30 = QWidget(self.widget_21)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setStyleSheet(u"")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_30)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_12.addWidget(self.label_11)

        self.label_cidade = QLabel(self.widget_30)
        self.label_cidade.setObjectName(u"label_cidade")
        self.label_cidade.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_cidade)


        self.verticalLayout_17.addWidget(self.widget_30)


        self.verticalLayout.addWidget(self.widget_21)

        self.widget_22 = QWidget(self.widget_19)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMaximumSize(QSize(16777215, 232))
        self.widget_22.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.widget_22)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_13 = QLabel(self.widget_22)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setFont(font)

        self.verticalLayout_18.addWidget(self.label_13)

        self.plainTextEdit = QPlainTextEdit(self.widget_22)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy2)
        self.plainTextEdit.setStyleSheet(u"border-radius: 20px;\n"
"padding: 10px;\n"
"background-color: #2d2d2d;")

        self.verticalLayout_18.addWidget(self.plainTextEdit)


        self.verticalLayout.addWidget(self.widget_22)


        self.horizontalLayout_4.addWidget(self.widget_19)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PEDIDOS EM MESA", None))
        self.mesa.setText("")
        self.btn_adicionar.setText(QCoreApplication.translate("MainWindow", u"ADD PRODUTO", None))
        self.status.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TAXA DE ENTREGA", None))
        self.taxa_entrega.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"QUANTIDADE ITENS", None))
        self.quantidade_itens_mesa.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TOTAL MESA", None))
        self.valor_total_mesa.setText("")
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        self.btn_finalizar.setText(QCoreApplication.translate("MainWindow", u"FINALIZAR", None))
        self.btn_imprimir.setText(QCoreApplication.translate("MainWindow", u"IMPRIMIR", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_cliente.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.label_telefone.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"E-mail:", None))
        self.label_email.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Cep:", None))
        self.label_cep.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Rua:", None))
        self.label_rua.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"N\u00ba:", None))
        self.label_numero.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Comp.:", None))
        self.label_complemento.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Bairro:", None))
        self.label_bairro.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Cidade:", None))
        self.label_cidade.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es:", None))
    # retranslateUi

