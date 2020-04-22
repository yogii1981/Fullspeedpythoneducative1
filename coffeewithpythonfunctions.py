"""Functions and Tricks"""

# map(func,iter)
"""Executes the function on all elelemts of the iterable"""
print(list(map(lambda x: x[0], ['red', 'green', 'yellow'])))

"""literation """

steps = ['post a vacancy', 'select resume', 'schedule interview', 'interview', 'offer the role']

for step in steps:
    print(step)

# countdown for date of joining
print('\n countdown to date of joining:')
for i in range(10, 0, -1):
    print(str(i) + '.....')
