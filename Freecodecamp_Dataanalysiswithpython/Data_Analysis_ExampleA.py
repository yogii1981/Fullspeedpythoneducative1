import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


sales = pd.read_csv(
    '/Users/yogeshsharma/Documents/Freecodecamp_datanalysiswithpython/sales_data.csv')  # import and read the file located in a specific folder
# print(sales)     #display the csv files

print()
print(sales.head())  # display the header and first few lines

# Info about the each column and what the data is all about
# pri
print(sales.info)

# provide statistical property of the rows
print()
print(sales.describe)

# Let us know the number of rows and columns
print(sales.shape)

## Numerical Analysis and visualization##
# we will analyze the column "Unit_Cost"
print(sales['Unit_Cost'].describe())

# displays the mean of the column of Unit_Cost
print(sales['Unit_Cost'].mean())

# img1 = pd.sales(np.random.randn(100,5), columns = list('Unit_Cost'))
# print(img1.boxplot(return_types = 'axes'))

print(sales.boxplot(column=['Unit_Cost'], return_type='axes'))
plt.show()

# print(sales['Unit_Cost'].plot(kind='box', vert = False, figsize = (14,6)))

# print(sales['Unit_Cost'].plot(kind='density', vert = False, figsize = (14,6))) #kde'

# help in show casing all the columns if describe funtion didn't show all the columns summary earlier
with pd.option_context('display.max_columns', 100):
    print(sales.describe)
