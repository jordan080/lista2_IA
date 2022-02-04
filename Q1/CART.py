import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.preprocessing import OrdinalEncoder

dataset = pd.read_csv('Q1/database.csv')
dataset = dataset.loc[:, dataset.columns != 'Exemplo']
enc = OrdinalEncoder()
dataset = enc.fit_transform(dataset)

X = dataset[:, :-1]
print(X[0])
print(X[1])
print(X[2])
print(X[3])

y = dataset[:, -1]

clf = DecisionTreeClassifier(random_state = 0)
clf = clf.fit(X, y)

plot_tree(clf)
plt.show()

