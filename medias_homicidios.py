import pandas as pd
import numpy as np
from scipy.stats import trim_mean





def get_medias(df_dados_brutos):

    media_populacao = df_dados_brutos['populacao'].mean()
    media_homicidios = df_dados_brutos['Taxa_homicidios'].mean()
    # medias aparadas:
    proporcao_corte = 0.1
    media_aparada_populacao = trim_mean(df_dados_brutos['populacao'], proportiontocut=proporcao_corte)
    media_aparada_homicidios = trim_mean(df_dados_brutos['Taxa_homicidios'], proportiontocut=proporcao_corte)
    # medianas:
    mediana_populacao = df_dados_brutos['populacao'].median()
    mediana_homicidios = df_dados_brutos['Taxa_homicidios'].median()
    # mediana ponderada = soma(valor x peso) / soma(peso)
    # onde valor é taxa_homicidios e o peso é polpulacao
    #calcular a média ponderada de homicidios onde o peso de cada cidade é sua população
    media_ponderada = np.average(df_dados_brutos['Taxa_homicidios'], weights=df_dados_brutos['populacao'])

    df_medias = pd.DataFrame({
        'populacao': [media_populacao, media_aparada_populacao, mediana_populacao, np.nan],
        'Taxa homicidios': [media_homicidios, media_aparada_homicidios, mediana_homicidios, media_ponderada]
    }, index=['Média','Média Aparada', 'Mediana', 'Media Ponderada'])
    return df_medias

    

df_dados_brutos = pd.read_csv('taxa_homicidios.csv')
df_medias = get_medias(df_dados_brutos)
print(df_medias.to_string(float_format="%.2f"))