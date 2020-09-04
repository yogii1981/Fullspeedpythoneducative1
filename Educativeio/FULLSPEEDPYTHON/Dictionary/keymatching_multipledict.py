"""
 how to find keys matching a given value with in as a parameter to the function within multiple dictionaries.

 Solution 1 using Nested Loop
"""


def find_students(address, students):
    names = []
    for key, subdict in students.items():
        for sublist in subdict.values():
            if (sublist == address):
                names.append(key)
    return sorted(names)


students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}
print(find_students("Lisbon", students))

"""
how to find keys matching a given value with in as a parameter to the function within multiple dictionaries.

Using FOR LOOP"""


def find_students(address, students):
    names = []
    for key, value in students.items():
        if value["address"] == address:
            names.append(key)
    return sorted(names)


students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}
print(find_students("Lisbon", students))
