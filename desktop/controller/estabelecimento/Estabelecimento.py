from PySide6.QtWidgets import *
from windows.form_establishment.form_estabelecimento_ui import Ui_MainWindow as estabelecimento
from controller.estabelecimento.AdicionarHorarios import AddHorarios
from controller.estabelecimento.TaxasEntregas import TaxasEntregas
from controller.estabelecimento.CoordEstabelecimento import CoordEstabelecimento

from core.app_context import app_context as APPContext
from services.websocket import HorarioStore

from PySide6.QtNetwork import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWebEngineWidgets import QWebEngineView

from config.config import settings
import base64
from datetime import datetime
from time import sleep
import folium
from io import BytesIO

def indice_dia_semana(dia_semana):
    dias = {
        0:"segunda-feira",
        1:"terca-feira",
        2:"quarta-feira",
        3:"quinta-feira",
        4:"sexta-feira",
        5:"sabado",
        6:"domingo"
    }
    return dias.get(dia_semana)

def enviar_dados_estabelecimento(parent=None):
    id = parent.IdLine.text()
    nome =parent.NomeLine.text()
    documento = parent.DocumentoLine.text()
    nome_fantasia = parent.NomeFanLine.text()
    email = parent.EmailLine.text()
    telefone = parent.TelefoneLine.text()
    endereco = parent.EnderecoLine.text()
    rede_social =parent.RedeSocialLine.text()
    descricao = parent.DescricaoLine.text()
    style = parent.cor_definida.styleSheet()
    cor = style.split("background-color:")[1].split(";")[0].strip()
    cor_layout = cor
    plano = parent.PlanoLine.text()
    limite_usuarios = parent.LimiteUsuarioLine.text()
    ativo = parent.AtivoLine.text()
    data_expiracao = parent.DataExpiracaoLine.text()
    subdominio = parent.SubDominioLine.text()
    data_criacao = parent.DataCriacaoLine.text()
    data_atualizacao = parent.DataAtualizacaoLine.text()
    botao_checked = parent.grupo.checkedButton()

    if parent.estabelecimento_logo.text() == "":
        pixmap = QPixmap(parent.pixmap_original)

        buffer = QBuffer()
        buffer.open(QIODevice.OpenModeFlag.WriteOnly)
        pixmap.save(buffer, "PNG")
        image_data = buffer.data().toBase64().data()
        imagem_data_string = image_data.decode("utf-8")

    else:
        imagem_data_string = None


    try:
        QMessageBox.information(parent, "Aguarde", "Enviando dados para o servidor!")
        data_json = {
            "id": f"{id}",
            "nome": f"{nome}",
            "nome_fantasia": f"{nome_fantasia}",
            "documento": f"{documento}",
            "telefone": f"{telefone}",
            "email": f"{email}",
            "logo_img": f"{imagem_data_string}",
            "endereco": f"{endereco}",
            "rede_social": f"{rede_social}",
            "descricao": f"{descricao}",
            "cor_layout": f"{cor_layout}",
            "plano": f"{plano}",
            "limite_usuarios": f"{limite_usuarios}",
            "ativo": f"{ativo}",
            "data_expiracao": f"{data_expiracao}",
            "subdominio": f"{subdominio}",
            "criado_em": f"{data_criacao}",
            "atualizado_em": f"{data_atualizacao}",
            "redirecionamento": f"{botao_checked.objectName()}"
        }
        
        response = APPContext.api_client.put("/estabelecimento/atualizar-infos", data_json)
        
    except Exception as e:
        QMessageBox.critical(parent, "Erro", f"Erro ao enviar dados: {str(e)}")

def format_data(data):
    dt_utc = datetime.fromisoformat(data.replace("Z", "+00:00"))
    dt_local = dt_utc.astimezone()
    data_formatada = dt_local.strftime("%d/%m/%Y %H:%M:%S")

    return data_formatada

def carregar_dados(self):
    try:
        response = APPContext.api_client.get("/estabelecimento/carregar-infos")
        return response
    except Exception as e:
        QMessageBox.critical(self, "Erro", f"Erro ao buscar dados: {str(e)}")

class Estabelecimento(QMainWindow, estabelecimento):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.coords_estabelecimento = None

        self.timer = QTimer()
        self.grupo = QButtonGroup()
        self.map_view = QWebEngineView()

        self.map_layout = self.widget_33.layout()

        if self.map_layout is None:
            self.map_layout = QVBoxLayout(self.widget_33)

        APPContext.horarios_store = HorarioStore()
        self.horarios_store = APPContext.horarios_store
        self.horarios_store.horario_adicionado.connect(self.atualizar_tabela_horarios)

        self.map_layout.addWidget(self.map_view)
        self.grupo.setExclusive(True)
        self.grupo.addButton(self.unique)
        self.grupo.addButton(self.whatsapp)
        self.response = carregar_dados(self)
        self.atualizar_dados(self.response)
        self.tabela = self.carregar_taxas()
        self.EnviaDados.clicked.connect(lambda: enviar_dados_estabelecimento(self))
        self.layout_tabela()
        
        horarios = self.horarios_store.listar()
        if horarios is not None:
            response = APPContext.api_client.get("/estabelecimento/horarios")
            self.atualizar_tabela_horarios(response)
     
        self.btn_informacoes.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page)
        )
        self.btn_layout.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_2)
        )
        self.btn_horarios_config.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_3)
        )
        self.btn_adicionar.clicked.connect(
            self.adicionar_novo_horario
        )
        self.btn_orange.clicked.connect(
            lambda: self.atualizar_cor_designer(self.btn_orange)
        )
        self.btn_green.clicked.connect(
            lambda: self.atualizar_cor_designer(self.btn_green)
        )
        self.btn_purple.clicked.connect(
            lambda: self.atualizar_cor_designer(self.btn_purple)
        )
        self.btn_red.clicked.connect(
            lambda: self.atualizar_cor_designer(self.btn_red)
        )
        self.btn_editar_taxas.clicked.connect(
           lambda: self.preencher_tabela()
        )
        self.btn_editar_localizacao.clicked.connect(
           lambda: self.atualizar_localizacao()
        )

    def atualizar_dados(self, response):
        self.IdLine.setText(response["id"])
        self.NomeLine.setText(str(response["nome"]))
        self.DocumentoLine.setText(str(response["documento"]))
        self.NomeFanLine.setText(str(response["nome_fantasia"]))
        self.EmailLine.setText(str(response["email"]))
        self.TelefoneLine.setText(str(response["telefone"]))
        self.EnderecoLine.setText(str(response["endereco"]))
        self.RedeSocialLine.setText(str(response["rede_social"]))
        self.DescricaoLine.setText(str(response["descricao"]))
        self.cor_definida.setStyleSheet(f"background-color: {response['cor_layout']};")
        self.PlanoLine.setText(str(response["plano"]))
        self.LimiteUsuarioLine.setText(str(response["limite_usuarios"]))
        self.AtivoLine.setText(str(response["ativo"]))
        self.SubDominioLine.setText(str(response["subdominio"]))

        self.redirecionado = response["redirecionamento"]

        for i in self.grupo.buttons():
            if i.objectName() == self.redirecionado:
                i.setChecked(True)
                break

        if response["data_expiracao"] == None:
            data_expiracao = None
            self.DataExpiracaoLine.setText(str(data_expiracao))
        else:
            data_formatada_expiracao = format_data(response["data_expiracao"])
            self.SubDominioLine.setText(str(data_formatada_expiracao))

        if response["criado_em"] == None:
            data_criacao = None
            self.DataCriacaoLine.setText(str(data_criacao))
        else:
            data_formatada_criacao = format_data(response["criado_em"])
            self.DataCriacaoLine.setText(str(data_formatada_criacao))

        if response["atualizado_em"] == None:
            data_atualizacao = None
            self.DataAtualizacaoLine.setText(str(data_atualizacao))
        else:
            data_formatada_atualizacao = format_data(response["atualizado_em"])
            self.DataAtualizacaoLine.setText(str(data_formatada_atualizacao))

        if response["logo_img"] == None:
            self.estabelecimento_logo.setText("Nenhuma imagem carregada")
        else:
            data = base64.b64decode(response["logo_img"])
            self.pixmap = QPixmap()
            self.pixmap.loadFromData(data)
            self.estabelecimento_logo.setScaledContents(True)
            self.estabelecimento_logo.setAlignment(Qt.AlignCenter)
            self.estabelecimento_logo.setPixmap(self.pixmap)

    def mouseDoubleClickEvent(self, event):
        if self.estabelecimento_logo.geometry().contains(event.pos()):
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getOpenFileName(self, "Selecionar Imagem", "", "Arquivos de Imagem (*.png *.jpg *.jpeg *.bmp *.gif)")
            
            if not file_path:
                return
            
            self.pixmap_original = QPixmap(file_path)

            if self.pixmap_original is None:
                QMessageBox.critical(self, "Erro", "Falha ao carregar a imagem.")
                return

            preview_pixmap = self.pixmap_original.scaled(self.estabelecimento_logo.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

            self.estabelecimento_logo.setPixmap(preview_pixmap)
            self.estabelecimento_logo.setText("")

    def on_evento_recebido(self, evento: dict):
        response = evento["dados"]
        if evento["tipo"] == "Atualizar_estabelecimento":
            # Se vier um dicionário único, transformamos em lista
            self.atualizar_dados(response)

    def showEvent(self, event):
        super().showEvent(event)
        
        APPContext.websocket_client.mensagem_recebida.connect(
            self.on_evento_recebido
        )
               
    def atualizar_cor_designer(self, botao):
        style = botao.styleSheet()

        if "background-color" in style:
            cor = style.split("background-color:")[1].split(";")[0].strip()
            if cor:
                self.cor_definida.setStyleSheet(f"background-color: {cor};")
            else:
                self.cor_definida.setStyleSheet("background-color: transparent;")

    def layout_tabela(self):
        columns = [ "dia_semana", "hora_inicio", "hora_fim"]

        quantidade_columns = len(columns)
        self.tableWidget.setColumnCount(quantidade_columns)
        self.tableWidget.setHorizontalHeaderLabels(columns)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def atualizar_tabela_horarios(self, horario):
        self.tableWidget.setRowCount(len(horario))

        for index, item in enumerate(horario):

            dia_semana = indice_dia_semana(item["dia_semana"])
            dia_semana = QTableWidgetItem(str(dia_semana))
            self.tableWidget.setItem(index, 0, dia_semana)

            hora_abertura = QTableWidgetItem(str(item["hora_abertura"][:5]))
            hora_abertura.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(index, 1, hora_abertura)

            hora_fechamento = QTableWidgetItem(str(item["hora_fechamento"][:5]))
            hora_fechamento.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(index, 2, hora_fechamento)

    def adicionar_novo_horario(self):
        self.add_horario_window = AddHorarios(parent=self)
        self.add_horario_window.show() 

    def carregar_taxas(self):
        """Carregar dados do backend"""
        try:
            # Simulando dados (substituir por chamadas reais)
            self.fretes = APPContext.api_client.get("/estabelecimento/desktop/taxas-km")

            # Buscar coordenadas do estabelecimento
            self.coords_estabelecimento = APPContext.api_client.get("/estabelecimento/desktop/coordenadas-estabelecimento")
            
            # Desenhar mapa inicial
            self.atualizar_mapa()

            return self.fretes  
            
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar dados: {str(e)}")
            return

    def atualizar_mapa(self):
        if not self.coords_estabelecimento or not self.fretes:
            return
        
        cores = ['green', 'yellowgreen', 'orange', 'red']

        mapa = folium.Map(
            location=[self.coords_estabelecimento['lat'], self.coords_estabelecimento['lon']],
            zoom_start=14,
            tiles="CartoDB positron"
        )
        
        folium.Marker(
            location=[self.coords_estabelecimento['lat'], self.coords_estabelecimento['lon']],
            popup=self.coords_estabelecimento['nome'],
            icon=folium.Icon(color='blue', icon='home')
        ).add_to(mapa)
        
        for idx, frete in enumerate(sorted(self.fretes, key=lambda x: x['km_maximo'], reverse=True)):
            if not frete['ativo']:
                continue
            
            raio = frete['km_maximo'] * 1000  # Converter KM para metros
            cor = cores[idx % len(cores)]
            
            circle = folium.Circle(
                location=[self.coords_estabelecimento['lat'], self.coords_estabelecimento['lon']],
                radius=raio,
                color=cor,
                fill=True,
                fillColor=cor,
                fillOpacity=0.2,
                weight=2
            )

            popup = folium.Popup(
                f"""
                <div style='text-align:center;'>
                    <b>{frete['km_minimo']:.1f} - {frete['km_maximo']:.1f} km</b><br>
                    R$ {frete['valor']:.2f}
                </div>
                """,
                max_width=200
            )

            circle.add_child(popup)
            circle.add_to(mapa)
        
        # Salvar mapa em HTML
        data = BytesIO()
        mapa.save(data, close_file=False)
        
        html = data.getvalue().decode()
        self.map_view.setHtml(html)
        
    def preencher_tabela(self):
        self.form_taxas = TaxasEntregas(parent=self, fretes=self.tabela)
        self.form_taxas.show()

    def atualizar_localizacao(self):
        self.form_coordenadas = CoordEstabelecimento(parent=self)
        self.form_coordenadas.show()