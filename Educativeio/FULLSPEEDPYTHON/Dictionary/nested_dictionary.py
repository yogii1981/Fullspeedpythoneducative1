""" Student dictionary - keys, subkeys, subvalues

Key                 Sub Keys                   Sub values
Name          Age         Address             Agenumber        Addressdetails

Peter                                           17               Lisbon

"""

students = {
    "Peter": {"age": 10, "address": "lisbon"},
    "Yogi": {"age": 12, "address": "Iceland"}
}

print(students)  # display all the information
print(students['Peter'])  # display all the information about Peter
print(students['Peter']['age'])  # display all the information of the peter's age
print(students['Yogi']['address'])  # display all the information of yogi's address
