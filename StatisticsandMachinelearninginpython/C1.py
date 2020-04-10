import numpy as np

X = np.array([[1, 2], [3, 4]])
v = np.array([1, 2])
np.dot(X, v)  # no broadcasting
X * v  # broadcasting
np.dot(v, X)
print(X - X.mean(axis=0))

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
