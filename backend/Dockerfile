# backend/Dockerfile
FROM python:3.13

# Diretório de trabalho no container
WORKDIR /backend

# Copia apenas as dependências primeiro para cache
COPY requirements.txt .
COPY alembic.ini .
COPY alembic ./alembic

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código restante do backend
COPY . .

# Expõe a porta do FastAPI
EXPOSE 8000

# Comando para rodar o FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
