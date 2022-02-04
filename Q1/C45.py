from chefboost import Chefboost as chef
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

dataset = pd.read_csv("Q1/database.csv")

config = {'algorithm' : 'CART'}

model = chef.fit(dataset.copy(),  config = config, target_label = 'Risco')

print(model)

