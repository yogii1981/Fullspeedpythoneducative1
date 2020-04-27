class Car:

    def __init__(self, maxspeed=None, minspeed=None, weight=None, isthecaron=None, condition=None):
        self.maxspeed = maxspeed
        self.minspeed = minspeed
        self.weight = weight
        self.isthecaron = isthecaron
        self.condition = condition

    def printmaxcarspeed(self):
        return ("Maximum speed of car is %d m/hr".format(self.maxspeed))

    def printmincarspeed(self):
        return ("Minimum speed of car is %d m/hr".format(self.minspeed))

    def printweight(self):
        return ("Weight of the car is %d kg".format(self.weight))

    def printstateofcar(self):
        return ("State of the car is %d".format(self.isthecaron))

    def printconditionofcar(self):
        return ("The condition of the car is %d".format(self.condition))


displaycarfeatures = Car(100)
print(displaycarfeatures.printmaxcarspeed())
