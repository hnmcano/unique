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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Category(object):
    def setupUi(self, Category):
        if not Category.objectName():
            Category.setObjectName(u"Category")
        Category.resize(720, 84)
        Category.setMinimumSize(QSize(720, 0))
        Category.setMaximumSize(QSize(720, 16777215))
        Category.setStyleSheet(u"#centralwidget{\n"
"	background-color: black;\n"
"}\n"
"\n"
"#centralwidget  #widget_2 {\n"
"	background-color: black;\n"
"}\n"
"\n"
"#centralwidget  #widget_2 stackedWidget {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(Category)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(720, 84))
        self.centralwidget.setMaximumSize(QSize(720, 84))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_2)
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
        self.adicionar_botao.setMinimumSize(QSize(0, 43))
        self.adicionar_botao.setMaximumSize(QSize(16777215, 16777215))
        self.adicionar_botao.setStyleSheet(u"")
        self.adicionar_botao.setIconSize(QSize(16, 16))

        self.verticalLayout.addWidget(self.adicionar_botao)

        self.excluir_botao = QPushButton(self.widget)
        self.excluir_botao.setObjectName(u"excluir_botao")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.excluir_botao.sizePolicy().hasHeightForWidth())
        self.excluir_botao.setSizePolicy(sizePolicy)
        self.excluir_botao.setMinimumSize(QSize(0, 43))
        self.excluir_botao.setMaximumSize(QSize(16777215, 16777215))
        self.excluir_botao.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.excluir_botao)


        self.horizontalLayout_2.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_3 = QHBoxLayout(self.page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.drop_modificar = QComboBox(self.page)
        self.drop_modificar.setObjectName(u"drop_modificar")
        self.drop_modificar.setMinimumSize(QSize(400, 0))
        self.drop_modificar.setMaximumSize(QSize(400, 16777215))

        self.horizontalLayout_3.addWidget(self.drop_modificar)

        self.btn_excluir = QPushButton(self.page)
        self.btn_excluir.setObjectName(u"btn_excluir")

        self.horizontalLayout_3.addWidget(self.btn_excluir)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_4 = QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.adicionar_cat_input = QLineEdit(self.page_2)
        self.adicionar_cat_input.setObjectName(u"adicionar_cat_input")
        self.adicionar_cat_input.setMinimumSize(QSize(400, 0))
        self.adicionar_cat_input.setMaximumSize(QSize(400, 16777215))

        self.horizontalLayout_4.addWidget(self.adicionar_cat_input)

        self.btn_adicionar = QPushButton(self.page_2)
        self.btn_adicionar.setObjectName(u"btn_adicionar")

        self.horizontalLayout_4.addWidget(self.btn_adicionar)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.widget_2)

        Category.setCentralWidget(self.centralwidget)

        self.retranslateUi(Category)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Category)
    # setupUi

    def retranslateUi(self, Category):
        Category.setWindowTitle(QCoreApplication.translate("Category", u"ADICIONAR CATEGORIAS", None))
        self.adicionar_botao.setText(QCoreApplication.translate("Category", u"ADICIONAR", None))
        self.excluir_botao.setText(QCoreApplication.translate("Category", u"MODIFICAR", None))
        self.btn_excluir.setText(QCoreApplication.translate("Category", u"EXCLUIR", None))
        self.btn_adicionar.setText(QCoreApplication.translate("Category", u"ADICIONAR", None))
    # retranslateUi

