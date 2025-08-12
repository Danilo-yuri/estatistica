import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
# pip install scikit-learn
from sklearn.linear_model import LinearRegression

# Carregamento e preparacao dos dados

EXPOSICAO_ALGODAO = 'data/lungDisease.csv'
dataframe = pd.read_csv(EXPOSICAO_ALGODAO)
print(dataframe.head())

# Grafico de DISPERÇÃO
# dataframe.plot.scarret(x = 'Exposure', y = 'PEFR')
# plt.show()

#dataframe.plot.scatter(x = 'Exposure', y = 'PEFR')
#plt.show()

# 3. Configuração e treinamento do modelo
# Defina a variavel preditora (independente), que e
# a Exposure e a variavel de resultado que e o PEFR
predictors= ['Exposure']
outcome = 'PEFR'
# Instanciar o modelo
model = LinearRegression()
# Treinar de treinamento
model.fit(dataframe[predictors], dataframe[outcome])

# 4. Exibição dos coeficiente
# intercepto
print(f'Intercepto: {model.intercept_:.3f}')
# Coeficiente angular
print(f'Coeficiente Angular: {model.coef_[0]}')
# 5. Geração do grafico
fig, (reg) = plt.subplots(1, 1, figsize=(4, 4))
#grafico regreção

reg = sns.regplot(x = 'Exposure', y = 'PEFR', data = dataframe,ax = reg)
plt.tight_layout()
plt.show()