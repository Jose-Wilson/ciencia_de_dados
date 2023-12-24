import pandas as pd

df = pd.read_csv('dataset.csv')
print(df.head(10))
print()

print(df.isna().sum())
print()

moda = df['Quantidade'].value_counts().index[0]
print(moda)
print()

df['Quantidade'].fillna(value=moda, inplace=True)
print(df.isna().sum())
print()

print(df.head())
print()

print(df.Valor_Venda.describe())
print()

df2 = df.query('229 < Valor_Venda < 1000')
print(df2.Valor_Venda.describe())
print()

df3 = df2.query('Valor_Venda > 766')
print(df3.head())
print()

print(df.shape)
print()

print(df[df['Quantidade'].isin([5, 7, 9, 11])])
print()

print(df[df['Quantidade'].isin([5, 7, 9, 11])][:10])
print()

