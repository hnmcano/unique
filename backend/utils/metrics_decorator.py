# utils/metrics_decorator.py
from functools import wraps
import time
from prometheus_client import Counter, Histogram

# Métricas
endpoint_requests = Counter(
    'pdv_endpoint_requests_total',
    'Total de requisições por endpoint',
    ['tenant', 'endpoint', 'method', 'status']
)

endpoint_duration = Histogram(
    'pdv_endpoint_duration_seconds',
    'Duração das requisições por endpoint',
    ['tenant', 'endpoint', 'method']
)

def track_metrics(endpoint_name: str = None):
    """
    Decorator para adicionar métricas automaticamente em qualquer rota
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Extrai tenant do kwargs (vem da dependência)
            estabelecimento = kwargs.get('estabelecimento')
            tenant = estabelecimento.subdominio if estabelecimento else 'unknown'
            
            # Nome do endpoint
            endpoint = endpoint_name or func.__name__
            
            # Obtém o método HTTP (GET, POST, etc)
            request = kwargs.get('request')
            method = request.method if request else 'GET'
            
            # Mede tempo
            start_time = time.time()
            
            try:
                # Executa a função
                result = await func(*args, **kwargs)
                status = "200"
                return result
            except Exception as e:
                status = "500"
                raise
            finally:
                duration = time.time() - start_time
                
                # Registra métricas
                endpoint_requests.labels(
                    tenant=tenant,
                    endpoint=endpoint,
                    method=method,
                    status=status
                ).inc()
                
                endpoint_duration.labels(
                    tenant=tenant,
                    endpoint=endpoint,
                    method=method
                ).observe(duration)
        
        return wrapper
    return decorator