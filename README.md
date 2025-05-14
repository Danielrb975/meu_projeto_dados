# Análise Exploratória de Dados - Projeto Xlung

Este projeto realiza uma análise exploratória do dataset `cleanedxlung.csv`, utilizando Python e bibliotecas como `pandas`, `matplotlib` e `seaborn`.

## 📁 Estrutura do projeto

- `cleanedxlung.csv`: Dataset analisado.
- `analise_exploratoria.py`: Script que faz a leitura dos dados, mostra informações básicas, estatísticas, valores ausentes e únicos.
- `graficos_exploratorios.py`: Script que gera visualizações dos dados para extrair insights.

## 📊 Análises realizadas

- Visualização de dados ausentes
- Distribuição de colunas categóricas
- Comparação entre `signature_active` e `order_price`
- Correlação entre variáveis numéricas
- Frequência de planos (`plan_duration`)

Os gráficos são salvos na pasta do projeto automaticamente.

## ▶️ Como rodar

1. Instale as bibliotecas necessárias:

```bash
pip install pandas matplotlib seaborn
