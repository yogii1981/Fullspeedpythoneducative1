# first dictionary
# make a sctionary with named people
people = {'htaka': 'Haru Taka', 'ppatel': 'priya patel', 'rmala': 'rita mala'}
print(people)
print(people['ppatel'])  # dictionaryname[key] displays value

# look for a people
person = 'rmala'
print(people[person])

# Getting the length of the dictionary
print(len(people))

# seeing whether a key exists in dictionary

print('rmala' in people)
print('nnagraj' in people)

# Getting dictionary data with get()
# dictionaryname.get(key)

print(people.get('rmala'))
print(people.get('raj'))  # it will give you "None" instead of crashing program

print(people.get('raj',
                 'the key is not found'))  # it will display the second value if first value is not found in the dictionary

# change the value of a key

people = {'htaka': 'Haru Taka', 'ppatel': 'priya patel', 'rmala': 'rita mala'}
people['htaka'] = "Hasya Taka"
print(people['htaka'])

# Adding or changing data dictionary
# dictionaryname.update(key,value)

people1 = {'htaka': 'Haru Taka', 'ppatel': 'priya patel', 'rmala': 'rita mala'}
people1.update({'lalex': 'lisa alex'})
print("The people1 has", people1)
people2 = {}
people2 = people1.update({'hhobbit': "huge hobbit"})
print(people2)


def add_two_numbers(x, y):  # function header
    """
    Takes in two numbers and returns the sum
    parameters
        x : str
            first number
        y : str
            second number
    returns
        x+y
    """
    z = x + y
    return z  # function return


print(add_two_numbers(100, 5))  # function  call


def squarerootnumber(x):
    z = (x) ** (1 / 2)
    return int(z)


print(squarerootnumber(9))

y = lambda x, y: x + y  # an anonymous function which takes x and y and input and returns x+y
print(y(100, 5))  # call the function

y1 = lambda x, y, z: x + y - z
print(y1(7, 9, 10))
