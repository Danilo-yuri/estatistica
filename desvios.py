import pandas as pd
import numpy as np
from faker import Faker

# instância do Faker para gerar nomes
fake = Faker('pt_BR')

#condições dos dados [população]
media_notas = 70
desvio_padrao_notas = 10
num_alunos = 100
notas = np.random.normal(loc=media_notas, scale=desvio_padrao_notas, size=num_alunos)
print(f"notas random: {notas}")
# limita as notas entre 0 e 100
# o que for menor que 0 vira 0 eo que è maior que 100 vira 100
notas = np.clip(notas, 0, 100)

# --- Cálculo das Medidas -- 0,
# 1. Média
media = np.mean(notas)
# 2. Mediana
mediana = np.median(notas)
# 3. FDesvio (Simples)
# ex. nota 80 - 70 = 10
desvios = notas - media
# 4. Desvio Absoluto
# ex. 60(nota) - 70(media) = |10| (desvio)
desvios_absolutos = np.abs(notas - media)
# 5. Variancia individual.
# ex. 80(nota) - 70(media) = 0 * 10 = 100(variÂncia)
variancias_individuais = (notas - media)**2
variancia = np.var(notas, ddof=1) # para variancia amostral (n-1)
# 6. Desvio padrão
desvio_padrao = np.std(notas)
# 7 .Desvio Absoluto (Mediana)
desvios_abs_emrelacao_mediana_individuais = np.abs(notas - mediana)
