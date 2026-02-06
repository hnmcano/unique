# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientes.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(456, 600)
        MainWindow.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border: transparent;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Monotype Corsiva"])
        font.setPointSize(45)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        self.frame_2.setPalette(palette)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setSpacing(9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.label_nome = QLabel(self.frame_2)
        self.label_nome.setObjectName(u"label_nome")

        self.gridLayout_2.addWidget(self.label_nome, 0, 0, 1, 1)

        self.label_telefone = QLabel(self.frame_2)
        self.label_telefone.setObjectName(u"label_telefone")

        self.gridLayout_2.addWidget(self.label_telefone, 1, 0, 1, 1)

        self.email_input = QLineEdit(self.frame_2)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.email_input, 3, 1, 1, 1)

        self.label_email = QLabel(self.frame_2)
        self.label_email.setObjectName(u"label_email")

        self.gridLayout_2.addWidget(self.label_email, 3, 0, 1, 1)

        self.nome_input = QLineEdit(self.frame_2)
        self.nome_input.setObjectName(u"nome_input")
        self.nome_input.setStyleSheet(u"")
        self.nome_input.setCursorPosition(0)

        self.gridLayout_2.addWidget(self.nome_input, 0, 1, 1, 1)

        self.telefone_input = QLineEdit(self.frame_2)
        self.telefone_input.setObjectName(u"telefone_input")
        self.telefone_input.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.telefone_input, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_25 = QLabel(self.frame_3)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout.addWidget(self.label_25)

        self.cepinput = QLineEdit(self.frame_3)
        self.cepinput.setObjectName(u"cepinput")
        self.cepinput.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.cepinput)

        self.btn_viacep = QPushButton(self.frame_3)
        self.btn_viacep.setObjectName(u"btn_viacep")
        self.btn_viacep.setEnabled(True)
        self.btn_viacep.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_viacep)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(9, -1, -1, -1)
        self.referencia_input = QLineEdit(self.frame)
        self.referencia_input.setObjectName(u"referencia_input")

        self.gridLayout_3.addWidget(self.referencia_input, 10, 1, 1, 1)

        self.complemento_input = QLineEdit(self.frame)
        self.complemento_input.setObjectName(u"complemento_input")
        self.complemento_input.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.complemento_input, 9, 1, 1, 1)

        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 2, 0, 1, 1)

        self.label_30 = QLabel(self.frame)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_3.addWidget(self.label_30, 7, 0, 1, 1)

        self.cidade_input = QLineEdit(self.frame)
        self.cidade_input.setObjectName(u"cidade_input")
        self.cidade_input.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.cidade_input, 7, 1, 1, 1)

        self.label_27 = QLabel(self.frame)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_3.addWidget(self.label_27, 6, 0, 1, 1)

        self.label_28 = QLabel(self.frame)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_3.addWidget(self.label_28, 9, 0, 1, 1)

        self.bairro_input = QLineEdit(self.frame)
        self.bairro_input.setObjectName(u"bairro_input")
        self.bairro_input.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.bairro_input, 6, 1, 1, 1)

        self.endereco_input = QLineEdit(self.frame)
        self.endereco_input.setObjectName(u"endereco_input")
        self.endereco_input.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.endereco_input, 2, 1, 1, 1)

        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_3.addWidget(self.label_29, 10, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 75))
        self.widget_3.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cad_clientes = QPushButton(self.widget_3)
        self.cad_clientes.setObjectName(u"cad_clientes")
        self.cad_clientes.setStyleSheet(u"")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ContactNew))
        self.cad_clientes.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.cad_clientes)

        self.cancelar = QPushButton(self.widget_3)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setStyleSheet(u"")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.cancelar.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.cancelar)


        self.verticalLayout.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_3.raise_()
        self.label.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.widget_3.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CADASTRAR CLIENTES", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Clientes", None))
        self.label_nome.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_telefone.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"E-mail:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Cep:", None))
        self.cepinput.setText("")
        self.cepinput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu CEP aqui...", None))
        self.btn_viacep.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Cidade:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Bairro:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Complemento:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Ref:", None))
        self.cad_clientes.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Cliente", None))
        self.cancelar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi

