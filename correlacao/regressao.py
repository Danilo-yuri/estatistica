import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
# pip install scikit-learn
from sklearn.linear_model import LinearRegression

EXPOSICAO_ALGODAO = 'data/lungDisease.csv'
dataframe = pd.read_csv(EXPOSICAO_ALGODAO)
print(dataframe.head())

dataframe.plot.scatter(x = 'Exposure', y = 'PEFR')
plt.show()