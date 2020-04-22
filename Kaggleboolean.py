x = True
print(x)
print(type(x))

"""
Operation	Description		         Operation	          Description
a == b	   a equal to b		           a != b	           a not equal to b
a < b	  a less than b		            a > b	            a greater than b
a <= b	 a less than or equal to b		a >= b	        a greater than or equal to b
"""


def can_run_for_president(age):
    """Can someone of the given age run for president in the US?"""
    # The US Constitution says you must "have attained to the Age of thirty-five Years"
    return age >= 35


print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))

# Comparison

print(3 == 3.0)
print('3' == 3.0)
