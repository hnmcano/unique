# from sqlalchemy import create_engine, MetaData, Table

#  # Configurar a conexão (exemplo com SQLite)
# engine = create_engine('sqlite:///banco.db')
# metadata = MetaData()

#  # Refletir a tabela (substitua 'nome_da_tabela' pelo nome real)
# tabela = Table('Carrinhos', metadata, autoload_with=engine)

#  # Conectar e deletar todos os dados
# with engine.connect() as conn:
#     conn.execute(tabela.delete())
#     conn.commit()

import psycopg2

conn = psycopg2.connect(
    "postgresql://neondb_owner:npg_1wGagLzHX3od@ep-rough-resonance-ahgf2c21.c-3.us-east-1.aws.neon.tech/backend-alembic?sslmode=require&channel_binding=require"
)

cur = conn.cursor()
cur.execute("select 1")
print(cur.fetchone())

conn.close()