import pandas as pd

tabela = pd.read_csv(r"C:\Users\eu\OneDrive\Documentos\produtos_.csv", sep=';', encoding='latin-1')

print(tabela.columns.tolist)

print(tabela)
