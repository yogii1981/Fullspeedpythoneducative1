# # python program to ullustrate the use of arguments (*values in this case)
# # which multiplies all the values given to a function as a parameter
# def multiplyall(*values):
#
# write a program using a inhertiance method to add squareroot,cuberoot,cubea nd sqaure calculation capability in
# the exisiting calculator class when the user enter 2 integers.

class Calculator:

    def __init__(self, *values):
        self.values = values

    def addall(self):
        add = 0
        print(self.values)
        for i in self.values:
            add = add + i
            print(add)
            return add

    def multiplyall(self):
        mul = 1
        print(self.values)
        for i in self.values:
            mul = mul * i
            print(mul)
            return mul


answer = Calculator(7, 8, 9)
answer.addall()
answer.multiplyall()
