"""Loop to get all the values"""

# Method 1
ages = {
    "Peter": 10,
    "Sanjay": 12,
    "Rita": 14,
    "dilbagh": 16,
}

for x in ages:
    print("Method1", ages[x])

"""Write a program to display age and name where age is greater than 12"""

# Method 2
ages = {
    "Peter": 10,
    "Sanjay": 12,
    "Rita": 14,
    "dilbagh": 16,
}

for name, age in ages.items():
    if age > 12:
        print(name, age)
