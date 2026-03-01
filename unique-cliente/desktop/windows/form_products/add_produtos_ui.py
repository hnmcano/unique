# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_produtos.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(646, 546)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(1731691, 16777215))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(300, 0))
        self.widget_4.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.widget_4)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 75))
        self.frame.setStyleSheet(u"")
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.image_label = QLabel(self.frame_2)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setMaximumSize(QSize(310, 378))
        self.image_label.setStyleSheet(u"")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.image_label)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 3)

        self.frame_3 = QFrame(self.widget_4)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QSize(16777215, 75))
        self.frame_3.setStyleSheet(u"")
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


        self.gridLayout.addWidget(self.widget_4, 3, 1, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMaximumSize(QSize(16777215, 75))
        self.widget_3.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.add_produto = QPushButton(self.widget_3)
        self.add_produto.setObjectName(u"add_produto")
        self.add_produto.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.add_produto, 0, 0, 1, 1)

        self.cancelar = QPushButton(self.widget_3)
        self.cancelar.setObjectName(u"cancelar")

        self.gridLayout_4.addWidget(self.cancelar, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 4, 0, 1, 2)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 9, 0, 0)
        self.nome_input = QLineEdit(self.widget_2)
        self.nome_input.setObjectName(u"nome_input")
        self.nome_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.nome_input, 8, 2, 1, 1)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 8, 0, 1, 1)

        self.preco_venda_input = QLineEdit(self.widget_2)
        self.preco_venda_input.setObjectName(u"preco_venda_input")
        self.preco_venda_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.preco_venda_input, 10, 2, 1, 1)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.estoque_min_input = QLineEdit(self.widget_2)
        self.estoque_min_input.setObjectName(u"estoque_min_input")
        self.estoque_min_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.estoque_min_input, 13, 2, 1, 1)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 13, 0, 1, 1)

        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_2.addWidget(self.label_13, 14, 0, 1, 1)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 7, 0, 1, 1)

        self.preco_custo_input = QLineEdit(self.widget_2)
        self.preco_custo_input.setObjectName(u"preco_custo_input")
        self.preco_custo_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.preco_custo_input, 9, 2, 1, 1)

        self.categoria_combo = QComboBox(self.widget_2)
        self.categoria_combo.setObjectName(u"categoria_combo")
        self.categoria_combo.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.categoria_combo, 7, 2, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(130, 16777215))

        self.gridLayout_2.addWidget(self.label_3, 9, 0, 1, 1)

        self.Estoque_input = QLineEdit(self.widget_2)
        self.Estoque_input.setObjectName(u"Estoque_input")
        self.Estoque_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.Estoque_input, 12, 2, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 12, 0, 1, 1)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 11, 0, 1, 1)

        self.cod_pdv_input = QLineEdit(self.widget_2)
        self.cod_pdv_input.setObjectName(u"cod_pdv_input")
        self.cod_pdv_input.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_2.addWidget(self.cod_pdv_input, 2, 2, 1, 1)

        self.desc_input = QPlainTextEdit(self.widget_2)
        self.desc_input.setObjectName(u"desc_input")
        self.desc_input.setMaximumSize(QSize(240, 150))

        self.gridLayout_2.addWidget(self.desc_input, 14, 2, 1, 1)

        self.label_12 = QLabel(self.widget_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 10, 0, 1, 1)

        self.radioWidget = QWidget(self.widget_2)
        self.radioWidget.setObjectName(u"radioWidget")
        self.radioWidget.setMaximumSize(QSize(240, 35))
        self.horizontalLayout_4 = QHBoxLayout(self.radioWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButton = QRadioButton(self.radioWidget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_4.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.radioWidget)
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_4.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.radioWidget)
        self.buttonGroup.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_4.addWidget(self.radioButton_3)


        self.gridLayout_2.addWidget(self.radioWidget, 11, 2, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.cod_pdv_input, self.nome_input)
        QWidget.setTabOrder(self.nome_input, self.preco_custo_input)
        QWidget.setTabOrder(self.preco_custo_input, self.preco_venda_input)
        QWidget.setTabOrder(self.preco_venda_input, self.Estoque_input)
        QWidget.setTabOrder(self.Estoque_input, self.estoque_min_input)
        QWidget.setTabOrder(self.estoque_min_input, self.selecionar_imagem)
        QWidget.setTabOrder(self.selecionar_imagem, self.limp_img)
        QWidget.setTabOrder(self.limp_img, self.add_produto)
        QWidget.setTabOrder(self.add_produto, self.cancelar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CADASTRO DE PRODUTOS", None))
        self.selecionar_imagem.setText(QCoreApplication.translate("MainWindow", u"Selecionar imagem", None))
        self.limp_img.setText(QCoreApplication.translate("MainWindow", u"Excluir Foto", None))
        self.image_label.setText("")
        self.add_categoria.setText(QCoreApplication.translate("MainWindow", u"ADD CATEGORIA", None))
        self.add_produto.setText(QCoreApplication.translate("MainWindow", u"Adicionar Produto", None))
        self.cancelar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"C\u00f3d. PDV", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Estoque m\u00edn", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o Custo", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Medida", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o Venda", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"UN", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"KG", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"GR", None))
    # retranslateUi

