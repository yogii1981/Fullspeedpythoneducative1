import numpy as np

# import timeit
#
# # a = np.array[1,2,3,4,5]
# # print(a)
#
#
# # time to calculate the square in million
# n = 1000000
# L = range(n)
# c = ([i**2 for i in L])
# print(timeit.timeit(setup = c, stmt = ))
#
#
#
# np.arrange(10)
#
# A = np.arrange (n)
# c1 = timeit.timeit(A**2)
# print(c1)


# Creating a two-dimensional array of size 3 rows and 4 columns

b = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
print(b)
print(b[1, ::-2])

print(b.ndim)  # informs about  dimension of array like one dimension, two dimension or so on
print(b.shape)  # informs about number of rows and column
print(len(b))  # informs about the length

# Three dimensional Array
n

# Create a matrix of zeros
x = np.zeros((3, 4))
print(x)

y = np.ones((5, 6))
print(y)

print(np.eye(3, 3))

print(np.diag([1, 2, 3]))

print(np.empty((2, 2)))

import numpy as np
from numpy import random

# np.ramdom.seed(3)
x = random.randint(0, 20, 15)  # generate random integers between to 0 to 20 and only generate 15 numbers
print(x)
