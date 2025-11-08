from sqlalchemy import create_engine, MetaData, Table

 # Configurar a conexão (exemplo com SQLite)
engine = create_engine('sqlite:///banco.db')
metadata = MetaData()

 # Refletir a tabela (substitua 'nome_da_tabela' pelo nome real)
tabela = Table('Carrinhos', metadata, autoload_with=engine)

 # Conectar e deletar todos os dados
with engine.connect() as conn:
    conn.execute(tabela.delete())
    conn.commit()
    print('Todos os dados da tabela foram deletados')