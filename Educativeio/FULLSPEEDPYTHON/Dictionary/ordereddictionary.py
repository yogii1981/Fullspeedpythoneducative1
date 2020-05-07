"""
You can create an ordered dictionary which preserves the order in which the keys are inserted.
This is done by importing the OrderedDictionary from the collections library,
 and call the OrderedDictionary() built-in method.
"""

from collections import OrderedDict

ages = OrderedDict()

ages['Peter'] = 12
ages['Susan'] = 10
ages['Maria'] = 5

for key, value in ages.items():
    print(key, value)
