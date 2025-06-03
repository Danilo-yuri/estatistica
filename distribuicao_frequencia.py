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

# 3. Valor Maximo e Mínimo
    x_min = rol[0]
    x_max = rol[-1]
    print("\n3. Valor Máximo e Mínimo:")
    print(f" valor min: {x_min}")
    print(f" valor max: {x_max}")

 # 4. Amplitude total (AT)
    at = x_max - x_min   
    print("\n4. Amplitude Total (AT): ")
    print(f" AT = {at:.2f}")

# 5. Número de classes (A)
    k = math.ceil(math.sqrt(n))
    print(f"\n5. Número de Classes (K):")
    print(f"K = {k}")

# 6. Amplitude das Classes (h)
    h = at / k
    print("\n6. Amplitude das Classes (h):")
    print(f"h = {h}")
    # Arredondar amplitude das Classes
    num_casas_decimais = 0
    if at < k: # 0.1
        num_casas_decimais = 1
        if at * 10 > k: #0.01
            num_casas_decimais = 2
    h = np.ceil(h * (10**num_casas_decimais)) / (10**num_casa_decimais)
    print("\n6. Amplitude da Classes (h):")
    print(f"h = {int(h)}")


# --- ESTUDO DE CASO 01: IDADE DOS ALUNOS
dados_idades = [21, 21, 21, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 25, 25, 26, 27, 27, 28, 28, 30, 30, 31, 31, 31]
df_idades = analisar_dados_estatisticos(dados_idades, "idades alunos")
# print(df_idades.to_string())