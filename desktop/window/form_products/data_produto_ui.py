# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_produto.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)
from pictures import imagens_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 562)
        MainWindow.setMinimumSize(QSize(880, 562))
        MainWindow.setMaximumSize(QSize(880, 562))
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
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
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


        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 2)

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


        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.widget_4, 3, 1, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(80, 40))
        self.label_6.setMaximumSize(QSize(80, 55))

        self.horizontalLayout_3.addWidget(self.label_6)

        self.nome_input = QLineEdit(self.widget_2)
        self.nome_input.setObjectName(u"nome_input")
        self.nome_input.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.nome_input)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 45))
        self.label_13.setMaximumSize(QSize(16777215, 45))
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label_13)

        self.desc_input = QPlainTextEdit(self.widget_2)
        self.desc_input.setObjectName(u"desc_input")
        self.desc_input.setMaximumSize(QSize(167778, 167778))

        self.verticalLayout.addWidget(self.desc_input)


        self.gridLayout_2.addLayout(self.verticalLayout, 17, 0, 1, 3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.preco_venda_input = QLineEdit(self.widget_2)
        self.preco_venda_input.setObjectName(u"preco_venda_input")
        self.preco_venda_input.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.preco_venda_input)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout_6.addWidget(self.label_3)

        self.preco_custo_input = QLineEdit(self.widget_2)
        self.preco_custo_input.setObjectName(u"preco_custo_input")
        self.preco_custo_input.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.preco_custo_input)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 0, 1, 3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.categoria_combo = QComboBox(self.widget_2)
        self.categoria_combo.setObjectName(u"categoria_combo")
        self.categoria_combo.setMinimumSize(QSize(180, 0))
        self.categoria_combo.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.categoria_combo)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.cod_pdv_input = QLineEdit(self.widget_2)
        self.cod_pdv_input.setObjectName(u"cod_pdv_input")
        self.cod_pdv_input.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.cod_pdv_input)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.radioButton_4 = QRadioButton(self.widget_2)
        self.GroupStatus = QButtonGroup(MainWindow)
        self.GroupStatus.setObjectName(u"GroupStatus")
        self.GroupStatus.addButton(self.radioButton_4)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_9.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.widget_2)
        self.GroupStatus.addButton(self.radioButton_5)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout_9.addWidget(self.radioButton_5)


        self.gridLayout_2.addLayout(self.horizontalLayout_9, 16, 0, 1, 3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_7.addWidget(self.label_8)

        self.radioWidget = QWidget(self.widget_2)
        self.radioWidget.setObjectName(u"radioWidget")
        self.radioWidget.setMaximumSize(QSize(167778, 35))
        self.horizontalLayout_4 = QHBoxLayout(self.radioWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButton = QRadioButton(self.radioWidget)
        self.GroupMedida = QButtonGroup(MainWindow)
        self.GroupMedida.setObjectName(u"GroupMedida")
        self.GroupMedida.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_4.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.radioWidget)
        self.GroupMedida.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_4.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.radioWidget)
        self.GroupMedida.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_4.addWidget(self.radioButton_3)


        self.horizontalLayout_7.addWidget(self.radioWidget)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 14, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.Estoque_input = QLineEdit(self.widget_2)
        self.Estoque_input.setObjectName(u"Estoque_input")
        self.Estoque_input.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.Estoque_input)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.estoque_min_input = QLineEdit(self.widget_2)
        self.estoque_min_input.setObjectName(u"estoque_min_input")
        self.estoque_min_input.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.estoque_min_input)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 15, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 3, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 75))
        self.widget.setMaximumSize(QSize(16777215, 55))
        self.horizontalLayout_10 = QHBoxLayout(self.widget)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 15)
        self.atualizar_dados = QPushButton(self.widget)
        self.atualizar_dados.setObjectName(u"atualizar_dados")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.atualizar_dados.setFont(font)
        self.atualizar_dados.setStyleSheet(u"background-color: transparent;")
        icon = QIcon()
        icon.addFile(u":/unique/atualizar.png", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.atualizar_dados.setIcon(icon)
        self.atualizar_dados.setIconSize(QSize(40, 40))
        self.atualizar_dados.setAutoDefault(True)
        self.atualizar_dados.setFlat(True)

        self.horizontalLayout_10.addWidget(self.atualizar_dados)

        self.excluir_produtos = QPushButton(self.widget)
        self.excluir_produtos.setObjectName(u"excluir_produtos")
        self.excluir_produtos.setFont(font)
        self.excluir_produtos.setStyleSheet(u"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/unique/excluir.png", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.excluir_produtos.setIcon(icon1)
        self.excluir_produtos.setIconSize(QSize(40, 40))
        self.excluir_produtos.setAutoRepeat(False)
        self.excluir_produtos.setAutoDefault(True)
        self.excluir_produtos.setFlat(True)

        self.horizontalLayout_10.addWidget(self.excluir_produtos)


        self.gridLayout.addWidget(self.widget, 4, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.selecionar_imagem, self.limp_img)

        self.retranslateUi(MainWindow)

        self.atualizar_dados.setDefault(True)
        self.excluir_produtos.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PRODUTOS", None))
        self.image_label.setText("")
        self.selecionar_imagem.setText(QCoreApplication.translate("MainWindow", u"ALTERAR", None))
        self.limp_img.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o Venda", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o Custo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"C\u00f3d. PDV", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Ativo", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Pausado", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Medida", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"UN", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"KG", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"GR", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Estoque m\u00edn", None))
        self.atualizar_dados.setText(QCoreApplication.translate("MainWindow", u"ATUALIZAR", None))
        self.excluir_produtos.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
    # retranslateUi

