import pandas as pd

df = pd.read_csv('dataset.csv')
print(df.head())
print()

# Filtrando as vendas que ocorreram para o segmento de Home Office e na região South
filtro = df[(df.Segmento == 'Home Office') & (df.Regiao == 'South')].head()
print(filtro)
