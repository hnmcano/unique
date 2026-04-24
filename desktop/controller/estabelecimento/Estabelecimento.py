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
from PySide6.QtWebEngineCore import QWebEngineSettings 

import base64
from datetime import datetime
from time import sleep
import psutil
import os
import subprocess
import json


# ============== DETECTOR DE GPU E SISTEMA FRACO ==============
def has_gpu():
    """Detecta se o sistema tem GPU disponível"""
    try:
        if os.name == 'nt':
            result = subprocess.run(['wmic', 'path', 'win32_VideoController', 'get', 'name'], 
                                  capture_output=True, text=True, timeout=5)
            return 'Microsoft Basic Display' not in result.stdout
        else:
            result = subprocess.run(['lspci'], capture_output=True, text=True, timeout=5)
            return 'VGA' in result.stdout or '3D' in result.stdout
    except:
        return False


def is_sistema_fraco():
    """Detecta se o sistema é fraco"""
    try:
        memory_mb = psutil.virtual_memory().available / (1024 ** 2)
        return memory_mb < 2048 or not has_gpu()
    except:
        return True


def indice_dia_semana(dia_semana):
    dias = {
        0: "segunda-feira",
        1: "terca-feira",
        2: "quarta-feira",
        3: "quinta-feira",
        4: "sexta-feira",
        5: "sabado",
        6: "domingo"
    }
    return dias.get(dia_semana)


def comprimir_imagem_para_base64(pixmap_original, max_width=400, max_height=300, quality=80):
    try:
        scaled = pixmap_original.scaledToWidth(max_width, Qt.SmoothTransformation)
        if scaled.height() > max_height:
            scaled = scaled.scaledToHeight(max_height, Qt.SmoothTransformation)
        
        buffer = QBuffer()
        buffer.open(QIODevice.OpenModeFlag.WriteOnly)
        scaled.save(buffer, "JPEG", quality)
        
        image_data = buffer.data().toBase64().data()
        return image_data.decode("utf-8")
    except Exception as e:
        print(f"Erro ao comprimir imagem: {e}")
        return None


def enviar_dados_estabelecimento(parent=None):
    id = parent.IdLine.text()
    nome = parent.NomeLine.text()
    documento = parent.DocumentoLine.text()
    nome_fantasia = parent.NomeFanLine.text()
    email = parent.EmailLine.text()
    telefone = parent.TelefoneLine.text()
    endereco = parent.EnderecoLine.text()
    rede_social = parent.RedeSocialLine.text()
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
        imagem_data_string = comprimir_imagem_para_base64(pixmap)
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


# ============== WIDGET DE CARREGAMENTO ==============
class LoadingWidget(QWidget):
    """Widget de carregamento animado que aparece enquanto o mapa carrega"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Configurar widget
        self.setStyleSheet("""
            QWidget {
                background-color: rgba(255, 255, 255, 0.95);
                border-radius: 15px;
            }
        """)
        
        # Layout
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setSpacing(20)
        
        # Ícone de mapa
        self.icon_label = QLabel("🗺️")
        self.icon_label.setAlignment(Qt.AlignCenter)
        self.icon_label.setStyleSheet("font-size: 48px;")
        
        # Texto de carregamento
        self.text_label = QLabel("Carregando Mapa...")
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #333;
                font-family: Arial;
            }
        """)
        
        # Barra de progresso indeterminada
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)  # Indeterminado
        self.progress_bar.setFixedWidth(300)
        self.progress_bar.setFixedHeight(8)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: #e0e0e0;
                border-radius: 4px;
                border: none;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #4CAF50, stop:0.5 #8BC34A, stop:1 #4CAF50);
                border-radius: 4px;
            }
        """)
        
        # Status detalhado
        self.status_label = QLabel("⬇️ Baixando tiles do OpenStreetMap...")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("""
            QLabel {
                font-size: 12px;
                color: #666;
                font-family: Arial;
            }
        """)
        
        # Timer para animação dos textos
        self.timer = QTimer()
        self.timer.timeout.connect(self._atualizar_animacao)
        self.contador = 0
        
        # Adicionar ao layout
        self.layout.addWidget(self.icon_label)
        self.layout.addWidget(self.text_label)
        self.layout.addWidget(self.progress_bar)
        self.layout.addWidget(self.status_label)
        
        # Efeito de sombra
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(20)
        self.shadow.setColor(QColor(0, 0, 0, 50))
        self.shadow.setOffset(0, 5)
        self.setGraphicsEffect(self.shadow)
    
    def _atualizar_animacao(self):
        """Atualiza a animação do texto de carregamento"""
        self.contador += 1
        pontos = "." * ((self.contador % 4) + 1)
        
        mensagens = [
            "⬇️ Baixando tiles do OpenStreetMap...",
            "🗺️ Renderizando mapa...",
            "📍 Posicionando marcadores...",
            "📊 Calculando áreas de entrega...",
            "🎨 Aplicando estilos...",
            "✅ Finalizando carregamento..."
        ]
        
        status = mensagens[self.contador % len(mensagens)]
        self.status_label.setText(status)
        self.text_label.setText(f"Carregando Mapa{pontos}")
    
    def iniciar(self):
        """Inicia a animação de carregamento"""
        self.show()
        self.timer.start(800)
    
    def parar(self):
        """Para a animação e esconde o widget"""
        self.timer.stop()
        self.hide()

# ============= WIDGET DE MAPA LEVE COM LEAFLET.JS PURO ==============
class MapaLeafletWidget(QWidget):
    """
    Widget de mapa interativo com tela de carregamento
    """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # ⚡ CORREÇÃO: Definir tamanho mínimo e política de redimensionamento
        self.setMinimumSize(400, 300)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Layout principal (stacked para alternar entre loading e mapa)
        self.layout = QStackedLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setStackingMode(QStackedLayout.StackAll)  # ⚡ MUDANÇA: StackAll para sobrepor
        
        # Página 0: WebEngine com mapa (ATRÁS - carrega em background)
        self.web_container = QWidget()
        self.web_container.setStyleSheet("background-color: #e8e8e8;")  # ⚡ Fundo cinza visível
        self.web_layout = QVBoxLayout(self.web_container)
        self.web_layout.setContentsMargins(0, 0, 0, 0)
        
        # Configurar WebEngine com flags de otimização
        os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = (
            "--disable-gpu "
            "--disable-software-rasterizer "
            "--disable-extensions "
            "--disable-plugins "
            "--disable-sync "
            "--no-sandbox "
            "--disable-web-security "
            "--max-active-webgl-contexts=1"
        )
        
        self.web_view = QWebEngineView()
        self.web_view.setMinimumSize(400, 300)
        self.web_view.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        self.web_view.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.web_view.settings().setAttribute(QWebEngineSettings.WebAttribute.Accelerated2dCanvasEnabled, False)
        self.web_view.settings().setAttribute(QWebEngineSettings.WebAttribute.WebGLEnabled, False)
        self.web_view.setStyleSheet("background-color: #e8e8e8;")  # ⚡ Fundo antes do HTML carregar
        
        self.web_layout.addWidget(self.web_view)
        self.layout.addWidget(self.web_container)
        
        # Página 1: Widget de carregamento (NA FRENTE - transparente)
        self.loading_overlay = QWidget()
        self.loading_overlay.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 0px;
        """)
        self.overlay_layout = QVBoxLayout(self.loading_overlay)
        self.overlay_layout.setAlignment(Qt.AlignCenter)
        self.overlay_layout.setSpacing(15)
        
        # Ícone de mapa
        self.icon_label = QLabel("🗺️")
        self.icon_label.setAlignment(Qt.AlignCenter)
        self.icon_label.setStyleSheet("font-size: 48px; background: transparent;")
        
        # Texto de carregamento
        self.text_label = QLabel("Carregando Mapa...")
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #333;
                font-family: Arial;
                background: transparent;
            }
        """)
        
        # Barra de progresso
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.setFixedWidth(300)
        self.progress_bar.setFixedHeight(8)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: #e0e0e0;
                border-radius: 4px;
                border: none;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #4CAF50, stop:0.5 #8BC34A, stop:1 #4CAF50);
                border-radius: 4px;
            }
        """)
        
        # Status
        self.status_label = QLabel("⬇️ Inicializando...")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("""
            QLabel {
                font-size: 12px;
                color: #666;
                font-family: Arial;
                background: transparent;
            }
        """)
        
        # Adicionar ao overlay
        self.overlay_layout.addWidget(self.icon_label)
        self.overlay_layout.addWidget(self.text_label)
        self.overlay_layout.addWidget(self.progress_bar)
        self.overlay_layout.addWidget(self.status_label)
        
        self.layout.addWidget(self.loading_overlay)
        
        # ⚡ CORREÇÃO: Mostrar ambos, mas overlay na frente
        self.layout.setCurrentIndex(1)  # Mostrar overlay
        self.web_container.show()  # Garantir que o fundo está visível
        
        # Dados
        self.coordenadas = None
        self.fretes = []
        self.mapa_carregado = False
        self.dados_prontos = False
        self.tentativas = 0
        self.max_tentativas = 10
        
        # Timer para animação
        self.anim_timer = QTimer()
        self.anim_timer.timeout.connect(self._atualizar_animacao)
        self.anim_timer.start(800)
        self.contador = 0
        
        # Conectar eventos
        self.web_view.loadFinished.connect(self._on_load_finished)
        self.web_view.loadProgress.connect(self._on_load_progress)
        
        # Timer para verificar carregamento
        self.verificar_timer = QTimer()
        self.verificar_timer.timeout.connect(self._verificar_carregamento)
        
        # ⚡ CORREÇÃO: Pequeno delay para a UI aparecer antes de carregar o HTML
        QTimer.singleShot(100, self._carregar_html_base)
    
    def _atualizar_animacao(self):
        """Atualiza a animação do texto de carregamento"""
        self.contador += 1
        pontos = "." * ((self.contador % 4) + 1)
        
        mensagens = [
            "⬇️ Baixando tiles do OpenStreetMap...",
            "🗺️ Renderizando mapa...",
            "📍 Posicionando marcadores...",
            "📊 Calculando áreas de entrega...",
            "🎨 Aplicando estilos...",
            "✅ Finalizando carregamento..."
        ]
        
        status = mensagens[self.contador % len(mensagens)]
        self.status_label.setText(status)
        self.text_label.setText(f"Carregando Mapa{pontos}")
    
    def _carregar_html_base(self):
        """Carrega o HTML base com Leaflet.js via CDN"""
        html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html, body { 
            width: 100%; 
            height: 100%; 
            overflow: hidden;
            background-color: #e8e8e8;  /* ⚡ Mesma cor do fundo */
        }
        #map { 
            width: 100%; 
            height: 100%;
            background-color: #e8e8e8;  /* ⚡ Evita flash branco */
        }
        
        .leaflet-control-zoom { display: none; }
        
        .legend {
            background: white;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            font-family: Arial, sans-serif;
            font-size: 12px;
            line-height: 1.5;
        }
        
        .legend-title {
            font-weight: bold;
            margin-bottom: 5px;
            font-size: 14px;
        }
        
        .legend-item {
            display: flex;
            align-items: center;
            margin: 2px 0;
        }
        
        .legend-color {
            width: 20px;
            height: 20px;
            margin-right: 8px;
            border: 2px solid #333;
            border-radius: 50%;
            opacity: 0.3;
        }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        // Variáveis globais
        let map;
        let marker;
        let circles = [];
        let centerLat = -23.5505;
        let centerLon = -46.6333;
        let defaultZoom = 14;
        
        // Inicializar mapa
        function initMap() {
            try {
                map = L.map('map', {
                    center: [centerLat, centerLon],
                    zoom: defaultZoom,
                    zoomControl: false,
                    attributionControl: false,
                    preferCanvas: true,
                    fadeAnimation: false,
                    zoomAnimation: false
                });
                
                // Camada do OpenStreetMap
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    minZoom: 8
                }).addTo(map);
                
                // Marcar como carregado
                window.mapaCarregado = true;
            } catch(e) {
                console.error('Erro ao inicializar mapa:', e);
            }
        }
        
        // Adicionar marcador do estabelecimento
        function addMarker(lat, lon, nome) {
            if (marker) {
                map.removeLayer(marker);
            }
            
            marker = L.marker([lat, lon], {
                title: nome,
                riseOnHover: true
            }).addTo(map);
            
            marker.bindPopup(`<b>${nome}</b><br>📍 ${lat.toFixed(4)}, ${lon.toFixed(4)}`);
            
            map.setView([lat, lon], map.getZoom());
        }
        
        // Adicionar círculos de entrega
        function addCircles(fretes, centerLat, centerLon) {
            circles.forEach(c => map.removeLayer(c));
            circles = [];
            
            const cores = ['#4CAF50', '#8BC34A', '#FF9800', '#F44336'];
            
            fretes.forEach((frete, idx) => {
                if (!frete.ativo) return;
                
                const cor = cores[idx % cores.length];
                const circle = L.circle([centerLat, centerLon], {
                    radius: frete.km_maximo * 1000,
                    color: cor,
                    fillColor: cor,
                    fillOpacity: 0.2,
                    weight: 2
                }).addTo(map);
                
                circle.bindPopup(
                    `<b>${frete.km_minimo.toFixed(1)} - ${frete.km_maximo.toFixed(1)} km</b><br>` +
                    `💰 R$ ${frete.valor.toFixed(2)}`
                );
                
                circles.push(circle);
            });
        }
        
        // Adicionar legenda
        function addLegend(fretes) {
            const existingLegend = document.querySelector('.legend');
            if (existingLegend) existingLegend.remove();
            
            const legend = L.control({position: 'bottomright'});
            
            legend.onAdd = function(map) {
                const div = L.DomUtil.create('div', 'legend');
                div.innerHTML = '<div class="legend-title">📦 Áreas de Entrega</div>';
                
                const cores = ['#4CAF50', '#8BC34A', '#FF9800', '#F44336'];
                
                fretes.filter(f => f.ativo).forEach((frete, idx) => {
                    div.innerHTML += `
                        <div class="legend-item">
                            <div class="legend-color" style="background:${cores[idx % cores.length]}"></div>
                            <span>${frete.km_minimo.toFixed(1)}-${frete.km_maximo.toFixed(1)}km = R$${frete.valor.toFixed(2)}</span>
                        </div>
                    `;
                });
                
                return div;
            };
            
            legend.addTo(map);
        }
        
        // Centralizar mapa
        function centralizarMapa(lat, lon) {
            map.setView([lat, lon], defaultZoom);
        }
        
        // Inicializar quando a página carregar
        if (document.readyState === 'complete') {
            initMap();
        } else {
            window.addEventListener('load', initMap);
        }
    </script>
</body>
</html>
        """
        self.web_view.setHtml(html)
    
    def _on_load_progress(self, progress):
        """Atualiza o progresso do carregamento"""
        if progress < 100:
            self.status_label.setText(f"⬇️ Carregando página... {progress}%")
    
    def _on_load_finished(self, ok):
        """Chamado quando a página HTML é carregada"""
        if ok:
            print("✅ HTML carregado com sucesso")
            self.verificar_timer.start(500)
        else:
            print("❌ Falha ao carregar HTML")
            self.tentativas += 1
            if self.tentativas < self.max_tentativas:
                QTimer.singleShot(1000, self._carregar_html_base)
            else:
                self._mostrar_erro()
    
    def _verificar_carregamento(self):
        """Verifica se o mapa JavaScript foi inicializado"""
        def check_map(result):
            if result == "true":
                print("✅ Mapa Leaflet inicializado com sucesso")
                self.mapa_carregado = True
                self.verificar_timer.stop()
                QTimer.singleShot(300, self._mostrar_mapa)
            else:
                self.tentativas += 1
                if self.tentativas >= self.max_tentativas:
                    self.verificar_timer.stop()
                    print("⚠️ Timeout ao carregar mapa, mas mostrando mesmo assim")
                    QTimer.singleShot(300, self._mostrar_mapa)
        
        self.web_view.page().runJavaScript(
            "typeof window.mapaCarregado !== 'undefined' && window.mapaCarregado === true ? 'true' : 'false'",
            check_map
        )
    
    def _mostrar_mapa(self):
        """Mostra o mapa e esconde o loading"""
        print("🗺️ Mostrando mapa...")
        
        # Parar animação
        self.anim_timer.stop()
        
        # ⚡ CORREÇÃO: Fade out do overlay
        self.loading_overlay.hide()
        
        # Mostrar mapa
        self.layout.setCurrentIndex(0)
        
        # Atualizar com dados se já disponíveis
        if self.dados_prontos and self.coordenadas and self.fretes:
            QTimer.singleShot(300, self._atualizar_mapa_js)
    
    def _mostrar_erro(self):
        """Mostra mensagem de erro no loading"""
        self.text_label.setText("⚠️ Erro ao carregar")
        self.status_label.setText("Verifique sua conexão com a internet")
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(100)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: #e0e0e0;
                border-radius: 4px;
                border: none;
            }
            QProgressBar::chunk {
                background-color: #F44336;
                border-radius: 4px;
            }
        """)
    
    def set_dados(self, coordenadas, fretes):
        """Define os dados e atualiza o mapa"""
        self.coordenadas = coordenadas
        self.fretes = fretes
        self.dados_prontos = True
        
        if self.mapa_carregado:
            self._atualizar_mapa_js()
    
    def _atualizar_mapa_js(self):
        """Executa JavaScript para atualizar o mapa"""
        if not self.coordenadas or not self.fretes:
            return
        
        lat = self.coordenadas['lat']
        lon = self.coordenadas['lon']
        nome = self.coordenadas.get('nome', 'Estabelecimento')
        
        fretes_data = []
        for frete in self.fretes:
            if frete.get('ativo', True):
                fretes_data.append({
                    'km_minimo': float(frete['km_minimo']),
                    'km_maximo': float(frete['km_maximo']),
                    'valor': float(frete['valor']),
                    'ativo': True
                })
        
        js_code = f"""
        try {{
            addMarker({lat}, {lon}, "{nome}");
            const fretes = {json.dumps(fretes_data)};
            addCircles(fretes, {lat}, {lon});
            addLegend(fretes);
            centralizarMapa({lat}, {lon});
            setTimeout(function() {{
                map.invalidateSize();
            }}, 100);
        }} catch(e) {{
            console.error('Erro ao atualizar mapa:', e);
        }}
        """
        
        self.web_view.page().runJavaScript(js_code)
        
class Estabelecimento(QMainWindow, estabelecimento):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Detectar sistema
        self.is_weak_system = is_sistema_fraco()
        self.has_gpu = has_gpu()
        
        if self.is_weak_system:
            print("⚠️ Sistema fraco detectado - usando Leaflet.js minimalista")
        else:
            print("✅ Sistema com GPU detectado - usando Leaflet.js otimizado")

        self.coords_estabelecimento = None
        self.timer = QTimer()
        self.grupo = QButtonGroup()
        
        # Configurar layout do mapa
        self.map_layout = self.widget_33.layout()
        if self.map_layout is None:
            self.map_layout = QVBoxLayout(self.widget_33)
        
        self.map_container = QWidget()
        self.map_container_layout = QVBoxLayout(self.map_container)
        self.map_container_layout.setContentsMargins(0, 0, 0, 0)
        self.map_layout.addWidget(self.map_container)
        
        # Usar SEMPRE Leaflet.js com loading
        print("🗺️ Usando Leaflet.js puro com tela de carregamento")
        self.mapa_widget = MapaLeafletWidget()
        self.map_container_layout.addWidget(self.mapa_widget)
        self.map_view = self.mapa_widget

        # Resto da inicialização...
        APPContext.horarios_store = HorarioStore()
        self.horarios_store = APPContext.horarios_store
        self.horarios_store.horario_adicionado.connect(self.atualizar_tabela_horarios)

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
            self.DataExpiracaoLine.setText(str(data_formatada_expiracao))

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
        columns = ["dia_semana", "hora_inicio", "hora_fim"]
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
            self.fretes = APPContext.api_client.get("/estabelecimento/desktop/taxas-km")
            self.coords_estabelecimento = APPContext.api_client.get("/estabelecimento/desktop/coordenadas-estabelecimento")
            
            # Atualizar mapa
            self.atualizar_mapa()
            
            return self.fretes  
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar dados: {str(e)}")
            return

    def atualizar_mapa(self):
        """Atualiza o mapa com os dados atuais"""
        if not self.coords_estabelecimento or not self.fretes:
            return
        
        if self.mapa_widget:
            self.mapa_widget.set_dados(self.coords_estabelecimento, self.fretes)
        
    def preencher_tabela(self):
        self.form_taxas = TaxasEntregas(parent=self, fretes=self.tabela)
        self.form_taxas.show()

    def atualizar_localizacao(self):
        self.form_coordenadas = CoordEstabelecimento(parent=self)
        self.form_coordenadas.show()