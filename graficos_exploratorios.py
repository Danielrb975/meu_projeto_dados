# graficos_exploratorios.py

# IMPORTAÇÕES

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega os dados
df = pd.read_csv("cleanedxlung.csv")

# Configurações iniciais
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# GRÁFICO 1 - Distribuição da duração dos planos

plt.figure()
sns.histplot(df['plan_duration'], bins=30, kde=True)
plt.title("Distribuição da Duração dos Planos")
plt.xlabel("Dias de Plano")
plt.ylabel("Frequência")
plt.savefig("grafico1_duracao_planos.png")
plt.close()

# GRÁFICO 2 - Situação das assinaturas

plt.figure()
sns.countplot(x="signature_active", data=df)
plt.title("Assinaturas Ativas vs Inativas")
plt.xlabel("Assinatura Ativa (0 = Não, 1 = Sim)")
plt.ylabel("Contagem")
plt.savefig("grafico2_assinaturas.png")
plt.close()

# GRÁFICO 3 - Métodos de pagamento mais usados

plt.figure()
sns.countplot(y="payment_method", data=df, order=df['payment_method'].value_counts().index)
plt.title("Frequência dos Métodos de Pagamento")
plt.xlabel("Contagem")
plt.ylabel("Método de Pagamento")
plt.savefig("grafico3_metodos_pagamento.png")
plt.close()

# GRÁFICO 4 - Descontos de cupons

# Remove valores nulos
cupons = df[df['coupon_amount'].notnull()]

plt.figure()
sns.histplot(cupons['coupon_amount'], bins=20)
plt.title("Distribuição dos Descontos de Cupons")
plt.xlabel("Valor do Desconto")
plt.ylabel("Frequência")
plt.savefig("grafico4_cupons.png")
plt.close()

# GRÁFICO 5 - Ocupações mais frequentes (Top 10)

top_ocupacoes = df['occupation'].value_counts().head(10)

plt.figure()
sns.barplot(x=top_ocupacoes.values, y=top_ocupacoes.index)
plt.title("Top 10 Ocupações Mais Frequentes")
plt.xlabel("Contagem")
plt.ylabel("Ocupação")
plt.savefig("grafico5_ocupacoes.png")
plt.close()
