"""Linear regression
    Y = mX + C
"""

"Impelenting the model, convert everything to code"

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [12.0, 9.0]

# preprocessing Input data
data = pd.read_csv('data.csv', sep='delimiter', header=None)
X = data.iloc[:, 0]
Y = data.iloc[:, 1]
plt.scatter(X, Y)
plt.show()
