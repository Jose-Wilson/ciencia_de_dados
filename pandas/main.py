from pandas import DataFrame
import pandas as pd

# Cria um dicionário
dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'],
         'Ano': [2004, 2005, 2006, 2007, 2008],
         'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]}
print(dados)
print()

df = DataFrame(dados)
print(df)
print()

print(type(df))
print()

colunas = DataFrame(dados, columns = ['Estado', 'Taxa Desemprego'])
print(colunas)
print()

# Criando outro dataframe com os mesmo dados anteriores mas adicionando uma coluna
df2 = DataFrame(dados,
                columns = ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'],
                index = ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])
print(df2)
print()

print(df2.values)
print()

print(df2.dtypes)
print()

print(df2.columns)
print()

print(df2['Estado'])
print()

print(df2[['Estado', 'Ano']])
print()

print(df2.index)
print()

print(df2.filter(items=['estado3'], axis=0))
print()

print(df2.head())
print()

print(df2.dtypes)
print()

print(df2.describe())
print()

print(df2.isna())
print()

print(df2['Taxa Crescimento'].isna())
print()

import numpy as np
df2['Taxa Crescimento'] = np.arange(5.)
print(df2)
print()

print(df2['estado2':'estado4'])
print()

print(df2[df2['Taxa Desemprego'] < 2])
print()

print(df2['Taxa Crescimento'])
print()

print(df2[['Estado', 'Taxa Crescimento']])
print()

print(df2[['Estado', 'Taxa Crescimento', 'Ano']])
