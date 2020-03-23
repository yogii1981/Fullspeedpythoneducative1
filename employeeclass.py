class Employee:

    def __init__(self, name, grade, jobtitle, salary, bonus=0):
        self.name = name
        self.grade = grade
        self.jobtitle = jobtitle
        self.salary = salary
        self.__bonus = bonus

    def calculatebonus(self):
        if self.grade == 10:
            self.__bonus = self.salary * 0.15
        elif self.grade == 9:
            self.__bonus = self.salary * 0.10
        elif self.grade == 8:
            self.__bonus = self.salary * 0.05
        return self.__bonus

    def netsalary(self):
        ntsalary = self.salary + self.__bonus
        return ntsalary


package = Employee("Jacob", 10, "Manager", 100000)
print(package.calculatebonus())
print(package.netsalary())

packageOne = Employee("Santosh", 9, "Team Lead", 100000)
print(package.calculatebonus())
print(package.netsalary())

# (jacob,10, manager, 15 bonus percent)
# (santosh, 9, team leade, 9 percent)

# name, grade, job title, salary, bonus(private , 5% of slary), grade ( 5 to 8)
