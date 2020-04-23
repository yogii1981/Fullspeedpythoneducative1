"""Linear regression
    Y = mX + C
"""

"Implementing the model, convert everything to code"

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [12.0, 9.0]

# preprocessing Input data
data = pd.read_csv('data.csv')
X = data.iloc[:, 0]
Y = data.iloc[:, 1]
plt.scatter(X, Y)
plt.show()

"""Building the model"""
m = 0
c = 0
L = 0.001  # The learning rate
epochs = 1000  # the number of iterations to perfrom gradient descent

n = float(len(X))  # number of elements

# Performing Gradient Descent

for i in range(epochs):
    Y_pred = m * X + c  # the current predicted value of Y
    D_m = (-2 / n) * sum(X * (Y - Y_pred))  # Derivative wrt m
    D_c = (-2 / n) * sum(Y - Y_pred)  # Derivative wrt c
    m = m - L * D_m  # Update m
    c = c - L * D_c  # Update c

print(m, c)

# Making predictions
Y_pred = m * X + c

plt.scatter(X, Y)
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')  # regression line
plt.show()
