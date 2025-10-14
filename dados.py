import pandas as pd
import requests
import math
from time import sleep
import json

# Carregar CSV
df = pd.read_csv(
    "C:/Users/eu/Downloads/PRODUTOS.csv",
    sep=';',
    encoding='latin1'
)

def sanitize_row(row):
    """Converte NaN ou Inf para None"""
    row_dict = row.to_dict()
    for k, v in row_dict.items():
        if isinstance(v, float) and (pd.isna(v) or math.isinf(v)):
            row_dict[k] = ""
    return row_dict


# Iterar sobre cada linha
for idx, row in df.iterrows():
    url = "http://127.0.0.1:8000/products/products"

    # Transformar a linha em um dicionário JSON
    data_json = sanitize_row(row)

    data_json["cod_sistema"] = str(data_json["cod_sistema"])
    data_json["cod_pdv"] = str(data_json["cod_pdv"])
    data_json["preco_custo"] = float(data_json["preco_custo"].replace(",", "."))# type: ignore
    data_json["preco_venda"] = float(data_json["preco_venda"].replace(",", "."))
    
    print(data_json)

      # Pequena pausa para evitar sobrecarga no servidor


    try:
        response = requests.post(url, json=data_json, timeout=10)
        if response.status_code == 200:
            print(f"Linha {idx} enviada com sucesso!")
        else:
            print(f"Erro ao enviar linha {idx}: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão na linha {idx}: {e}")

print("Envio finalizado!")