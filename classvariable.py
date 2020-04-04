class Team:
    classVariable = "India team"

    def __init__(self, sportName):
        self.sportName = sportName

    @classmethod
    def printStatement(cls):
        return print(cls.classVariable)


Team.printStatement()
