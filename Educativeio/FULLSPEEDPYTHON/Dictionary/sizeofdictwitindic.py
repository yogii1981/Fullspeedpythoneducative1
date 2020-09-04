"""
Determine the size of the dictionary within the dictionary
To calculate the number of students in the dictionary, get the
length of the total keys in the dictionary using len(student.keys())

"""


def totalStudentsKey(students):
    return (len(students.keys()))


students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

displaytotalkey = totalStudentsKey(students)
print(displaytotalkey)

print(students["Anna"])  # display the values associated with Anna

"""
The solution1 looks more easy to understand
 but the simple len function can also return 
 the correct result using len(students).

"""


def totalStudents(students):
    return len(students)


students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}
print(totalStudents(students))
