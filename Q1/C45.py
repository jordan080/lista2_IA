from chefboost import Chefboost as chef
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.preprocessing import OrdinalEncoder

dataset = pd.read_csv("Q1/database.csv")
dataset = dataset.loc[:, dataset.columns != 'Exemplo']

config = {'algorithm' : 'C4.5'}

model = chef.fit(dataset.copy(),  config = {}, target_label = 'Risco', validation_df = None)

features = ['História de Credito',	'Dívida', 'Garantia', 'Renda']
X = dataset[features]

features2 = ['Risco']
Y = dataset[features2]

enc = OrdinalEncoder()
a = enc.fit_transform(X)
b = enc.fit_transform(Y)

clf = DecisionTreeClassifier(random_state = 0)
clf = clf.fit(a, b)

plot_tree(clf)
plt.show()
