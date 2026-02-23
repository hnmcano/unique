from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtNetwork import *
from windows.form_clients.add_clientes_ui import Ui_MainWindow as addclientes
from core.app_context import app_context as APPContext

import json
import requests
from services.network_conn import handle_network_reply
import os

from config.config import settings


def buscar_cep(parent=None):
    """Busca CEP usando ViaCEP"""
    try:
        cep = parent.cepinput.text().replace("-", "").replace(".", "").strip()# type: ignore
        if len(cep) != 8:
            QMessageBox.warning(parent, "CEP Inválido", "Digite um CEP válido com 8 dígitos")
            return
        try:
            response = APPContext.api_client.get(f"https://viacep.com.br/ws/{cep}/json/")
            data = response
            if "erro" not in data:
                parent.endereco_input.setText(data.get("logradouro", ""))# type: ignore
                parent.bairro_input.setText(data.get("bairro", ""))# type: ignore
                parent.cidade_input.setText(f"{data.get('localidade', '')}/{data.get('uf', '')}")# type: ignore

        except Exception as e:
            QMessageBox.critical(parent, "Erro", "Falha ao buscar CEP")

    except Exception as e:
        QMessageBox.critical(parent, "Erro", f"Erro na busca do CEP: {str(e)}")


def salvar_dados_clientes(parent=None):

    # O parent.nome_input é acessível diretamente
    cliente = parent.nome_input.text()# type: ignore
    email = parent.email_input.text()# type: ignore
    telefone = parent.telefone_input.text()# type: ignore
    cep = parent.cepinput.text()# type: ignore
    endereco = parent.endereco_input.text()# type: ignore
    bairro = parent.bairro_input.text()# type: ignore
    cidade= parent.cidade_input.text()# type: ignore
    complemento = parent.complemento_input.text()# type: ignore
    referencia = parent.referencia_input.text()# type: ignore

    try:
        QMessageBox.information(parent, "Aguarde", "Enviando dados para o servidor!")
        data_json = {
                "cliente": f"{cliente}",
                "telefone": f"{telefone}",
                "email": f"{email}",
                "cep": f"{cep}",
                "endereco": f"{endereco}",
                "bairro": f"{bairro}",
                "cidade": f"{cidade}",
                "complemento": f"{complemento}",
                "referencia": f"{referencia}"
        }

        response = APPContext.api_client.post("/clientes/users", data_json)

        #adicionar_novo_usuario(Cliente, email, telefone, cep, endereco, bairro, cidade, complemento, referencia)
        QMessageBox.information(parent, "Sucesso", "Usuário adicionado com sucesso!")
        # Limpa os campos após salvar
        parent.nome_input.clear()# type: ignore
        parent.email_input.clear()# type: ignore
        parent.telefone_input.clear()# type: ignore
        parent.cepinput.clear()# type: ignore
        parent.endereco_input.clear()# type: ignore
        parent.bairro_input.clear()# type: ignore
        parent.cidade_input.clear()# type: ignore
        parent.complemento_input.clear()# type: ignore
        parent.referencia_input.clear()# type: ignore

    except ValueError:
        QMessageBox.warning(parent, "Erro", "A informação está incorreta.")
    except Exception as e:
        QMessageBox.critical(parent, "Erro de BD", f"Ocorreu um erro: {e}")


def exibir_confirmacao_exclusao(parent= None):
    msg_box = QMessageBox(parent)
    msg_box.setIcon(QMessageBox.Question) # type: ignore
    msg_box.setWindowTitle("Confirmar Exclusão")
    msg_box.setText("Tem certeza de que deseja fechar esta janela?\n Todos os dados serão perdidos.")
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No) # type: ignore

    # A resposta é armazenada aqui, o código é bloqueado até o usuário interagir
    resposta = msg_box.exec()

    if resposta == QMessageBox.Yes: # type: ignore
        # Se o usuário confirmar, emita o sinal e feche a janela
        parent.janela_fechada.emit() # type: ignore
        parent.close() # type: ignore
    # Se a resposta for QMessageBox.No, o diálogo simplesmente fecha e nada acontece


class AddClientes(QMainWindow, addclientes):
    janela_fechada = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)# type: ignore

        # Ao clicar no botão buscar CEP, Aciona a função de buscar CEP localizada em scripts/aux_func.py
        self.btn_viacep.clicked.connect(lambda: buscar_cep(self))
        # Gerenciador de rede para requisições HTTP
        self.network_manager = QNetworkAccessManager(self)
        # Ao clicar no botão salvar, Aciona a função de salvar dados clientes localizada em scripts/aux_func.py
        self.cad_clientes.clicked.connect(lambda: salvar_dados_clientes(self))
        # Ao clicar no botão cancelar, Aciona a função de confirmação de exclusão localizada em scripts/aux_func.py
        self.cancelar.clicked.connect(lambda: exibir_confirmacao_exclusao(self))
