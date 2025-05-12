import pandas as pd
# le o arquivo CSV
df=pd.read_csv("EXPORT_XLUNG_CLIENTES_ORDER_STATUS_20250502.csv")
# mostrar as 5 primeiras linhas
print (df.head())
#informações gerais da tabela
print (df.info())
