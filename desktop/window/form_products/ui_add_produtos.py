# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Produtos.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(661, 766)
        MainWindow.setMinimumSize(QSize(620, 698))
        MainWindow.setMaximumSize(QSize(1731691, 16777215))
        MainWindow.setStyleSheet(u"QLineEdit, QComboBox{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 4px 2px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLineEdit, QComboBox:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QLineEdit, QComboBox:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 5px 17px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4"
                        "e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}\n"
"\n"
"QTextEdit{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 4px 2px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 10px;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QTextEdit:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 9, 0, 0)
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 18, 0, 1, 1)

        self.preco_venda_input = QLineEdit(self.widget_2)
        self.preco_venda_input.setObjectName(u"preco_venda_input")
        self.preco_venda_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.preco_venda_input, 11, 2, 1, 1)

        self.cod_sistema_input = QLineEdit(self.widget_2)
        self.cod_sistema_input.setObjectName(u"cod_sistema_input")
        self.cod_sistema_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.cod_sistema_input, 2, 2, 1, 1)

        self.estoque_min_input = QLineEdit(self.widget_2)
        self.estoque_min_input.setObjectName(u"estoque_min_input")
        self.estoque_min_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.estoque_min_input, 14, 2, 1, 1)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 9, 0, 1, 1)

        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_2.addWidget(self.label_13, 15, 0, 1, 1)

        self.sit_estoque_input = QLineEdit(self.widget_2)
        self.sit_estoque_input.setObjectName(u"sit_estoque_input")
        self.sit_estoque_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.sit_estoque_input, 16, 2, 1, 1)

        self.label_12 = QLabel(self.widget_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 11, 0, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(130, 16777215))

        self.gridLayout_2.addWidget(self.label_3, 10, 0, 1, 1)

        self.desc_input = QLineEdit(self.widget_2)
        self.desc_input.setObjectName(u"desc_input")
        self.desc_input.setMinimumSize(QSize(240, 130))
        self.desc_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.desc_input, 15, 2, 1, 1)

        self.Estoque_input = QLineEdit(self.widget_2)
        self.Estoque_input.setObjectName(u"Estoque_input")
        self.Estoque_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.Estoque_input, 13, 2, 1, 1)

        self.Medida_input = QLineEdit(self.widget_2)
        self.Medida_input.setObjectName(u"Medida_input")
        self.Medida_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.Medida_input, 12, 2, 1, 1)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 8, 0, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 13, 0, 1, 1)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 16, 0, 1, 1)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 14, 0, 1, 1)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 12, 0, 1, 1)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 17, 0, 1, 1)

        self.ficha_tec_input = QLineEdit(self.widget_2)
        self.ficha_tec_input.setObjectName(u"ficha_tec_input")
        self.ficha_tec_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.ficha_tec_input, 17, 2, 1, 1)

        self.nome_input = QLineEdit(self.widget_2)
        self.nome_input.setObjectName(u"nome_input")
        self.nome_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.nome_input, 9, 2, 1, 1)

        self.status_venda_input = QLineEdit(self.widget_2)
        self.status_venda_input.setObjectName(u"status_venda_input")
        self.status_venda_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.status_venda_input, 18, 2, 1, 1)

        self.preco_custo_input = QLineEdit(self.widget_2)
        self.preco_custo_input.setObjectName(u"preco_custo_input")
        self.preco_custo_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.preco_custo_input, 10, 2, 1, 1)

        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)

        self.cod_pdv_input = QLineEdit(self.widget_2)
        self.cod_pdv_input.setObjectName(u"cod_pdv_input")
        self.cod_pdv_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.cod_pdv_input, 3, 2, 1, 1)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)

        self.categoria_combo = QComboBox(self.widget_2)
        self.categoria_combo.setObjectName(u"categoria_combo")
        self.categoria_combo.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.categoria_combo, 8, 2, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 4, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QSize(16777215, 90))
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 0);\n"
"    border-bottom: 1px solid red;\n"
"    \n"
"    /* Gradiente para profundidade */\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, \n"
"        stop: 0.5 #000000,\n"
"        stop: 1 #000000);\n"
"    \n"
"    /* Sombra externa para efeito 3D */\n"
"    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.2),\n"
"                -1px -1px 2px rgba(255, 255, 255, 0.3);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        font = QFont()
        font.setFamilies([u"Monotype Corsiva"])
        font.setPointSize(45)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_14)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 2)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMaximumSize(QSize(16777215, 75))
        self.widget_3.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 5px 17px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.add_produto = QPushButton(self.widget_3)
        self.add_produto.setObjectName(u"add_produto")
        self.add_produto.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.add_produto, 0, 0, 1, 1)

        self.atual_produto = QPushButton(self.widget_3)
        self.atual_produto.setObjectName(u"atual_produto")

        self.gridLayout_4.addWidget(self.atual_produto, 0, 1, 1, 1)

        self.cancelar = QPushButton(self.widget_3)
        self.cancelar.setObjectName(u"cancelar")

        self.gridLayout_4.addWidget(self.cancelar, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 5, 0, 1, 2)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(300, 0))
        self.widget_4.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.widget_4)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 75))
        self.frame.setStyleSheet(u"\n"
"QPushButton, QFrame {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 5px 17px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.selecionar_imagem = QPushButton(self.frame)
        self.selecionar_imagem.setObjectName(u"selecionar_imagem")

        self.horizontalLayout.addWidget(self.selecionar_imagem)

        self.limp_img = QPushButton(self.frame)
        self.limp_img.setObjectName(u"limp_img")

        self.horizontalLayout.addWidget(self.limp_img)


        self.gridLayout_3.addWidget(self.frame, 2, 0, 1, 3)

        self.frame_2 = QFrame(self.widget_4)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"border: 1px solid red;\n"
"border-radius: 8px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.image_label = QLabel(self.frame_2)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setMaximumSize(QSize(310, 378))
        self.image_label.setStyleSheet(u"border: 1px solid red;\n"
"border-radius: 8px;")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.image_label)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 3)

        self.frame_3 = QFrame(self.widget_4)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QSize(16777215, 75))
        self.frame_3.setStyleSheet(u"\n"
"QPushButton, QFrame {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 5px 17px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.add_categoria = QPushButton(self.frame_3)
        self.add_categoria.setObjectName(u"add_categoria")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.add_categoria.setIcon(icon)
        self.add_categoria.setIconSize(QSize(14, 32))

        self.horizontalLayout_3.addWidget(self.add_categoria)


        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 3)


        self.gridLayout.addWidget(self.widget_4, 4, 1, 1, 1)

        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 30))
        self.widget_5.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 0);\n"
"    border-top: 1px solid red;\n"
"    \n"
"    /* Gradiente para profundidade */\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, \n"
"        stop: 0.5 #000000,\n"
"        stop: 1 #000000);\n"
"    \n"
"    /* Sombra externa para efeito 3D */\n"
"    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.2),\n"
"                -1px -1px 2px rgba(255, 255, 255, 0.3);\n"
"}")

        self.gridLayout.addWidget(self.widget_5, 6, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.cod_sistema_input, self.cod_pdv_input)
        QWidget.setTabOrder(self.cod_pdv_input, self.nome_input)
        QWidget.setTabOrder(self.nome_input, self.preco_custo_input)
        QWidget.setTabOrder(self.preco_custo_input, self.preco_venda_input)
        QWidget.setTabOrder(self.preco_venda_input, self.Medida_input)
        QWidget.setTabOrder(self.Medida_input, self.Estoque_input)
        QWidget.setTabOrder(self.Estoque_input, self.estoque_min_input)
        QWidget.setTabOrder(self.estoque_min_input, self.desc_input)
        QWidget.setTabOrder(self.desc_input, self.sit_estoque_input)
        QWidget.setTabOrder(self.sit_estoque_input, self.ficha_tec_input)
        QWidget.setTabOrder(self.ficha_tec_input, self.status_venda_input)
        QWidget.setTabOrder(self.status_venda_input, self.selecionar_imagem)
        QWidget.setTabOrder(self.selecionar_imagem, self.limp_img)
        QWidget.setTabOrder(self.limp_img, self.add_produto)
        QWidget.setTabOrder(self.add_produto, self.atual_produto)
        QWidget.setTabOrder(self.atual_produto, self.cancelar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Status Venda", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o Venda", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o Custo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sit Estoque", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Estoque m\u00edn", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Medida", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Ficha Tenica", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"C\u00f3d. Sistema", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"C\u00f3d. PDV", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Produtos", None))
        self.add_produto.setText(QCoreApplication.translate("MainWindow", u"Adicionar Produto", None))
        self.atual_produto.setText(QCoreApplication.translate("MainWindow", u"Atualizar Produto", None))
        self.cancelar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.selecionar_imagem.setText(QCoreApplication.translate("MainWindow", u"Selecionar imagem", None))
        self.limp_img.setText(QCoreApplication.translate("MainWindow", u"Excluir Foto", None))
        self.image_label.setText("")
        self.add_categoria.setText(QCoreApplication.translate("MainWindow", u"ADD CATEGORIA", None))
    # retranslateUi

