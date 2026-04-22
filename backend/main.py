from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator, metrics
from prometheus_client import Counter, Histogram, Gauge
import logging
import os

# ============================================
# LOGGING
# ============================================
logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

# ============================================
# CRIAR APP FASTAPI
# ============================================
app = FastAPI(
    title="UniqueSystems - PDV",
    version="1.0.0",
)

# ============================================
# MÉTRICAS CUSTOMIZADAS (OPCIONAL)
# ============================================
# Métricas de negócio customizadas
pedidos_total = Counter('pdv_pedidos_total', 'Total de pedidos realizados')
vendas_total = Counter('pdv_vendas_total', 'Total de vendas em reais')
usuarios_ativos = Gauge('pdv_usuarios_ativos', 'Número de usuários ativos')

http_requests_by_tenant = Counter(
    'http_requests_by_tenant_total',
    'HTTP requests by tenant',
    ['tenant', 'handler', 'method', 'status']
)

@app.middleware("http")
async def add_tenant_to_metrics(request: Request, call_next):
    # Extrair tenant do header
    tenant = request.headers.get("x-tenant-slug", "unknown")
    
    # Processar requisição
    response = await call_next(request)
    
    # Registrar métrica com tenant
    handler = request.scope.get("route", {}).path if request.scope.get("route") else request.url.path
    
    http_requests_by_tenant.labels(
        tenant=tenant,
        handler=handler,
        method=request.method,
        status=str(response.status_code)
    ).inc()
    
    return response


# ============================================
# PROMETHEUS METRICS
# ============================================
if os.getenv("ENABLE_METRICS", "false").lower() == "true":
    instrumentator = Instrumentator(
        should_group_status_codes=True,
        should_ignore_untemplated=True,
        should_instrument_requests_inprogress=True,
        excluded_handlers=["/metrics", "/health"],
    )
    
    # Adiciona métricas padrão
    instrumentator.add(metrics.latency())
    instrumentator.add(metrics.request_size())
    instrumentator.add(metrics.response_size())
    instrumentator.add(metrics.requests())
    
    # Instrumenta a aplicação
    instrumentator.instrument(app).expose(app, endpoint="/metrics")
    
    logger.info("✅ Prometheus metrics enabled at /metrics")

# ============================================
# CORS
# ============================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://hookahshisha.localhost:5173",
        "http://boahora.localhost:5173",
        "http://localhost:5173"
    ],
    allow_origin_regex=r"https://.*\.uniqsystems\.com\.br",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# ============================================
# INCLUIR ROUTERS
# ============================================
from routers import clientes, produtos, carrinhos, pedidos, caixa, estabelecimento, categorias, mesas, usuarios, impressoras, update
from service import websocketservice

app.include_router(clientes.router, prefix="/clientes", tags=["clientes"])
app.include_router(produtos.router, prefix="/produtos", tags=["produtos"])
app.include_router(carrinhos.router, prefix="/carrinho", tags=["carrinho"])
app.include_router(pedidos.router, prefix="/pedidos", tags=["pedidos"])
app.include_router(caixa.router, prefix="/caixa", tags=["caixa"])
app.include_router(estabelecimento.router, prefix="/estabelecimento", tags=["estabelecimento"])
app.include_router(categorias.router, prefix="/categorias", tags=["categorias"])
app.include_router(mesas.router, prefix="/mesas", tags=["mesas"])
app.include_router(websocketservice.router, prefix="/ws", tags=["websocket"])
app.include_router(usuarios.router, prefix="/usuarios", tags=["usuarios"])
app.include_router(impressoras.router, prefix="/impressoras", tags=["impressoras"])
app.include_router(update.router, prefix="/update", tags=["update"])