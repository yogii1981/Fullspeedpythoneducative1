class Calculatorkaggle:

    def __init__(self, value1=None, value2=None):
        self.value1 = value1
        self.value2 = value2

    def __add__(self):
        return (self.value1 + self.value2)

    def __and__(self):
        return (self.value1 & self.value2)

    def __bool__(self):
        return (self.value1 != 0, self.value2 != 0)

    def __ceil__(self):
        return (self.value1, self.value2)

    def __divmod__(self):
        return divmod(self.value1, self.value2)


# |
# |  __divmod__(self, value, /)
# |      Return divmod(self, value).
# |
# |  __eq__(self, value, /)
# |      Return self==value.
# |
# |  __float__(self, /)
# |      float(self)
# |
# |  __floor__(...)
# |      Flooring an Integral returns itself.
# |


calc = Calculatorkaggle(5, 6)
print(calc.__add__())
print(calc.__and__())
print(calc.__bool__())
print(calc.__ceil__())
print(calc.__divmod__())
