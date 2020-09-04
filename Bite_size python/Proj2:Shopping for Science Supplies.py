# Total Money given for experiment

# total_money = 25

# tax

tax = 0.06

# Number of flowerpots
No_flowerpot = int(input("Enter the number of flower pots:"))

# Cost of Flowerpots

cost_flowerpot = 4.00

total_cost_of_flowers = (No_flowerpot * cost_flowerpot)
print(total_cost_of_flowers)


# Number of flowerseed bags
No_of_flower_seedbags = int(input("Enter the number of flower seed bags:"))

# cost of pack of flower seeds

cost_flowerseed = 1.00

total_cost_of_flowerseed = (No_of_flower_seedbags * cost_flowerseed)
print(total_cost_of_flowerseed)

# Number of soilbags
No_soil_bag = int(input("Enter the number of soil bags:"))

# cost of bag soil

cost_bagofsoil = 5.00

total_cost_of_soilbag = (No_soil_bag * cost_bagofsoil)
print(total_cost_of_soilbag)

# total_cost
total_cost = total_cost_of_flowers + total_cost_of_flowers + total_cost_of_flowerseed
print(total_cost)
