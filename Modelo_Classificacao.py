"""
Criando um modelo de classificação
"""

# Importando as bibliotecas (pandas, matplotlib, numpy)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Importando o DataSet iris
# Instalar com pip install scikit-learn
from sklearn.datasets import load_iris

# Obtendo os dados do dataset
data = load_iris()

# Valores de X
data.data

# Valores de Y
data.target

# Transformando em um DataFrame
iris = pd.DataFrame(data.data)

# Nome das colunas
iris.columns = data.feature_names

# Adicionando a coluna Target ao DataFrame
iris['Target'] = data.target

# Contando a quantidade de cada um dos targets
iris['Target'].value_counts()
# Retirando os dados que são iguais ao Target = 2
iris = iris[iris.Target != 2]

# Plotando a matriz de todos os valores com Scatter Matrix do pandas
pd.plotting.scatter_matrix(iris);   

# Plotando a matriz de todos os valores com o seaborn
# Propriedade hue= colore os dados de acordo com a coluna escolhida.
sns.pairplot(iris, hue='Target');

# Tracando um scatter do matplotlib das colunas "petal length (cm) e "petal width (cm)".
fig, ax = plt.subplots()

ax.scatter(iris['petal length (cm)'], iris['petal width (cm)'])

print(plt.show())
#print(iris.head())

