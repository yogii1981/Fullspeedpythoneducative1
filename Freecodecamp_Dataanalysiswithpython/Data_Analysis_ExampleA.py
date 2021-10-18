import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %matplotlib inline

sales = pd.read_csv(
    '/Users/yogeshsharma/Documents/Freecodecamp_datanalysiswithpython/sales_data.csv')  # import and read the file located in a specific folder
# print(sales)     #display the csv files

print()
print(sales.head())  # display the header and first few lines

# Info about the each column and what the data is all about
print(sales.info())

# provide statistical property of the rows
print()
print(sales.describe())

# Let us know the number of rows and columns
print(sales.shape)
