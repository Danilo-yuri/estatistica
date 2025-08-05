import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = 'data\sp500_data.csv.gz'
df = pd.read_csv(data)
print(df.head(5))

df=df.drop(columns=['ADS'])
print(df.head(5))
# Renomear coluna específica
df = df.rename(columns={'Unnamed: 0': 'Data'})
print(df.head(5))

# Trtansformar o campo data para datetime e settar ele como indice
df['Data'] = pd.to_datetime(df['Data'])
df = df.set_index('Data')
print(df.head(5))

# Encontrar a maior e menor data
data_inicio = df.index.min()
data_fim = df.index.max()
print(f"Quantidade de variações coletadas: { len(df)}")
print(f"Período de coleta: {data_inicio.strftime('%d/%m/%Y')} à {data_fim.strftime('%d/%m/%Y')}")

# quardar o ativo sendo usado
ativo = 'IBM'

# Encontrar o valor máximo e mínimo do ativo
maior_valor = df[ativo].max()
data_maior = df[ativo].idxmax()
menor_valor = df[ativo].min()
data_menor = df[ativo].idxmin()
print("-" * 30)
print("Ativo: {ativo}")
print(f"Maior variação diária: {menor_valor:.4f}")
print(f"Ocorreu no dia: {data_menor.strftime('%d/%m/%Y')}")

# MEDIDAS DE TENDÊNCIA CENTRAL
media = df[ativo].mean()
mediana = df[ativo].median()
moda = df [ativo].mode()
print(f"Medidas de tendência central para {ativo}:")
print(f"Média: {media:.4f}")
print(f"Mediana: {mediana:.4f}")
if (len(moda) > 0):
    print(f"Modas: {moda}")
else:
    print(f"O ativo {ativo} é amodal")
