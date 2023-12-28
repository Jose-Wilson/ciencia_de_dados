import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

# Carrega o dataset
df = pd.read_csv('dataset.csv')
print(df)
print()
print(df.shape)
print()
print(df.head())
print()
print(df.tail())
print()
print(df.columns)
print()
# Verificando o tipo de dado de cada coluna
print(df.dtypes)
print()
# Resumo estatístico da coluna com o valor de venda
print(df['Valor_Venda'].describe())
print()
# Verificando se há registros duplicados
print(df[df.duplicated()])
print()
# Verificando de há valores ausentes
print(df.isnull().sum())
print()
print(df.head())
print()
# Primeiro filtramos o dataframe com os registros da categoria que desejamos
df_p1 = df[df['Categoria'] == 'Office Supplies']
# Em seguida agrupamos por cidade e calculamos o total de valor_venda
df_p1_total = df_p1.groupby('Cidade')['Valor_Venda'].sum()
# Então encontramos a cidade com maior valor de venda
cidade_maior_venda = df_p1_total.idxmax()
print(f'Cidade com maior venda: {cidade_maior_venda}')
print()
# Para conferir o resultado
print(df_p1_total.sort_values(ascending=False))
print()
# Calculamos o total de vendas para cada data de pedido
df_p2 = df.groupby('Data_Pedido')['Valor_Venda'].sum()
print(df_p2.head())
print()
# Plot
#plt.figure(figsize=(20, 6))
#df_p2.plot(x = 'Data_Pedido', y = 'Valor_Venda', color = 'green')
#plt.title('Total de vendas por Data do Pedido')
#plt.show()
# Agrupamos por estado e calculamos o total de vendas
df_p3 = df.groupby('Estado')['Valor_Venda'].sum().reset_index()
print()
# Plot
plt.figure(figsize=(16, 6))
sns.barplot(data=df_p3,
            y = 'Valor_Venda',
            x = 'Estado').set_title('Vendas por Estados')
plt.xticks(rotation = 80)
plt.show()
print()