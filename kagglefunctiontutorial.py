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

    def __float_(self):
        return float(self.value1)

    def __floordiv__(self):
        return self.value2 // self.value1

    def __format__(self):
        return (self.value2, self.value1)

    def __mod__(self):
        return self.value1




calc = Calculatorkaggle(5, 6)
print(calc.__add__())
print(calc.__and__())
print(calc.__bool__())
print(calc.__ceil__())
print(calc.__divmod__())
print(calc.__floordiv__())
print(calc.__format__())
print(calc.__mod__())
