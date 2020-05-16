"""Determine the size of the dictionary within the dictionary"""


def totalStudents(students):
    return (len(students.keys()))


students = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

displaytotal = totalStudents(students)
print(displaytotal)
