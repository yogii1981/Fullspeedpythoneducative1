# # Exercise 2.10
# print("Problem1")
# n = 42
# print(n)
#
# # print("Problem2")
# # 42 = n
# print(n)    # this will give error as integer can act like a variable name

# print("Problem3")
x = y = 1
print(x)
print(y)

c = "xy"
print(c)

# Exercise 2.2
# volume of sphere with radius 5
import math

radius = 5
volume = (int(4 / 3) * math.pi * (radius) ** 3)
print(volume)

# def volofspehere(r):
#     return ((4/3) * 3.14 * (r) ** 3)
#
# print(volofspehere(5))
#
#
# # def area(a,b):
# #     return ( a  * b)
# #
# # area(3,4)


# Exercise 2.2.2
cover_price = 24.95
discount = 40 * (1 / 100)
afterdiscountpriceofbook = 24.95 * 0.6
shipping_cost_first = 3
subsequent_shipping_cost = 0.75
numofbookordered = 60

for numofbookordered in range(61):  # for book order number 60
    if numofbookordered == 1:  # if only one book is ordered
        totalwholesalecost = (afterdiscountpriceofbook + shipping_cost_first)
        print(totalwholesalecost)
        numofbookordered += 1  # if bookordered are more than one
    else:
        totalwholesalecost = (numofbookordered * afterdiscountpriceofbook) + (
                    (numofbookordered - 1) * 0.75) + shipping_cost_first
        print(totalwholesalecost)
print(totalwholesalecost)

# Exercise 2.2.3
# start_time = (6 + 52/60.0)
#
# run_easypace  = 2 * (8 +15/ 60.0)/60
# tempo_speed = 3 * (7 + 12/60.0)/60
# totaltime = run_easypace + tempo_speed
# print("Totaltime", totaltime)


start_time = (6 * 60 + 52) * 60
easy_time = (8 * 60 + 15) * 2
tempo_time = (7 * 60 + 12) * 3

breakfast_hour = (start_time + easy_time + tempo_time) / (60 * 60)
breakfast_int_hour = int(breakfast_hour)

breakfast_minute = (breakfast_hour - breakfast_int_hour) * 60
breakfast_int_minute = int(breakfast_minute)

print('Breakfast is at {}.{}'.format(breakfast_int_hour, breakfast_int_minute))
