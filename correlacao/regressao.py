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
fig, (reg, ax, res) = plt.subplots(1, 3, figsize=(12, 4))
#grafico regreção

reg = sns.regplot(x = 'Exposure', y = 'PEFR', data = dataframe,ax = reg)

# Parcial
# Definir os limites dos eixos x e y 
ax.set_xlim(0, 23)
ax.set_ylim(295, 450)
# Definir os rotulos
ax.set_xlabel('Exposure')
ax.set_ylabel('PERF')
#Plotar a linha
ax.plot(dataframe['Exposure'], model.predict(dataframe[predictors]), '-')
# Adicionar o texto b0
ax.text(0.4, model.intercept_, r'$b_0$', size='larger')
# Criar dataframe dos dados parciais e treinar
x = pd.DataFrame({'Exposure': [7.5, 17.5]})
y = model.predict(x)
print(y)
ax.plot((7.5, 7.5, 17.5), (y[0], y[1], y[1]), '--')
# Exibir DeltaY e Deltax no grafico
ax.text(5, np.mean(y), r'$\Delta Y$', size='larger')
ax.text(12, y[1] - 10, r'$\Delta X$', size='larger')
# Adicionar anotação para o coeficiente angular
ax.text(12, 390, r'$b_1 = \frac{\Delta Y}{\Delta X}$', size='larger')

#Valores ajustado e residuos
#Gera os valores ajustados do modelo
fitted = model.predict(dataframe[predictors])
 #calcula os residuos
residuals = dataframe[outcome] - fitted

#Exibe o gráfico de correlação
res = dataframe.plot.scatter(x = 'Exposure', y = 'PEFR', ax = res)
res.plot(dataframe.Exposure, fitted)
# Para cada valor de índece
for x, yatual, yfitted in zip(dataframe.Exposure, dataframe.PEFR, fitted):
    print(f'x: {x} - yreal: {yatual} - yreta: {yfitted}')
    res.plot((x, x), (yatual,yfitted), '--', color='C1')
plt.tight_layout()
plt.show()