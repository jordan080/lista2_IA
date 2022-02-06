import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.preprocessing import OneHotEncoder
from sklearn import tree
import graphviz

dataset = pd.read_csv('database.csv')
dataset = dataset.loc[:, dataset.columns != 'Exemplo']

X = dataset[['História de Credito', 'Dívida', 'Garantia', 'Renda']]
y = dataset["Risco"]

enc = OneHotEncoder()
X_enc = enc.fit_transform(X)

clf = DecisionTreeClassifier(random_state = 0)
clf = clf.fit(X_enc, y)

dot_data = tree.export_graphviz(clf, feature_names=enc.get_feature_names_out(input_features = X.columns), class_names=clf.classes_)

graph = graphviz.Source(dot_data)
graph.render("tree_plot")
graph.view()

