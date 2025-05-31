import pandas as pd
import numpy as np
import math

def analisar_dados_estatisticos(dados_brutos, nome_do_conjunto):
    print(f"--- Análise Estatistica para: {nome_do_conjunto} ---")

    # 1. Rol(Dados Ordenados)
    rol = sorted(dados_brutos)
    print("\n1. Rol (Dados Ordenados):")
    print(f" {rol}")

# 2. Tamanho da Amostra 
    n = len(rol)
    print("\n2. Tamanho da Amostra (n):")
    print(f" n = {n}")

# --- ESYTUDO DE CASO 01: IDADE DOS ALUNOS
dados_idades = [21, 21, 21, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 25, 25, 26, 27, 27, 28, 28, 30, 30, 31, 31, 31]
df_idades = analisar_dados_estatisticos(dados_idades, "idades alunos")
# print(df_idades.to_string())