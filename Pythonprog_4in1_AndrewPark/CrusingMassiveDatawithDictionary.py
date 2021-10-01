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

# change
