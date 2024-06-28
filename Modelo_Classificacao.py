"""
Criando um modelo de classificação
"""

# Importando as bibliotecas (pandas, matplotlib, numpy)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importando o cataset iris
from sklearn.datasets import load_iris

# Obtendo os dados do dataset
data = load_iris()

# Valores de X
data.data

# Valores de Y
data.target
