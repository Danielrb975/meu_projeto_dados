# analise_exploratoria.py

import pandas as pd

# Lê os dados
df = pd.read_csv('cleanedxlung.csv')

# Visualiza as 5 primeiras linhas
print("Prévia dos dados:")
print(df.head(), "\n")

# Mostra as colunas e tipos de dados
print("Colunas e tipos:")
print(df.info(), "\n")

# Estatísticas básicas das colunas numéricas
print("Estatísticas descritivas:")
print(df.describe(), "\n")

# Verifica valores ausentes
print("Valores ausentes por coluna:")
print(df.isnull().sum(), "\n")

# Contagem de valores únicos por coluna
print("Valores únicos por coluna:")
print(df.nunique(), "\n")
