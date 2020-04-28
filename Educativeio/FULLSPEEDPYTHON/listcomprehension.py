"""LIST COMPREHENSION"""

"""List comprehensions are a concise way to create lists.
 They consist of square brackets containing an expression 
 followed by the for keyword; the result will be a list whose 
 results match the expression."""

print([x * x for x in [0, 1, 2, 3]])

print([x * x for x in range(5)])

print([x * x for x in range(7) if (x % 2 == 0)])
