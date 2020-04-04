class Team:
    classVariable = "India team"

    def __init__(self, sportName):
        self.sportName = sportName

    @staticmethod
    def printStatement():
        print("static method")


objectTeam = Team('Kabaddi')
objectTeam.printStatement()
