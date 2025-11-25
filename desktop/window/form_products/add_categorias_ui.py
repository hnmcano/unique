# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_categorias.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Category(object):
    def setupUi(self, Category):
        if not Category.objectName():
            Category.setObjectName(u"Category")
        Category.resize(812, 159)
        Category.setMinimumSize(QSize(812, 159))
        Category.setMaximumSize(QSize(812, 159))
        Category.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: transparent;\n"
"	border: transparent;	\n"
"\n"
"}")
        self.centralwidget = QWidget(Category)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(130, 0))
        self.widget.setMaximumSize(QSize(130, 16777215))
        self.widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.adicionar_botao = QPushButton(self.widget)
        self.adicionar_botao.setObjectName(u"adicionar_botao")
        self.adicionar_botao.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.adicionar_botao)

        self.modificar_botao = QPushButton(self.widget)
        self.modificar_botao.setObjectName(u"modificar_botao")
        self.modificar_botao.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.modificar_botao)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMaximumSize(QSize(90, 16777215))
        self.widget_3.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.adicionar_cat_input = QLineEdit(self.frame_4)
        self.adicionar_cat_input.setObjectName(u"adicionar_cat_input")
        self.adicionar_cat_input.setEnabled(True)
        self.adicionar_cat_input.setGeometry(QRect(15, 60, 400, 25))
        self.drop_modificar = QComboBox(self.frame_4)
        self.drop_modificar.setObjectName(u"drop_modificar")
        self.drop_modificar.setEnabled(True)
        self.drop_modificar.setGeometry(QRect(15, 60, 400, 25))

        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(130, 16777215))
        self.frame_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_3.setFrameShape(QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setEnabled(True)
        self.btn_excluir.setGeometry(QRect(15, 60, 101, 25))
        self.btn_excluir.setMinimumSize(QSize(90, 0))
        self.btn_adicionar = QPushButton(self.frame_3)
        self.btn_adicionar.setObjectName(u"btn_adicionar")
        self.btn_adicionar.setEnabled(True)
        self.btn_adicionar.setGeometry(QRect(15, 60, 101, 25))
        self.btn_adicionar.setMinimumSize(QSize(0, 0))
        self.btn_adicionar.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.widget_2)

        Category.setCentralWidget(self.centralwidget)

        self.retranslateUi(Category)

        QMetaObject.connectSlotsByName(Category)
    # setupUi

    def retranslateUi(self, Category):
        Category.setWindowTitle(QCoreApplication.translate("Category", u"Categorias", None))
        self.adicionar_botao.setText(QCoreApplication.translate("Category", u"ADICIONAR", None))
        self.modificar_botao.setText(QCoreApplication.translate("Category", u"MODIFICAR", None))
        self.label.setText(QCoreApplication.translate("Category", u"CATEGORIA", None))
        self.btn_excluir.setText(QCoreApplication.translate("Category", u"Excluir", None))
        self.btn_adicionar.setText(QCoreApplication.translate("Category", u"Adicionar", None))
    # retranslateUi

