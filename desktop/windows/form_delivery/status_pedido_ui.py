# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'status_pedido.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(235, 168)
        MainWindow.setStyleSheet(u"#centralwidget QPushButton{\n"
"	background-color: transparent;\n"
"	border: 1px solid white;	\n"
"}\n"
"\n"
"#centralwidget QPushButton:hover{\n"
"	background-color: #3c3c3c;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_pendente = QPushButton(self.centralwidget)
        self.btn_pendente.setObjectName(u"btn_pendente")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pendente.sizePolicy().hasHeightForWidth())
        self.btn_pendente.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_pendente)

        self.btn_em_producao = QPushButton(self.centralwidget)
        self.btn_em_producao.setObjectName(u"btn_em_producao")
        sizePolicy.setHeightForWidth(self.btn_em_producao.sizePolicy().hasHeightForWidth())
        self.btn_em_producao.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_em_producao)

        self.btn_pronto_retirada = QPushButton(self.centralwidget)
        self.btn_pronto_retirada.setObjectName(u"btn_pronto_retirada")
        sizePolicy.setHeightForWidth(self.btn_pronto_retirada.sizePolicy().hasHeightForWidth())
        self.btn_pronto_retirada.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_pronto_retirada)

        self.btn_saiu_para_entrega = QPushButton(self.centralwidget)
        self.btn_saiu_para_entrega.setObjectName(u"btn_saiu_para_entrega")
        sizePolicy.setHeightForWidth(self.btn_saiu_para_entrega.sizePolicy().hasHeightForWidth())
        self.btn_saiu_para_entrega.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_saiu_para_entrega)

        self.btn_finalizado = QPushButton(self.centralwidget)
        self.btn_finalizado.setObjectName(u"btn_finalizado")
        sizePolicy.setHeightForWidth(self.btn_finalizado.sizePolicy().hasHeightForWidth())
        self.btn_finalizado.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_finalizado)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"STATUS", None))
        self.btn_pendente.setText(QCoreApplication.translate("MainWindow", u"PENDENTE", None))
        self.btn_em_producao.setText(QCoreApplication.translate("MainWindow", u"EM PRODU\u00c7\u00c3O", None))
        self.btn_pronto_retirada.setText(QCoreApplication.translate("MainWindow", u"PRONTO RETIRADA", None))
        self.btn_saiu_para_entrega.setText(QCoreApplication.translate("MainWindow", u"SAIU PARA ENTREGA", None))
        self.btn_finalizado.setText(QCoreApplication.translate("MainWindow", u"FINALIZADO", None))
    # retranslateUi

