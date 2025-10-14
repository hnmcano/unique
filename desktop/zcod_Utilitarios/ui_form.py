# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_TicketApp(object):
    def setupUi(self, TicketApp):
        if not TicketApp.objectName():
            TicketApp.setObjectName(u"TicketApp")
        TicketApp.setWindowModality(Qt.WindowModality.ApplicationModal)
        TicketApp.resize(774, 682)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TicketApp.sizePolicy().hasHeightForWidth())
        TicketApp.setSizePolicy(sizePolicy)
        TicketApp.setMinimumSize(QSize(4, 500))
        TicketApp.setMaximumSize(QSize(938, 868))
        TicketApp.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(TicketApp)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(TicketApp)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label)

        self.pedido_input = QLineEdit(TicketApp)
        self.pedido_input.setObjectName(u"pedido_input")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.pedido_input)

        self.label_2 = QLabel(TicketApp)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.cliente_input = QLineEdit(TicketApp)
        self.cliente_input.setObjectName(u"cliente_input")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cliente_input)

        self.label_3 = QLabel(TicketApp)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.email_input = QLineEdit(TicketApp)
        self.email_input.setObjectName(u"email_input")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.email_input)

        self.label_4 = QLabel(TicketApp)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.telefone_input = QLineEdit(TicketApp)
        self.telefone_input.setObjectName(u"telefone_input")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.telefone_input)

        self.label_5 = QLabel(TicketApp)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.widget_cep = QWidget(TicketApp)
        self.widget_cep.setObjectName(u"widget_cep")
        self.horizontalLayout = QHBoxLayout(self.widget_cep)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cepinput = QLineEdit(self.widget_cep)
        self.cepinput.setObjectName(u"cepinput")

        self.horizontalLayout.addWidget(self.cepinput)

        self.btn_viacep = QPushButton(self.widget_cep)
        self.btn_viacep.setObjectName(u"btn_viacep")

        self.horizontalLayout.addWidget(self.btn_viacep)

        self.resultado_cep = QLabel(self.widget_cep)
        self.resultado_cep.setObjectName(u"resultado_cep")

        self.horizontalLayout.addWidget(self.resultado_cep)


        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.widget_cep)

        self.label_6 = QLabel(TicketApp)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.endereco_input = QLineEdit(TicketApp)
        self.endereco_input.setObjectName(u"endereco_input")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.endereco_input)

        self.label_7 = QLabel(TicketApp)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.bairro_input = QLineEdit(TicketApp)
        self.bairro_input.setObjectName(u"bairro_input")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.bairro_input)

        self.label_8 = QLabel(TicketApp)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.complemento_input = QLineEdit(TicketApp)
        self.complemento_input.setObjectName(u"complemento_input")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.complemento_input)

        self.label_9 = QLabel(TicketApp)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.ref_input = QLineEdit(TicketApp)
        self.ref_input.setObjectName(u"ref_input")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.FieldRole, self.ref_input)

        self.label_10 = QLabel(TicketApp)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(12, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.cidade_input = QLineEdit(TicketApp)
        self.cidade_input.setObjectName(u"cidade_input")

        self.formLayout.setWidget(12, QFormLayout.ItemRole.FieldRole, self.cidade_input)

        self.label_11 = QLabel(TicketApp)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(13, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.previsao_input = QComboBox(TicketApp)
        self.previsao_input.setObjectName(u"previsao_input")

        self.formLayout.setWidget(13, QFormLayout.ItemRole.FieldRole, self.previsao_input)

        self.label_12 = QLabel(TicketApp)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(14, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.scrollArea = QScrollArea(TicketApp)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 100))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 674, 98))
        self.items_container = QVBoxLayout(self.scrollAreaWidgetContents)
        self.items_container.setObjectName(u"items_container")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.formLayout.setWidget(14, QFormLayout.ItemRole.FieldRole, self.scrollArea)

        self.label_13 = QLabel(TicketApp)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(15, QFormLayout.ItemRole.LabelRole, self.label_13)

        self.subtotal_input = QLineEdit(TicketApp)
        self.subtotal_input.setObjectName(u"subtotal_input")

        self.formLayout.setWidget(15, QFormLayout.ItemRole.FieldRole, self.subtotal_input)

        self.label_14 = QLabel(TicketApp)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(16, QFormLayout.ItemRole.LabelRole, self.label_14)

        self.taxa_input = QLineEdit(TicketApp)
        self.taxa_input.setObjectName(u"taxa_input")

        self.formLayout.setWidget(16, QFormLayout.ItemRole.FieldRole, self.taxa_input)

        self.label_15 = QLabel(TicketApp)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(17, QFormLayout.ItemRole.LabelRole, self.label_15)

        self.total_input = QLineEdit(TicketApp)
        self.total_input.setObjectName(u"total_input")

        self.formLayout.setWidget(17, QFormLayout.ItemRole.FieldRole, self.total_input)

        self.label_16 = QLabel(TicketApp)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(18, QFormLayout.ItemRole.LabelRole, self.label_16)

        self.pagamento_input = QLineEdit(TicketApp)
        self.pagamento_input.setObjectName(u"pagamento_input")

        self.formLayout.setWidget(18, QFormLayout.ItemRole.FieldRole, self.pagamento_input)

        self.label_17 = QLabel(TicketApp)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(19, QFormLayout.ItemRole.LabelRole, self.label_17)

        self.obs_input = QTextEdit(TicketApp)
        self.obs_input.setObjectName(u"obs_input")

        self.formLayout.setWidget(19, QFormLayout.ItemRole.FieldRole, self.obs_input)

        self.label_18 = QLabel(TicketApp)
        self.label_18.setObjectName(u"label_18")

        self.formLayout.setWidget(20, QFormLayout.ItemRole.LabelRole, self.label_18)

        self.cpf_input = QLineEdit(TicketApp)
        self.cpf_input.setObjectName(u"cpf_input")

        self.formLayout.setWidget(20, QFormLayout.ItemRole.FieldRole, self.cpf_input)

        self.label_data = QLabel(TicketApp)
        self.label_data.setObjectName(u"label_data")
        self.label_data.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.label_data)

        self.label_titulo = QLabel(TicketApp)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.label_titulo)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_add_item = QPushButton(TicketApp)
        self.btn_add_item.setObjectName(u"btn_add_item")

        self.horizontalLayout_2.addWidget(self.btn_add_item)

        self.btn_preview = QPushButton(TicketApp)
        self.btn_preview.setObjectName(u"btn_preview")

        self.horizontalLayout_2.addWidget(self.btn_preview)

        self.btn_enviar = QPushButton(TicketApp)
        self.btn_enviar.setObjectName(u"btn_enviar")

        self.horizontalLayout_2.addWidget(self.btn_enviar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_19 = QLabel(TicketApp)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout.addWidget(self.label_19)

        self.preview_area = QTextEdit(TicketApp)
        self.preview_area.setObjectName(u"preview_area")
        self.preview_area.setReadOnly(True)

        self.verticalLayout.addWidget(self.preview_area)

        QWidget.setTabOrder(self.pedido_input, self.cliente_input)
        QWidget.setTabOrder(self.cliente_input, self.email_input)
        QWidget.setTabOrder(self.email_input, self.telefone_input)
        QWidget.setTabOrder(self.telefone_input, self.cepinput)
        QWidget.setTabOrder(self.cepinput, self.btn_viacep)
        QWidget.setTabOrder(self.btn_viacep, self.endereco_input)
        QWidget.setTabOrder(self.endereco_input, self.bairro_input)
        QWidget.setTabOrder(self.bairro_input, self.complemento_input)
        QWidget.setTabOrder(self.complemento_input, self.ref_input)
        QWidget.setTabOrder(self.ref_input, self.cidade_input)
        QWidget.setTabOrder(self.cidade_input, self.previsao_input)
        QWidget.setTabOrder(self.previsao_input, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.subtotal_input)
        QWidget.setTabOrder(self.subtotal_input, self.taxa_input)
        QWidget.setTabOrder(self.taxa_input, self.total_input)
        QWidget.setTabOrder(self.total_input, self.pagamento_input)
        QWidget.setTabOrder(self.pagamento_input, self.obs_input)
        QWidget.setTabOrder(self.obs_input, self.cpf_input)
        QWidget.setTabOrder(self.cpf_input, self.btn_add_item)
        QWidget.setTabOrder(self.btn_add_item, self.btn_preview)
        QWidget.setTabOrder(self.btn_preview, self.btn_enviar)
        QWidget.setTabOrder(self.btn_enviar, self.preview_area)

        self.retranslateUi(TicketApp)

        QMetaObject.connectSlotsByName(TicketApp)
    # setupUi

    def retranslateUi(self, TicketApp):
        TicketApp.setWindowTitle(QCoreApplication.translate("TicketApp", u"Enviar Ticket Completo", None))
        self.label.setText(QCoreApplication.translate("TicketApp", u"Pedido:", None))
        self.label_2.setText(QCoreApplication.translate("TicketApp", u"Cliente:", None))
        self.label_3.setText(QCoreApplication.translate("TicketApp", u"E-mail:", None))
        self.label_4.setText(QCoreApplication.translate("TicketApp", u"Telefone:", None))
        self.label_5.setText(QCoreApplication.translate("TicketApp", u"CEP:", None))
        self.cepinput.setPlaceholderText(QCoreApplication.translate("TicketApp", u"Digite seu CEP aqui...", None))
        self.btn_viacep.setText(QCoreApplication.translate("TicketApp", u"Buscar", None))
        self.resultado_cep.setText("")
        self.label_6.setText(QCoreApplication.translate("TicketApp", u"Endere\u00e7o:", None))
        self.label_7.setText(QCoreApplication.translate("TicketApp", u"Bairro:", None))
        self.label_8.setText(QCoreApplication.translate("TicketApp", u"Complemento:", None))
        self.label_9.setText(QCoreApplication.translate("TicketApp", u"Ref:", None))
        self.label_10.setText(QCoreApplication.translate("TicketApp", u"Cidade:", None))
        self.label_11.setText(QCoreApplication.translate("TicketApp", u"Previs\u00e3o Entrega:", None))
        self.label_12.setText(QCoreApplication.translate("TicketApp", u"Itens do Pedido:", None))
        self.label_13.setText(QCoreApplication.translate("TicketApp", u"Subtotal:", None))
        self.label_14.setText(QCoreApplication.translate("TicketApp", u"Taxa:", None))
        self.label_15.setText(QCoreApplication.translate("TicketApp", u"Total:", None))
        self.label_16.setText(QCoreApplication.translate("TicketApp", u"Pagamento:", None))
        self.label_17.setText(QCoreApplication.translate("TicketApp", u"Observa\u00e7\u00f5es:", None))
        self.label_18.setText(QCoreApplication.translate("TicketApp", u"CPF:", None))
        self.label_data.setText("")
        self.label_titulo.setText(QCoreApplication.translate("TicketApp", u"HOOKAHSHISHA TABACARIA", None))
        self.btn_add_item.setText(QCoreApplication.translate("TicketApp", u"Adicionar Item", None))
        self.btn_preview.setText(QCoreApplication.translate("TicketApp", u"Pr\u00e9-visualizar Ticket", None))
        self.btn_enviar.setText(QCoreApplication.translate("TicketApp", u"Enviar Ticket", None))
        self.label_19.setText(QCoreApplication.translate("TicketApp", u"Pr\u00e9-visualiza\u00e7\u00e3o do Ticket:", None))
    # retranslateUi

