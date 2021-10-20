import numpy as np
import pandas as pd

import matplotlib as plt

sales = pd.read_csv(
    '/Users/yogeshsharma/Documents/Freecodecamp_datanalysiswithpython/sales_data.csv')  # import and read the file located in a specific folder
# print(sales)     #display the csv files


## Column Wrangling##

print('Sales[Revenue_per_Age')
sales['Revenue_per_Age'] = sales['Revenue'] / sales['Customer_Age']

# print first 100 rows of revenue per age
print(sales['Revenue_per_Age'][:100])

# Calculate new column
sales['Calculated_Cost'] = sales['Order_Quantity'] * sales['Unit_Cost']

# Print the first 10 rows of the new column - Calculated Costs
print(sales['Calculated_Cost'][0:10]

ax = sales.plot(kind='scatter', x='Calculated_Cost', y='Profit', figsize(4, 5))
print(ax)

import numpy as np

# prob
data = {i: np.random.rand() for i in range(7)}
print(data)
