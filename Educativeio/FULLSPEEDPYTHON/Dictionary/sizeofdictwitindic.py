"""Determine the size of the dictionary within the dictionary"""


def totalStudents(students):
    return (len(students.keys()))


students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

displaytotal = totalStudents(students)
print(displaytotal)
